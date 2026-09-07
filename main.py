import streamlit as st
import tensorflow as tf
import numpy as np
import json
import os



from PIL import Image, UnidentifiedImageError
from datetime import datetime, date

import os as _os
_PROJECT_ROOT = _os.path.dirname(_os.path.abspath(__file__))

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

from language import t, render_language_selector, translate_text, translate_crop_name, translate_disease_name, get_translated_disease_info

from treatment import get_treatment

from demo import (
    render_sih_demo_banner,
    render_onboarding,
    render_ai_explanation,
    render_sample_images_gallery,
    get_top_predictions,
    get_voice_feedback_html,
    export_diagnosis_csv,
    export_raksha_csv,
    get_current_demo_step,
)
from ivr.ivr_app import render_anjaneya_voice

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

st.markdown(
    """
<style>

/* =======================================================
   LIGHT AGRICULTURAL DASHBOARD THEME
   Reference-style: clean, light, green accents
   ======================================================= */

/* Page background */
.stApp {
    background-color: #f7faf6;
}

.block-container {
    padding-top: 1.25rem;
    padding-bottom: 2.5rem;
    max-width: 1400px;
}

/* Hide the default Streamlit header strip for a more app-like feel */
#MainMenu {visibility: hidden;}
header[data-testid="stHeader"] {background: transparent;}

/* ---------- HERO (agricultural field gradient) ---------- */
.hero-wrap {
    position: relative;
    border-radius: 22px;
    overflow: hidden;
    margin-bottom: 22px;
    box-shadow: 0 8px 28px rgba(20,80,40,0.12);
}
.hero-bg {
    position: absolute;
    inset: 0;
    background:
        linear-gradient(135deg, rgba(20,80,40,0.78) 0%,
                          rgba(46,125,50,0.62) 55%,
                          rgba(102,187,106,0.25) 100%),
        linear-gradient(180deg, #a5d6a7 0%, #66bb6a 100%);
    background-blend-mode: multiply;
}
.hero-bg::after {
    content: "";
    position: absolute;
    right: -120px;
    top: -60px;
    width: 420px;
    height: 420px;
    background: radial-gradient(circle at 30% 30%,
                                rgba(255,255,255,0.25),
                                transparent 70%);
    border-radius: 50%;
}
.hero-bg::before {
    content: "";
    position: absolute;
    left: 30%;
    bottom: -200px;
    width: 700px;
    height: 260px;
    background:
        linear-gradient(0deg, rgba(46,125,50,0.35), transparent);
    border-radius: 50%;
    filter: blur(2px);
}
.hero-inner {
    position: relative;
    z-index: 2;
    padding: 38px 36px 32px 36px;
    color: #ffffff;
}
.hero-status {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.28);
    padding: 5px 12px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
    color: #f1f8e9;
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
}
.hero-status .dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #76ff7e;
    box-shadow: 0 0 8px #76ff7e;
}
.hero-welcome {
    font-size: 14px;
    color: rgba(255,255,255,0.85);
    margin: 14px 0 4px 0;
    font-weight: 500;
}
.hero-name {
    font-size: 36px;
    font-weight: 800;
    letter-spacing: -0.8px;
    margin: 0 0 10px 0;
    line-height: 1.15;
}
.hero-desc {
    font-size: 15px;
    line-height: 1.5;
    color: rgba(255,255,255,0.92);
    margin: 0 0 22px 0;
    max-width: 540px;
}
.hero-cta {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}
.hero-cta .stButton>button {
    background: #ffffff !important;
    color: #1b5e20 !important;
    font-weight: 700 !important;
    border: none !important;
    padding: 9px 18px !important;
    border-radius: 10px !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.18);
    transition: all 0.15s ease;
}
.hero-cta .stButton>button:hover {
    background: #f1f8e9 !important;
    transform: translateY(-1px);
}
.hero-cta .secondary button {
    background: transparent !important;
    color: #ffffff !important;
    border: 1.5px solid rgba(255,255,255,0.7) !important;
    box-shadow: none !important;
}
.hero-cta .secondary button:hover {
    background: rgba(255,255,255,0.12) !important;
}

/* ---------- KPI ROW ---------- */
.kpi-card {
    background: #ffffff;
    border-radius: 14px;
    padding: 16px 16px;
    border: 1px solid #e6efe6;
    box-shadow: 0 2px 10px rgba(20,80,40,0.04);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    height: 100%;
}
.kpi-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(20,80,40,0.10);
}
.kpi-icon {
    width: 38px;
    height: 38px;
    border-radius: 10px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    margin-bottom: 8px;
}
.kpi-icon.green  { background: #e8f5e9; color: #2e7d32; }
.kpi-icon.orange { background: #fff3e0; color: #ef6c00; }
.kpi-icon.red    { background: #ffebee; color: #c62828; }
.kpi-icon.blue   { background: #e3f2fd; color: #1565c0; }
.kpi-label {
    font-size: 12px;
    color: #6b7e6b;
    font-weight: 500;
    margin-bottom: 2px;
}
.kpi-value {
    font-size: 26px;
    font-weight: 800;
    color: #1b3a1f;
    line-height: 1.15;
}
.kpi-delta {
    font-size: 11px;
    color: #2e7d32;
    font-weight: 600;
    margin-top: 2px;
}
.kpi-delta.warn { color: #c62828; }

/* ---------- SECTION TITLE ---------- */
.section-title {
    font-size: 18px;
    font-weight: 800;
    color: #1b3a1f;
    margin: 8px 0 12px 2px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-title .dot {
    width: 8px; height: 8px;
    background: #2e7d32;
    border-radius: 50%;
}

/* ---------- AI MODULE CARDS ---------- */
.ai-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 20px 18px;
    border: 1px solid #e6efe6;
    box-shadow: 0 2px 12px rgba(20,80,40,0.05);
    height: 100%;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.ai-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 24px rgba(20,80,40,0.10);
}
.ai-icon {
    width: 44px; height: 44px;
    border-radius: 12px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    margin-bottom: 12px;
    color: #ffffff;
}
.ai-icon.green  { background: linear-gradient(135deg, #43a047, #66bb6a); }
.ai-icon.blue   { background: linear-gradient(135deg, #1e88e5, #26c6da); }
.ai-icon.orange { background: linear-gradient(135deg, #fb8c00, #ffb300); }
.ai-icon.purple { background: linear-gradient(135deg, #8e24aa, #d81b60); }
.ai-card h4 {
    font-size: 15px;
    font-weight: 700;
    color: #1b3a1f;
    margin: 0 0 4px 0;
}
.ai-card p {
    font-size: 12.5px;
    color: #5b6e5b;
    line-height: 1.45;
    margin: 0;
}

/* ---------- MONITORING + ANJANEYA (2 col) ---------- */
.panel-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 20px;
    border: 1px solid #e6efe6;
    box-shadow: 0 2px 12px rgba(20,80,40,0.05);
    height: 100%;
}
.panel-title {
    font-size: 15px;
    font-weight: 800;
    color: #1b3a1f;
    margin: 0 0 14px 0;
    display: flex;
    align-items: center;
    gap: 8px;
}
.panel-title .ico {
    width: 22px; height: 22px;
    border-radius: 6px;
    background: #e8f5e9;
    color: #2e7d32;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
}
.monitor-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 0;
    border-bottom: 1px solid #f1f5f0;
}
.monitor-row:last-child { border-bottom: none; }
.monitor-name {
    flex: 0 0 110px;
    font-size: 13px;
    color: #1b3a1f;
    font-weight: 600;
}
.monitor-bar {
    flex: 1;
    height: 7px;
    background: #e8f5e9;
    border-radius: 10px;
    overflow: hidden;
}
.monitor-fill {
    height: 100%;
    background: linear-gradient(90deg, #66bb6a, #2e7d32);
    border-radius: 10px;
}
.monitor-pct {
    flex: 0 0 40px;
    text-align: right;
    font-size: 12px;
    color: #2e7d32;
    font-weight: 700;
}
.anjaneya-mini {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    margin-bottom: 8px;
}
.anjaneya-icon {
    width: 46px; height: 46px;
    border-radius: 50%;
    background: linear-gradient(135deg, #43a047, #66bb6a);
    color: #fff;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    flex: 0 0 46px;
}
.anjaneya-mini h4 {
    font-size: 15px;
    font-weight: 700;
    color: #1b3a1f;
    margin: 0 0 4px 0;
}
.anjaneya-mini p {
    font-size: 12.5px;
    color: #5b6e5b;
    margin: 0;
    line-height: 1.4;
}
.anjaneya-btn .stButton>button {
    background: #2e7d32 !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    border: none !important;
    padding: 7px 14px !important;
    border-radius: 8px !important;
    width: 100%;
    margin-top: 10px;
}
.anjaneya-btn .stButton>button:hover {
    background: #1b5e20 !important;
}

/* ---------- SUPPORTED CROPS (image row) ---------- */
.crop-image-card {
    background: #ffffff;
    border-radius: 14px;
    padding: 8px 8px 10px 8px;
    border: 1px solid #e6efe6;
    box-shadow: 0 2px 10px rgba(20,80,40,0.05);
    text-align: center;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    height: 100%;
}
.crop-image-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 22px rgba(20,80,40,0.10);
}
.crop-image-card img {
    width: 100%;
    aspect-ratio: 4 / 3;
    object-fit: cover;
    border-radius: 10px;
    display: block;
    margin-bottom: 6px;
}
.crop-name {
    font-size: 13px;
    font-weight: 700;
    color: #1b3a1f;
    margin: 0;
}
.crop-count {
    font-size: 11px;
    color: #6b7e6b;
    margin: 1px 0 0 0;
}

/* ---------- FOOTER ---------- */
.app-footer {
    text-align: center;
    color: #6b7e6b;
    font-size: 12px;
    padding: 14px 0 4px 0;
    margin-top: 18px;
    border-top: 1px solid #e6efe6;
}

/* =======================================================
   WIDGET OVERRIDES — force light theme regardless of OS
   Explicit colours prevent browser/OS dark mode from
   inverting Streamlit's default widget styling.
   ======================================================= */

/* --- Buttons (general) --- */
.stButton>button {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
    border: 1px solid #e6efe6 !important;
    border-radius: 8px !important;
}

.stButton>button:hover {
    background-color: #f1f8e9 !important;
    color: #1b3a1f !important;
}

.stButton>button:active {
    background-color: #e8f5e9 !important;
    color: #1b3a1f !important;
}

/* --- Selectbox --- */
.stSelectbox>div>div {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

.stSelectbox div[role="listbox"] {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

/* --- Text Input --- */
.stTextInput>div>div>input {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

/* --- Text Area --- */
.stTextArea>div>div>textarea {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

/* --- Number Input --- */
.stNumberInput>div>div>input {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

/* --- Date Input --- */
.stDateInput>div>div>input {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

/* --- Time Input --- */
.stTimeInput>div>div>input {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

/* --- File Uploader --- */
.stFileUploader {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

.stFileUploader div[data-testid="stFileUploaderDropzone"] {
    background-color: #f7faf6 !important;
    border: 1px solid #e6efe6 !important;
    color: #1b3a1f !important;
}

/* --- Expander --- */
.stExpander>div {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

/* --- Tabs --- */
.stTabs>div>div {
    background-color: #ffffff !important;
}

.stTabs div[role="tab"] {
    color: #1b3a1f !important;
}

.stTabs div[aria-selected="true"] {
    color: #2e7d32 !important;
    border-bottom: 2px solid #2e7d32 !important;
}

/* --- Sidebar --- */
section[data-testid="stSidebar"] {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

section[data-testid="stSidebar"] div {
    color: #1b3a1f !important;
}

section[data-testid="stSidebar"] a {
    color: #2e7d32 !important;
}

/* --- Metric --- */
.stMetric>label {
    color: #6b7e6b !important;
}

.stMetric>div>div {
    color: #1b3a1f !important;
}

/* --- Alerts (Info, Success, Warning, Error) --- */
.stAlert {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

.stInfo {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

.stSuccess {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

.stWarning {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

.stError {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

/* --- Caption --- */
.stCaption {
    color: #6b7e6b !important;
}

/* --- Markdown --- */
.stMarkdown {
    color: #1b3a1f !important;
}

.stMarkdown a {
    color: #2e7d32 !important;
}

/* --- Table --- */
.stTable {
    color: #1b3a1f !important;
    background-color: #ffffff !important;
}

.stTable th {
    background-color: #e8f5e9 !important;
    color: #1b3a1f !important;
}

.stTable td {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

/* --- Checkbox --- */
.stCheckbox>div>label {
    color: #1b3a1f !important;
}

/* --- Radio --- */
.stRadio>div>label {
    color: #1b3a1f !important;
}

/* --- Multiselect --- */
.stMultiSelect>div>div {
    background-color: #ffffff !important;
    color: #1b3a1f !important;
}

/* --- Slider --- */
.stSlider>div>div {
    color: #2e7d32 !important;
}

/* --- Progress --- */
.stProgress>div>div>div {
    background-color: #2e7d32 !important;
}

/* --- Spinner --- */
.stSpinner>div {
    border-top-color: #2e7d32 !important;
}

/* --- Link --- */
a {
    color: #2e7d32 !important;
}

/* --- Horizontal Rule --- */
hr {
    border-color: #e6efe6 !important;
}

/* --- Code --- */
code {
    background-color: #f0f4f0 !important;
    color: #1b3a1f !important;
}

/* --- Pre --- */
pre {
    background-color: #f0f4f0 !important;
    color: #1b3a1f !important;
}

</style>
""",
    unsafe_allow_html=True,
)


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
    confidence,
    crop_id=None
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
            ),

        "crop_id": crop_id

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
        f"## 🌱 {t('app_name')}"
    )

    st.caption(t("ai_assistant"))

    st.divider()

    # ---- SIH DEMO MODE ----
    demo_step = render_sih_demo_banner()

    st.divider()

    # ---- ONBOARDING ----
    render_onboarding()

    st.divider()

    render_language_selector()

    st.divider()

    page_names = [
        "Dashboard",
        "Crop Registration",
        "Crop Raksha",
        "Anjaneya Voice",
        "Diagnose",
        "Monitoring",
        "Disease Library",
        "About"
    ]

    page_labels = [
        t("dashboard"),
        t("crop_registration"),
        t("crop_raksha"),
        t("anjaneya_voice"),
        t("diagnose"),
        t("monitoring"),
        t("disease_library"),
        t("about")
    ]

    _nav_default = 0
    _nav_target = st.session_state.pop("nav_target", None)
    if _nav_target and _nav_target in page_labels:
        _nav_default = page_labels.index(_nav_target)

    selected_page = option_menu(

        translate_text('Navigation'),

        page_labels,

        icons=[
            "house",
            "clipboard-plus",
            "shield-check",
            "telephone",
            "camera",
            "graph-up",
            "book",
            "info-circle"
        ],

        menu_icon="leaf",

        default_index=_nav_default
    )

    page = page_names[
        page_labels.index(selected_page)
    ]

    # ---- SIH DEMO MODE: auto-navigate ----
    demo_step = get_current_demo_step()
    if demo_step:
        page = demo_step.get("page", page)



    st.divider()

    st.caption(translate_text("AI-assisted crop health monitoring"))


