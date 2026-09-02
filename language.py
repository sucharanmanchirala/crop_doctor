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
# COMPREHENSIVE TRANSLATIONS
# =====================================================

TRANSLATIONS = {

    # -------------------------------------------------
    # COMMON UI
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

    # -------------------------------------------------
    # NAVIGATION
    # -------------------------------------------------

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
    # DIAGNOSIS PAGE
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

    "analyzing": {
        "en": "Analyzing crop...",
        "te": "పంటను విశ్లేషిస్తోంది...",
        "hi": "फसल का विश्लेषण जारी है...",
        "mr": "पीकाचे विश्लेषण सुरू आहे..."
    },

    "analysis_complete": {
        "en": "✅ Analysis Complete",
        "te": "✅ విశ్లేషణ పూర్తయింది",
        "hi": "✅ विश्लेषण पूरा हुआ",
        "mr": "✅ विश्लेषण पूर्ण झाले"
    },

    "crop": {
        "en": "🌱 Crop",
        "te": "🌱 పంట",
        "hi": "🌱 फसल",
        "mr": "🌱 पीक"
    },

    "result": {
        "en": "🦠 Result",
        "te": "🦠 ఫలితం",
        "hi": "🦠 परिणाम",
        "mr": "🦠 परिणाम"
    },

    "confidence": {
        "en": "🎯 Confidence",
        "te": "🎯 నమ్మక స్థాయి",
        "hi": "🎯 विश्वास स्तर",
        "mr": "🎯 विश्वास पातळी"
    },

    "healthy": {
        "en": "Healthy",
        "te": "ఆరోగ్యంగా ఉంది",
        "hi": "स्वस्थ",
        "mr": "निरोगी"
    },

    "description": {
        "en": "📋 Description",
        "te": "📋 వివరణ",
        "hi": "📋 विवरण",
        "mr": "📋 वर्णन"
    },

    "symptoms": {
        "en": "🔍 Symptoms",
        "te": "🔍 లక్షణాలు",
        "hi": "🔍 लक्षण",
        "mr": "🔍 लक्षणे"
    },

    "management": {
        "en": "🩺 Management",
        "te": "🩺 నిర్వహణ",
        "hi": "🩺 प्रबंधन",
        "mr": "🩺 व्यवस्थापन"
    },

    "prevention": {
        "en": "🛡️ Prevention",
        "te": "🛡️ నివారణ",
        "hi": "🛡️ रोकथाम",
        "mr": "🛡️ प्रतिबंध"
    },

    "low_confidence": {
        "en": "⚠️ Low confidence. Try a clearer leaf image.",
        "te": "⚠️ తక్కువ నమ్మకం. స్పష్టమైన ఆకు ఫోటోను ప్రయత్నించండి.",
        "hi": "⚠️ कम विश्वास। स्पष्ट पत्ते की तस्वीर लें।",
        "mr": "⚠️ कमी विश्वास. स्पष्ट पानाचा फोटो घ्या."
    },

    "best_results": {
        "en": "💡 For best results, use a clear image with good lighting.",
        "te": "💡 ఉత్తమ ఫలితాల కోసం, మంచి కాంతితో స్పష్టమైన ఇమేజ్ ఉపయోగించండి.",
        "hi": "💡 सर्वोत्तम परिणामों के लिए, अच्छी रोशनी के साथ स्पष्ट तस्वीर लें।",
        "mr": "💡 सर्वोत्तम परिणामांसाठी, चांगल्या प्रकाशासह स्पष्ट चित्र वापरा."
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

    "baseline_created": {
        "en": "🌱 Baseline created",
        "te": "🌱 ప్రాథమిక పరిశీలన సృష్టించబడింది",
        "hi": "🌱 प्रारंभिक अवलोकन बनाया गया",
        "mr": "🌱 प्रारंभिक निरीक्षण तयार केले"
    },

    "normal_change": {
        "en": "🟢 No significant visual change detected",
        "te": "🟢 గణనీయమైన దృశ్య మార్పు గుర్తించబడలేదు",
        "hi": "🟢 कोई महत्वपूर्ण दृश्य परिवर्तन नहीं मिला",
        "mr": "🟢 लक्षणीय दृश्य बदल आढळला नाही"
    },

    "minor_change": {
        "en": "🟠 A small visual change was detected",
        "te": "🟠 చిన్న దృశ్య మార్పు గుర్తించబడింది",
        "hi": "🟠 एक छोटा दृश्य परिवर्तन पाया गया",
        "mr": "🟠 थोडा दृश्य बदल आढळला"
    },

    "significant_change": {
        "en": "🔴 A significant visual change was detected",
        "te": "🔴 గణనీయమైన దృశ్య మార్పు గుర్తించబడింది",
        "hi": "🔴 एक महत्वपूर्ण दृश्य परिवर्तन पाया गया",
        "mr": "🔴 लक्षणीय दृश्य बदल आढळला"
    },

    "continue_monitoring": {
        "en": "Continue monitoring your crop.",
        "te": "మీ పంటను పర్యవేక్షించడం కొనసాగించండి.",
        "hi": "अपनी फसल की निगरानी जारी रखें।",
        "mr": "आपल्या पिकाचे निरीक्षण सुरू ठेवा."
    },

    "talk_to_raksha": {
        "en": "💬 Talk to Crop Raksha...",
        "te": "💬 క్రాప్ రక్ష తో మాట్లాడండి...",
        "hi": "💬 क्रॉप रक्षा से बातचीत करें...",
        "mr": "💬 क्रॉप रक्षा शी बोला..."
    },

    # -------------------------------------------------
    # GENERAL TERMS
    # -------------------------------------------------

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

    "day": {
        "en": "Day",
        "te": "రోజు",
        "hi": "दिन",
        "mr": "दिवस"
    },

    "ai_result": {
        "en": "AI Result",
        "te": "AI ఫలితం",
        "hi": "AI परिणाम",
        "mr": "AI परिणाम"
    },

    "select_language": {
        "en": "🌐 Select Language",
        "te": "🌐 భాషను ఎంచుకోండి",
        "hi": "🌐 भाषा चुनें",
        "mr": "🌐 भाषा निवडा"
    },

    # -------------------------------------------------
    # MONITORING PAGE
    # -------------------------------------------------

    "crop_health_monitoring": {
        "en": "📊 Crop Health Monitoring",
        "te": "📊 పంట ఆరోగ్య పర్యవేక్షణ",
        "hi": "📊 फसल स्वास्थ्य निगरानी",
        "mr": "📊 पीक आरोग्य निरीक्षण"
    },

    "no_monitoring_data": {
        "en": "No monitoring data yet. Diagnose a crop to create your first record.",
        "te": "ఇంకా పర్యవేక్షణ డేటా లేదు. మీ మొదటి రికార్డ్ సృష్టించడానికి పంటను నిర్ధారించండి.",
        "hi": "अभी तक कोई निगरानी डेटा नहीं है। अपना पहला रिकॉर्ड बनाने के लिए फसल की जांच करें।",
        "mr": "अद्याप कोणतेही निरीक्षण डेटा नाही. आपला पहिला रिकॉर्ड तयार करण्यासाठी पिकाचे निदान करा."
    },

    "total_scans": {
        "en": "🔬 Total Scans",
        "te": "🔬 మొత్తం స్కాన్‌లు",
        "hi": "🔬 कुल स्कैन",
        "mr": "🔬 एकूण स्कॅन्स"
    },

    "issues_detected": {
        "en": "🦠 Issues Detected",
        "te": "🦠 గుర్తించిన సమస్యలు",
        "hi": "🦠 समस्याएं पाई गईं",
        "mr": "🦠 समस्या आढळल्या"
    },

    "crops_monitored": {
        "en": "🌾 Crops Monitored",
        "te": "🌾 పర్యవేక్షణ చేసిన పంటలు",
        "hi": "🌾 निगरानी वाली फसलें",
        "mr": "🌾 निरीक्षण केलेल्या पिकें"
    },

    "confidence_trend": {
        "en": "📈 AI Confidence Trend",
        "te": "📈 AI నమ్మక ధోరణి",
        "hi": "📈 AI विश्वास प्रवृत्ति",
        "mr": "📈 AI विश्वास प्रवृत्ती"
    },

    "diagnosis_history": {
        "en": "📅 Diagnosis History",
        "te": "📅 రోగ నిర్ధారణ చరిత్ర",
        "hi": "📅 निदान इतिहास",
        "mr": "📅 निदान इतिहास"
    },

    "clear_history": {
        "en": "🗑️ Clear History",
        "te": "🗑️ చరిత్ర తీసివేయండి",
        "hi": "🗑️ इतिहास साफ़ करें",
        "mr": "🗑️ इतिहास साफ करा"
    },

    "history_cleared": {
        "en": "History cleared.",
        "te": "చరిత్ర తీసివేయబడింది.",
        "hi": "इतिहास साफ़ कर दिया गया।",
        "mr": "इतिहास साफ केले."
    },

    # -------------------------------------------------
    # DISEASE LIBRARY
    # -------------------------------------------------

    "explore_diseases": {
        "en": "Explore supported crop diseases, symptoms, management and prevention.",
        "te": "సమర్థిత పంట వ్యాధులు, లక్షణాలు, నిర్వహణ మరియు నివారణను అన్వేషించండి.",
        "hi": "समर्थित फसल रोग, लक्षण, प्रबंधन और रोकथाम का अन्वेषण करें।",
        "mr": "समर्थित पीक रोग, लक्षणे, व्यवस्थापन आणि प्रतिबंध शोधा."
    },

    "information_not_available": {
        "en": "Information not available yet.",
        "te": "సమాచారం ఇంకా లేనట్లు ఉంది.",
        "hi": "जानकारी अभी तक उपलब्ध नहीं है।",
        "mr": "माहिती अद्याप उपलब्ध नाही."
    },

    # -------------------------------------------------
    # ABOUT PAGE
    # -------------------------------------------------

    "about_crop_doctor": {
        "en": "ℹ️ About Crop Doctor",
        "te": "ℹ️ క్రాప్ డాక్టర్ గురించి",
        "hi": "ℹ️ क्रॉप डॉक्टर के बारे में",
        "mr": "ℹ️ क्रॉप डॉक्टर बद्दल"
    },

    "ai_detection": {
        "en": "🤖 AI Detection",
        "te": "🤖 AI గుర్తింపు",
        "hi": "🤖 AI पहचान",
        "mr": "🤖 AI ओळख"
    },

    "offline_capable": {
        "en": "Works completely offline for farmer accessibility.",
        "te": "కృషకుల అందుబాటుకు సంపూర్ణంగా ఆఫ్‌లైన్‌లో పనిచేస్తుంది.",
        "hi": "किसानों की पहुंच के लिए पूरी तरह से ऑफलाइन काम करता है।",
        "mr": "शेतकऱ्यांच्या प्रवेशाकरिता पूर्णपणे ऑफलाइन कार्य करते."
    },

    "supported_crops": {
        "en": "🌾 Supported Crops",
        "te": "🌾 సమర్థిత పంటలు",
        "hi": "🌾 समर्थित फसलें",
        "mr": "🌾 समर्थित पिकें"
    },

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
    """Display language selector in sidebar."""

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
        t("select_language"),
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
