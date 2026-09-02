# =====================================================
# CROP DOCTOR — OFFLINE LANGUAGE SYSTEM
# =====================================================

import streamlit as st


# =====================================================
# SUPPORTED LANGUAGES
# =====================================================

LANGUAGES = {
    "English": "en",
    "తెలుగు": "te",
    "हिन्दी": "hi",
    "मराठी": "mr"
}


# =====================================================
# TRANSLATIONS
# =====================================================

TRANSLATIONS = {

    # -------------------------------------------------
    # COMMON
    # -------------------------------------------------

    "app_name": {
        "en": "Crop Doctor",
        "te": "క్రాప్ డాక్టర్",
        "hi": "क्रॉप डॉक्टर",
        "mr": "क्रॉप डॉक्टर"
    },

    "ai_assistant": {
        "en": "AI Crop Health Assistant",
        "te": "AI పంట ఆరోగ్య సహాయకుడు",
        "hi": "AI फसल स्वास्थ्य सहायक",
        "mr": "AI पीक आरोग्य सहाय्यक"
    },

    "dashboard": {
        "en": "Dashboard",
        "te": "డ్యాష్‌బోర్డ్",
        "hi": "डैशबोर्ड",
        "mr": "डॅशबोर्ड"
    },

    "crop_registration": {
        "en": "Crop Registration",
        "te": "పంట నమోదు",
        "hi": "फसल पंजीकरण",
        "mr": "पीक नोंदणी"
    },

    "crop_raksha": {
        "en": "Crop Raksha",
        "te": "క్రాప్ రక్ష",
        "hi": "क्रॉप रक्षा",
        "mr": "क्रॉप रक्षा"
    },

    "diagnose": {
        "en": "Diagnose",
        "te": "వ్యాధి నిర్ధారణ",
        "hi": "रोग पहचान",
        "mr": "रोग निदान"
    },

    "monitoring": {
        "en": "Monitoring",
        "te": "పర్యవేక్షణ",
        "hi": "निगरानी",
        "mr": "निरीक्षण"
    },

    "disease_library": {
        "en": "Disease Library",
        "te": "వ్యాధుల లైబ్రరీ",
        "hi": "रोग पुस्तकालय",
        "mr": "रोग ग्रंथालय"
    },

    "about": {
        "en": "About",
        "te": "గురించి",
        "hi": "जानकारी",
        "mr": "माहिती"
    },

    # -------------------------------------------------
    # DIAGNOSIS
    # -------------------------------------------------

    "crop_diagnosis": {
        "en": "Crop Diagnosis",
        "te": "పంట వ్యాధి నిర్ధారణ",
        "hi": "फसल रोग पहचान",
        "mr": "पीक रोग निदान"
    },

    "upload_leaf": {
        "en": "Upload a clear photograph of a crop leaf.",
        "te": "పంట ఆకుకు సంబంధించిన స్పష్టమైన ఫోటోను అప్‌లోడ్ చేయండి.",
        "hi": "फसल के पत्ते की स्पष्ट तस्वीर अपलोड करें।",
        "mr": "पिकाच्या पानाचा स्पष्ट फोटो अपलोड करा."
    },

    "choose_image": {
        "en": "Choose leaf image",
        "te": "ఆకు చిత్రాన్ని ఎంచుకోండి",
        "hi": "पत्ते की तस्वीर चुनें",
        "mr": "पानाचा फोटो निवडा"
    },

    "diagnose_crop": {
        "en": "Diagnose Crop",
        "te": "పంటను నిర్ధారించండి",
        "hi": "फसल की जांच करें",
        "mr": "पिकाचे निदान करा"
    },

    "ai_analysis": {
        "en": "AI Analysis",
        "te": "AI విశ్లేషణ",
        "hi": "AI विश्लेषण",
        "mr": "AI विश्लेषण"
    },

    "analysis_complete": {
        "en": "Analysis Complete",
        "te": "విశ్లేషణ పూర్తయింది",
        "hi": "विश्लेषण पूरा हुआ",
        "mr": "विश्लेषण पूर्ण झाले"
    },

    "healthy": {
        "en": "Healthy",
        "te": "ఆరోగ్యంగా ఉంది",
        "hi": "स्वस्थ",
        "mr": "निरोगी"
    },

    "confidence": {
        "en": "Confidence",
        "te": "నమ్మక స్థాయి",
        "hi": "विश्वास स्तर",
        "mr": "विश्वास पातळी"
    },

    "description": {
        "en": "Description",
        "te": "వివరణ",
        "hi": "विवरण",
        "mr": "वर्णन"
    },

    "symptoms": {
        "en": "Symptoms",
        "te": "లక్షణాలు",
        "hi": "लक्षण",
        "mr": "लक्षणे"
    },

    "management": {
        "en": "Management",
        "te": "నివారణ / నిర్వహణ",
        "hi": "प्रबंधन",
        "mr": "व्यवस्थापन"
    },

    "prevention": {
        "en": "Prevention",
        "te": "నివారణ",
        "hi": "रोकथाम",
        "mr": "प्रतिबंध"
    },

    # -------------------------------------------------
    # CROP RAKSHA
    # -------------------------------------------------

    "daily_monitoring": {
        "en": "Daily Crop Monitoring",
        "te": "రోజువారీ పంట పర్యవేక్షణ",
        "hi": "दैनिक फसल निगरानी",
        "mr": "दैनंदिन पीक निरीक्षण"
    },

    "upload_today": {
        "en": "Upload today's crop photograph",
        "te": "ఈరోజు పంట ఫోటోను అప్‌లోడ్ చేయండి",
        "hi": "आज की फसल की तस्वीर अपलोड करें",
        "mr": "आजच्या पिकाचा फोटो अपलोड करा"
    },

    "save_observation": {
        "en": "Save Observation",
        "te": "పరిశీలనను సేవ్ చేయండి",
        "hi": "अवलोकन सहेजें",
        "mr": "निरीक्षण जतन करा"
    },

    "baseline": {
        "en": "Baseline created",
        "te": "ప్రాథమిక పరిశీలన సృష్టించబడింది",
        "hi": "प्रारंभिक अवलोकन बनाया गया",
        "mr": "प्रारंभिक निरीक्षण तयार केले"
    },

    "normal_change": {
        "en": "No significant visual change detected",
        "te": "గణనీయమైన దృశ్య మార్పు గుర్తించబడలేదు",
        "hi": "कोई महत्वपूर्ण दृश्य परिवर्तन नहीं मिला",
        "mr": "लक्षणीय दृश्य बदल आढळला नाही"
    },

    "minor_change": {
        "en": "A small visual change was detected",
        "te": "చిన్న దృశ్య మార్పు గుర్తించబడింది",
        "hi": "एक छोटा दृश्य परिवर्तन पाया गया",
        "mr": "थोडा दृश्य बदल आढळला"
    },

    "significant_change": {
        "en": "A significant visual change was detected",
        "te": "గణనీయమైన దృశ్య మార్పు గుర్తించబడింది",
        "hi": "एक महत्वपूर्ण दृश्य परिवर्तन पाया गया",
        "mr": "लक्षणीय दृश्य बदल आढळला"
    },

    "continue_monitoring": {
        "en": "Continue monitoring your crop.",
        "te": "మీ పంటను పర్యవేక్షించడం కొనసాగించండి.",
        "hi": "अपनी फसल की निगरानी जारी रखें।",
        "mr": "आपल्या पिकाचे निरीक्षण सुरू ठेवा."
    },

    # -------------------------------------------------
    # GENERAL
    # -------------------------------------------------

    "crop": {
        "en": "Crop",
        "te": "పంట",
        "hi": "फसल",
        "mr": "पीक"
    },

    "farmer": {
        "en": "Farmer",
        "te": "రైతు",
        "hi": "किसान",
        "mr": "शेतकरी"
    },

    "sowing_date": {
        "en": "Sowing Date",
        "te": "విత్తిన తేదీ",
        "hi": "बुवाई की तारीख",
        "mr": "पेरणीची तारीख"
    },

    "crop_age": {
        "en": "Crop Age",
        "te": "పంట వయస్సు",
        "hi": "फसल की आयु",
        "mr": "पिकाचे वय"
    },

    "observations": {
        "en": "Observations",
        "te": "పరిశీలనలు",
        "hi": "अवलोकन",
        "mr": "निरीक्षणे"
    },

    "status": {
        "en": "Status",
        "te": "స్థితి",
        "hi": "स्थिति",
        "mr": "स्थिती"
    },

    "help": {
        "en": "Help",
        "te": "సహాయం",
        "hi": "मदद",
        "mr": "मदत"
    },

    "select_language": {
        "en": "Select Language",
        "te": "భాషను ఎంచుకోండి",
        "hi": "भाषा चुनें",
        "mr": "भाषा निवडा"
    }
}


