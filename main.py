import streamlit as st
import tensorflow as tf
import numpy as np
import json
import os
import matplotlib.pyplot as plt



from PIL import Image, UnidentifiedImageError
from datetime import datetime, date

from disease_info import DISEASE_INFO
from streamlit_option_menu import option_menu

from crop_registration import (
    add_crop,
    load_crops,
    delete_crop,
    days_since_sowing,
    display_name
)

from crop_raksha import (
    get_crop_records,
    get_next_day,
    add_monitoring_record,
    get_latest_record,
)
from crop_comparison import (
    calculate_image_difference,
    classify_change,
    generate_difference_heatmap
)

from crop_raksha_chat import (
    render_crop_raksha_chat,
    get_disease_message,
    get_change_message
)

from language import render_language_selector
from language import t, render_language_selector

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Crop Doctor",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

MODEL_PATH = "models/best_crop_doctor.keras"
CLASS_PATH = "class_names.json"
HISTORY_FILE = "monitoring_history.json"

IMAGE_SIZE = (224, 224)

PAGE_SIZE = 20


# =====================================================
# UI STYLE
# =====================================================

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    padding: 35px;
    border-radius: 24px;
    background: linear-gradient(135deg, #e8f5e9, #f7fff8);
    border: 1px solid #d8eadb;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 48px;
    margin-bottom: 5px;
}

.hero p {
    font-size: 19px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# LOAD MODEL
# =====================================================

@st.cache_resource
def load_model():

    if not os.path.exists(MODEL_PATH):

        st.error(
            f"❌ Model file not found at `{MODEL_PATH}`. "
            "Please make sure the trained model is present before "
            "running Crop Doctor."
        )

        st.stop()

    try:

        return tf.keras.models.load_model(
            MODEL_PATH
        )

    except Exception as e:

        st.error(
            f"❌ Failed to load the AI model: {e}"
        )

        st.stop()


@st.cache_data
def load_classes():

    if not os.path.exists(CLASS_PATH):

        st.error(
            f"❌ Class list not found at `{CLASS_PATH}`."
        )

        st.stop()

    try:

        with open(
            CLASS_PATH,
            "r"
        ) as f:

            data = json.load(f)

    except Exception as e:

        st.error(
            f"❌ Failed to read `{CLASS_PATH}`: {e}"
        )

        st.stop()

    if isinstance(data, list):

        return data

    return list(
        data.values()
    )


model = load_model()
class_names = load_classes()


# =====================================================
# HISTORY FUNCTIONS
# =====================================================

def load_history():

    if not os.path.exists(
        HISTORY_FILE
    ):

        return []

    try:

        with open(
            HISTORY_FILE,
            "r"
        ) as f:

            return json.load(f)

    except Exception:

        return []


def save_history(history):

    try:

        with open(
            HISTORY_FILE,
            "w"
        ) as f:

            json.dump(
                history,
                f,
                indent=4
            )

        return True

    except Exception as e:

        st.error(
            f"❌ Could not save history: {e}"
        )

        return False


def add_record(
    crop,
    disease,
    confidence
):

    history = load_history()

    history.append({

        "date":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            ),

        "crop":
            crop,

        "disease":
            disease,

        "confidence":
            round(
                confidence,
                2
            )

    })

    save_history(history)


# =====================================================
# HELPER FUNCTIONS
# =====================================================

def get_crop_name(class_name):

    return class_name.split(
        "_"
    )[0].capitalize()


def get_disease_name(class_name):

    if "healthy" in class_name.lower():

        return "Healthy"

    info = DISEASE_INFO.get(
        class_name
    )

    if info:

        return info["disease"]

    return class_name.replace(
        "_",
        " "
    ).title()


def safe_open_image(uploaded_file):

    try:

        return Image.open(
            uploaded_file
        ).convert("RGB")

    except (
        UnidentifiedImageError,
        OSError
    ) as e:

        st.error(
            f"⚠️ Couldn't read that image file: {e}"
        )

        return None


# =====================================================
# VISUAL DIFFERENCE HEATMAP
# =====================================================