# =====================================================
# DASHBOARD HELPERS
# =====================================================
import base64 as _b64


def _img_b64(path):
    """Encode a small image as a base64 data URI for inline HTML rendering."""
    try:
        with open(path, "rb") as f:
            data = f.read()
        return _b64.b64encode(data).decode("ascii")
    except Exception:
        return ""


# =====================================================
# DASHBOARD
# =====================================================

if page == "Dashboard":

    # Demo step overlay
    demo_step = get_current_demo_step()

    history = load_history()

    total_scans = len(history)

    healthy = sum(
        1
        for r in history
        if r["disease"].lower() == "healthy"
    )

    issues = total_scans - healthy

    crops_count = len(
        set(r["crop"] for r in history)
    )

    if total_scans > 0:
        health_pct = int(
            (healthy / total_scans) * 100
        )
    else:
        health_pct = 0

    # =====================================================
    # HERO (agricultural gradient with status pill)
    # =====================================================
    st.markdown(
        f"""
        <div class="hero-wrap">
          <div class="hero-bg"></div>
          <div class="hero-inner">
            <div class="hero-status">
              <span class="dot"></span>
              {t("ai_online")}
            </div>
            <div class="hero-welcome">{t("dashboard_welcome")}</div>
            <div class="hero-name">{t("dashboard_farmer_greeting")}</div>
            <div class="hero-desc">{t("dashboard_hero_subtitle")}</div>
            <div class="hero-cta">
        """,
        unsafe_allow_html=True,
    )

    hcol1, hcol2, _ = st.columns([1, 1, 4])
    with hcol1:
        st.markdown('<div class="hero-cta">', unsafe_allow_html=True)
        if st.button(
            f"🩺 {t('diagnose_crop')}",
            key="hero_diagnose_btn",
            use_container_width=True,
        ):
            st.session_state["nav_target"] = t("diagnose")
            st.rerun()
    with hcol2:
        st.markdown(
            '<div class="secondary">',
            unsafe_allow_html=True,
        )
        if st.button(
            f"📋 {t('view_recent_reports')}",
            key="hero_reports_btn",
            use_container_width=True,
        ):
            st.session_state["nav_target"] = t("monitoring")
            st.rerun()

    st.markdown("</div></div></div></div>", unsafe_allow_html=True)

    if demo_step:
        st.info(
            f"🎬 **{t('sih_demo_mode')}:** {t(demo_step['desc_key'])}"
        )

    # =====================================================
    # 4 KPI CARDS
    # =====================================================
    st.markdown(
        '<div class="section-title">'
        f'{t("dashboard_kpi_overview")}'
        '<span class="dot"></span></div>',
        unsafe_allow_html=True,
    )

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-icon green">🩺</div>
                <div class="kpi-label">{t("kpi_total_scans")}</div>
                <div class="kpi-value">{total_scans}</div>
                <div class="kpi-delta">↑ {t("kpi_tracked")}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with k2:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-icon orange">🌿</div>
                <div class="kpi-label">{t("kpi_healthy")}</div>
                <div class="kpi-value">{healthy}</div>
                <div class="kpi-delta">↑ {t("kpi_tracked")}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with k3:
        delta_class = "warn" if issues > 0 else ""
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-icon red">⚠️</div>
                <div class="kpi-label">{t("kpi_issues")}</div>
                <div class="kpi-value">{issues}</div>
                <div class="kpi-delta {delta_class}">
                  {t("needs_attention") if issues > 0 else t("all_clear")}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with k4:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-icon blue">📋</div>
                <div class="kpi-label">{t("kpi_crops")}</div>
                <div class="kpi-value">{crops_count}</div>
                <div class="kpi-delta">↑ {t("kpi_tracked")}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # =====================================================
    # AI INTELLIGENCE MODULES (4 cards in one row)
    # =====================================================
    st.markdown(
        '<div class="section-title">'
        f'{t("ai_intelligence_modules")}'
        '<span class="dot"></span></div>',
        unsafe_allow_html=True,
    )

    a1, a2, a3, a4 = st.columns(4)

    with a1:
        st.markdown(
            f"""
            <div class="ai-card">
                <div class="ai-icon green">🩺</div>
                <h4>{t("ai_diagnosis_feature")}</h4>
                <p>{t("ai_diagnosis_desc")}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with a2:
        st.markdown(
            f"""
            <div class="ai-card">
                <div class="ai-icon blue">🛡️</div>
                <h4>{t("crop_raksha_feature")}</h4>
                <p>{t("crop_raksha_desc")}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with a3:
        st.markdown(
            f"""
            <div class="ai-card">
                <div class="ai-icon orange">📈</div>
                <h4>{t("monitoring_short")}</h4>
                <p>{t("monitoring_desc")}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with a4:
        st.markdown(
            f"""
            <div class="ai-card">
                <div class="ai-icon purple">📚</div>
                <h4>{t("disease_library_short")}</h4>
                <p>{t("disease_library_desc")}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # =====================================================
    # MONITORING PROGRESS  |  ANJANEYA VOICE (2 cols)
    # =====================================================
    st.markdown(
        '<div class="section-title">'
        f'{t("monitoring_progress")}'
        '<span class="dot"></span></div>',
        unsafe_allow_html=True,
    )

    mon_l, mon_r = st.columns([7, 5])

    with mon_l:
        # Build per-crop rows based on history (top 4)
        rows_html = ""
        by_crop = {}
        for r in history:
            cname = r.get("crop", "—")
            dname = (r.get("disease", "") or "").lower()
            by_crop.setdefault(cname, [0, 0])
            by_crop[cname][0] += 1
            if dname == "healthy":
                by_crop[cname][1] += 1

        # If no history, fall back to class data
        if not by_crop:
            for c in class_names:
                crop_label = translate_crop_name(get_crop_name(c))
                rows_html += (
                    f'<div class="monitor-row">'
                    f'<div class="monitor-name">{crop_label}</div>'
                    f'<div class="monitor-bar">'
                    f'<div class="monitor-fill" style="width:100%;"></div>'
                    f'</div>'
                    f'<div class="monitor-pct">100%</div>'
                    f'</div>'
                )
        else:
            for crop_label, (n, h) in list(by_crop.items())[:4]:
                pct = int((h / n) * 100) if n else 0
                rows_html += (
                    f'<div class="monitor-row">'
                    f'<div class="monitor-name">{translate_crop_name(crop_label)}</div>'
                    f'<div class="monitor-bar">'
                    f'<div class="monitor-fill" style="width:{pct}%;"></div>'
                    f'</div>'
                    f'<div class="monitor-pct">{pct}%</div>'
                    f'</div>'
                )

        st.markdown(
            f"""
            <div class="panel-card">
                <div class="panel-title">
                    <span class="ico">📊</span>
                    {t("dashboard_crop_health")}
                </div>
                {rows_html or ''}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with mon_r:
        # Clickable button to launch Anjaneya
        st.markdown(
            f"""
            <div class="panel-card">
                <div class="anjaneya-mini">
                    <div class="anjaneya-icon">🎙️</div>
                    <div>
                        <h4>{t("anjaneya_card_title")}</h4>
                        <p>{t("anjaneya_card_desc")}</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<div class="anjaneya-btn">', unsafe_allow_html=True)
        if st.button(
            f"🎙️ {t('anjaneya_voice')}",
            key="dashboard_anjaneya_btn",
            use_container_width=True,
        ):
            st.session_state["nav_target"] = t("anjaneya_voice")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # SUPPORTED CROP SPECIES (image row)
    # =====================================================
    st.markdown(
        '<div class="section-title">'
        f'{t("supported_crop_species")}'
        '<span class="dot"></span></div>',
        unsafe_allow_html=True,
    )

    supported_crops = sorted(
        set(get_crop_name(c) for c in class_names)
    )

    # Build disease-count per crop for the caption
    crop_to_diseases = {}
    for c in class_names:
        crop_to_diseases.setdefault(get_crop_name(c), set()).add(c)

    # Resolve the images directory once, anchored to the project root
    # so the Dashboard works regardless of the user's CWD.
    _images_dir = _os.path.join(_PROJECT_ROOT, "demo_images", "dashboard")
    _image_cache = {}

    # Explicit, hard-coded crop -> dashboard image mapping.
    # The Dashboard MUST use these exact dashboard_*.jpg files. There is no
    # fallback search and no generic substitution.
    _crop_image_map = {
        "banana":   "dashboard_banana.jpg",
        "corn":     "dashboard_corn.jpg",
        "cotton":   "dashboard_cotton.jpg",
        "grape":    "dashboard_grape.jpg",
        "mango":    "dashboard_mango.jpg",
        "paddy":    "dashboard_paddy.jpg",
        "potato":   "dashboard_potato.jpg",
        "soybean":  "dashboard_soybean.jpg",
        "tomato":   "dashboard_tomato.jpg",
        "wheat":    "dashboard_wheat.jpg",
    }

    def _resolve_crop_image(crop):
        """Return an absolute path to the dashboard image for `crop`.

        The function looks up the explicit map above. If a crop has no
        mapping (or the file is missing), it returns None so the caller
        can render the card without an image rather than substituting a
        generic or diseased photo.
        """
        if not _os.path.isdir(_images_dir):
            return None
        key = crop.lower()
        chosen = _crop_image_map.get(key)
        if not chosen:
            return None
        candidate = _os.path.join(_images_dir, chosen)
        if _os.path.isfile(candidate):
            return candidate
        return None

    cols_per_row = 6
    for start in range(0, len(supported_crops), cols_per_row):
        row_crops = supported_crops[start:start + cols_per_row]
        row_cols = st.columns(len(row_crops))
        for i, crop in enumerate(row_crops):
            with row_cols[i]:
                if crop not in _image_cache:
                    _image_cache[crop] = _resolve_crop_image(crop)
                img_path = _image_cache[crop]
                diseases_n = len(crop_to_diseases.get(crop, []))
                img_b64 = _img_b64(img_path) if img_path else ""
                st.markdown(
                    f"""
                    <div class="crop-image-card">
                      <img src="data:image/jpeg;base64,{img_b64}" />
                      <p class="crop-name">{translate_crop_name(crop)}</p>
                      <p class="crop-count">{diseases_n} {t("diseases_tracked") if "diseases_tracked" in t.__globals__ else "diseases tracked"}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    # =====================================================
    # FOOTER
    # =====================================================
    st.markdown(
        f'<div class="app-footer">{t("footer_text")}</div>',
        unsafe_allow_html=True,
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
            t("farmer_name")
        )

        crop_name = st.selectbox(

            t("crop"),

            [
                translate_crop_name(c)
                for c in sorted(
                    set(
                        get_crop_name(c)
                        for c in class_names
                    )
                )
            ]
        )

        field_label = st.text_input(
            t("field_name"),
            placeholder=t("example_field")
        )

        sowing_date = st.date_input(
            t("sowing_date")
        )

        monitoring_time = st.time_input(
            t("daily_crop_raksha_time")
        )

        submitted = st.form_submit_button(
            t("register_crop")
        )

        if submitted:

            if not farmer_name.strip():

                st.error(
                    t("please_enter_farmer_name")
                )

            elif sowing_date > date.today():

                st.error(
                    t("date_not_future")
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
                    t("crop_registered_success")
                )

                st.write(
                    f"**{t('farmer_label')}** {farmer_name}"
                )

                st.write(
                    f"**{t('crop_label')}** {crop_name}"
                )

                st.write(
                    f"**{t('field_label')}** "
                    f"{field_label or t('not_specified')}"
                )

                st.write(
                    f"**{t('date_of_sowing')}** "
                    f"{sowing_date}"
                )

                st.write(
                    f"**{t('crop_raksha_time_label')}** "
                    f"{monitoring_time.strftime('%I:%M %p')}"
                )

                st.write(
                    f"**{t('crop_id_label')}** `{crop_id}`"
                )

    st.divider()

    st.subheader(t("my_registered_crops"))

    crops = load_crops()

    if not crops:

        st.info(t("no_crops_registered"))

    else:

        for crop in crops:

            with st.container(
                border=True
            ):

                # Translate crop_name for display while keeping internal storage
                display_crop_name = translate_crop_name(crop.get("crop_name", ""))
                display_field = crop.get("field_label", "")
                full_display = f"{display_crop_name} — {display_field}" if display_field else display_crop_name

                st.write(
                    f"### 🌱 {full_display}"
                )

                if crop.get(
                    "farmer_name"
                ):

                    st.write(
                        f"👨‍🌾 {t('farmer_label')} "
                        f"{crop['farmer_name']}"
                    )

                st.write(
                    f"{t('sowing_date_label')} "
                    f"{crop['sowing_date']}"
                )

                crop_age_value = days_since_sowing(crop['sowing_date'])
                st.write(
                    f"🌿 {t('crop_age')}: "
                    f"{crop_age_value} {t('crop_age_days')}"
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
                        f"{t('crop_raksha_time_field')} "
                        f"{formatted_time}"
                    )

                st.write(
                    f"{t('status_label')} "
                    f"{crop.get('status', 'unknown')}"
                )

                if st.button(
                    t("delete"),
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

    st.write(t('ai_crop_companion_monitoring'))

    st.divider()

    # =================================================
    # LOAD CROPS
    # =================================================

    crops = load_crops()

    if not crops:

        st.warning(t('no_crops_registered'))

        st.info(t('go_to_crop_registration'))

    else:

        active_crops = [
            crop
            for crop in crops
            if crop.get("status")
            == "active"
        ]

        if not active_crops:

            st.warning(t('no_active_crops'))

        else:

            # =================================================
            # SELECT CROP
            # =================================================

            # Build options with translated crop names for display
            crop_options = {}
            for crop in active_crops:
                translated_name = translate_crop_name(crop.get("crop_name", ""))
                field = crop.get("field_label", "")
                display = f"{translated_name} — {field}" if field else translated_name
                crop_options[display] = crop["id"]

            selected_crop_name = st.selectbox(
                t('select_your_crop'),
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

            st.subheader(t('crop_profile'))

            c1, c2, c3, c4 = st.columns(4)

            with c1:

                st.metric(
                    t("crop"),
                    translate_crop_name(selected_crop["crop_name"])
                )

            with c2:

                st.metric(
                    t("sowing_date"),
                    selected_crop["sowing_date"]
                )

            with c3:

                st.metric(
                    t("crop_age"),
                    f"{crop_age} {t('crop_age_days')}"
                )

            with c4:

                st.metric(
                    t("observations"),
                    len(records)
                )

            st.info(
                f"{t('daily_raksha_time_info')} **{display_time}**"
            )

            st.divider()

            # =================================================
            # CROP RAKSHA AI COMPANION
            # =================================================

            st.subheader(t('crop_raksha_ai_companion'))

            st.caption(t('companion_remembers_history'))

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
                    t("daily_crop_check", day=next_day)
                )

                st.write(t("record_today_condition"))

                uploaded_image = st.file_uploader(
                    t("upload_crops_photograph"),
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
                            caption=t("day_observation", day=next_day),
                            width="stretch"
                        )

                        st.divider()

                        if st.button(
                            t("save_day_observation", day=next_day),
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
                            heatmap = None
                            heatmap_path = None

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

                                    # Persist the heatmap so it survives
                                    # Streamlit reruns and can be shown
                                    # again from the monitoring timeline.
                                    if heatmap is not None:
                                        heatmap_filename = (
                                            f"{selected_crop_id}"
                                            f"_day_{next_day}_heatmap.jpg"
                                        )
                                        heatmap_path = os.path.join(
                                            "crop_raksha_images",
                                            heatmap_filename
                                        )
                                        heatmap.save(heatmap_path, "JPEG", quality=95)

                                except (
                                    OSError,
                                    UnidentifiedImageError
                                ):

                                    change_level = (
                                        "baseline"
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
                                        ai_confidence,

                                    heatmap_path=
                                        heatmap_path
                                )
                            )

                            # =================================
                            # RESULT
                            # =================================

                            st.success(t("observation_saved", day=record['day']))

                            st.divider()

                            # =================================
                            # VISUAL DIFFERENCE HEATMAP
                            # =================================

                            if (
                                    previous_record
                                    and heatmap is not None
                            ):

                                st.subheader(t("visual_change_heatmap"))

                                st.caption(t("bright_areas_caption"))

                                st.image(
                                    heatmap,
                                    caption=t("hotter_areas_caption"),
                                    width="stretch"
                                )

                                if difference is not None:
                                    st.info(
                                        f"{t('overall_visual_difference')} "
                                        f"**{difference:.2f}%**"
                                    )

                            st.subheader(t('crop_raksha_ai_assessment'))

                            if ai_result:

                                r1, r2, r3 = (
                                    st.columns(3)
                                )

                                with r1:

                                    st.metric(
                                        t("crop"),
                                        translate_crop_name(ai_result["crop"])
                                    )

                                with r2:

                                    st.metric(
                                        t("ai_result_label"),
                                        ai_result[
                                            "disease"
                                        ]
                                    )

                                with r3:

                                    st.metric(
                                        t("confidence"),
                                        f"{ai_result['confidence']:.2f}%"
                                    )

                            # =================================
                            # VISUAL CHANGE RESULT
                            # =================================

                            st.divider()

                            st.subheader(t("visual_change_analysis"))

                            if (
                                change_level
                                == "baseline"
                            ):

                                st.info(t("baseline_created_msg"))

                            else:

                                c1, c2 = (
                                    st.columns(2)
                                )

                                with c1:

                                    if difference is not None:

                                        st.metric(
                                            t('visual_difference_label'),
                                            f"{difference:.2f}%"
                                        )

                                with c2:

                                    if (
                                        change_level
                                        == "normal"
                                    ):

                                        st.success(t('normal'))

                                    elif (
                                        change_level
                                        == "minor_change"
                                    ):

                                        st.warning(t('minor_change'))

                                    elif (
                                        change_level
                                        == "significant_change"
                                    ):

                                        st.error(t('significant_change'))

                            # =================================
                            # CROP RAKSHA COMPANION MESSAGES
                            # =================================

                            st.divider()

                            st.subheader(t('crop_raksha_assessment'))

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

                                st.error(t("significant_change_detected_alert"))

                                st.warning(t("open_diagnose_section"))

                            elif (
                                change_level
                                in [
                                    "minor_change",
                                    "significant_change"
                                ]
                                and is_healthy
                            ):

                                st.warning(t("visual_change_noticed_healthy"))

                            elif is_healthy:

                                st.success(t("no_major_health_concern"))

                            else:

                                st.warning(t("possible_issue_detected"))

                            # Do not call st.rerun() here. The heatmap and
                            # assessment are rendered in this run. A forced
                            # rerun would immediately discard that UI output.

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
                        t("todays_check_complete", time=today_record['date'].split(" ")[1])
                    )

                else:

                    st.info(
                        t("check_not_due_yet", time=display_time)
                    )

            # =================================================
            # TIMELINE
            # =================================================

            st.divider()

            st.subheader(t("crop_raksha_timeline"))

            if not records:

                st.info(t("observations_appear_here"))

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
                                f"### {t('day_label')} "
                                f"{record['day']}"
                            )

                        with c2:

                            st.write(
                                f"🕒 "
                                f"{record['date']}"
                            )

                        with c3:

                            st.write(
                                f"{t('status_label')} "
                                f"**{record['status']}**"
                            )

                        st.write(
                            record["observation"]
                        )

                        if record.get(
                            "disease"
                        ):

                            st.caption(
                                f"{t('ai_caption')} "
                                f"{record['disease']} "
                                f"({record.get('confidence', 0):.1f}%)"
                            )

                        # Persisted visual-change map. This makes the heatmap
                        # available even after Streamlit reruns or navigation.
                        saved_heatmap_path = record.get("heatmap_path")
                        if saved_heatmap_path and os.path.exists(saved_heatmap_path):
                            with st.expander(t("view_heatmap")):
                                st.image(
                                    saved_heatmap_path,
                                    caption=t("hotter_areas_caption"),
                                    width="stretch"
                                )

                if shown < len(
                    ordered_records
                ):

                    if st.button(
                        t("show_more", shown=shown, total=len(ordered_records)),
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

elif page == "Anjaneya Voice":

    render_anjaneya_voice()


# =====================================================
# DIAGNOSIS
# =====================================================

elif page == "Diagnose":

    st.title(
        f"🩺 {t('crop_diagnosis')}"
    )

    st.write(t("upload_leaf"))

    registered_crops = load_crops()

    # Build crop link options with translated names
    diagnosis_crop_labels = {
        t("general_diagnosis"): None
    }
    for registered_crop in registered_crops:
        display_name_crop = display_name(registered_crop)
        # Translate the crop name in display
        translated_display = display_name_crop
        if registered_crop.get("crop_name"):
            translated_display = translate_crop_name(registered_crop.get("crop_name", ""))
            if registered_crop.get("field_label"):
                translated_display = f"{translated_display} — {registered_crop.get('field_label', '')}"
        diagnosis_crop_labels[translated_display] = registered_crop["id"]

    selected_diagnosis_crop = st.selectbox(
        t("link_diagnosis_crop"),
        list(diagnosis_crop_labels.keys()),
        key="diagnosis_crop_link"
    )

    diagnosis_crop_id = diagnosis_crop_labels[selected_diagnosis_crop]

    uploaded_file = st.file_uploader(

        f"📷 {t('choose_image')}",

        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )

    # =====================================================
    # SAMPLE IMAGES GALLERY
    # =====================================================
    render_sample_images_gallery()

    # =====================================================
    # AI ANALYSIS
    # =====================================================
    # Determine which image to use
    process_image = None

    # Check if diagnosis was just completed from a sample image (clear the flag)
    if st.session_state.get("sample_diagnose_completed"):
        if "auto_sample_data" in st.session_state:
            del st.session_state["auto_sample_data"]
        st.session_state.sample_diagnose_completed = False

    # Check if a sample image was selected from the gallery
    if "auto_sample_data" in st.session_state and st.session_state.get("auto_sample_data"):
        sample_data = st.session_state["auto_sample_data"]
        try:
            process_image = Image.open(sample_data["image_path"]).convert("RGB")
        except Exception:
            st.warning(t("sample_load_error", id=sample_data.get("id", "unknown")))
            process_image = None

    # If no sample image, use uploaded file
    if process_image is None and uploaded_file:
        process_image = safe_open_image(uploaded_file)

    if process_image is not None:

        col1, col2 = st.columns([1, 1])

        with col1:

            st.image(
                process_image,
                caption=t("uploaded_leaf"),
                width="stretch"
            )

        with col2:

            st.subheader(t('ai_analysis'))

            diagnose = st.button(
                f"🩺 {t('diagnose_crop')}",
                width="stretch",
                key="diagnose_btn"
            )

            # Check if this is a sample image diagnosis
            is_sample_diagnosis = "auto_sample_data" in st.session_state and st.session_state.get("auto_sample_data")

            if diagnose:

                with st.spinner(t("analyzing")):

                    ai_result = (
                        analyze_crop_image(
                            process_image
                        )
                    )

                # Mark sample diagnosis as completed (to clear state on next rerun)
                if is_sample_diagnosis:
                    st.session_state.sample_diagnose_completed = True

                if not ai_result:

                    st.error(t("upload_valid_rgb"))

                else:

                    crop = ai_result["crop"]

                    disease = ai_result["disease"]

                    confidence = ai_result["confidence"]

                    predicted_class = ai_result["class"]

                    info = DISEASE_INFO.get(predicted_class)

                    # Get top predictions for explanation
                    top_predictions = get_top_predictions(
                        model, process_image, class_names, top_n=5
                    )

                    # SAVE RESULT
                    add_record(
                        crop,
                        disease,
                        confidence,
                        crop_id=diagnosis_crop_id
                    )

                    st.success(t("analysis_complete"))

                    st.divider()

                    # ---- VOICE FEEDBACK ----
                    voice_html = get_voice_feedback_html(disease, confidence, crop)
                    st.components.v1.html(voice_html, height=80)

                    r1, r2, r3 = st.columns(3)

                    with r1:
                        st.metric(t("crop"), translate_crop_name(crop))

                    with r2:
                        st.metric(t("result"), disease)

                    with r3:
                        st.metric(t("confidence"), f"{confidence:.2f}%")

                    st.divider()

                    if info:

                        st.subheader(t("description"))

                        st.write(info["description"])

                        st.subheader(t("symptoms"))

                        for symptom in info["symptoms"]:
                            st.write(f"• {symptom}")

                        st.subheader(t("management"))

                        for item in info["management"]:
                            st.write(f"• {item}")

                        st.subheader(t("prevention"))

                        for item in info["prevention"]:
                            st.write(f"• {item}")

                    else:

                        st.warning(t("disease_info_not_available"))

                    # ---- TREATMENT RECOMMENDATION ----
                    # Skip treatment card for healthy predictions.
                    if "healthy" not in predicted_class.lower():
                        st.divider()

                        st.markdown(
                            f"<h3 style='color:#2e7d32;'>💊 {t('treatment_recommendation')}</h3>",
                            unsafe_allow_html=True
                        )

                        treatment_info = get_treatment(predicted_class)

                        if treatment_info:

                            st.markdown(
                                """
                                <style>
                                .treatment-card {
                                    padding: 20px;
                                    border-radius: 16px;
                                    background: linear-gradient(135deg, #f1f8e9, #ffffff);
                                    border: 1px solid #c5e1a5;
                                    margin-bottom: 15px;
                                }
                                .treatment-row {
                                    padding: 10px 0;
                                    border-bottom: 1px solid #e0e0e0;
                                }
                                .treatment-row:last-child {
                                    border-bottom: none;
                                }
                                .treatment-label {
                                    font-weight: 600;
                                    color: #33691e;
                                    margin-bottom: 4px;
                                }
                                .treatment-value {
                                    color: #424242;
                                    font-size: 15px;
                                }
                                </style>
                                """,
                                unsafe_allow_html=True
                            )

                            st.markdown(
                                f"""
                                <div class="treatment-card">
                                    <div class="treatment-row">
                                        <div class="treatment-label">🌿 {t("fertilizer_nutrient")}</div>
                                        <div class="treatment-value">{treatment_info.get("fertilizer", "—")}</div>
                                    </div>
                                    <div class="treatment-row">
                                        <div class="treatment-label">📏 {t("fertilizer_quantity")}</div>
                                        <div class="treatment-value">{treatment_info.get("fertilizer_quantity", "—")}</div>
                                    </div>
                                    <div class="treatment-row">
                                        <div class="treatment-label">🧪 {t("pesticide_treatment")}</div>
                                        <div class="treatment-value">{treatment_info.get("pesticide", "—")}</div>
                                    </div>
                                    <div class="treatment-row">
                                        <div class="treatment-label">📏 {t("pesticide_quantity")}</div>
                                        <div class="treatment-value">{treatment_info.get("pesticide_quantity", "—")}</div>
                                    </div>
                                    <div class="treatment-row">
                                        <div class="treatment-label">📝 {t("treatment_description")}</div>
                                        <div class="treatment-value">{treatment_info.get("description", "—")}</div>
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        else:

                            st.info(t("treatment_not_available"))

                    # ---- AI EXPLANATION ----
                    if top_predictions:
                        render_ai_explanation(
                            predicted_class,
                            confidence,
                            top_predictions,
                            crop
                        )

                    # Low confidence warning
                    if confidence < 60:
                        st.warning(t("low_confidence"))
                    else:
                        st.info(t("best_results"))


# =====================================================
# MONITORING
# =====================================================

elif page == "Monitoring":

    st.title(
        t("crop_health_monitoring")
    )

    history = load_history()

    if not history:

        st.info(
            t("no_monitoring_data")
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
                t("total_scans"),
                total
            )

        with b:

            st.metric(
                translate_text('🌱 Healthy'),
                healthy
            )

        with c:

            st.metric(
                translate_text('🦠 Issues'),
                issues
            )

        st.divider()

        st.subheader(
            t("confidence_trend")
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
            t("confidence_values_recent")
        )

        st.divider()

        st.subheader(
            t("diagnosis_history")
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
                        f"{t('monitoring_record_date')}: "
                        f"{record['date']}"
                    )

                with c2:

                    st.write(
                        f"🌱 "
                        f"{t('monitoring_record_crop')}: "
                        f"{translate_crop_name(record['crop'])}"
                    )

                with c3:

                    st.write(
                        f"🦠 "
                        f"{t('monitoring_record_disease')}: "
                        f"{record['disease']}"
                    )

                with c4:

                    st.write(
                        f"🎯 "
                        f"{t('monitoring_record_confidence')}: "
                        f"{record['confidence']:.2f}%"
                    )

        if shown < len(
            ordered_history
        ):

            if st.button(
                t(
                    "show_more_monitoring",
                    shown=shown,
                    total=len(ordered_history)
                )
            ):

                st.session_state[
                    "monitoring_shown"
                ] += PAGE_SIZE

                st.rerun()

        st.divider()

        # ---- DIAGNOSIS EXPORT ----
        st.subheader(t("export_diagnosis_records"))

        col_exp1, col_exp2 = st.columns(2)

        with col_exp1:
            csv_data = export_diagnosis_csv()
            if csv_data:
                st.download_button(
                    t("download_diagnosis_csv"),
                    csv_data.encode("utf-8"),
                    file_name="crop_doctor_diagnoses.csv",
                    mime="text/csv",
                    use_container_width=True,
                )
            else:
                st.info(t("no_diagnosis_records"))

        with col_exp2:
            raksha_csv = export_raksha_csv()
            if raksha_csv:
                st.download_button(
                    t("download_raksha_csv"),
                    raksha_csv.encode("utf-8"),
                    file_name="crop_raksha_observations.csv",
                    mime="text/csv",
                    use_container_width=True,
                )
            else:
                st.info(t("no_raksha_records"))

        st.caption(
            t("csv_share_note")
        )

        st.divider()

        confirm_clear = st.checkbox(
            t("clear_history_confirm")
        )

        if st.button(
            t("clear_history"),
            disabled=not confirm_clear
        ):

            if save_history([]):

                st.success(
                    t("history_cleared")
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
        t("disease_library")
    )

    st.write(
        t("explore_diseases")
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

        # Translate crop name and disease name for display
        crop_display = translate_crop_name(crop)
        disease_display = translate_disease_name(class_name)

        # Get translated disease info (description, symptoms, etc.)
        # Falls back to English from DISEASE_INFO if no translation
        # is available. Internal disease IDs are NOT modified.
        info = get_translated_disease_info(class_name)

        with st.expander(
            f"🌱 {crop_display} — 🦠 {disease_display}"
        ):

            if info:

                st.write(
                    t("description")
                )

                st.write(
                    info[
                        "description"
                    ]
                )

                st.write(
                    t("symptoms")
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
                    t("management")
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
                    t("prevention")
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
                    t("information_not_available")
                )


# =====================================================
# ABOUT
# =====================================================

elif page == "About":

    st.title(
        t("about_crop_doctor")
    )

    st.write(
        t("about_crop_doctor_description")
    )

    st.subheader(
        t("ai_detection")
    )

    st.write(
        t("about_ai_detection_desc")
    )

    st.subheader(
        t("about_crop_raksha")
    )

    st.write(
        t("about_crop_raksha_desc")
    )

    st.subheader(
        t("visual_change_heatmap_about")
    )

    st.write(
        t("about_visual_change_desc")
    )

    st.subheader(
        t("daily_monitoring_about")
    )

    st.write(
        t("about_daily_monitoring_desc")
    )

    st.subheader(t("about_sih_title"))
    st.success(f"""
    {t("about_sih_why_crop_doctor_wins")}

    {t("about_sih_real_farmer_value")}

    {t("about_sih_multilingual")}

    {t("about_sih_voice_first")}

    {t("about_sih_offline_first")}

    {t("about_sih_time_aware")}

    {t("about_sih_honest_ai")}

    {t("about_sih_exportable")}

    {t("about_sih_production_grade")}
    """)

    st.subheader(t("about_tech_stack"))
    st.markdown(f"""
    {t("about_tech_ai_model")}
    {t("about_tech_ui")}
    {t("about_tech_voice_ivr")}
    {t("about_tech_image")}
    {t("about_tech_languages")}
    {t("about_tech_storage")}
    """)

    st.subheader(
        t("supported_crops")
    )

    for crop in sorted(
        set(
            get_crop_name(c)
            for c in class_names
        )
    ):

        st.write(
            f"• {translate_crop_name(crop)}"
        )

    st.divider()

    st.caption(
        t("app_name") + " — " + translate_text("AI-assisted crop health monitoring")
    )