# =====================================================
# TRANSLATION FUNCTION
# =====================================================

def t(key, language=None):
    """
    Offline translation function.

    Example:

        t("dashboard", "te")

    No internet connection is required.
    """

    if language is None:
        language = st.session_state.get(
            "language",
            "en"
        )

    if language not in ["en", "te", "hi", "mr"]:
        language = "en"

    translation = TRANSLATIONS.get(key)

    if translation is None:
        return key

    return translation.get(
        language,
        translation.get("en", key)
    )


# =====================================================
# LANGUAGE SELECTOR
# =====================================================

def render_language_selector():

    language_names = list(
        LANGUAGES.keys()
    )

    current_code = st.session_state.get(
        "language",
        "en"
    )

    current_index = 0

    for index, name in enumerate(
        language_names
    ):

        if LANGUAGES[name] == current_code:
            current_index = index
            break

    selected_language = st.selectbox(
        "🌐 Language",
        language_names,
        index=current_index,
        key="language_selector"
    )

    st.session_state.language = (
        LANGUAGES[selected_language]
    )

    return st.session_state.language


# =====================================================
# LANGUAGE HELPERS
# =====================================================

def get_current_language():
    """Return the currently selected language code."""
    return st.session_state.get("language", "en")


def set_language(language_code):
    """Set the current language."""
    if language_code in ["en", "te", "hi", "mr"]:
        st.session_state.language = language_code
    else:
        st.session_state.language = "en"


def translate(key):
    """
    Short alias for the offline translation function.

    Example:
        translate("dashboard")
    """
    return t(key, get_current_language())