def create_difference_heatmap(
    previous_image,
    current_image
):
    """
    Create a visual heatmap showing where the
    previous and current crop images differ.

    Brighter / hotter areas indicate larger
    visual differences.
    """

    try:

        previous_image = (
            previous_image
            .convert("RGB")
            .resize(IMAGE_SIZE)
        )

        current_image = (
            current_image
            .convert("RGB")
            .resize(IMAGE_SIZE)
        )

        previous_array = np.array(
            previous_image
        ).astype(
            np.float32
        )

        current_array = np.array(
            current_image
        ).astype(
            np.float32
        )

        # -------------------------------------------------
        # PIXEL DIFFERENCE
        # -------------------------------------------------

        pixel_difference = np.mean(
            np.abs(
                previous_array -
                current_array
            ),
            axis=2
        )

        # -------------------------------------------------
        # NORMALIZE DIFFERENCE
        # -------------------------------------------------

        max_difference = (
            pixel_difference.max()
        )

        if max_difference > 0:

            normalized_difference = (
                pixel_difference /
                max_difference
            )

        else:

            normalized_difference = (
                np.zeros_like(
                    pixel_difference
                )
            )

        # -------------------------------------------------
        # CREATE HEATMAP
        # -------------------------------------------------

        fig, ax = plt.subplots(
            figsize=(7, 5)
        )

        heatmap = ax.imshow(
            normalized_difference,
            cmap="hot",
            vmin=0,
            vmax=1
        )

        ax.set_title(
            "Visual Difference Heatmap"
        )

        ax.axis(
            "off"
        )

        fig.colorbar(
            heatmap,
            ax=ax,
            fraction=0.046,
            pad=0.04,
            label="Relative Visual Change"
        )

        fig.tight_layout()

        return fig

    except Exception:

        return None


# =====================================================
# CHECK WHETHER TODAY'S MONITORING IS DUE
# =====================================================

def is_monitoring_due(
    crop,
    records
):

    monitoring_time = crop.get(
        "monitoring_time"
    )

    if not monitoring_time:

        return True

    try:

        scheduled_time = datetime.strptime(
            monitoring_time,
            "%H:%M"
        ).time()

    except ValueError:

        return True

    now = datetime.now()

    today = date.today().strftime(
        "%Y-%m-%d"
    )

    # -------------------------------------------------
    # TODAY ALREADY RECORDED
    # -------------------------------------------------

    for record in records:

        if record["date"].startswith(
            today
        ):

            return False

    # -------------------------------------------------
    # CHECK SCHEDULE
    # -------------------------------------------------

    return now.time() >= scheduled_time


# =====================================================
# AI IMAGE ANALYSIS
# =====================================================

def analyze_crop_image(
    image
):

    try:

        img = image.resize(
            IMAGE_SIZE
        )

        img_array = np.array(
            img
        ).astype(
            np.float32
        )

        if (
            img_array.ndim != 3
            or img_array.shape[2] != 3
        ):

            return None

        # IMPORTANT:
        # Do NOT normalize.
        # This matches predict.py preprocessing.

        img_array = np.expand_dims(
            img_array,
            axis=0
        )

        predictions = model.predict(
            img_array,
            verbose=0
        )

        predicted_index = np.argmax(
            predictions[0]
        )

        confidence = (
            float(
                predictions[0][
                    predicted_index
                ]
            ) * 100
        )

        predicted_class = (
            class_names[
                predicted_index
            ]
        )

        crop = get_crop_name(
            predicted_class
        )

        disease = get_disease_name(
            predicted_class
        )

        return {

            "class":
                predicted_class,

            "crop":
                crop,

            "disease":
                disease,

            "confidence":
                confidence

        }

    except Exception:

        return None


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown(
        "## 🌱 Crop Doctor"
    )

    st.caption(
        "AI Crop Health Assistant"
    )

    st.divider()


    render_language_selector()

    st.divider()

    page_names = [
        "Dashboard",
        "Crop Registration",
        "Crop Raksha",
        "Diagnose",
        "Monitoring",
        "Disease Library",
        "About"
    ]

    page_labels = [
        t("dashboard"),
        t("crop_registration"),
        t("crop_raksha"),
        t("diagnose"),
        t("monitoring"),
        t("disease_library"),
        t("about")
    ]

    selected_page = option_menu(

        "Navigation",

        page_labels,

        icons=[
            "house",
            "clipboard-plus",
            "shield-check",
            "camera",
            "graph-up",
            "book",
            "info-circle"
        ],

        menu_icon="leaf",

        default_index=0
    )

    page = page_names[
        page_labels.index(selected_page)
    ]



    st.divider()

    st.caption(
        "AI-assisted crop health monitoring"
    )


# =====================================================
# DASHBOARD
# =====================================================

