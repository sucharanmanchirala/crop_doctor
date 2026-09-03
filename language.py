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

    "anjaneya_voice": {
        "en": "🔱 Anjaneya Voice",
        "te": "🔱 ఆంజనేయ వాయిస్",
        "hi": "🔱 आंजनेय वॉइस",
        "mr": "🔱 आंजनेय व्हॉइस"
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




TEXT_TRANSLATIONS = {'AI-assisted crop health monitoring': {'en': 'AI-assisted crop health monitoring', 'te': 'AI సహాయంతో పంట ఆరోగ్య పర్యవేక్షణ', 'hi': 'AI-सहायित फसल स्वास्थ्य निगरानी', 'mr': 'AI-सहाय्यित पीक आरोग्य निरीक्षण'}, 'Navigation': {'en': 'Navigation', 'te': 'నావిగేషన్', 'hi': 'नेविगेशन', 'mr': 'नेव्हिगेशन'}, '🚀 Crop Doctor Features': {'en': '🚀 Crop Doctor Features', 'te': '🚀 క్రాప్ డాక్టర్ ఫీచర్లు', 'hi': '🚀 क्रॉप डॉक्टर सुविधाएँ', 'mr': '🚀 क्रॉप डॉक्टर वैशिष्ट्ये'}, '🌱 Healthy': {'en': '🌱 Healthy', 'te': '🌱 ఆరోగ్యంగా', 'hi': '🌱 स्वस्थ', 'mr': '🌱 निरोगी'}, '🦠 Issues': {'en': '🦠 Issues', 'te': '🦠 సమస్యలు', 'hi': '🦠 समस्याएँ', 'mr': '🦠 समस्या'}, 'Your AI crop companion for continuous daily monitoring.': {'en': 'Your AI crop companion for continuous daily monitoring.', 'te': 'నిరంతర రోజువారీ పర్యవేక్షణ కోసం మీ AI పంట సహాయకుడు.', 'hi': 'निरंतर दैनिक निगरानी के लिए आपका AI फसल सहायक।', 'mr': 'सतत दैनंदिन निरीक्षणासाठी तुमचा AI पीक सहाय्यक.'}, '🌱 No crops registered yet.': {'en': '🌱 No crops registered yet.', 'te': '🌱 ఇంకా పంటలు నమోదు కాలేదు.', 'hi': '🌱 अभी तक कोई फसल पंजीकृत नहीं है।', 'mr': '🌱 अद्याप कोणतीही पिके नोंदलेली नाहीत.'}, 'Go to Crop Registration and register your crop first.': {'en': 'Go to Crop Registration and register your crop first.', 'te': 'పంట నమోదు విభాగానికి వెళ్లి ముందుగా మీ పంటను నమోదు చేయండి.', 'hi': 'फसल पंजीकरण में जाकर पहले अपनी फसल पंजीकृत करें।', 'mr': 'पीक नोंदणीमध्ये जाऊन प्रथम तुमचे पीक नोंदवा.'}, 'No active crops found.': {'en': 'No active crops found.', 'te': 'క్రియాశీల పంటలు ఏవీ కనుగొనబడలేదు.', 'hi': 'कोई सक्रिय फसल नहीं मिली।', 'mr': 'कोणतीही सक्रिय पिके आढळली नाहीत.'}, '🌾 Select your crop': {'en': '🌾 Select your crop', 'te': '🌾 మీ పంటను ఎంచుకోండి', 'hi': '🌾 अपनी फसल चुनें', 'mr': '🌾 तुमचे पीक निवडा'}, '🌱 Crop Profile': {'en': '🌱 Crop Profile', 'te': '🌱 పంట వివరాలు', 'hi': '🌱 फसल प्रोफ़ाइल', 'mr': '🌱 पीक प्रोफाइल'}, "Let's record today's condition.": {'en': "Let's record today's condition.", 'te': 'ఈరోజు పంట పరిస్థితిని నమోదు చేద్దాం.', 'hi': 'आज की स्थिति दर्ज करें।', 'mr': 'आजची स्थिती नोंदवूया.'}, "📸 Upload today's crop photograph": {'en': "📸 Upload today's crop photograph", 'te': '📸 ఈరోజు పంట ఫోటోను అప్\u200cలోడ్ చేయండి', 'hi': '📸 आज की फसल की तस्वीर अपलोड करें', 'mr': '📸 आजच्या पिकाचा फोटो अपलोड करा'}, '🔬 AI Analysis': {'en': '🔬 AI Analysis', 'te': '🔬 AI విశ్లేషణ', 'hi': '🔬 AI विश्लेषण', 'mr': '🔬 AI विश्लेषण'}, '⚠️ Please upload a valid RGB leaf image — analysis could not be completed.': {'en': '⚠️ Please upload a valid RGB leaf image — analysis could not be completed.', 'te': '⚠️ చెల్లుబాటు అయ్యే RGB ఆకు చిత్రాన్ని అప్\u200cలోడ్ చేయండి — విశ్లేషణ పూర్తికాలేదు.', 'hi': '⚠️ मान्य RGB पत्ते की तस्वीर अपलोड करें — विश्लेषण पूरा नहीं हो सका।', 'mr': '⚠️ वैध RGB पानाचा फोटो अपलोड करा — विश्लेषण पूर्ण होऊ शकले नाही.'}, '📊 Visual Difference': {'en': '📊 Visual Difference', 'te': '📊 దృశ్య తేడా', 'hi': '📊 दृश्य अंतर', 'mr': '📊 दृश्य फरक'}, '🟢 Normal': {'en': '🟢 Normal', 'te': '🟢 సాధారణం', 'hi': '🟢 सामान्य', 'mr': '🟢 सामान्य'}, '🟠 Minor Change': {'en': '🟠 Minor Change', 'te': '🟠 స్వల్ప మార్పు', 'hi': '🟠 मामूली बदलाव', 'mr': '🟠 किरकोळ बदल'}, '🔴 Significant Change': {'en': '🔴 Significant Change', 'te': '🔴 గణనీయమైన మార్పు', 'hi': '🔴 महत्वपूर्ण बदलाव', 'mr': '🔴 लक्षणीय बदल'}, '🤖 Crop Raksha Assessment': {'en': '🤖 Crop Raksha Assessment', 'te': '🤖 క్రాప్ రక్ష అంచనా', 'hi': '🤖 क्रॉप रक्षा आकलन', 'mr': '🤖 क्रॉप रक्षा मूल्यांकन'}, '🤖 Crop Raksha AI Assessment': {'en': '🤖 Crop Raksha AI Assessment', 'te': '🤖 క్రాప్ రక్ష AI అంచనా', 'hi': '🤖 क्रॉप रक्षा AI आकलन', 'mr': '🤖 क्रॉप रक्षा AI मूल्यांकन'}, 'Hotter/brighter areas show where the current image differs most from the previous observation.': {'en': 'Hotter/brighter areas show where the current image differs most from the previous observation.', 'te': 'వేడి/ప్రకాశవంతమైన ప్రాంతాలు ప్రస్తుత చిత్రం మునుపటి పరిశీలనతో ఎక్కువగా భిన్నంగా ఉన్న ప్రాంతాలను చూపుతాయి.', 'hi': 'अधिक चमकीले क्षेत्र दिखाते हैं कि वर्तमान तस्वीर पिछली तस्वीर से कहाँ सबसे अधिक अलग है।', 'mr': 'उष्ण/प्रकाशमान भाग वर्तमान फोटो मागील निरीक्षणापेक्षा कुठे जास्त वेगळा आहे ते दाखवतात.'}, 'The previous observation image could not be loaded, so the visual heatmap could not be created.': {'en': 'The previous observation image could not be loaded, so the visual heatmap could not be created.', 'te': 'మునుపటి పరిశీలన చిత్రం లోడ్ కాలేదు, కాబట్టి దృశ్య హీట్\u200cమ్యాప్ రూపొందించలేకపోయాం.', 'hi': 'पिछली तस्वीर लोड नहीं हो सकी, इसलिए दृश्य हीटमैप नहीं बनाया जा सका।', 'mr': 'मागील निरीक्षणाचा फोटो लोड झाला नाही, त्यामुळे दृश्य हीटमॅप तयार करता आला नाही.'}, '🟠 Crop Raksha noticed a visual change, but the AI currently considers the crop healthy.': {'en': '🟠 Crop Raksha noticed a visual change, but the AI currently considers the crop healthy.', 'te': '🟠 క్రాప్ రక్ష దృశ్య మార్పును గుర్తించింది, కానీ AI ప్రస్తుతం పంటను ఆరోగ్యంగా పరిగణిస్తోంది.', 'hi': '🟠 क्रॉप रक्षा ने दृश्य परिवर्तन देखा, लेकिन AI अभी फसल को स्वस्थ मानता है।', 'mr': '🟠 क्रॉप रक्षा ने दृश्य बदल लक्षात घेतला, पण AI सध्या पीक निरोगी मानतो.'}, '🟢 Crop Raksha currently sees no major health concern.': {'en': '🟢 Crop Raksha currently sees no major health concern.', 'te': '🟢 క్రాప్ రక్ష ప్రస్తుతం పెద్ద ఆరోగ్య సమస్యను చూడడం లేదు.', 'hi': '🟢 क्रॉप रक्षा को अभी कोई बड़ी स्वास्थ्य चिंता नहीं दिख रही है।', 'mr': '🟢 क्रॉप रक्षा ला सध्या मोठी आरोग्याची चिंता दिसत नाही.'}, '🟠 The AI detected a possible issue. Consider using the Diagnose section for confirmation.': {'en': '🟠 The AI detected a possible issue. Consider using the Diagnose section for confirmation.', 'te': '🟠 AI ఒక సాధ్యమైన సమస్యను గుర్తించింది. నిర్ధారణ కోసం డయాగ్నోసిస్ విభాగాన్ని ఉపయోగించండి.', 'hi': '🟠 AI ने संभावित समस्या पहचानी। पुष्टि के लिए निदान अनुभाग का उपयोग करें।', 'mr': '🟠 AI ने संभाव्य समस्या ओळखली. पुष्टीसाठी निदान विभाग वापरा.'}, '🚨 Crop Raksha detected a significant visual change and the AI identified a possible crop health issue.': {'en': '🚨 Crop Raksha detected a significant visual change and the AI identified a possible crop health issue.', 'te': '🚨 క్రాప్ రక్ష గణనీయమైన దృశ్య మార్పును గుర్తించింది మరియు AI పంట ఆరోగ్య సమస్యను సూచించింది.', 'hi': '🚨 क्रॉप रक्षा ने महत्वपूर्ण दृश्य परिवर्तन पाया और AI ने संभावित फसल स्वास्थ्य समस्या पहचानी।', 'mr': '🚨 क्रॉप रक्षा ने लक्षणीय दृश्य बदल ओळखला आणि AI ने संभाव्य पीक आरोग्य समस्या दर्शवली.'}, '🩺 Please open the Diagnose section for a detailed assessment.': {'en': '🩺 Please open the Diagnose section for a detailed assessment.', 'te': '🩺 వివరమైన అంచనా కోసం నిర్ధారణ విభాగాన్ని తెరవండి.', 'hi': '🩺 विस्तृत जांच के लिए निदान अनुभाग खोलें।', 'mr': '🩺 सविस्तर तपासणीसाठी निदान विभाग उघडा.'}}

TEXT_TRANSLATIONS["🌾 Link diagnosis to a registered crop"] = {"en":"🌾 Link diagnosis to a registered crop","te":"🌾 నిర్ధారణను నమోదు చేసిన పంటకు లింక్ చేయండి","hi":"🌾 निदान को पंजीकृत फसल से जोड़ें","mr":"🌾 निदान नोंदणीकृत पिकाशी जोडा"}
TEXT_TRANSLATIONS["— General diagnosis (not linked to a crop) —"] = {"en":"— General diagnosis (not linked to a crop) —","te":"— సాధారణ నిర్ధారణ (పంటకు లింక్ చేయలేదు) —","hi":"— सामान्य जांच (फसल से लिंक नहीं) —","mr":"— सामान्य निदान (पिकाशी जोडलेले नाही) —"}
TEXT_TRANSLATIONS.update({'Your AI crop companion remembers your monitoring history and helps you understand what is happening over time.': {'en': 'Your AI crop companion remembers your monitoring history and helps you understand what is happening over time.', 'te': 'మీ AI పంట సహాయకుడు మీ పర్యవేక్షణ చరిత్రను గుర్తుంచుకుని కాలక్రమేణా ఏమి జరుగుతుందో అర్థం చేసుకోవడంలో సహాయపడుతుంది.', 'hi': 'आपका AI फसल सहायक आपकी निगरानी का इतिहास याद रखता है और समय के साथ क्या हो रहा है यह समझने में मदद करता है।', 'mr': 'तुमचा AI पीक सहाय्यक तुमचा निरीक्षण इतिहास लक्षात ठेवतो आणि कालांतराने काय घडत आहे हे समजून घेण्यास मदत करतो.'}, 'I understand this will permanently delete all diagnosis history.': {'en': 'I understand this will permanently delete all diagnosis history.', 'te': 'నా నిర్ధారణ చరిత్ర మొత్తం శాశ్వతంగా తొలగించబడుతుందని నాకు తెలుసు.', 'hi': 'मैं समझता हूँ कि इससे पूरा निदान इतिहास स्थायी रूप से हट जाएगा।', 'mr': 'मला समजते की यामुळे संपूर्ण निदान इतिहास कायमचा हटवला जाईल.'}, '🔥 Visual Change Analysis': {'en': '🔥 Visual Change Analysis', 'te': '🔥 దృశ్య మార్పు విశ్లేషణ', 'hi': '🔥 दृश्य परिवर्तन विश्लेषण', 'mr': '🔥 दृश्य बदल विश्लेषण'}, 'Information for this disease is not available yet.': {'en': 'Information for this disease is not available yet.', 'te': 'ఈ వ్యాధికి సంబంధించిన సమాచారం ఇంకా అందుబాటులో లేదు.', 'hi': 'इस रोग की जानकारी अभी उपलब्ध नहीं है।', 'mr': 'या रोगाची माहिती अद्याप उपलब्ध नाही.'}})

def translate_text(text, language=None):
    if language is None:
        language = st.session_state.get("language", "en")
    if language not in ("en", "te", "hi", "mr"):
        language = "en"
    value = TEXT_TRANSLATIONS.get(text)
    if value:
        return value.get(language, value.get("en", text))
    return text

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
