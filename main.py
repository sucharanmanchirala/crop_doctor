import streamlit as st
import tensorflow as tf
import numpy as np
import json
import os
from PIL import Image
from datetime import datetime

from disease_info import DISEASE_INFO
from streamlit_option_menu import option_menu


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

    return tf.keras.models.load_model(
        MODEL_PATH
    )


@st.cache_data
def load_classes():

    with open(CLASS_PATH, "r") as f:

        data = json.load(f)

    if isinstance(data, list):

        return data

    return list(data.values())


model = load_model()

class_names = load_classes()


# =====================================================
# HISTORY FUNCTIONS
# =====================================================

def load_history():

    if not os.path.exists(HISTORY_FILE):

        return []

    try:

        with open(HISTORY_FILE, "r") as f:

            return json.load(f)

    except:

        return []


def save_history(history):

    with open(HISTORY_FILE, "w") as f:

        json.dump(
            history,
            f,
            indent=4
        )


def add_record(
    crop,
    disease,
    confidence
):

    history = load_history()

    history.append({

        "date": datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        ),

        "crop": crop,

        "disease": disease,

        "confidence": round(
            confidence,
            2
        )
    })

    save_history(history)


# =====================================================
# HELPER FUNCTIONS
# =====================================================

def get_crop_name(class_name):

    return class_name.split("_")[0].capitalize()


def get_disease_name(class_name):

    if "healthy" in class_name:

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

    page = option_menu(

        "Navigation",

        [
            "Dashboard",
            "Diagnose",
            "Monitoring",
            "Disease Library",
            "About"
        ],

        icons=[
            "house",
            "camera",
            "graph-up",
            "book",
            "info-circle"
        ],

        menu_icon="leaf",

        default_index=0
    )

    st.divider()

    st.caption(
        "AI-assisted crop health monitoring"
    )


# =====================================================
# DASHBOARD
# =====================================================

if page == "Dashboard":

    st.markdown("""
    <div class="hero">

    <h1>🌱 Crop Doctor</h1>

    <p>
    AI-powered crop disease detection and
    continuous crop health monitoring.
    </p>

    </div>
    """, unsafe_allow_html=True)

    history = load_history()

    total_scans = len(history)

    healthy = sum(
        1
        for r in history
        if r["disease"].lower() == "healthy"
    )

    issues = total_scans - healthy

    crops = len(
        set(
            r["crop"]
            for r in history
        )
    )

    # -------------------------------------------------
    # STATISTICS
    # -------------------------------------------------

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
            crops
        )

    st.divider()

    # -------------------------------------------------
    # FEATURES
    # -------------------------------------------------

    st.subheader(
        "🚀 Crop Doctor Features"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.info(
            """
            ### 🩺 AI Diagnosis

            Upload a leaf image and
            get an AI-based disease
            prediction.
            """
        )

    with c2:

        st.info(
            """
            ### 📊 Daily Monitoring

            Track diagnosis history
            and observe crop health
            over time.
            """
        )

    with c3:

        st.info(
            """
            ### 🩺 Management Advice

            Get management and
            prevention information
            for detected problems.
            """
        )

    st.divider()

    # -------------------------------------------------
    # SUPPORTED CROPS
    # -------------------------------------------------

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

        with crop_columns[i % 5]:

            st.write(
                f"🌱 **{crop}**"
            )


# =====================================================
# DIAGNOSIS
# =====================================================

elif page == "Diagnose":

    st.title(
        "🩺 Crop Diagnosis"
    )

    st.write(
        "Upload a clear photograph of a crop leaf."
    )

    uploaded_file = st.file_uploader(

        "📷 Choose leaf image",

        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )

    if uploaded_file:

        image = Image.open(
            uploaded_file
        ).convert("RGB")

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
                "🩺 Diagnose Crop",
                width="stretch"
            )

            if diagnose:

                with st.spinner(
                    "Analyzing crop..."
                ):

                    # ---------------------------------
                    # SAME PREPROCESSING AS predict.py
                    # ---------------------------------

                    img = image.resize(
                        IMAGE_SIZE
                    )

                    img_array = np.array(
                        img
                    )

                    # DO NOT NORMALIZE

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

                info = DISEASE_INFO.get(
                    predicted_class
                )

                # Save result

                add_record(
                    crop,
                    disease,
                    confidence
                )

                st.success(
                    "✅ Analysis Complete"
                )

                st.divider()

                r1, r2, r3 = st.columns(3)

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

                # ---------------------------------
                # DISEASE INFORMATION
                # ---------------------------------

                if info:

                    st.subheader(
                        "📋 Description"
                    )

                    st.write(
                        info["description"]
                    )

                    st.subheader(
                        "🔍 Symptoms"
                    )

                    for symptom in info[
                        "symptoms"
                    ]:

                        st.write(
                            f"• {symptom}"
                        )

                    st.subheader(
                        "🩺 Management"
                    )

                    for item in info[
                        "management"
                    ]:

                        st.write(
                            f"• {item}"
                        )

                    st.subheader(
                        "🛡️ Prevention"
                    )

                    for item in info[
                        "prevention"
                    ]:

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
                        "💡 For best results, use "
                        "a clear image with good lighting."
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
            "Diagnose a crop to create your first record."
        )

    else:

        # ---------------------------------------------
        # STATISTICS
        # ---------------------------------------------

        total = len(history)

        healthy = sum(
            1
            for r in history
            if r["disease"].lower() == "healthy"
        )

        issues = total - healthy

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

        # ---------------------------------------------
        # TREND
        # ---------------------------------------------

        st.subheader(
            "📈 AI Confidence Trend"
        )

        recent = history[-10:]

        confidence_values = [
            r["confidence"]
            for r in recent
        ]

        st.line_chart(
            confidence_values
        )

        st.caption(
            "Confidence values from recent diagnoses."
        )

        st.divider()

        # ---------------------------------------------
        # HISTORY
        # ---------------------------------------------

        st.subheader(
            "📅 Diagnosis History"
        )

        for record in reversed(
            history
        ):

            with st.container(
                border=True
            ):

                c1, c2, c3, c4 = st.columns(4)

                with c1:

                    st.write(
                        f"🕒 {record['date']}"
                    )

                with c2:

                    st.write(
                        f"🌱 {record['crop']}"
                    )

                with c3:

                    st.write(
                        f"🦠 {record['disease']}"
                    )

                with c4:

                    st.write(
                        f"🎯 {record['confidence']:.2f}%"
                    )

        st.divider()

        if st.button(
            "🗑️ Clear History"
        ):

            save_history([])

            st.success(
                "History cleared."
            )

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

    for class_name in class_names:

        # Skip healthy classes

        if "healthy" in class_name:

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
                    info["description"]
                )

                st.write(
                    "### 🔍 Symptoms"
                )

                for symptom in info[
                    "symptoms"
                ]:

                    st.write(
                        f"• {symptom}"
                    )

                st.write(
                    "### 🩺 Management"
                )

                for item in info[
                    "management"
                ]:

                    st.write(
                        f"• {item}"
                    )

                st.write(
                    "### 🛡️ Prevention"
                )

                for item in info[
                    "prevention"
                ]:

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
        "📊 Daily Monitoring"
    )

    st.write(
        """
        Diagnosis results are stored locally,
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
        "🌱 Crop Doctor — AI-assisted crop health monitoring"
    )