if page == "Dashboard":

    st.markdown(
        f"""
        <div class="hero">

            <h1>🌱 {t("app_name")}</h1>

            <p>
            {t("ai_assistant")}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    history = load_history()

    total_scans = len(
        history
    )

    healthy = sum(
        1
        for r in history
        if r["disease"].lower()
        == "healthy"
    )

    issues = (
        total_scans -
        healthy
    )

    crops_count = len(
        set(
            r["crop"]
            for r in history
        )
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "🔬 Total Scans",
            total_scans
        )

    with c2:

        st.metric(
            "🌱 Healthy",
            healthy
        )

    with c3:

        st.metric(
            "🦠 Issues Detected",
            issues
        )

    with c4:

        st.metric(
            "🌾 Crops Monitored",
            crops_count
        )

    st.divider()

    st.subheader(
        "🚀 Crop Doctor Features"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.info("""
        ### 🩺 AI Diagnosis

        Upload a leaf image and get
        an AI-based disease prediction.
        """)

    with c2:

        st.info("""
        ### 🛡️ Crop Raksha

        Monitor your crop every day
        and detect changes over time.
        """)

    with c3:

        st.info("""
        ### 🩺 Management Advice

        Get management and prevention
        information for detected problems.
        """)

    st.divider()

    st.subheader(
        "🌾 Supported Crops"
    )

    supported_crops = sorted(
        set(
            get_crop_name(c)
            for c in class_names
        )
    )

    crop_columns = st.columns(5)

    for i, crop in enumerate(
        supported_crops
    ):

        with crop_columns[
            i % 5
        ]:

            st.write(
                f"🌱 **{crop}**"
            )


# =====================================================
# CROP REGISTRATION
# =====================================================

elif page == "Crop Registration":

    st.title(
        f"📋 {t('crop_registration')}"
    )

    st.write(
        f"🌱 {t('crop_registration')}"
    )

    st.divider()

    with st.form(
        "crop_registration_form"
    ):

        farmer_name = st.text_input(
            "👨‍🌾 Farmer Name"
        )

        crop_name = st.selectbox(

            "🌾 Crop",

            sorted(
                set(
                    get_crop_name(c)
                    for c in class_names
                )
            )
        )

        field_label = st.text_input(
            "📍 Field Name",
            placeholder="Example: Field 1"
        )

        sowing_date = st.date_input(
            "📅 Date of Sowing"
        )

        monitoring_time = st.time_input(
            "⏰ Daily Crop Raksha Monitoring Time"
        )

        submitted = st.form_submit_button(
            "🌱 Register Crop"
        )

        if submitted:

            if not farmer_name.strip():

                st.error(
                    "Please enter the farmer name."
                )

            elif sowing_date > date.today():

                st.error(
                    "The date of sowing cannot be in the future."
                )

            else:

                crop_id = add_crop(

                    farmer_name=farmer_name,

                    crop_name=crop_name,

                    sowing_date=sowing_date,

                    field_label=field_label,

                    monitoring_time=
                    monitoring_time.strftime(
                        "%H:%M"
                    )
                )

                st.success(
                    "✅ Crop registered successfully!"
                )

                st.write(
                    f"**Farmer:** {farmer_name}"
                )

                st.write(
                    f"**Crop:** {crop_name}"
                )

                st.write(
                    f"**Field:** "
                    f"{field_label or 'Not specified'}"
                )

                st.write(
                    f"**Date of Sowing:** "
                    f"{sowing_date}"
                )

                st.write(
                    f"**Daily Crop Raksha Time:** "
                    f"{monitoring_time.strftime('%I:%M %p')}"
                )

                st.write(
                    f"**Crop ID:** `{crop_id}`"
                )

    st.divider()

    st.subheader(
        "🌾 My Registered Crops"
    )

    crops = load_crops()

    if not crops:

        st.info(
            "No crops registered yet."
        )

    else:

        for crop in crops:

            with st.container(
                border=True
            ):

                st.write(
                    f"### 🌱 {display_name(crop)}"
                )

                if crop.get(
                    "farmer_name"
                ):

                    st.write(
                        f"👨‍🌾 Farmer: "
                        f"{crop['farmer_name']}"
                    )

                st.write(
                    f"📅 Sowing Date: "
                    f"{crop['sowing_date']}"
                )

                st.write(
                    f"🌿 Crop Age: "
                    f"{days_since_sowing(crop['sowing_date'])} days"
                )

                if crop.get(
                    "monitoring_time"
                ):

                    try:

                        formatted_time = (
                            datetime.strptime(
                                crop["monitoring_time"],
                                "%H:%M"
                            ).strftime(
                                "%I:%M %p"
                            )
                        )

                    except ValueError:

                        formatted_time = (
                            crop["monitoring_time"]
                        )

                    st.write(
                        f"⏰ Crop Raksha Time: "
                        f"{formatted_time}"
                    )

                st.write(
                    f"🟢 Status: "
                    f"{crop.get('status', 'unknown')}"
                )

                if st.button(
                    "🗑️ Delete",
                    key=f"delete_{crop['id']}"
                ):

                    delete_crop(
                        crop["id"]
                    )

                    st.rerun()


# =====================================================
# CROP RAKSHA
# =====================================================

elif page == "Crop Raksha":

    st.title(
        f"🛡️ {t('crop_raksha')}"
    )

    st.write(
        "Your AI crop companion for continuous daily monitoring."
    )

    st.divider()

    # =================================================
    # LOAD CROPS
    # =================================================

    crops = load_crops()

    if not crops:

        st.warning(
            "🌱 No crops registered yet."
        )

        st.info(
            "Go to Crop Registration and register your crop first."
        )

    else:

        active_crops = [
            crop
            for crop in crops
            if crop.get("status")
            == "active"
        ]

        if not active_crops:

            st.warning(
                "No active crops found."
            )

        else:

            # =================================================
            # SELECT CROP
            # =================================================

            crop_options = {
                display_name(crop):
                    crop["id"]

                for crop in active_crops
            }

            selected_crop_name = st.selectbox(
                "🌾 Select your crop",
                list(
                    crop_options.keys()
                )
            )

            selected_crop_id = (
                crop_options[
                    selected_crop_name
                ]
            )

            selected_crop = next(
                crop
                for crop in active_crops
                if crop["id"]
                == selected_crop_id
            )

            # =================================================
            # CROP INFORMATION
            # =================================================

            monitoring_time = (
                selected_crop.get(
                    "monitoring_time",
                    "18:00"
                )
            )

            try:

                display_time = datetime.strptime(
                    monitoring_time,
                    "%H:%M"
                ).strftime(
                    "%I:%M %p"
                )

            except ValueError:

                display_time = (
                    monitoring_time
                )

            records = get_crop_records(
                selected_crop_id
            )

            next_day = get_next_day(
                selected_crop_id
            )

            monitoring_due = (
                is_monitoring_due(
                    selected_crop,
                    records
                )
            )

            crop_age = days_since_sowing(
                selected_crop["sowing_date"]
            )

            farmer_name = (
                selected_crop.get(
                    "farmer_name",
                    "Farmer"
                )
            )

            # =================================================
            # CROP PROFILE
            # =================================================

            st.subheader(
                "🌱 Crop Profile"
            )

            c1, c2, c3, c4 = st.columns(4)

            with c1:

                st.metric(
                    "🌾 Crop",
                    selected_crop["crop_name"]
                )

            with c2:

                st.metric(
                    "📅 Sowing Date",
                    selected_crop["sowing_date"]
                )

            with c3:

                st.metric(
                    "🌿 Crop Age",
                    f"{crop_age} days"
                )

            with c4:

                st.metric(
                    "📊 Observations",
                    len(records)
                )

            st.info(
                f"⏰ Your daily Crop Raksha time is "
                f"**{display_time}**"
            )

            st.divider()

            # =================================================
            # CROP RAKSHA AI COMPANION
            # =================================================

            st.subheader(
                f"🤖 {t('crop_raksha')}"
            )

            st.caption(
                "Your AI crop companion remembers your monitoring "
                "history and helps you understand what is happening "
                "over time."
            )

            render_crop_raksha_chat(
                selected_crop,
                records
            )

            st.divider()

            # =================================================
            # DAILY MONITORING
            # =================================================

            if monitoring_due:

                st.subheader(
                    f"📸 Day {next_day} — Daily Crop Check"
                )

                st.write(
                    "Let's record today's condition."
                )

                uploaded_image = st.file_uploader(
                    "📷 Upload today's crop photograph",
                    type=[
                        "jpg",
                        "jpeg",
                        "png"
                    ],
                    key=(
                        f"raksha_upload_"
                        f"{selected_crop_id}_"
                        f"{next_day}"
                    )
                )

                if uploaded_image:

                    image = safe_open_image(
                        uploaded_image
                    )

                    if image is not None:

                        st.image(
                            image,
                            caption=(
                                f"Day {next_day} "
                                f"observation"
                            ),
                            width="stretch"
                        )

                        st.divider()

                        if st.button(
                            f"💾 Save Day {next_day} Observation",
                            width="stretch",
                            key=(
                                f"save_raksha_"
                                f"{selected_crop_id}_"
                                f"{next_day}"
                            )
                        ):

                            # =================================
                            # SAVE IMAGE
                            # =================================

                            os.makedirs(
                                "crop_raksha_images",
                                exist_ok=True
                            )

                            filename = (
                                f"{selected_crop_id}"
                                f"_day_{next_day}.jpg"
                            )

                            image_path = os.path.join(
                                "crop_raksha_images",
                                filename
                            )

                            image.save(
                                image_path
                            )

                            # =================================
                            # AI ANALYSIS
                            # =================================

                            ai_result = (
                                analyze_crop_image(
                                    image
                                )
                            )

                            if ai_result:

                                predicted_disease = (
                                    ai_result["disease"]
                                )

                                ai_confidence = (
                                    ai_result["confidence"]
                                )

                            else:

                                predicted_disease = (
                                    "Unknown"
                                )

                                ai_confidence = 0

                            # =================================
                            # PREVIOUS OBSERVATION
                            # =================================

                            previous_record = (
                                get_latest_record(
                                    selected_crop_id
                                )
                            )

                            difference = None

                            change_level = (
                                "baseline"
                            )

                            previous_image = None

                            if previous_record:

                                previous_image_path = (
                                    previous_record[
                                        "image_path"
                                    ]
                                )

                                try:

                                    previous_image = (
                                        Image.open(
                                            previous_image_path
                                        ).convert(
                                            "RGB"
                                        )
                                    )

                                    difference = (
                                        calculate_image_difference(
                                            previous_image,
                                            image
                                        )
                                    )

                                    change_level = (
                                        classify_change(
                                            difference
                                        )
                                    )
                                    heatmap = generate_difference_heatmap(
                                        previous_image,
                                        image
                                    )

                                except (
                                    OSError,
                                    UnidentifiedImageError
                                ):

                                    change_level = (
                                        "baseline"
                                    )

                            # =================================
                            # CREATE VISUAL HEATMAP
                            # =================================

                            difference_heatmap = None

                            if (
                                previous_image
                                is not None
                            ):

                                difference_heatmap = (
                                    create_difference_heatmap(
                                        previous_image,
                                        image
                                    )
                                )

                            # =================================
                            # HEALTH STATUS
                            # =================================

                            is_healthy = (
                                ai_result is not None
                                and
                                predicted_disease.lower()
                                == "healthy"
                            )

                            # =================================
                            # CROP RAKSHA DECISION
                            # =================================

                            if (
                                change_level
                                == "baseline"
                            ):

                                observation = (
                                    "Baseline observation "
                                    "recorded. "
                                    f"AI result: "
                                    f"{predicted_disease} "
                                    f"({ai_confidence:.2f}%)."
                                )

                            elif (
                                change_level
                                == "normal"
                                and is_healthy
                            ):

                                observation = (
                                    "No significant visual "
                                    "change detected. "
                                    "AI result: Healthy "
                                    f"({ai_confidence:.2f}%)."
                                )

                            elif (
                                change_level
                                == "minor_change"
                                and is_healthy
                            ):

                                observation = (
                                    "A minor visual change "
                                    "was detected. "
                                    "AI currently predicts "
                                    f"Healthy "
                                    f"({ai_confidence:.2f}%). "
                                    "Continue monitoring."
                                )

                            elif (
                                change_level
                                == "significant_change"
                                and is_healthy
                            ):

                                observation = (
                                    "A significant visual "
                                    "change was detected, "
                                    "but the AI currently "
                                    "predicts Healthy "
                                    f"({ai_confidence:.2f}%). "
                                    "Further monitoring "
                                    "is recommended."
                                )

                            elif (
                                not is_healthy
                                and ai_confidence >= 60
                            ):

                                observation = (
                                    f"AI detected "
                                    f"{predicted_disease} "
                                    f"with "
                                    f"{ai_confidence:.2f}% "
                                    f"confidence."
                                )

                            else:

                                observation = (
                                    f"AI result: "
                                    f"{predicted_disease} "
                                    f"({ai_confidence:.2f}%). "
                                    "Further observation "
                                    "is recommended."
                                )

                            # =================================
                            # SAVE RECORD
                            # =================================

                            record = (
                                add_monitoring_record(
                                    crop_id=
                                        selected_crop_id,

                                    image_path=
                                        image_path,

                                    status=
                                        change_level,

                                    observation=
                                        observation,

                                    disease=
                                        predicted_disease,

                                    confidence=
                                        ai_confidence
                                )
                            )

                            # =================================
                            # RESULT
                            # =================================

                            st.success(
                                f"✅ Day {record['day']} "
                                f"observation saved!"
                            )

                            st.divider()

                            # =================================
                            # VISUAL DIFFERENCE HEATMAP
                            # =================================

                            if (
                                    previous_record
                                    and heatmap is not None
                            ):

                                st.subheader(
                                    "🔥 Visual Change Heatmap"
                                )

                                st.caption(
                                    "Bright areas indicate regions where "
                                    "the crop image changed most compared "
                                    "with the previous observation."
                                )

                                st.image(
                                    heatmap,
                                    caption="Crop Raksha visual difference map",
                                    width="stretch"
                                )

                                if difference is not None:
                                    st.info(
                                        f"📊 Overall visual difference: "
                                        f"**{difference:.2f}%**"
                                    )

                            st.subheader(
                                "🤖 Crop Raksha AI Assessment"
                            )

                            if ai_result:

                                r1, r2, r3 = (
                                    st.columns(3)
                                )

                                with r1:

                                    st.metric(
                                        "🌱 Crop",
                                        ai_result[
                                            "crop"
                                        ]
                                    )

                                with r2:

                                    st.metric(
                                        "🔬 AI Result",
                                        ai_result[
                                            "disease"
                                        ]
                                    )

                                with r3:

                                    st.metric(
                                        "🎯 Confidence",
                                        f"{ai_result['confidence']:.2f}%"
                                    )

                            # =================================
                            # VISUAL CHANGE RESULT
                            # =================================

                            st.divider()

                            st.subheader(
                                "🔥 Visual Change Analysis"
                            )

                            if (
                                change_level
                                == "baseline"
                            ):

                                st.info(
                                    """
                                    🌱 **Baseline created**

                                    This is the first Crop Raksha
                                    observation.

                                    Future observations will be
                                    compared against previous images.
                                    """
                                )

                            else:

                                c1, c2 = (
                                    st.columns(2)
                                )

                                with c1:

                                    if difference is not None:

                                        st.metric(
                                            "📊 Visual Difference",
                                            f"{difference:.2f}%"
                                        )

                                with c2:

                                    if (
                                        change_level
                                        == "normal"
                                    ):

                                        st.success(
                                            "🟢 Normal"
                                        )

                                    elif (
                                        change_level
                                        == "minor_change"
                                    ):

                                        st.warning(
                                            "🟠 Minor Change"
                                        )

                                    elif (
                                        change_level
                                        == "significant_change"
                                    ):

                                        st.error(
                                            "🔴 Significant Change"
                                        )

                                # ---------------------------------
                                # HEATMAP
                                # ---------------------------------

                                if difference_heatmap is not None:

                                    st.markdown(
                                        "### 🔥 Visual Difference Heatmap"
                                    )

                                    st.caption(
                                        "Hotter/brighter areas show "
                                        "where the current image differs "
                                        "most from the previous observation."
                                    )

                                    st.pyplot(
                                        difference_heatmap,
                                        clear_figure=True
                                    )

                                    plt.close(
                                        difference_heatmap
                                    )

                                else:

                                    st.info(
                                        "The previous observation image "
                                        "could not be loaded, so the "
                                        "visual heatmap could not be created."
                                    )

                            # =================================
                            # CROP RAKSHA COMPANION MESSAGES
                            # =================================

                            st.divider()

                            st.subheader(
                                "🤖 Crop Raksha Assessment"
                            )

                            st.markdown(
                                get_change_message(
                                    change_level,
                                    difference
                                )
                            )

                            st.markdown(
                                get_disease_message(
                                    predicted_disease,
                                    ai_confidence
                                )
                            )

                            # =================================
                            # EARLY WARNING
                            # =================================

                            if (
                                change_level
                                == "significant_change"
                                and not is_healthy
                                and ai_confidence >= 60
                            ):

                                st.error(
                                    "🚨 Crop Raksha detected "
                                    "a significant visual "
                                    "change and the AI "
                                    "identified a possible "
                                    "crop health issue."
                                )

                                st.warning(
                                    "🩺 Please open the "
                                    "Diagnose section for "
                                    "a detailed assessment."
                                )

                            elif (
                                change_level
                                in [
                                    "minor_change",
                                    "significant_change"
                                ]
                                and is_healthy
                            ):

                                st.warning(
                                    "🟠 Crop Raksha noticed "
                                    "a visual change, but "
                                    "the AI currently "
                                    "considers the crop "
                                    "healthy."
                                )

                            elif is_healthy:

                                st.success(
                                    "🟢 Crop Raksha currently "
                                    "sees no major health "
                                    "concern."
                                )

                            else:

                                st.warning(
                                    "🟠 The AI detected a "
                                    "possible issue. "
                                    "Consider using the "
                                    "Diagnose section "
                                    "for confirmation."
                                )

                            st.rerun()

            else:

                # =================================================
                # TODAY ALREADY COMPLETED / NOT DUE
                # =================================================

                today_record = None

                today = date.today().strftime(
                    "%Y-%m-%d"
                )

                for record in records:

                    if record["date"].startswith(
                        today
                    ):

                        today_record = record

                        break

                if today_record:

                    st.success(
                        f"""
                        ✅ **Today's Crop Raksha
                        check is complete!**

                        You completed today's observation
                        at **{today_record['date'].split(" ")[1]}**.

                        🧠 Crop Raksha has remembered it.

                        Your next observation will be
                        available tomorrow.
                        """
                    )

                else:

                    st.info(
                        f"""
                        ⏰ **Today's Crop Raksha check
                        is not due yet.**

                        Your selected monitoring time is
                        **{display_time}**.

                        Come back at that time and we'll
                        continue today's crop check.
                        """
                    )

            # =================================================
            # TIMELINE
            # =================================================

            st.divider()

            st.subheader(
                "📅 Crop Raksha Timeline"
            )

            if not records:

                st.info(
                    "Your daily observations "
                    "will appear here."
                )

            else:

                timeline_state_key = (
                    f"raksha_shown_"
                    f"{selected_crop_id}"
                )

                if timeline_state_key not in (
                    st.session_state
                ):

                    st.session_state[
                        timeline_state_key
                    ] = PAGE_SIZE

                shown = st.session_state[
                    timeline_state_key
                ]

                ordered_records = list(
                    reversed(records)
                )

                for record in (
                    ordered_records[:shown]
                ):

                    with st.container(
                        border=True
                    ):

                        c1, c2, c3 = (
                            st.columns(3)
                        )

                        with c1:

                            st.write(
                                f"### 🌱 Day "
                                f"{record['day']}"
                            )

                        with c2:

                            st.write(
                                f"🕒 "
                                f"{record['date']}"
                            )

                        with c3:

                            st.write(
                                f"Status: "
                                f"**{record['status']}**"
                            )

                        st.write(
                            record["observation"]
                        )

                        if record.get(
                            "disease"
                        ):

                            st.caption(
                                f"🤖 AI: "
                                f"{record['disease']} "
                                f"({record.get('confidence', 0):.1f}%)"
                            )

                if shown < len(
                    ordered_records
                ):

                    if st.button(
                        f"Show more "
                        f"(showing {shown} of "
                        f"{len(ordered_records)})",
                        key=(
                            f"raksha_more_"
                            f"{selected_crop_id}"
                        )
                    ):

                        st.session_state[
                            timeline_state_key
                        ] += PAGE_SIZE

                        st.rerun()


# =====================================================
# DIAGNOSIS
# =====================================================

elif page == "Diagnose":

    st.title(
        f"🩺 {t('crop_diagnosis')}"
    )

    st.write(
        t("upload_leaf")
    )

    uploaded_file = st.file_uploader(

        f"📷 {t('choose_image')}",

        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )

    if uploaded_file:

        image = safe_open_image(
            uploaded_file
        )

        if image is not None:

            col1, col2 = st.columns(2)

            with col1:

                st.image(
                    image,
                    caption="Uploaded leaf",
                    width="stretch"
                )

            with col2:

                st.subheader(
                    "🔬 AI Analysis"
                )

                diagnose = st.button(
                    f"🩺 {t('diagnose_crop')}",
                    width="stretch"
                )

                if diagnose:

                    with st.spinner(
                        "Analyzing crop..."
                    ):

                        ai_result = (
                            analyze_crop_image(
                                image
                            )
                        )

                    if not ai_result:

                        st.error(
                            "⚠️ Please upload a valid RGB leaf "
                            "image — analysis could not be "
                            "completed."
                        )

                    else:

                        crop = ai_result[
                            "crop"
                        ]

                        disease = ai_result[
                            "disease"
                        ]

                        confidence = ai_result[
                            "confidence"
                        ]

                        predicted_class = (
                            ai_result[
                                "class"
                            ]
                        )

                        info = (
                            DISEASE_INFO.get(
                                predicted_class
                            )
                        )

                        # SAVE RESULT

                        add_record(
                            crop,
                            disease,
                            confidence
                        )

                        st.success(
                            "✅ Analysis Complete"
                        )

                        st.divider()

                        r1, r2, r3 = (
                            st.columns(3)
                        )

                        with r1:

                            st.metric(
                                "🌱 Crop",
                                crop
                            )

                        with r2:

                            st.metric(
                                "🦠 Result",
                                disease
                            )

                        with r3:

                            st.metric(
                                "🎯 Confidence",
                                f"{confidence:.2f}%"
                            )

                        st.divider()

                        if info:

                            st.subheader(
                                "📋 Description"
                            )

                            st.write(
                                info[
                                    "description"
                                ]
                            )

                            st.subheader(
                                "🔍 Symptoms"
                            )

                            for symptom in (
                                info[
                                    "symptoms"
                                ]
                            ):

                                st.write(
                                    f"• {symptom}"
                                )

                            st.subheader(
                                "🩺 Management"
                            )

                            for item in (
                                info[
                                    "management"
                                ]
                            ):

                                st.write(
                                    f"• {item}"
                                )

                            st.subheader(
                                "🛡️ Prevention"
                            )

                            for item in (
                                info[
                                    "prevention"
                                ]
                            ):

                                st.write(
                                    f"• {item}"
                                )

                        else:

                            st.warning(
                                "Information for this "
                                "disease is not available yet."
                            )

                        if confidence < 60:

                            st.warning(
                                "⚠️ Low confidence. "
                                "Try a clearer leaf image."
                            )

                        else:

                            st.info(
                                "💡 For best results, "
                                "use a clear image "
                                "with good lighting."
                            )


# =====================================================
# MONITORING
# =====================================================

elif page == "Monitoring":

    st.title(
        "📊 Crop Health Monitoring"
    )

    history = load_history()

    if not history:

        st.info(
            "No monitoring data yet. "
            "Diagnose a crop to create "
            "your first record."
        )

    else:

        total = len(
            history
        )

        healthy = sum(
            1
            for r in history
            if r["disease"].lower()
            == "healthy"
        )

        issues = (
            total -
            healthy
        )

        a, b, c = st.columns(3)

        with a:

            st.metric(
                "🔬 Total Scans",
                total
            )

        with b:

            st.metric(
                "🌱 Healthy",
                healthy
            )

        with c:

            st.metric(
                "🦠 Issues",
                issues
            )

        st.divider()

        st.subheader(
            "📈 AI Confidence Trend"
        )

        recent = history[
            -10:
        ]

        confidence_values = [
            r["confidence"]
            for r in recent
        ]

        st.line_chart(
            confidence_values
        )

        st.caption(
            "Confidence values from "
            "recent diagnoses."
        )

        st.divider()

        st.subheader(
            "📅 Diagnosis History"
        )

        if (
            "monitoring_shown"
            not in st.session_state
        ):

            st.session_state[
                "monitoring_shown"
            ] = PAGE_SIZE

        shown = st.session_state[
            "monitoring_shown"
        ]

        ordered_history = list(
            reversed(history)
        )

        for record in (
            ordered_history[:shown]
        ):

            with st.container(
                border=True
            ):

                c1, c2, c3, c4 = (
                    st.columns(4)
                )

                with c1:

                    st.write(
                        f"🕒 "
                        f"{record['date']}"
                    )

                with c2:

                    st.write(
                        f"🌱 "
                        f"{record['crop']}"
                    )

                with c3:

                    st.write(
                        f"🦠 "
                        f"{record['disease']}"
                    )

                with c4:

                    st.write(
                        f"🎯 "
                        f"{record['confidence']:.2f}%"
                    )

        if shown < len(
            ordered_history
        ):

            if st.button(
                f"Show more (showing {shown} of "
                f"{len(ordered_history)})"
            ):

                st.session_state[
                    "monitoring_shown"
                ] += PAGE_SIZE

                st.rerun()

        st.divider()

        confirm_clear = st.checkbox(
            "I understand this will permanently delete all "
            "diagnosis history."
        )

        if st.button(
            "🗑️ Clear History",
            disabled=not confirm_clear
        ):

            if save_history([]):

                st.success(
                    "History cleared."
                )

                st.session_state[
                    "monitoring_shown"
                ] = PAGE_SIZE

                st.rerun()


# =====================================================
# DISEASE LIBRARY
# =====================================================

elif page == "Disease Library":

    st.title(
        "📚 Disease Library"
    )

    st.write(
        "Explore supported crop diseases, "
        "symptoms, management and prevention."
    )

    st.divider()

    for class_name in (
        class_names
    ):

        if "healthy" in (
            class_name.lower()
        ):

            continue

        crop = get_crop_name(
            class_name
        )

        disease = get_disease_name(
            class_name
        )

        info = DISEASE_INFO.get(
            class_name
        )

        with st.expander(
            f"🌱 {crop} — 🦠 {disease}"
        ):

            if info:

                st.write(
                    "### 📋 Description"
                )

                st.write(
                    info[
                        "description"
                    ]
                )

                st.write(
                    "### 🔍 Symptoms"
                )

                for symptom in (
                    info[
                        "symptoms"
                    ]
                ):

                    st.write(
                        f"• {symptom}"
                    )

                st.write(
                    "### 🩺 Management"
                )

                for item in (
                    info[
                        "management"
                    ]
                ):

                    st.write(
                        f"• {item}"
                    )

                st.write(
                    "### 🛡️ Prevention"
                )

                for item in (
                    info[
                        "prevention"
                    ]
                ):

                    st.write(
                        f"• {item}"
                    )

            else:

                st.info(
                    "Information not available yet."
                )


# =====================================================
# ABOUT
# =====================================================

elif page == "About":

    st.title(
        "ℹ️ About Crop Doctor"
    )

    st.write(
        """
        Crop Doctor is an AI-powered crop health
        assistant designed to help identify crop
        diseases from leaf images.
        """
    )

    st.subheader(
        "🤖 AI Detection"
    )

    st.write(
        """
        A trained deep-learning model analyzes
        uploaded crop leaf images and predicts
        the most likely disease or healthy class.
        """
    )

    st.subheader(
        "🛡️ Crop Raksha"
    )

    st.write(
        """
        Crop Raksha monitors registered crops
        through daily observations, remembers
        previous observations and looks for
        changes that may require attention.
        """
    )

    st.subheader(
        "🔥 Visual Change Heatmap"
    )

    st.write(
        """
        Crop Raksha compares consecutive crop
        photographs and generates a visual
        difference heatmap showing areas where
        the crop image has changed.
        """
    )

    st.subheader(
        "📊 Daily Monitoring"
    )

    st.write(
        """
        Diagnosis results and Crop Raksha
        observations are stored locally,
        allowing users to track crop health
        over multiple observations.
        """
    )

    st.subheader(
        "🌾 Supported Crops"
    )

    for crop in sorted(
        set(
            get_crop_name(c)
            for c in class_names
        )
    ):

        st.write(
            f"• {crop}"
        )

    st.divider()

    st.caption(
        "🌱 Crop Doctor — "
        "AI-assisted crop health monitoring"
    )