# ============================================================
# CROP DOCTOR - OFFLINE IVR SIMULATOR
# ============================================================

import streamlit as st
import os

from ivr_logic import (
    LANGUAGES,
    t,
    load_class_names,
    analyze_image,
    clean_disease_name,
    get_crop_history
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Crop Doctor - Offline IVR",
    page_icon="📞",
    layout="centered"
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    .block-container {
        max-width: 820px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .phone {
        border: 2px solid #333;
        border-radius: 30px;
        padding: 28px;
        background: #fafafa;
        box-shadow: 0 12px 35px rgba(0,0,0,0.12);
    }

    .call-header {
        text-align: center;
        font-size: 32px;
        font-weight: 800;
    }

    .call-status {
        text-align: center;
        font-size: 14px;
        opacity: 0.65;
        margin-bottom: 25px;
        letter-spacing: 1px;
    }

    .call-message {
        border-radius: 18px;
        padding: 20px;
        margin: 12px 0;
        background: white;
        border: 1px solid #ddd;
        font-size: 17px;
        line-height: 1.6;
    }

    .ivr-title {
        text-align: center;
        font-size: 26px;
        font-weight: 750;
        margin-bottom: 18px;
    }

    .keypad-title {
        text-align: center;
        font-size: 15px;
        opacity: 0.7;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "ivr_stage" not in st.session_state:
    st.session_state.ivr_stage = "welcome"

if "ivr_language" not in st.session_state:
    st.session_state.ivr_language = "en"

if "ivr_call_active" not in st.session_state:
    st.session_state.ivr_call_active = True

if "ivr_result" not in st.session_state:
    st.session_state.ivr_result = None

if "ivr_log" not in st.session_state:
    st.session_state.ivr_log = []


# ============================================================
# STATE FUNCTIONS
# ============================================================

def go_to(stage):

    st.session_state.ivr_stage = stage
    st.session_state.ivr_result = None


def choose_language(language):

    st.session_state.ivr_language = language
    st.session_state.ivr_stage = "main_menu"


def end_call():

    st.session_state.ivr_call_active = False
    st.session_state.ivr_stage = "ended"


def restart_call():

    st.session_state.ivr_stage = "welcome"
    st.session_state.ivr_language = "en"
    st.session_state.ivr_call_active = True
    st.session_state.ivr_result = None
    st.session_state.ivr_log = []


def repeat_current():

    st.rerun()


# ============================================================
# MODEL
# ============================================================

@st.cache_resource
def load_model():

    try:

        import tensorflow as tf

        project_root = os.path.dirname(
            os.path.dirname(__file__)
        )

        model_path = os.path.join(
            project_root,
            "models",
            "best_crop_doctor.keras"
        )

        if not os.path.exists(model_path):
            return None

        return tf.keras.models.load_model(model_path)

    except Exception:
        return None


model = load_model()
class_names = load_class_names()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="call-header">
        📞 Crop Doctor
    </div>

    <div class="call-status">
        ● CALL CONNECTED · OFFLINE IVR
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="phone">', unsafe_allow_html=True)


language = st.session_state.ivr_language


# ============================================================
# WELCOME
# ============================================================

if st.session_state.ivr_stage == "welcome":

    st.markdown(
        f"""
        <div class="call-message">
            👩‍🌾 <b>Crop Doctor:</b><br><br>
            {t("welcome", language)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="call-message">
            🔊 {t("language", language)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="keypad-title">SELECT LANGUAGE</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(2)

    languages = list(LANGUAGES.items())

    for index, (code, name) in enumerate(languages):

        with cols[index % 2]:

            if st.button(
                f"{index + 1}   {name}",
                key=f"language_{code}",
                use_container_width=True
            ):

                choose_language(code)
                st.rerun()


# ============================================================
# MAIN MENU
# ============================================================

elif st.session_state.ivr_stage == "main_menu":

    st.markdown(
        f"""
        <div class="ivr-title">
            🌱 {t("main_menu", language)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="call-message">
            🔊 {t("select", language)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="keypad-title">IVR KEYPAD</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # ROW 1
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            f"1️⃣  {t('diagnose', language)}",
            use_container_width=True
        ):

            go_to("diagnose")
            st.rerun()

    with col2:

        if st.button(
            f"2️⃣  {t('status', language)}",
            use_container_width=True
        ):

            go_to("status")
            st.rerun()

    # --------------------------------------------------------
    # ROW 2
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            f"3️⃣  {t('raksha', language)}",
            use_container_width=True
        ):

            go_to("raksha")
            st.rerun()

    with col2:

        if st.button(
            f"4️⃣  {t('help', language)}",
            use_container_width=True
        ):

            go_to("help")
            st.rerun()

    # --------------------------------------------------------
    # IVR CONTROLS
    # --------------------------------------------------------

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "🔁 9 Repeat",
            use_container_width=True
        ):

            repeat_current()

    with col2:

        if st.button(
            "📞 0 End Call",
            use_container_width=True
        ):

            end_call()
            st.rerun()

    with col3:

        if st.button(
            "ℹ️ Help",
            use_container_width=True
        ):

            go_to("help")
            st.rerun()


# ============================================================
# DIAGNOSIS
# ============================================================

elif st.session_state.ivr_stage == "diagnose":

    st.markdown(
        f"""
        <div class="ivr-title">
            🩺 {t("diagnose", language)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="call-message">
            🔊 {t("upload", language)}
        </div>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Upload Crop Image",
        type=["jpg", "jpeg", "png"],
        key="ivr_crop_image"
    )

    if uploaded_file is not None:

        st.image(
            uploaded_file,
            caption="Crop image",
            use_container_width=True
        )

        if st.button(
            "🔢 1  Analyze",
            type="primary",
            use_container_width=True
        ):

            if model is None:

                st.error(
                    "Crop Doctor model could not be loaded."
                )

            elif not class_names:

                st.error(
                    "class_names.json could not be loaded."
                )

            else:

                with st.spinner(
                    t("diagnosing", language)
                ):

                    result = analyze_image(
                        uploaded_file,
                        model,
                        class_names
                    )

                st.session_state.ivr_result = result

    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    result = st.session_state.ivr_result

    if result:

        class_name = result.get(
            "class_name",
            "Unknown"
        )

        confidence = result.get(
            "confidence",
            0
        )

        disease_name = clean_disease_name(
            class_name
        )

        st.divider()

        st.subheader(
            f"📢 {t('result', language)}"
        )

        if disease_name.lower() == "healthy":

            st.success(
                f"✅ {t('healthy', language)}"
            )

        elif disease_name.lower() == "unknown":

            st.warning(
                f"⚠️ {t('unknown', language)}"
            )

        else:

            st.warning(
                f"⚠️ {disease_name}"
            )

        st.metric(
            t("confidence", language),
            f"{confidence:.2f}%"
        )

        st.info(
            "💡 For detailed treatment and management, "
            "open Crop Diagnosis in the main Crop Doctor application."
        )

    # --------------------------------------------------------
    # NAVIGATION
    # --------------------------------------------------------

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "⬅️ Back",
            use_container_width=True
        ):

            go_to("main_menu")
            st.rerun()

    with col2:

        if st.button(
            "🔁 Repeat",
            use_container_width=True
        ):

            repeat_current()

    with col3:

        if st.button(
            "📴 End",
            use_container_width=True
        ):

            end_call()
            st.rerun()


# ============================================================
# STATUS
# ============================================================

elif st.session_state.ivr_stage == "status":

    st.markdown(
        f"""
        <div class="ivr-title">
            📊 {t("status_title", language)}
        </div>
        """,
        unsafe_allow_html=True
    )

    history = get_crop_history()

    if not history:

        st.info(
            t("no_records", language)
        )

    else:

        st.metric(
            t("records", language),
            len(history)
        )

        latest = history[-1]

        st.markdown(
            f"""
            <div class="call-message">
                📅 <b>Latest Observation</b><br><br>

                Day: {latest.get("day", "—")}<br>
                Status: {latest.get("status", "—")}<br>
                Disease: {latest.get("disease", "—")}<br>
                Confidence:
                {latest.get("confidence", "—")}%
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "⬅️ Back",
            use_container_width=True
        ):

            go_to("main_menu")
            st.rerun()

    with col2:

        if st.button(
            "🔁 Repeat",
            use_container_width=True
        ):

            repeat_current()

    with col3:

        if st.button(
            "📴 End",
            use_container_width=True
        ):

            end_call()
            st.rerun()


# ============================================================
# CROP RAKSHA
# ============================================================

elif st.session_state.ivr_stage == "raksha":

    st.markdown(
        f"""
        <div class="ivr-title">
            🛡️ {t("raksha_title", language)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="call-message">
            {t("raksha_message", language)}
        </div>
        """,
        unsafe_allow_html=True
    )

    history = get_crop_history()

    if history:

        st.success(
            f"🌱 {len(history)} monitoring observation(s) recorded."
        )

        latest = history[-1]

        st.write(
            f"**Latest status:** "
            f"{latest.get('status', 'Unknown')}"
        )

    else:

        st.info(
            t("no_records", language)
        )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "⬅️ Back",
            use_container_width=True
        ):

            go_to("main_menu")
            st.rerun()

    with col2:

        if st.button(
            "🔁 Repeat",
            use_container_width=True
        ):

            repeat_current()

    with col3:

        if st.button(
            "📴 End",
            use_container_width=True
        ):

            end_call()
            st.rerun()


# ============================================================
# HELP
# ============================================================

elif st.session_state.ivr_stage == "help":

    st.markdown(
        f"""
        <div class="ivr-title">
            ❓ {t("help", language)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="call-message">
            {t("help_message", language)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "⬅️  Main Menu",
        use_container_width=True
    ):

        go_to("main_menu")
        st.rerun()

    if st.button(
        "📴  End Call",
        use_container_width=True
    ):

        end_call()
        st.rerun()


# ============================================================
# CALL ENDED
# ============================================================

elif st.session_state.ivr_stage == "ended":

    st.markdown(
        f"""
        <div class="call-message">
            📞 <b>CALL ENDED</b><br><br>
            {t("call_ended", language)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "📞 Start New Call",
        type="primary",
        use_container_width=True
    ):

        restart_call()
        st.rerun()


# ============================================================
# CLOSE PHONE UI
# ============================================================

st.markdown(
    "</div>",
    unsafe_allow_html=True
)