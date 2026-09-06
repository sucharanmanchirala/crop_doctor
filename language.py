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

    "select_language": {
        "en": "Select Language",
        "te": "భాషను ఎంచుకోండి",
        "hi": "भाषा चुनें",
        "mr": "भाषा निवडा"
    },

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
    # DEMO MODE / SIDEBAR
    # -------------------------------------------------

    "demo_mode": {
        "en": "Demo Mode",
        "te": "డెమో మోడ్",
        "hi": "डेमो मोड",
        "mr": "डेमो मोड"
    },

    "start_guided_tour": {
        "en": "🎬 Start Guided Tour",
        "te": "🎬 గైడెడ్ టూర్ ప్రారంభించండి",
        "hi": "🎬 गाइडेड टूर शुरू करें",
        "mr": "🎬 गाइडेड टूर सुरू करा"
    },

    "getting_started": {
        "en": "🚀 Getting Started",
        "te": "🚀 ప్రారంభించడం",
        "hi": "🚀 शुरू करना",
        "mr": "🚀 सुरू करणे"
    },

    "welcome_crop_doctor": {
        "en": "Welcome to Crop Doctor! 🌱",
        "te": "క్రాప్ డాక్టర్‌కు స్వాగతం! 🌱",
        "hi": "क्रॉप डॉक्टर में आपका स्वागत है! 🌱",
        "mr": "क्रॉप डॉक्टरमध्ये आपले स्वागत आहे! 🌱"
    },

    "how_to_get_started": {
        "en": "Here's how to get started:",
        "te": "ప్రారంభించడం ఎలా:",
        "hi": "शुरू कैसे करें:",
        "mr": "सुरू कसे करायचे:"
    },

    "step1_register_crop": {
        "en": "1️⃣ Register Your Crop",
        "te": "1️⃣ మీ పంటను నమోదు చేయండి",
        "hi": "1️⃣ अपनी फसल पंजीकृत करें",
        "mr": "1️⃣ तुमचे पीक नोंदवा"
    },

    "step1_register_desc": {
        "en": "→ Add your crop with sowing date",
        "te": "→ విత్తిన తేదీతో మీ పంటను జోడించండి",
        "hi": "→ बुवाई की तारीख के साथ अपनी फसल जोड़ें",
        "mr": "→ पेरणीच्या तारखेसह तुमचे पीक जोडा"
    },

    "step2_daily_monitoring": {
        "en": "2️⃣ Daily Monitoring",
        "te": "2️⃣ రోజువారీ పర్యవేక్షణ",
        "hi": "2️⃣ दैनिक निगरानी",
        "mr": "2️⃣ दैनिक निरीक्षण"
    },

    "step2_monitoring_desc": {
        "en": "→ Crop Raksha tracks changes over time",
        "te": "→ క్రాప్ రక్ష కాలక్రమేణా మార్పులను ట్రాక్ చేస్తుంది",
        "hi": "→ क्रॉप रक्षा समय के साथ बदलाव ट्रैक करता है",
        "mr": "→ क्रॉप रक्षा वेळेनुसार बदल ट्रॅक करतो"
    },

    "step3_ai_diagnosis": {
        "en": "3️⃣ AI Diagnosis",
        "te": "3️⃣ AI నిర్ధారణ",
        "hi": "3️⃣ AI जांच",
        "mr": "3️⃣ AI निदान"
    },

    "step3_diagnosis_desc": {
        "en": "→ Upload any leaf image for instant diagnosis",
        "te": "→ తక్షణ నిర్ధారణ కోసం ఏదైనా ఆకు చిత్రాన్ని అప్‌లోడ్ చేయండి",
        "hi": "→ तुरंत निदान के लिए कोई भी पत्ते की तस्वीर अपलोड करें",
        "mr": "→ त्वरित निदानासाठी कोणताही पानाचा फोटो अपलोड करा"
    },

    "step4_voice_assistant": {
        "en": "4️⃣ Voice Assistant",
        "te": "4️⃣ వాయిస్ అసిస్టెంట్",
        "hi": "4️⃣ वॉइस असिस्टेंट",
        "mr": "4️⃣ व्हॉइस असिस्टंट"
    },

    "step4_voice_desc": {
        "en": "→ Talk to Anjaneya in your language!",
        "te": "→ మీ భాషలో ఆంజనేయతో మాట్లాడండి!",
        "hi": "→ अपनी भाषा में आंजनेय से बात करें!",
        "mr": "→ तुमच्या भाषेत आंजनेयशी बोला!"
    },

    "step5_sample_images": {
        "en": "5️⃣ Try Sample Images",
        "te": "5️⃣ నమూనా చిత్రాలను ప్రయత్నించండి",
        "hi": "5️⃣ नमूना चित्र देखें",
        "mr": "5️⃣ नमूना प्रतिमा पहा"
    },

    "step5_sample_desc": {
        "en": "→ Click any sample in Diagnose for instant demo",
        "te": "→ తక్షణ డెమో కోసం నిర్ధారణలో ఏదైనా నమూనాను క్లిక్ చేయండి",
        "hi": "→ तुरंत डेमो के लिए निदान में किसी भी नमूने पर क्लिक करें",
        "mr": "→ त्वरित डेमोसाठी निदानात कोणताही नमूना क्लिक करा"
    },

    # -------------------------------------------------
    # SIH DEMO STEP TITLES & DESCRIPTIONS
    # -------------------------------------------------

    "demo_step1_title": {
        "en": "🌱 Welcome to Crop Doctor",
        "te": "🌱 క్రాప్ డాక్టర్‌కు స్వాగతం",
        "hi": "🌱 क्रॉप डॉक्टर में आपका स्वागत है",
        "mr": "🌱 क्रॉप डॉक्टरमध्ये आपले स्वागत आहे"
    },

    "demo_step1_desc": {
        "en": "AI-powered crop health monitoring for farmers. This dashboard shows your overall farm health summary.",
        "te": "రైతుల కోసం AI-ఆధారిత పంట ఆరోగ్య పర్యవేక్షణ. ఈ డ్యాష్‌బోర్డ్ మీ మొత్తం పంట ఆరోగ్య సారాంశంను చూపుతుంది.",
        "hi": "किसानों के लिए AI-आधारित फसल स्वास्थ्य निगरानी। यह डैशबोर्ड आपके समग्र खेत स्वास्थ्य सारांश दिखाता है।",
        "mr": "शेतकऱ्यांसाठी AI-आधारित पीक आरोग्य निरीक्षण. हा डॅशबोर्ड तुमच्या एकूण शेती आरोग्य सारांश दर्शवितो."
    },

    "demo_step2_title": {
        "en": "📋 Register Your Crops",
        "te": "📋 మీ పంటలను నమోదు చేయండి",
        "hi": "📋 अपनी फसलें पंजीकृत करें",
        "mr": "📋 तुमची पिके नोंदवा"
    },

    "demo_step2_desc": {
        "en": "Register your crops with sowing date and monitoring time. Each crop gets a unique ID for tracking.",
        "te": "విత్తిన తేదీ మరియు పర్యవేక్షణ సమయంతో మీ పంటలను నమోదు చేయండి. ప్రతి పంటకు ట్రాకింగ్ కోసం ప్రత్యేక ID లభిస్తుంది.",
        "hi": "बुवाई की तारीख और निगरानी समय के साथ अपनी फसलें पंजीकृत करें। प्रत्येक फसल को ट्रैकिंग के लिए एक अद्वितीय ID मिलता है।",
        "mr": "पेरणीची तारीख आणि निरीक्षण वेळेनिशी तुमची पिके नोंदवा. प्रत्येक पिकाला ट्रॅकिंगसाठी एक अद्वितीय ID मिळते."
    },

    "demo_step3_title": {
        "en": "🩺 AI Crop Diagnosis",
        "te": "🩺 AI పంట వ్యాధి నిర్ధారణ",
        "hi": "🩺 AI फसल रोग पहचान",
        "mr": "🩺 AI पीक रोग निदान"
    },

    "demo_step3_desc": {
        "en": "Upload any leaf photo and the AI will identify the disease. Try the 'Sample Images' section for instant demos!",
        "te": "ఏదైనా ఆకు ఫోటోను అప్‌లోడ్ చేయండి మరియు AI వ్యాధిని గుర్తిస్తుంది. తక్షణ డెమోల కోసం 'నమూనా చిత్రాల' విభాగాన్ని ప్రయత్నించండి!",
        "hi": "कोई भी पत्ते की तस्वीर अपलोड करें और AI रोग की पहचान करेगा। तुरंत डेमो के लिए 'नमूना चित्र' अनुभाग आज़माएं!",
        "mr": "कोणताही पानाचा फोटो अपलोड करा आणि AI रोगाची ओळख पटवेल. त्वरित डेमोसाठी 'नमूना प्रतिमा' विभाग वापरा!"
    },

    "demo_step4_title": {
        "en": "🛡️ Crop Raksha — Daily Monitoring",
        "te": "🛡️ క్రాప్ రక్ష — రోజువారీ పర్యవేక్షణ",
        "hi": "🛡️ क्रॉप रक्षा — दैनिक निगरानी",
        "mr": "🛡️ क्रॉप रक्षा — दैनंदिन निरीक्षण"
    },

    "demo_step4_desc": {
        "en": "Monitor your crop every day with visual comparisons. The AI detects changes over time and alerts you when something looks different.",
        "te": "దృశ్య పోలికలతో రోజువారీ మీ పంటను పర్యవేక్షించండి. AI కాలక్రమేణా మార్పులను గుర్తిస్తుంది మరియు ఏదైనా భిన్నంగా కనిపిస్తే మిమ్మల్ని హెచ్చరిస్తుంది.",
        "hi": "दृश्य तुलनाओं के साथ अपनी फसल की दैनिक निगरानी करें। AI समय के साथ बदलाव का पता लगाता है और जब कुछ अलग दिखता है तो आपको सूचित करता है।",
        "mr": "दृश्य तुलनांसह तुमच्या पिकाचे दैनंदिन निरीक्षण करा. AI वेळेनुसार बदल शोधतो आणि काहीतरी वेगळे दिसल्यास तुम्हाला सूचित करतो."
    },

    "demo_step5_title": {
        "en": "🔱 Anjaneya — Voice Assistant",
        "te": "🔱 ఆంజనేయ — వాయిస్ అసిస్టెంట్",
        "hi": "🔱 आंजनेय — वॉइस असिस्टेंट",
        "mr": "🔱 आंजनेय — व्हॉइस असिस्टंट"
    },

    "demo_step5_desc": {
        "en": "Call Anjaneya and speak in your language! Get crop status, start diagnoses, or check Crop Raksha — all by voice.",
        "te": "ఆంజనేయకు కాల్ చేసి మీ భాషలో మాట్లాడండి! పంట స్థితి పొందండి, నిర్ధారణలు ప్రారంభించండి, లేదా క్రాప్ రక్షను తనిఖీ చేయండి — అన్నీ వాయిస్‌తో.",
        "hi": "आंजनेय को कॉल करें और अपनी भाषा में बात करें! फसल की स्थिति प्राप्त करें, निदान शुरू करें, या क्रॉप रक्षा की जांच करें — सब कुछ वॉइस से।",
        "mr": "आंजनेयला कॉल करा आणि तुमच्या भाषेत बोला! पीक स्थिती मिळवा, निदान सुरू करा, किंवा क्रॉप रक्षा तपासा — सर्व व्हॉइसने."
    },

    "demo_step6_title": {
        "en": "📚 Disease Library",
        "te": "📚 వ్యాధుల లైబ్రరీ",
        "hi": "📚 रोग पुस्तकालय",
        "mr": "📚 रोग ग्रंथालय"
    },

    "demo_step6_desc": {
        "en": "Browse all supported diseases with symptoms, management tips, and prevention advice.",
        "te": "లక్షణాలు, నిర్వహణ చిట్కాలు మరియు నివారణ సలహాలతో అన్ని సమర్థిత వ్యాధులను బ్రౌజ్ చేయండి.",
        "hi": "लक्षण, प्रबंधन सुझाव और रोकथाम की सलाह के साथ सभी समर्थित रोगों को ब्राउज़ करें।",
        "mr": "लक्षणे, व्यवस्थापन टिप्स आणि प्रतिबंध सल्ल्यासह सर्व समर्थित रोग ब्राउझ करा."
    },

    "demo_step7_title": {
        "en": "📊 Diagnosis History",
        "te": "📊 నిర్ధారణ చరిత్ర",
        "hi": "📊 निदान इतिहास",
        "mr": "📊 निदान इतिहास"
    },

    "demo_step7_desc": {
        "en": "Track all your AI diagnoses over time with confidence trends and exportable reports.",
        "te": "నమ్మక ధోరణులు మరియు ఎగుమతి చేయదగిన నివేదికలతో కాలక్రమేణా అన్ని AI నిర్ధారణలను ట్రాక్ చేయండి.",
        "hi": "विश्वास रुझानों और निर्यात योग्य रिपोर्टों के साथ समय के साथ अपने सभी AI निदानों को ट्रैक करें।",
        "mr": "विश्वास प्रवृत्ती आणि एक्सपोर्ट करण्यायोग्य अहवालांसह काळानुसार तुमच्या सर्व AI निदानांचा मागोवा घ्या."
    },

    "works_offline": {
        "en": "🌍 Works offline — no internet needed!",
        "te": "🌍 ఆఫ్‌లైన్‌లో పనిచేస్తుంది — ఇంటర్‌నెట్ అవసరం లేదు!",
        "hi": "🌍 ऑफलाइन काम करता है — इंटरनेट की ज़रूरत नहीं!",
        "mr": "🌍 ऑफलाइन काम करते — इंटरनेटची गरज नाही!"
    },

    "got_it_hide": {
        "en": "✅ Got it, hide this",
        "te": "✅ అర్థమయ్యింది, ఇదిని లుక్కుంచు",
        "hi": "✅ समझ गया, इसे छुपाएं",
        "mr": "✅ समजले, हे लपवा"
    },

    "exit_demo": {
        "en": "🚪 Exit Demo",
        "te": "🚪 డెమో నుండి నిష్క్రమించండి",
        "hi": "🚪 डेमो से बाहर निकलें",
        "mr": "🚪 डेमोमधून बाहर पडा"
    },

    "prev": {
        "en": "⬅️ Prev",
        "te": "⬅️ మునుపు",
        "hi": "⬅️ पिछला",
        "mr": "⬅️ मागे"
    },

    "next": {
        "en": "Next ➡️",
        "te": "తరువాత ➡️",
        "hi": "अगला ➡️",
        "mr": "पुढे ➡️"
    },

    "demo_tip": {
        "en": "🎬 Demo Tip:",
        "te": "🎬 డెమో చిట్కా:",
        "hi": "🎬 डेमो टिप:",
        "mr": "🎬 डेमो टिप:"
    },

    # -------------------------------------------------
    # DASHBOARD
    # -------------------------------------------------

    "ai_diagnosis_feature": {
        "en": "🩺 AI Diagnosis",
        "te": "🩺 AI నిర్ధారణ",
        "hi": "🩺 AI जांच",
        "mr": "🩺 AI निदान"
    },

    "ai_diagnosis_desc": {
        "en": "Upload a leaf image and get an AI-based disease prediction.",
        "te": "ఆకు చిత్రాన్ని అప్‌లోడ్ చేయండి మరియు AI-ఆధారిత వ్యాధి అంచనాను పొందండి.",
        "hi": "पत्ते की तस्वीर अपलोड करें और AI-आधारित रोग पूर्वानुमान प्राप्त करें।",
        "mr": "पानाचा फोटो अपलोड करा आणि AI-आधारित रोग अंदाज मिळवा."
    },

    "crop_raksha_feature": {
        "en": "🛡️ Crop Raksha",
        "te": "🛡️ క్రాప్ రక్ష",
        "hi": "🛡️ क्रॉप रक्षा",
        "mr": "🛡️ क्रॉप रक्षा"
    },

    "crop_raksha_desc": {
        "en": "Monitor your crop every day and detect changes over time.",
        "te": "మీ పంటను ప్రతిరోజూ పర్యవేక్షించండి మరియు కాలక్రమేణా మార్పులను గుర్తించండి.",
        "hi": "अपनी फसल की रोज़ाना निगरानी करें और समय के साथ बदलाव का पता लगाएं।",
        "mr": "तुमच्या पिकाचे दररोज निरीक्षण करा आणि वेळेनुसार बदल शोध."
    },

    "management_advice_feature": {
        "en": "🩺 Management Advice",
        "te": "🩺 నిర్వహణ సలహా",
        "hi": "🩺 प्रबंधन सलाह",
        "mr": "🩺 व्यवस्थापन सल्ला"
    },

    "management_advice_desc": {
        "en": "Get management and prevention information for detected problems.",
        "te": "గుర్తించిన సమస్యల కోసం నిర్వహణ మరియు నివారణ సమాచారం పొందండి.",
        "hi": "पाई गई समस्याओं के लिए प्रबंधन और रोकथाम की जानकारी प्राप्त करें।",
        "mr": "आढळलेल्या समस्यांसाठी व्यवस्थापन आणि प्रतिबंध माहिती मिळवा."
    },

    "anjaneya_voice_feature": {
        "en": "🔱 Anjaneya Voice",
        "te": "🔱 ఆంజనేయ వాయిస్",
        "hi": "🔱 आंजनेय वॉइस",
        "mr": "🔱 आंजनेय व्हॉइस"
    },

    "anjaneya_voice_desc": {
        "en": "Voice-only AI assistant in your local language.",
        "te": "మీ స్థానిక భాషలో వాయిస్-మాత్రమే AI సహాయకుడు.",
        "hi": "आपकी स्थानीय भाषा में वॉइस-ओनली AI सहायक।",
        "mr": "तुमच्या स्थानिक भाषेत व्हॉइस-ओनली AI सहाय्यक."
    },

    "smart_history_feature": {
        "en": "📊 Smart History",
        "te": "📊 స్మార్ట్ చరిత్ర",
        "hi": "📊 स्मार्ट हिस्ट्री",
        "mr": "📊 स्मार्ट हिस्ट्री"
    },

    "smart_history_desc": {
        "en": "Export diagnosis records as CSV for your records.",
        "te": "మీ రికార్డుల కోసం నిర్ధారణ రికార్డులను CSVగా ఎగుమతి చేయండి.",
        "hi": "अपने रिकॉर्ड के लिए निदान रिकॉर्ड को CSV के रूप में निर्यात करें।",
        "mr": "तुमच्या रेकॉर्डसाठी निदान रेकॉर्ड CSV म्हणून एक्सपोर्ट करा."
    },

    "sample_gallery_feature": {
        "en": "🖼️ Sample Gallery",
        "te": "🖼️ నమూనా గ్యాలరీ",
        "hi": "🖼️ नमूना गैलरी",
        "mr": "🖼️ नमूना गॅलरी"
    },

    "sample_gallery_desc": {
        "en": "Try AI diagnosis instantly with sample leaf images.",
        "te": "నమూనా ఆకు చిత్రాలతో AI నిర్ధారణను తక్షణం ప్రయత్నించండి.",
        "hi": "नमूना पत्ते की तस्वीरों के साथ तुरंत AI निदान आज़माएं।",
        "mr": "नमूना पानाच्या प्रतिमांसह त्वरित AI निदान करा."
    },

    "crop_doctor_features": {
        "en": "🚀 Crop Doctor Features",
        "te": "🚀 క్రాప్ డాక్టర్ ఫీచర్లు",
        "hi": "🚀 क्रॉप डॉक्टर सुविधाएं",
        "mr": "🚀 क्रॉप डॉक्टर वैशिष्ट्ये"
    },

    # -------------------------------------------------
    # DASHBOARD (POLISHED)
    # -------------------------------------------------

    "dashboard_hero_subtitle": {
        "en": "AI-powered crop health assistant — diagnose, monitor and protect your crops with multilingual offline support.",
        "te": "AI-ఆధారిత పంట ఆరోగ్య సహాయకుడు — బహుళ భాష ఆఫ్‌లైన్ మద్దతుతో మీ పంటలను నిర్ధారించండి, పర్యవేక్షించండి మరియు రక్షించండి.",
        "hi": "AI-संचालित फसल स्वास्थ्य सहायक — बहुभाषी ऑफलाइन सहायता के साथ अपनी फसलों का निदान, निगरानी और सुरक्षा करें।",
        "mr": "AI-चालित पीक आरोग्य सहाय्यक — बहुभाषिक ऑफलाइन समर्थनासह आपल्या पिकांचे निदान, निरीक्षण आणि संरक्षण करा."
    },

    "kpi_total_scans": {
        "en": "Total Scans",
        "te": "మొత్తం స్కాన్‌లు",
        "hi": "कुल स्कैन",
        "mr": "एकूण स्कॅन"
    },

    "kpi_healthy": {
        "en": "Healthy",
        "te": "ఆరోగ్యకరం",
        "hi": "स्वस्थ",
        "mr": "निरोगी"
    },

    "kpi_issues": {
        "en": "Issues Detected",
        "te": "సమస్యలు గుర్తించబడ్డాయి",
        "hi": "समस्याएं मिलीं",
        "mr": "समस्या आढळल्या"
    },

    "kpi_crops": {
        "en": "Crops Monitored",
        "te": "పంటలు పర్యవేక్షించబడ్డాయి",
        "hi": "निगरानी की गई फसलें",
        "mr": "निरीक्षण केलेली पिके"
    },

    "kpi_tracked": {
        "en": "All-time tracked",
        "te": "అన్ని సమయాలు ట్రాక్ చేయబడ్డాయి",
        "hi": "हर समय ट्रैक किया गया",
        "mr": "सर्वकालीन ट्रॅक केले"
    },

    "ai_intelligence_modules": {
        "en": "🧠 AI Intelligence Modules",
        "te": "🧠 AI ఇంటెలిజెన్స్ మాడ్యూల్స్",
        "hi": "🧠 AI इंटेलिजेंस मॉड्यूल",
        "mr": "🧠 AI इंटेलिजन्स मॉड्यूल्स"
    },

    "monitoring_progress": {
        "en": "📈 Monitoring Progress",
        "te": "📈 పర్యవేక్షణ ప్రగతి",
        "hi": "📈 निगरानी प्रगति",
        "mr": "📈 निरीक्षण प्रगती"
    },

    "anjaneya_card_title": {
        "en": "🔱 Anjaneya Voice",
        "te": "🔱 ఆంజనేయ వాయిస్",
        "hi": "🔱 आंजनेय वॉइस",
        "mr": "🔱 आंजनेय व्हॉइस"
    },

    "anjaneya_card_desc": {
        "en": "Voice-only AI assistant in your local language. Just speak — no typing needed. Designed for farmers in the field.",
        "te": "మీ స్థానిక భాషలో వాయిస్-మాత్రమే AI సహాయకుడు. కేవలం మాట్లాడండి — టైపింగ్ అవసరం లేదు. క్షేత్రంలోని రైతుల కోసం రూపొందించబడింది.",
        "hi": "आपकी स्थानीय भाषा में वॉइस-ओनली AI सहायक। बस बोलिए — टाइपिंग की जरूरत नहीं। खेत में किसानों के लिए डिज़ाइन किया गया।",
        "mr": "तुमच्या स्थानिक भाषेत व्हॉइस-ओनली AI सहाय्यक. फक्त बोला — टायपिंगची गरज नाही. शेतातील शेतकऱ्यांसाठी डिझाइन केलेले."
    },

    "supported_crop_species": {
        "en": "🌾 Supported Crop Species",
        "te": "🌾 సమర్థిత పంట జాతులు",
        "hi": "🌾 समर्थित फसल प्रजातियाँ",
        "mr": "🌾 समर्थित पीक प्रजाती"
    },

    "footer_text": {
        "en": "🌱 Crop Doctor · Built for farmers · Works offline · Powered by AI",
        "te": "🌱 క్రాప్ డాక్టర్ · రైతుల కోసం నిర్మించబడింది · ఆఫ్‌లైన్‌లో పనిచేస్తుంది · AI ద్వారా శక్తిని పొందుతుంది",
        "hi": "🌱 क्रॉप डॉक्टर · किसानों के लिए बनाया गया · ऑफ़लाइन काम करता है · AI द्वारा संचालित",
        "mr": "🌱 क्रॉप डॉक्टर · शेतकऱ्यांसाठी बनवलेले · ऑफलाइन कार्य करते · AI द्वारे चालित"
    },

    # -------------------------------------------------
    # DASHBOARD (POLISHED)
    # -------------------------------------------------

    "dashboard_welcome": {
        "en": "Welcome back,",
        "te": "తిరిగి స్వాగతం,",
        "hi": "वापस स्वागत है,",
        "mr": "पुन्हा स्वागत आहे,"
    },

    "dashboard_farmer_greeting": {
        "en": "Farmer",
        "te": "రైతు",
        "hi": "किसान",
        "mr": "शेतकरी"
    },

    "ai_online": {
        "en": "AI Online",
        "te": "AI ఆన్‌లైన్",
        "hi": "AI ऑनलाइन",
        "mr": "AI ऑनलाइन"
    },

    "view_recent_reports": {
        "en": "View Recent Reports",
        "te": "ఇటీవలి నివేదికలను చూడండి",
        "hi": "हाल की रिपोर्ट देखें",
        "mr": "अलीकडील अहवाल पहा"
    },

    "dashboard_kpi_overview": {
        "en": "Dashboard Overview",
        "te": "డాష్‌బోర్డ్ అవలోకనం",
        "hi": "डैशबोर्ड अवलोकन",
        "mr": "डॅशबोर्ड विहंगावलोकन"
    },

    "needs_attention": {
        "en": "Needs attention",
        "te": "శ్రద్ధ అవసరం",
        "hi": "ध्यान आवश्यक",
        "mr": "लक्ष देणे आवश्यक"
    },

    "all_clear": {
        "en": "All clear",
        "te": "అంతా స్పష్టం",
        "hi": "सब ठीक",
        "mr": "सर्व स्वच्छ"
    },

    "monitoring_short": {
        "en": "Monitoring",
        "te": "పర్యవేక్షణ",
        "hi": "निगरानी",
        "mr": "निरीक्षण"
    },

    "monitoring_desc": {
        "en": "Track daily crop observations and detect changes over time.",
        "te": "రోజువారీ పంట పరిశీలనలను ట్రాక్ చేసి, కాలక్రమేణా మార్పులను గుర్తించండి.",
        "hi": "दैनिक फसल अवलोकन ट्रैक करें और समय के साथ परिवर्तन का पता लगाएं।",
        "mr": "दैनंदिन पीक निरीक्षण ट्रॅक करा आणि वेळेनुसार बदल शोधा."
    },

    "disease_library_short": {
        "en": "Disease Library",
        "te": "వ్యాధి గ్రంథాలయం",
        "hi": "रोग पुस्तकालय",
        "mr": "रोग ग्रंथालय"
    },

    "disease_library_desc": {
        "en": "Browse the catalog of supported diseases and treatments.",
        "te": "మద్దతు ఉన్న వ్యాధులు మరియు చికిత్సల కేటలాగ్‌ను బ్రౌజ్ చేయండి.",
        "hi": "समर्थित रोगों और उपचारों की सूची ब्राउज़ करें।",
        "mr": "समर्थित रोग आणि उपचारांची सूची ब्राउझ करा."
    },

    "anjaneya_voice": {
        "en": "Anjaneya Voice",
        "te": "ఆంజనేయ వాయిస్",
        "hi": "आंजनेय वॉइस",
        "mr": "आंजनेय व्हॉइस"
    },

    "dashboard_crop_health": {
        "en": "Crop health by type",
        "te": "రకం వారీగా పంట ఆరోగ్యం",
        "hi": "फसल के प्रकार के अनुसार स्वास्थ्य",
        "mr": "पीक प्रकारानुसार आरोग्य"
    },

    "diseases_tracked": {
        "en": "diseases tracked",
        "te": "వ్యాధులు ట్రాక్ చేయబడ్డాయి",
        "hi": "रोग ट्रैक किए गए",
        "mr": "रोग ट्रॅक केले"
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
        "en": "🔬 AI Analysis",
        "te": "🔬 AI విశ్లేషణ",
        "hi": "🔬 AI विश्लेषण",
        "mr": "🔬 AI विश्लेषण"
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

    "uploaded_leaf": {
        "en": "Uploaded leaf",
        "te": "అప్‌లోడ్ చేసిన ఆకు",
        "hi": "अपलोड किया गया पत्ता",
        "mr": "अपलोड केलेले पान"
    },

    "running_ai_sample": {
        "en": "🖼️ Running AI on sample image:",
        "te": "🖼️ నమూనా చిత్రంపై AI నడుపబడుతోంది:",
        "hi": "🖼️ नमूना छवि पर AI चला रहा है:",
        "mr": "🖼️ नमूना प्रतिमेवर AI चालू आहे:"
    },

    "could_not_load_sample": {
        "en": "Could not load sample image.",
        "te": "నమూనా చిత్రం లోడ్ కాలేకపోయింది.",
        "hi": "नमूना छवि लोड नहीं हो सकी।",
        "mr": "नमूना प्रतिमा लोड होऊ शकली नाही."
    },

    "upload_valid_rgb": {
        "en": "⚠️ Please upload a valid RGB leaf image — analysis could not be completed.",
        "te": "⚠️ చెల్లుబాటు అయ్యే RGB ఆకు చిత్రాన్ని అప్‌లోడ్ చేయండి — విశ్లేషణ పూర్తికాలేదు.",
        "hi": "⚠️ कृपया मान्य RGB पत्ते की तस्वीर अपलोड करें — विश्लेषण पूरा नहीं हो सका।",
        "mr": "⚠️ कृपया वैध RGB पानाचा फोटो अपलोड करा — विश्लेषण पूर्ण होऊ शकले नाही."
    },

    "disease_info_not_available": {
        "en": "Information for this disease is not available yet.",
        "te": "ఈ వ్యాధికి సంబంధించిన సమాచారం ఇంకా అందుబాటులో లేదు.",
        "hi": "इस रोग की जानकारी अभी उपलब्ध नहीं है।",
        "mr": "या रोगाची माहिती अद्याप उपलब्ध नाही."
    },

    # -------------------------------------------------
    # TREATMENT RECOMMENDATIONS
    # -------------------------------------------------

    "treatment_recommendation": {
        "en": "💊 Treatment Recommendation",
        "te": "💊 చికిత్స సిఫార్సు",
        "hi": "💊 उपचार अनुशंसा",
        "mr": "💊 उपचार शिफारस"
    },

    "fertilizer_nutrient": {
        "en": "🌿 Fertilizer / Nutrient",
        "te": "🌿 ఎరువు / పోషకం",
        "hi": "🌿 खाद / पोषक तत्व",
        "mr": "🌿 खत / पोषक द्रव्य"
    },

    "fertilizer_quantity": {
        "en": "Fertilizer Quantity",
        "te": "ఎరువు పరిమాణం",
        "hi": "खाद मात्रा",
        "mr": "खत प्रमाण"
    },

    "pesticide_treatment": {
        "en": "🧪 Pesticide / Treatment",
        "te": "🧪 Pesticide / చికిత్స",
        "hi": "🧪 कीटनाशक / उपचार",
        "mr": "🧪 किटकनाशक / उपचार"
    },

    "pesticide_quantity": {
        "en": "Pesticide Quantity",
        "te": "Pesticide పరిమాణం",
        "hi": "कीटनाशक मात्रा",
        "mr": "किटकनाशक प्रमाण"
    },

    "treatment_description": {
        "en": "📝 Description",
        "te": "📝 వివరణ",
        "hi": "📝 विवरण",
        "mr": "📝 वर्णन"
    },

    "treatment_not_available": {
        "en": "Treatment recommendation for this condition is not available.",
        "te": "ఈ పరిస్థితి కోసం చికిత్స సిఫార్సు అందుబాటులో లేదు.",
        "hi": "इस स्थिति के लिए उपचार अनुशंसा उपलब्ध नहीं है।",
        "mr": "या स्थितीसाठी उपचार शिफारस उपलब्ध नाही."
    },

    "how_ai_reached_result": {
        "en": "🧠 How Did the AI Reach This Result?",
        "te": "🧠 AI ఈ ఫలితానికి ఎలా చేరింది?",
        "hi": "🧠 AI इस परिणाम पर कैसे पहुंचा?",
        "mr": "🧠 AI या निकाल्यावर कसे पोहोचले?"
    },

    "high_confidence": {
        "en": "🟢 High Confidence",
        "te": "🟢 అధిక నమ్మకం",
        "hi": "🟢 उच्च विश्वास",
        "mr": "🟢 उच्च विश्वास"
    },

    "medium_confidence": {
        "en": "🟡 Medium Confidence",
        "te": "🟡 మధ్యమ నమ్మకం",
        "hi": "🟡 मध्यम विश्वास",
        "mr": "🟡 मध्यम विश्वास"
    },

    "lower_confidence": {
        "en": "🟠 Lower Confidence",
        "te": "🟠 తక్కువ నమ్మకం",
        "hi": "🟠 कम विश्वास",
        "mr": "🟠 कम विश्वास"
    },

    "what_ai_looked_for": {
        "en": "🤖 What the AI Looked For",
        "te": "🤖 AI ఏమి చూసింది",
        "hi": "🤖 AI ने क्या देखा",
        "mr": "🤖 AI ने काय पाहिले"
    },

    "top_ai_predictions": {
        "en": "📊 Top AI Predictions",
        "te": "📊 అగ్ర AI అంచనాలు",
        "hi": "📊 शीर्ष AI पूर्वानुमान",
        "mr": "📊 शीर्ष AI अंदाज"
    },

    "about_ai_confidence": {
        "en": "💡 About AI Confidence: The confidence score shows how strongly the model favors one class over others. It does NOT guarantee accuracy.",
        "te": "💡 AI నమ్మకం గురించి: నమ్మకం స్కోరు మోడల్ ఒక క్లాస్‌ను ఇతరులపై ఎంత బలంగా ఇష్టపడుతుంది చూపుతుంది. ఇది ఖచ్చితత్వాన్ని హామీ ఇవ్వదు.",
        "hi": "💡 AI विश्वास के बारे में: विश्वास स्कोर दिखाता है कि मॉडल एक क्लास को दूसरों पर कितना पसंद करता है। यह सटीकता की गारंटी नहीं देता।",
        "mr": "💡 AI विश्वासाबद्दल: विश्वास स्कोर दर्शवितो की मॉडेल एका वर्गाला दुसऱ्यांपेक्षा किती जास्त आवडतो. हे अचूकतेची खात्री देत नाही."
    },

    "quick_demo_sample_images": {
        "en": "🖼️ Quick Demo — Try Sample Images",
        "te": "🖼️ త్వరిత డెమో — నమూనా చిత్రాలను ప్రయత్నించండి",
        "hi": "🖼️ त्वरित डेमो — नमूना चित्र देखें",
        "mr": "🖼️ जल्दी डेमो — नमूना प्रतिमा पहा"
    },

    "click_any_image_below": {
        "en": "Click any image below for an instant AI diagnosis demo. No upload needed — the AI will analyze the sample immediately.",
        "te": "తక్షణ AI నిర్ధారణ డెమో కోసం కింద ఏదైనా చిత్రంపై క్లిక్ చేయండి. అప్‌లోడ్ అవసరం లేదు — AI నమూనాను తక్షణం విశ్లేషిస్తుంది.",
        "hi": "तुरंत AI निदान डेमो के लिए नीचे किसी भी छवि पर क्लिक करें। अपलोड की जरूरत नहीं — AI तुरंत नमूने का विश्लेषण करेगा।",
        "mr": "त्वरित AI निदान डेमोसाठी खाली कोणत्याही प्रतिमेवर क्लिक करा. अपलोडची गरज नाही — AI त्वरित नमुन्याचे विश्लेषण करेल."
    },

    "samples_count": {
        "en": "Samples",
        "te": "నమూనాలు",
        "hi": "नमूने",
        "mr": "नमूने"
    },

    "could_not_load": {
        "en": "Could not load",
        "te": "లోడ్ కాలేకపోయింది",
        "hi": "लोड नहीं हो सका",
        "mr": "लोड होऊ शकले नाही"
    },

    "link_diagnosis_crop": {
        "en": "🌾 Link diagnosis to a registered crop",
        "te": "🌾 నిర్ధారణను నమోదు చేసిన పంటకు లింక్ చేయండి",
        "hi": "🌾 निदान को पंजीकृत फसल से जोड़ें",
        "mr": "🌾 निदान नोंदणीकृत पिकाशी जोडा"
    },

    "general_diagnosis": {
        "en": "— General diagnosis (not linked to a crop) —",
        "te": "— సాధారణ నిర్ధారణ (పంటకు లింక్ చేయలేదు) —",
        "hi": "— सामान्य जांच (फसल से लिंक नहीं) —",
        "mr": "— सामान्य निदान (पिकाशी जोडलेले नाही) —"
    },

    # -------------------------------------------------
    # CROP REGISTRATION
    # -------------------------------------------------

    "farmer_name": {
        "en": "👨‍🌾 Farmer Name",
        "te": "👨‍🌾 రైతు పేరు",
        "hi": "👨‍🌾 किसान का नाम",
        "mr": "👨‍🌾 शेतकऱ्याचे नाव"
    },

    "field_name": {
        "en": "📍 Field Name",
        "te": "📍 పొలం పేరు",
        "hi": "📍 खेत का नाम",
        "mr": "📍 शेताचे नाव"
    },

    "example_field": {
        "en": "Example: Field 1",
        "te": "ఉదాహరణ: పొలం 1",
        "hi": "उदाहरण: खेत 1",
        "mr": "उदाहरण: शेत 1"
    },

    "daily_crop_raksha_time": {
        "en": "⏰ Daily Crop Raksha Monitoring Time",
        "te": "⏰ ప్రతిరోజు క్రాప్ రక్ష పర్యవేక్షణ సమయం",
        "hi": "⏰ दैनिक क्रॉप रक्षा निगरानी समय",
        "mr": "⏰ दैनिक क्रॉप रक्षा निरीक्षण वेळ"
    },

    "register_crop": {
        "en": "🌱 Register Crop",
        "te": "🌱 పంటను నమోదు చేయండి",
        "hi": "🌱 फसल पंजीकृत करें",
        "mr": "🌱 पीक नोंदवा"
    },

    "please_enter_farmer_name": {
        "en": "Please enter the farmer name.",
        "te": "దయచేసి రైతు పేరు నమోదు చేయండి.",
        "hi": "कृपया किसान का नाम दर्ज करें।",
        "mr": "कृपया शेतकऱ्याचे नाव नोंदवा."
    },

    "date_not_future": {
        "en": "The date of sowing cannot be in the future.",
        "te": "విత్తిన తేదీ భవిష్యంలో ఉండకూడదు.",
        "hi": "बुवाई की तारीख भविष्य में नहीं हो सकती।",
        "mr": "पेरणीची तारीख भविष्यात असू शकत नाही."
    },

    "crop_registered_success": {
        "en": "✅ Crop registered successfully!",
        "te": "✅ పంట విజయవంతంగా నమోదు చేయబడింది!",
        "hi": "✅ फसल सफलतापूर्वक पंजीकृत!",
        "mr": "✅ पीक यशस्वीरित्या नोंदले!"
    },

    "farmer_label": {
        "en": "Farmer:",
        "te": "రైతు:",
        "hi": "किसान:",
        "mr": "शेतकरी:"
    },

    "crop_label": {
        "en": "Crop:",
        "te": "పంట:",
        "hi": "फसल:",
        "mr": "पीक:"
    },

    "field_label": {
        "en": "Field:",
        "te": "పొలం:",
        "hi": "खेत:",
        "mr": "शेत:"
    },

    "not_specified": {
        "en": "Not specified",
        "te": "పేర్కొనబడలేదు",
        "hi": "निर्दिष्ट नहीं",
        "mr": "निर्दिष्ट नाही"
    },

    "date_of_sowing": {
        "en": "Date of Sowing:",
        "te": "విత్తిన తేదీ:",
        "hi": "बुवाई की तारीख:",
        "mr": "पेरणीची तारीख:"
    },

    "crop_raksha_time_label": {
        "en": "Daily Crop Raksha Time:",
        "te": "ప్రతిరోజు క్రాప్ రక్ష సమయం:",
        "hi": "दैनिक क्रॉप रक्षा समय:",
        "mr": "दैनिक क्रॉप रक्षा वेळ:"
    },

    "crop_id_label": {
        "en": "Crop ID:",
        "te": "పంట ID:",
        "hi": "फसल ID:",
        "mr": "पीक ID:"
    },

    "my_registered_crops": {
        "en": "🌾 My Registered Crops",
        "te": "🌾 నా నమోదు చేసిన పంటలు",
        "hi": "🌾 मेरी पंजीकृत फसलें",
        "mr": "🌾 माझी नोंदणीकृत पिकें"
    },

    "no_crops_registered": {
        "en": "🌱 No crops registered yet.",
        "te": "🌱 ఇంకా పంటలు నమోదు కాలేదు.",
        "hi": "🌱 अभी तक कोई फसल पंजीकृत नहीं है।",
        "mr": "🌱 अद्याप कोणतीही पिके नोंदलेली नाहीत."
    },

    "go_to_crop_registration": {
        "en": "Go to Crop Registration and register your crop first.",
        "te": "పంట నమోదు విభాగానికి వెళ్లి ముందుగా మీ పంటను నమోదు చేయండి.",
        "hi": "फसल पंजीकरण में जाकर पहले अपनी फसल पंजीकृत करें।",
        "mr": "पीक नोंदणीमध्ये जाऊन प्रथम तुमचे पीक नोंदवा."
    },

    "sowing_date_label": {
        "en": "📅 Sowing Date:",
        "te": "📅 విత్తిన తేదీ:",
        "hi": "📅 बुवाई की तारीख:",
        "mr": "📅 पेरणीची तारीख:"
    },

    "crop_age_days": {
        "en": "days",
        "te": "రోజులు",
        "hi": "दिन",
        "mr": "दिवस"
    },

    "crop_age": {
        "en": "🌿 Crop Age",
        "te": "🌿 పంట వయస్సు",
        "hi": "🌿 फसल की आयु",
        "mr": "🌿 पीक वय"
    },

    "observations": {
        "en": "Observations",
        "te": "పరిశీలనలు",
        "hi": "अवलोकन",
        "mr": "निरीक्षणे"
    },

    "sowing_date": {
        "en": "Sowing Date",
        "te": "విత్తిన తేదీ",
        "hi": "बुवाई की तारीख",
        "mr": "पेरणीची तारीख"
    },

    "status": {
        "en": "Status",
        "te": "స్థితి",
        "hi": "स्थिति",
        "mr": "स्थिती"
    },

    "crop_raksha_time_field": {
        "en": "⏰ Crop Raksha Time:",
        "te": "⏰ క్రాప్ రక్ష సమయం:",
        "hi": "⏰ क्रॉप रक्षा समय:",
        "mr": "⏰ क्रॉप रक्षा वेळ:"
    },

    "status_label": {
        "en": "🟢 Status:",
        "te": "🟢 స్థితి:",
        "hi": "🟢 स्थिति:",
        "mr": "🟢 स्थिती:"
    },

    "delete": {
        "en": "🗑️ Delete",
        "te": "🗑️ తొలగించు",
        "hi": "🗑️ हटाएं",
        "mr": "🗑️ हटवा"
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

    "ai_crop_companion_monitoring": {
        "en": "Your AI crop companion for continuous daily monitoring.",
        "te": "నిరంతర రోజువారీ పర్యవేక్షణ కోసం మీ AI పంట సహాయకుడు.",
        "hi": "निरंतर दैनिक निगरानी के लिए आपका AI फसल सहायक।",
        "mr": "सतत दैनंदिन निरीक्षणासाठी तुमचा AI पीक सहाय्यक."
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

    "no_active_crops": {
        "en": "No active crops found.",
        "te": "క్రియాశీల పంటలు ఏవీ కనుగొనబడలేదు.",
        "hi": "कोई सक्रिय फसल नहीं मिली।",
        "mr": "कोणतीही सक्रिय पिके आढळली नाहीत."
    },

    "select_your_crop": {
        "en": "🌾 Select your crop",
        "te": "🌾 మీ పంటను ఎంచుకోండి",
        "hi": "🌾 अपनी फसल चुनें",
        "mr": "🌾 तुमचे पीक निवडा"
    },

    "crop_profile": {
        "en": "🌱 Crop Profile",
        "te": "🌱 పంట వివరాలు",
        "hi": "🌱 फसल प्रोफ़ाइल",
        "mr": "🌱 पीक प्रोफाइल"
    },

    "daily_raksha_time_info": {
        "en": "⏰ Your daily Crop Raksha time is",
        "te": "⏰ మీ ప్రతిరోజు క్రాప్ రక్ష సమయం",
        "hi": "⏰ आपका दैनिक क्रॉप रक्षा समय है",
        "mr": "⏰ तुमची दैनिक क्रॉप रक्षा वेळ आहे"
    },

    "crop_raksha_ai_companion": {
        "en": "🤖 Crop Raksha AI Companion",
        "te": "🤖 క్రాప్ రక్ష AI సహాయకుడు",
        "hi": "🤖 क्रॉप रक्षा AI सहायक",
        "mr": "🤖 क्रॉप रक्षा AI सहाय्यक"
    },

    "companion_remembers_history": {
        "en": "Your AI crop companion remembers your monitoring history and helps you understand what is happening over time.",
        "te": "మీ AI పంట సహాయకుడు మీ పర్యవేక్షణ చరిత్రను గుర్తుంచుకుని కాలక్రమేణా ఏమి జరుగుతుందో అర్థం చేసుకోవడంలో సహాయపడుతుంది.",
        "hi": "आपका AI फसल सहायक आपकी निगरानी का इतिहास याद रखता है और समय के साथ क्या हो रहा है यह समझने में मदद करता है।",
        "mr": "तुमचा AI पीक सहाय्यक तुमचा निरीक्षण इतिहास लक्षात ठेवतो आणि कालांतराने काय घडत आहे हे समजून घेण्यास मदत करतो."
    },

    "record_today_condition": {
        "en": "Let's record today's condition.",
        "te": "ఈరోజు పంట పరిస్థితిని నమోదు చేద్దాం.",
        "hi": "आज की स्थिति दर्ज करें।",
        "mr": "आजची स्थिती नोंदवूया."
    },

    "upload_crops_photograph": {
        "en": "📷 Upload today's crop photograph",
        "te": "📷 ఈరోజు పంట ఫోటోను అప్‌లోడ్ చేయండి",
        "hi": "📷 आज की फसल की तस्वीर अपलोड करें",
        "mr": "📷 आजच्या पिकाचा फोटो अपलोड करा"
    },

    "day_observation": {
        "en": "Day {day} observation",
        "te": "రోజు {day} పరిశీలన",
        "hi": "दिन {day} अवलोकन",
        "mr": "दिवस {day} निरीक्षण"
    },

    "save_day_observation": {
        "en": "💾 Save Day {day} Observation",
        "te": "💾 రోజు {day} పరిశీలనను సేవ్ చేయండి",
        "hi": "💾 दिन {day} अवलोकन सहेजें",
        "mr": "💾 दिवस {day} निरीक्षण जतन करा"
    },

    "observation_saved": {
        "en": "✅ Day {day} observation saved!",
        "te": "✅ రోజు {day} పరిశీలన సేవ్ చేయబడింది!",
        "hi": "✅ दिन {day} अवलोकन सहेजा गया!",
        "mr": "✅ दिवस {day} निरीक्षण जतन केले!"
    },

    "visual_change_heatmap": {
        "en": "🔥 Visual Change Heatmap",
        "te": "🔥 దృశ్య మార్పు హీట్‌మ్యాప్",
        "hi": "🔥 दृश्य परिवर्तन हीटमैप",
        "mr": "🔥 दृश्य बदल हीटमॅप"
    },

    "bright_areas_caption": {
        "en": "Bright areas indicate regions where the crop image changed most compared with the previous observation.",
        "te": "ప్రకాశవంతమైన ప్రాంతాలు పంట చిత్రం గత పరిశీలనతో పోలిస్తే ఎక్కువగా మారిన ప్రాంతాలను సూచిస్తాయి.",
        "hi": "चमकीले क्षेत्र उन क्षेत्रों को दर्शाते हैं जहां फसल की तस्वीर पिछली तस्वीर की तुलना में सबसे अधिक बदल गई है।",
        "mr": "प्रकाशमान भाग असे क्षेत्र दर्शवितात जेथे पीक प्रतिमा मागील निरीक्षणापेक्षा सर्वात जास्त बदलली आहे."
    },

    "hotter_areas_caption": {
        "en": "Hotter/brighter areas show where the current image differs most from the previous observation.",
        "te": "వేడి/ప్రకాశవంతమైన ప్రాంతాలు ప్రస్తుత చిత్రం మునుపటి పరిశీలనతో ఎక్కువగా భిన్నంగా ఉన్న ప్రాంతాలను చూపుతాయి.",
        "hi": "अधिक चमकीले क्षेत्र दिखाते हैं कि वर्तमान तस्वीर पिछली तस्वीर से कहाँ सबसे अधिक अलग है।",
        "mr": "उष्ण/प्रकाशमान भाग वर्तमान फोटो मागील निरीक्षणापेक्षा कुठे जास्त वेगळा आहे ते दाखवतात."
    },

    "overall_visual_difference": {
        "en": "📊 Overall visual difference:",
        "te": "📊 మొత్తం దృశ్య తేడా:",
        "hi": "📊 समग्र दृश्य अंतर:",
        "mr": "📊 एकूण दृश्य फरक:"
    },

    "crop_raksha_ai_assessment": {
        "en": "🤖 Crop Raksha AI Assessment",
        "te": "🤖 క్రాప్ రక్ష AI అంచనా",
        "hi": "🤖 क्रॉप रक्षा AI आकलन",
        "mr": "🤖 क्रॉप रक्षा AI मूल्यांकन"
    },

    "ai_result_label": {
        "en": "🔬 AI Result",
        "te": "🔬 AI ఫలితం",
        "hi": "🔬 AI परिणाम",
        "mr": "🔬 AI परिणाम"
    },

    "visual_change_analysis": {
        "en": "🔥 Visual Change Analysis",
        "te": "🔥 దృశ్య మార్పు విశ్లేషణ",
        "hi": "🔥 दृश्य परिवर्तन विश्लेषण",
        "mr": "🔥 दृश्य बदल विश्लेषण"
    },

    "baseline_created_msg": {
        "en": "🌱 **Baseline created**\n\nThis is the first Crop Raksha observation.\n\nFuture observations will be compared against previous images.",
        "te": "🌱 **ప్రాథమిక పరిశీలన సృష్టించబడింది**\n\nఇది మొదటి క్రాప్ రక్ష పరిశీలన.\n\nభవిష్యత్తు పరిశీలనలు మునుపటి చిత్రాలతో పోల్చబడతాయి.",
        "hi": "🌱 **प्रारंभिक अवलोकन बनाया गया**\n\nयह पहला क्रॉप रक्षा अवलोकन है।\n\nभविष्य के अवलोकनों की तुलना पिछली तस्वीरों से की जाएगी।",
        "mr": "🌱 **प्रारंभिक निरीक्षण तयार केले**\n\nहे पहिले क्रॉप रक्षा निरीक्षण आहे.\n\nभविष्यातील निरीक्षणे मागील प्रतिमांशी तुलना केली जाईल."
    },

    "visual_difference_label": {
        "en": "📊 Visual Difference",
        "te": "📊 దృశ్య తేడా",
        "hi": "📊 दृश्य अंतर",
        "mr": "📊 दृश्य फरक"
    },

    "normal": {
        "en": "🟢 Normal",
        "te": "🟢 సాధారణం",
        "hi": "🟢 सामान्य",
        "mr": "🟢 सामान्य"
    },

    "minor_change": {
        "en": "🟠 Minor Change",
        "te": "🟠 స్వల్ప మార్పు",
        "hi": "🟠 मामूली बदलाव",
        "mr": "🟠 किरकोळ बदल"
    },

    "significant_change": {
        "en": "🔴 Significant Change",
        "te": "🔴 గణనీయమైన మార్పు",
        "hi": "🔴 महत्वपूर्ण बदलाव",
        "mr": "🔴 लक्षणीय बदल"
    },

    "crop_raksha_assessment": {
        "en": "🤖 Crop Raksha Assessment",
        "te": "🤖 క్రాప్ రక్ష అంచనా",
        "hi": "🤖 क्रॉप रक्षा आकलन",
        "mr": "🤖 क्रॉप रक्षा मूल्यांकन"
    },

    "significant_change_detected_alert": {
        "en": "🚨 Crop Raksha detected a significant visual change and the AI identified a possible crop health issue.",
        "te": "🚨 క్రాప్ రక్ష గణనీయమైన దృశ్య మార్పును గుర్తించింది మరియు AI పంట ఆరోగ్య సమస్యను సూచించింది.",
        "hi": "🚨 क्रॉप रक्षा ने महत्वपूर्ण दृश्य परिवर्तन पाया और AI ने संभावित फसल स्वास्थ्य समस्या पहचानी।",
        "mr": "🚨 क्रॉप रक्षा ने लक्षणीय दृश्य बदल ओळखला आणि AI ने संभाव्य पीक आरोग्य समस्या दर्शवली."
    },

    "open_diagnose_section": {
        "en": "🩺 Please open the Diagnose section for a detailed assessment.",
        "te": "🩺 వివరమైన అంచనా కోసం నిర్ధారణ విభాగాన్ని తెరవండి.",
        "hi": "🩺 विस्तृत जांच के लिए निदान अनुभाग खोलें।",
        "mr": "🩺 सविस्तर तपासणीसाठी निदान विभाग उघडा."
    },

    "visual_change_noticed_healthy": {
        "en": "🟠 Crop Raksha noticed a visual change, but the AI currently considers the crop healthy.",
        "te": "🟠 క్రాప్ రక్ష దృశ్య మార్పును గుర్తించింది, కానీ AI ప్రస్తుతం పంటను ఆరోగ్యంగా పరిగణిస్తోంది.",
        "hi": "🟠 क्रॉप रक्षा ने दृश्य परिवर्तन देखा, लेकिन AI अभी फसल को स्वस्थ मानता है।",
        "mr": "🟠 क्रॉप रक्षा ने दृश्य बदल लक्षात घेतला, पण AI सध्या पीक निरोगी मानतो."
    },

    "no_major_health_concern": {
        "en": "🟢 Crop Raksha currently sees no major health concern.",
        "te": "🟢 క్రాప్ రక్ష ప్రస్తుతం పెద్ద ఆరోగ్య సమస్యను చూడడం లేదు.",
        "hi": "🟢 क्रॉप रक्षा को अभी कोई बड़ी स्वास्थ्य चिंता नहीं दिख रही है।",
        "mr": "🟢 क्रॉप रक्षा ला सध्या मोठी आरोग्याची चिंता दिसत नाही."
    },

    "possible_issue_detected": {
        "en": "🟠 The AI detected a possible issue. Consider using the Diagnose section for confirmation.",
        "te": "🟠 AI ఒక సాధ్యమైన సమస్యను గుర్తించింది. నిర్ధారణ కోసం డయాగ్నోసిస్ విభాగాన్ని ఉపయోగించండి.",
        "hi": "🟠 AI ने संभावित समस्या पहचानी। पुष्टि के लिए निदान अनुभाग का उपयोग करें।",
        "mr": "🟠 AI ने संभाव्य समस्या ओळखली. पुष्टीसाठी निदान विभाग वापरा."
    },

    "todays_check_complete": {
        "en": "✅ **Today's Crop Raksha check is complete!**\n\nYou completed today's observation at **{time}**.\n\n🧠 Crop Raksha has remembered it.\n\nYour next observation will be available tomorrow.",
        "te": "✅ **ఈరోజు క్రాప్ రక్ష చెక్ పూర్తయింది!**\n\nమీరు **{time}** ఈరోజు పరిశీలనను పూర్తి చేశారు.\n\n🧠 క్రాప్ రక్ష అదన్గా గుర్తుంచుకుంది.\n\nమీ తదుపరి పరిశీలన రే్కలో అందుబాటులో ఉంటుంది.",
        "hi": "✅ **आज की क्रॉप रक्षा जांच पूरी हो गई!**\n\nआपने **{time}** आज का अवलोकन पूरा किया।\n\n🧠 क्रॉप रक्षा ने इसे याद कर लिया है।\n\nआपका अगला अवलोकन कल उपलब्ध होगा।",
        "mr": "✅ **आजचे क्रॉप रक्षा चेक पूर्ण झाले!**\n\nतुम्ही **{time}** आजचे निरीक्षण पूर्ण केले.\n\n🧠 क्रॉप रक्षा ने ते आठवले.\n\nतुमचे पुढील निरीक्षण उद्या उपलब्ध होईल."
    },

    "check_not_due_yet": {
        "en": "⏰ **Today's Crop Raksha check is not due yet.**\n\nYour selected monitoring time is **{time}**.\n\nCome back at that time and we'll continue today's crop check.",
        "te": "⏰ **ఈరోజు క్రాప్ రక్ష చెక్ ఇంకా రావాల్సి ఉంది.**\n\nమీ ఎంచుకున్న పర్యవేక్షణ సమయం **{time}**.\n\nఆ సమయంలో తిరిగి రండి మరియు ఈరోజు పంట చెక్ కొనసాగిస్తాము.",
        "hi": "⏰ **आज की क्रॉप रक्षा जांच अभी तय नहीं है।**\n\nआपका चुना हुआ निगरानी समय **{time}** है।\n\nउस समय वापस आएं और हम आज की फसल जांच जारी रखेंगे।",
        "mr": "⏰ **आजचे क्रॉप रक्षा चेक अद्याप आलेले नाही.**\n\nतुमची निवडलेली निरीक्षण वेळ **{time}** आहे.\n\nत्या वेळी परत या आणि आजचे पीक चेक सुरू करूया."
    },

    "crop_raksha_timeline": {
        "en": "📅 Crop Raksha Timeline",
        "te": "📅 క్రాప్ రక్ష టైమ్‌లైన్",
        "hi": "📅 क्रॉप रक्षा टाइमलाइन",
        "mr": "📅 क्रॉप रक्षा टाइमलाइन"
    },

    "observations_appear_here": {
        "en": "Your daily observations will appear here.",
        "te": "మీ రోజువారీ పరిశీలనలు ఇక్కడ కనిపిస్తాయి.",
        "hi": "आपके दैनिक अवलोकन यहां दिखाई देंगे।",
        "mr": "तुमची दैनिक निरीक्षणे येथे दिसतील."
    },

    "day_label": {
        "en": "🌱 Day",
        "te": "🌱 రోజు",
        "hi": "🌱 दिन",
        "mr": "🌱 दिवस"
    },

    "ai_caption": {
        "en": "🤖 AI:",
        "te": "🤖 AI:",
        "hi": "🤖 AI:",
        "mr": "🤖 AI:"
    },

    "view_heatmap": {
        "en": "🔥 View Visual Change Heatmap",
        "te": "🔥 दృశ్య మార్పు హీట్‌మ్యాప్ చూడండి",
        "hi": "🔥 दृश्य परिवर्तन हीटमैप देखें",
        "mr": "🔥 दृश्य बदल हीटमॅप पहा"
    },

    "show_more": {
        "en": "Show more (showing {shown} of {total})",
        "te": "మరిన్ని చూపించు ({total}లో {shown} చూపిస్తున్నాము)",
        "hi": "और दिखाएं ({total} में से {shown} दिखा रहे हैं)",
        "mr": "आणखी दाखवा ({total} पैकी {shown} दाखवत आहोत)"
    },

    # -------------------------------------------------
    # COMPARISON VIEWER
    # -------------------------------------------------

    "before_after_comparison": {
        "en": "🔍 Before/After Comparison",
        "te": "🔍 ముందు/తర్వాత పోలిక",
        "hi": "🔍 पहले/बाद की तुलना",
        "mr": "🔍 आधी/नंतरची तुलना"
    },

    "hide_comparison": {
        "en": "🔍 Hide Comparison",
        "te": "🔍 పోలికలు దాచండి",
        "hi": "🔍 तुलना छुपाएं",
        "mr": "🔍 तुलना लपवा"
    },

    "before_after_pick_days": {
        "en": "📸 Before / After — Pick Any Two Days",
        "te": "📸 ముందు / తర్వాత — ఏవైనా రెండు రోజులను ఎంచుకోండి",
        "hi": "📸 पहले / बाद — कोई भी दो दिन चुनें",
        "mr": "📸 आधी / नंतर — कोणतेही दोन दिवस निवडा"
    },

    "select_earlier_observation": {
        "en": "Select earlier observation",
        "te": "మునుపటి పరిశీలనను ఎంచుకోండి",
        "hi": "पहला अवलोकन चुनें",
        "mr": "आधीचे निरीक्षण निवडा"
    },

    "select_later_observation": {
        "en": "Select later observation",
        "te": "తరువాతి పరిశీలనను ఎంచుకోండి",
        "hi": "बाद का अवलोकन चुनें",
        "mr": "नंतरचे निरीक्षण निवडा"
    },

    "before_label": {
        "en": "📷 Before",
        "te": "📷 ముందు",
        "hi": "📷 पहले",
        "mr": "📷 आधी"
    },

    "after_label": {
        "en": "📷 After",
        "te": "📷 తర్వాత",
        "hi": "📷 बाद में",
        "mr": "📷 नंतर"
    },

    "select_different_observations": {
        "en": "⚠️ Please select two different observations to compare.",
        "te": "⚠️ పోలించడానికి భిన్నమైన రెండు పరిశీలనలను ఎంచుకోండి.",
        "hi": "⚠️ कृपया तुलना के लिए दो अलग-अलग अवलोकन चुनें।",
        "mr": "⚠️ कृपया तुलनेसाठी दोन वेगळी निरीक्षणे निवडा."
    },

    "could_not_load_images": {
        "en": "Could not load images.",
        "te": "చిత్రాలను లోడ్ కాలేకపోయింది.",
        "hi": "चित्र लोड नहीं हो सके।",
        "mr": "प्रतिमा लोड होऊ शकल्या नाहीत."
    },

    "ai_confidence_label": {
        "en": "🎯 AI Confidence:",
        "te": "🎯 AI నమ్మకం:",
        "hi": "🎯 AI विश्वास:",
        "mr": "🎯 AI विश्वास:"
    },

    "visual_difference_analysis": {
        "en": "🔥 Visual Difference Analysis",
        "te": "🔥 दృశ్య తేడా విశ్లేషణ",
        "hi": "🔥 दृश्य अंतर विश्लेषण",
        "mr": "🔥 दृश्य फरक विश्लेषण"
    },

    "could_not_compute": {
        "en": "Could not compute visual difference.",
        "te": "దృశ్య తేడాను లెక్కించలేకపోయింది.",
        "hi": "दृश्य अंतर की गणना नहीं हो सकी।",
        "mr": "दृश्य फरक काढता आला नाही."
    },

    "days_apart": {
        "en": "Days Apart",
        "te": "రోజుల తేడా",
        "hi": "दिनों का अंतर",
        "mr": "दिवसांचे अंतर"
    },

    "show_heatmap": {
        "en": "🔥 Show Visual Change Heatmap",
        "te": "🔥 दృశ్య మార్పు హీట్‌మ్యాప్ చూపించు",
        "hi": "🔥 दृश्य परिवर्तन हीटमैप दिखाएं",
        "mr": "🔥 दृश्य बदल हीटमॅप दाखवा"
    },

    "ai_comparison": {
        "en": "🤖 AI Comparison",
        "te": "🤖 AI పోలిక",
        "hi": "🤖 AI तुलना",
        "mr": "🤖 AI तुलना"
    },

    "ai_verdict_consistent": {
        "en": "🤖 **AI verdict is consistent:** both days show **{disease}**.",
        "te": "🤖 **AI తీర్మానం స్థిరంగా ఉంది:** రెండు రోజుల్లో **{disease}** చూపిస్తుంది.",
        "hi": "🤖 **AI verdict is consistent:** both days show **{disease}**.",
        "mr": "🤖 **AI verdict आहे consistent:** both days show **{disease}**."
    },

    "ai_verdict_changed": {
        "en": "🤖 **AI verdict changed:** Day {day1} = **{disease1}** ({conf1}%) → Day {day2} = **{disease2}** ({conf2}%)",
        "te": "🤖 **AI తీర్మానం మారింది:** రోజు {day1} = **{disease1}** ({conf1}%) → రోజు {day2} = **{disease2}** ({conf2}%)",
        "hi": "🤖 **AI verdict बदल गई:** दिन {day1} = **{disease1}** ({conf1}%) → दिन {day2} = **{disease2}** ({conf2}%)",
        "mr": "🤖 **AI verdict बदलले:** दिवस {day1} = **{disease1}** ({conf1}%) → दिवस {day2} = **{disease2}** ({conf2}%)"
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

    "confidence_values_recent": {
        "en": "Confidence values from recent diagnoses.",
        "te": "ఇటీవలి నిర్ధారణల నుండి నమ్మకం విలువలు.",
        "hi": "हाल की जांचों से विश्वास मान।",
        "mr": "अलीकडील निदानांमधून विश्वास मूल्ये."
    },

    "diagnosis_history": {
        "en": "📅 Diagnosis History",
        "te": "📅 రోగ నిర్ధారణ చరిత్ర",
        "hi": "📅 निदान इतिहास",
        "mr": "📅 निदान इतिहास"
    },

    "show_more_monitoring": {
        "en": "Show more (showing {shown} of {total})",
        "te": "మరిన్ని చూపించు ({total}లో {shown} చూపిస్తున్నాము)",
        "hi": "और दिखाएं ({total} में से {shown} दिखा रहे हैं)",
        "mr": "आणखी दाखवा ({total} पैकी {shown} दाखवत आहोत)"
    },

    "monitoring_record_date": {
        "en": "Date",
        "te": "తేదీ",
        "hi": "तारीख",
        "mr": "तारीख"
    },

    "monitoring_record_crop": {
        "en": "Crop",
        "te": "పంట",
        "hi": "फसल",
        "mr": "पीक"
    },

    "monitoring_record_disease": {
        "en": "Disease",
        "te": "వ్యాధి",
        "hi": "रोग",
        "mr": "रोग"
    },

    "monitoring_record_confidence": {
        "en": "Confidence",
        "te": "నమ్మకం",
        "hi": "विश्वास",
        "mr": "विश्वास"
    },

    "export_diagnosis_records": {
        "en": "📥 Export Diagnosis Records",
        "te": "📥 నిర్ధారణ రికార్డులను ఎగుమతి చేయండి",
        "hi": "📥 निदान रिकॉर्ड निर्यात करें",
        "mr": "📥 निदान रेकॉर्ड एक्सपोर्ट करा"
    },

    "download_diagnosis_csv": {
        "en": "📄 Download Diagnosis History (CSV)",
        "te": "📄 నిర్ధారణ చరిత్ర (CSV) డౌన్‌లోడ్ చేయండి",
        "hi": "📄 निदान इतिहास (CSV) डाउनलोड करें",
        "mr": "📄 निदान इतिहास (CSV) डाउनलोड करा"
    },

    "download_raksha_csv": {
        "en": "📄 Download Crop Raksha Records (CSV)",
        "te": "📄 క్రాప్ రక్ష రికార్డులను (CSV) డౌన్‌లోడ్ చేయండి",
        "hi": "📄 क्रॉप रक्षा रिकॉर्ड (CSV) डाउनलोड करें",
        "mr": "📄 क्रॉप रक्षा रेकॉर्ड (CSV) डाउनलोड करा"
    },

    "no_diagnosis_records": {
        "en": "No diagnosis records to export yet.",
        "te": "ఇంకా ఎగుమతి చేయడానికి నిర్ధారణ రికార్డులు లేవు.",
        "hi": "अभी तक निर्यात के लिए कोई निदान रिकॉर्ड नहीं।",
        "mr": "अद्याप एक्सपोर्ट करण्यासाठी कोणतेही निदान रेकॉर्ड नाहीत."
    },

    "no_raksha_records": {
        "en": "No Crop Raksha records to export yet.",
        "te": "ఇంకా ఎగుమతి చేయడానికి క్రాప్ రక్ష రికార్డులు లేవు.",
        "hi": "अभी तक निर्यात के लिए कोई क्रॉप रक्षा रिकॉर्ड नहीं।",
        "mr": "अद्याप एक्सपोर्ट करण्यासाठी कोणतेही क्रॉप रक्षा रेकॉर्ड नाहीत."
    },

    "csv_share_note": {
        "en": "📋 CSV files can be shared with extension officers, agricultural experts, or kept for farm records.",
        "te": "📋 CSV ఫైల్‌లను విస్తరణ అధికారులు, వ్యవసాయ నిపుణులతో భాగస్వామ్యం చేయవచ్చు లేదా పంట రికార్డుల కోసం ఉంచవచ్చు.",
        "hi": "📋 CSV फ़ाइलें विस्तार अधिकारियों, कृषि विशेषज्ञों के साथ साझा की जा सकती हैं, या खेत के रिकॉर्ड के लिए रखी जा सकती हैं।",
        "mr": "📋 CSV फाइली विस्तार अधिकाऱ्यांसोबत, शेती तज्ञांसोबत शेअर करता येतात किंवा शेती रेकॉर्डसाठी ठेवता येतात."
    },

    "clear_history_confirm": {
        "en": "I understand this will permanently delete all diagnosis history.",
        "te": "ఈ నిర్ధారణ చరిత్ర మొత్తం శాశ్వతంగా తొలగించబడుతుందని నాకు తెలుసు.",
        "hi": "मैं समझता हूँ कि इससे पूरा निदान इतिहास स्थायी रूप से हट जाएगा।",
        "mr": "मला समजते की यामुळे संपूर्ण निदान इतिहास कायमचा हटवला जाईल."
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
    # ANJANEYA VOICE / IVR
    # -------------------------------------------------

    "anjaneya_ai_voice_guardian": {
        "en": "🔱 Anjaneya — AI Voice Crop Guardian",
        "te": "🔱 ఆంజనేయ — AI వాయిస్ క్రాప్ గార్డియన్",
        "hi": "🔱 आंजनेय — AI वॉइस क्रॉप गार्जियन",
        "mr": "🔱 आंजनेय — AI व्हॉइस क्रॉप गार्जियन"
    },

    "multilingual_offline_ai": {
        "en": "Multilingual Offline AI Voice Assistant",
        "te": "బహుభాషా ఆఫ్‌లైన్ AI వాయిస్ అసిస్టెంట్",
        "hi": "बहुभाषी ऑफ़लाइन AI वॉइस असिस्टेंट",
        "mr": "बहुभाषी ऑफलाइन AI व्हॉइस असिस्टंट"
    },

    "ivr_demo_how_it_works": {
        "en": "ℹ️ IVR Demo — How it works",
        "te": "ℹ️ IVR డెమో — ఇది ఎలా పనిచేస్తుంది",
        "hi": "ℹ️ IVR डेमो — यह कैसे काम करता है",
        "mr": "ℹ️ IVR डेमो — हे कसे काम करते"
    },

    "registered_crops_metric": {
        "en": "Registered Crops",
        "te": "నమోదు చేసిన పంటలు",
        "hi": "पंजीकृत फसलें",
        "mr": "नोंदणीकृत पिकें"
    },

    "raksha_records_metric": {
        "en": "Raksha Records",
        "te": "క్రాప్ రక్ష రికార్డులు",
        "hi": "क्रॉप रक्षा रिकॉर्ड",
        "mr": "क्रॉप रक्षा रेकॉर्ड"
    },

    "monitoring_records_metric": {
        "en": "Monitoring Records",
        "te": "పర్యవేక్షణ రికార్డులు",
        "hi": "निगरानी रिकॉर्ड",
        "mr": "निरीक्षण रेकॉर्ड"
    },

    # -------------------------------------------------
    # IVR VOICE ASSISTANT (Anjaneya)
    # -------------------------------------------------

    "main_menu": {
        "en": "Main Menu",
        "te": "ప్రధాన మెనూ",
        "hi": "मुख्य मेनू",
        "mr": "मुख्य मेनू"
    },

    "no_crops": {
        "en": "No crops registered.",
        "te": "పంటలు నమోదు కాలేదు.",
        "hi": "कोई फसल पंजीकृत नहीं।",
        "mr": "कोणतीही पीक नोंदलेली नाही."
    },

    "choose_crop": {
        "en": "Please choose a crop.",
        "te": "దయచేసి ఒక పంటను ఎంచుకోండి.",
        "hi": "कृपया एक फसल चुनें।",
        "mr": "कृपया एक पीक निवडा."
    },

    "last_observation": {
        "en": "Last observation was on {date}.",
        "te": "చివరి పరిశీలన {date} న జరిగింది.",
        "hi": "अंतिम अवलोकन {date} को हुआ था।",
        "mr": "शेवटचे निरीक्षण {date} रोजी झाले."
    },

    "raksha_count": {
        "en": "You have {count} Crop Raksha records.",
        "te": "మీకు {count} క్రాప్ రక్ష రికార్డులు ఉన్నాయి.",
        "hi": "आपके पास {count} क्रॉप रक्षा रिकॉर्ड हैं।",
        "mr": "तुमच्याकडे {count} क्रॉप रक्षा रेकॉर्ड आहेत."
    },

    "monitoring_count": {
        "en": "You have {count} monitoring records.",
        "te": "మీకు {count} పర్యవేక్షణ రికార్డులు ఉన్నాయి.",
        "hi": "आपके पास {count} निगरानी रिकॉर्ड हैं।",
        "mr": "तुमच्याकडे {count} निरीक्षण रेकॉर्ड आहेत."
    },

    "raksha": {
        "en": "Crop Raksha",
        "te": "క్రాప్ రక్ష",
        "hi": "क्रॉप रक्षा",
        "mr": "क्रॉप रक्षा"
    },

    "no_history": {
        "en": "No history available.",
        "te": "చరిత్ర ఏదీ అందుబాటులో లేదు.",
        "hi": "कोई इतिहास उपलब्ध नहीं।",
        "mr": "कोणताही इतिहास उपलब्ध नाही."
    },

    "diagnosis": {
        "en": "Diagnosis",
        "te": "నిర్ధారణ",
        "hi": "निदान",
        "mr": "निदान"
    },

    "help": {
        "en": "Help",
        "te": "సహాయం",
        "hi": "मदद",
        "mr": "मदत"
    },

    "goodbye": {
        "en": "Goodbye!",
        "te": "వీడ్కోలు!",
        "hi": "अलविदा!",
        "mr": "निरोप!"
    },

    "invalid": {
        "en": "Invalid option. Please try again.",
        "te": "చెల్లని ఎంపిక. దయచేసి మళ్లీ ప్రయత్నించండి.",
        "hi": "अमान्य विकल्प। कृपया पुनः प्रयास करें।",
        "mr": "अवैध पर्याय. कृपया पुन्हा प्रयत्न करा."
    },

    "repeat": {
        "en": "Press 9 to repeat.",
        "te": "పునరావృతం చేయడానికి 9 నొక్కండి.",
        "hi": "दोहराने के लिए 9 दबाएं।",
        "mr": "पुन्हा ऐकण्यासाठी 9 दाबा."
    },

    "choose_language": {
        "en": "Please choose your language.",
        "te": "దయచేసి మీ భాషను ఎంచుకోండి.",
        "hi": "कृपया अपनी भाषा चुनें।",
        "mr": "कृपया तुमची भाषा निवडा."
    },

    "confirm_crop": {
        "en": "You selected {crop}. Press 1 to confirm.",
        "te": "మీరు {crop} ఎంచుకున్నారు. నిర్ధారించడానికి 1 నొక్కండి.",
        "hi": "आपने {crop} चुना। पुष्टि के लिए 1 दबाएं।",
        "mr": "तुम्ही {crop} निवडले. पुष्टीसाठी 1 दाबा."
    },

    # -------------------------------------------------
    # ANJANEYA VOICE UI STRINGS
    # -------------------------------------------------

    "anjaneya_title": {
        "en": "🔱 Anjaneya — AI Voice Crop Guardian",
        "te": "🔱 ఆంజనేయ — AI వాయిస్ క్రాప్ గార్డియన్",
        "hi": "🔱 आंजनेय — AI वॉइस क्रॉप गार्जियन",
        "mr": "🔱 आंजनेय — AI व्हॉइस क्रॉप गार्जियन"
    },

    "anjaneya_subtitle": {
        "en": "Multilingual Offline AI Voice Assistant",
        "te": "బహుభాషా ఆఫ్‌లైన్ AI వాయిస్ అసిస్టెంట్",
        "hi": "बहुभाषी ऑफ़लाइन AI वॉइस असिस्टेंट",
        "mr": "बहुभाषी ऑफलाइन AI व्हॉइस असिस्टंट"
    },

    "status_not_connected": {
        "en": "Not connected",
        "te": "కనెక్ట్ చేయబడలేదు",
        "hi": "कनेक्ट नहीं है",
        "mr": "कनेक्ट केलेले नाही"
    },

    "status_connected": {
        "en": "Connected",
        "te": "కనెక్ట్ చేయబడింది",
        "hi": "कनेक्ट है",
        "mr": "कनेक्ट केलेले आहे"
    },

    "status_connecting": {
        "en": "Connecting",
        "te": "కనెక్ట్ చేస్తోంది",
        "hi": "कनेक्ट हो रहा है",
        "mr": "कनेक्ट होत आहे"
    },

    "status_ready": {
        "en": "Ready",
        "te": "సిద్ధంగా ఉంది",
        "hi": "तैयार",
        "mr": "तयार"
    },

    "status_speaking": {
        "en": "Speaking",
        "te": "మాట్లాడుతోంది",
        "hi": "बोल रहा है",
        "mr": "बोलत आहे"
    },

    "status_listening": {
        "en": "Listening...",
        "te": "వినుతోంది...",
        "hi": "सुन रहा है...",
        "mr": "ऐकत आहे..."
    },

    "status_voice_error": {
        "en": "Voice error",
        "te": "వాయిస్ ఎరర్",
        "hi": "वॉइस त्रुटि",
        "mr": "व्हॉइस एरर"
    },

    "status_call_ended": {
        "en": "Call ended",
        "te": "కాల్ ముగిసింది",
        "hi": "कॉल खत्म",
        "mr": "कॉल संपली"
    },

    "status_voice_unavailable": {
        "en": "Voice input unavailable",
        "te": "వాయిస్ ఇన్‌పుట్ అందుబాటులో లేదు",
        "hi": "वॉइस इनपुट उपलब्ध नहीं",
        "mr": "व्हॉइस इनपुट उपलब्ध नाही"
    },

    "status_mic_unavailable": {
        "en": "Microphone unavailable",
        "te": "మైక్రోఫోన్ అందుబాటులో లేదు",
        "hi": "माइक्रोफ़ोन उपलब्ध नहीं",
        "mr": "माइक्रोफोन उपलब्ध नाही"
    },

    "checking_language_voices": {
        "en": "Checking language voices...",
        "te": "భాష వాయిస్‌లను తనిఖీ చేస్తోంది...",
        "hi": "भाषा वॉइस की जाँच हो रही है...",
        "mr": "भाषा व्हॉइस तपासत आहे..."
    },

    "choose_language_activate": {
        "en": "Choose a language to activate its voice.",
        "te": "దృశ్య స్థితిని చూడడానికి భాషను ఎంచుకోండి.",
        "hi": "आवाज़ सक्रिय करने के लिए भाषा चुनें।",
        "mr": "आवाज सक्रिय करण्यासाठी भाषा निवडा."
    },

    "voice_not_installed": {
        "en": "voice not installed in this browser.",
        "te": "ఈ బ్రౌజర్‌లో వాయిస్ ఇన్‌స్టాల్ చేయబడలేదు.",
        "hi": "इस ब्राउज़र में वॉइस इंस्टॉल नहीं है।",
        "mr": "या ब्राउझरमध्ये व्हॉइस इंस्टॉल नाही."
    },

    "no_voice_available": {
        "en": "No {language} voice is available.",
        "te": "{language} వాయిస్ అందుబాటులో లేదు.",
        "hi": "{language} वॉइस उपलब्ध नहीं है।",
        "mr": "{language} व्हॉइस उपलब्ध नाही."
    },

    "speech_not_supported": {
        "en": "Speech synthesis is not supported.",
        "te": "స్పీచ్ సింథసిస్ సపోర్టెడ్ కాదు.",
        "hi": "स्पीच सिंथेसिस समर्थित नहीं है।",
        "mr": "स्पीच सिंथेसिस समर्थित नाही."
    },

    "screen_label": {
        "en": "AI VOICE ASSISTANT",
        "te": "AI వాయిస్ అసిస్టెంట్",
        "hi": "AI वॉइस असिस्टेंट",
        "mr": "AI व्हॉइस असिस्टंट"
    },

    "press_ok_start": {
        "en": "Press OK to start the call.",
        "te": "కాల్ ప్రారంభించడానికి OK నొక్కండి.",
        "hi": "कॉल शुरू करने के लिए OK दबाएं।",
        "mr": "कॉल सुरू करण्यासाठी OK दाबा."
    },

    "mic_instruction": {
        "en": "This is a voice call — just speak",
        "te": "ఇది వాయిస్ కాల్ — కేవలం మాట్లాడండి",
        "hi": "यह एक वॉइस कॉल है — बस बोलें",
        "mr": "ही एक व्हॉइस कॉल आहे — फक्त बोला"
    },

    "status_not_connected": {
        "en": "Not connected",
        "te": "కనెక్ట్ చేయబడలేదు",
        "hi": "कनेक्ट नहीं है",
        "mr": "कनेक्ट केलेले नाही"
    },

    "status_connected": {
        "en": "Connected",
        "te": "కనెక్ట్ చేయబడింది",
        "hi": "कनेक्ट है",
        "mr": "कनेक्ट केलेले आहे"
    },

    "status_connecting": {
        "en": "Connecting",
        "te": "కనెక్ట్ చేస్తోంది",
        "hi": "कनेक्ट हो रहा है",
        "mr": "कनेक्ट होत आहे"
    },

    "status_ready": {
        "en": "Ready",
        "te": "సిద్ధంగా ఉంది",
        "hi": "तैयार",
        "mr": "तयार"
    },

    "status_speaking": {
        "en": "Speaking",
        "te": "మాట్లాడుతోంది",
        "hi": "बोल रहा है",
        "mr": "बोलत आहे"
    },

    "status_listening": {
        "en": "Listening...",
        "te": "వినుతోంది...",
        "hi": "सुन रहा है...",
        "mr": "ऐकत आहे..."
    },

    "status_voice_error": {
        "en": "Voice error",
        "te": "వాయిస్ ఎరర్",
        "hi": "वॉइस त्रुटि",
        "mr": "व्हॉइस एरर"
    },

    "status_call_ended": {
        "en": "Call ended",
        "te": "కాల్ ముగిసింది",
        "hi": "कॉल खत्म",
        "mr": "कॉल संपली"
    },

    "status_voice_unavailable": {
        "en": "Voice input unavailable",
        "te": "వాయిస్ ఇన్‌పుట్ అందుబాటులో లేదు",
        "hi": "वॉइस इनपुट उपलब्ध नहीं",
        "mr": "व्हॉइस इनपुट उपलब्ध नाही"
    },

    "status_mic_unavailable": {
        "en": "Microphone unavailable",
        "te": "మైక్రోఫోన్ అందుబాటులో లేదు",
        "hi": "माइक्रोफ़ोन उपलब्ध नहीं",
        "mr": "माइक्रोफोन उपलब्ध नाही"
    },

    "checking_language_voices": {
        "en": "Checking language voices...",
        "te": "భాష వాయిస్‌లను తనిఖీ చేస్తోంది...",
        "hi": "भाषा वॉइस की जाँच हो रही है...",
        "mr": "भाषा व्हॉइस तपासत आहे..."
    },

    "choose_language_activate": {
        "en": "Choose a language to activate its voice.",
        "te": "దృశ్య స్థితిని చూడడానికి భాషను ఎంచుకోండి.",
        "hi": "आवाज़ सक्रिय करने के लिए भाषा चुनें।",
        "mr": "आवाज सक्रिय करण्यासाठी भाषा निवडा."
    },

    "voice_not_installed": {
        "en": "voice not installed in this browser.",
        "te": "ఈ బ్రౌజర్‌లో వాయిస్ ఇన్‌స్టాల్ చేయబడలేదు.",
        "hi": "इस ब्राउज़र में वॉइस इंस्टॉल नहीं है।",
        "mr": "या ब्राउझरमध्ये व्हॉइस इंस्टॉल नाही."
    },

    "no_voice_available": {
        "en": "No {language} voice is available.",
        "te": "{language} వాయిస్ అందుబాటులో లేదు.",
        "hi": "{language} वॉइस उपलब्ध नहीं है।",
        "mr": "{language} व्हॉइस उपलब्ध नाही."
    },

    "speech_not_supported": {
        "en": "Speech synthesis is not supported.",
        "te": "స్పీచ్ సింథసిస్ సపోర్టెడ్ కాదు.",
        "hi": "स्पीच सिंथेसिस समर्थित नहीं है।",
        "mr": "स्पीच सिंथेसिस समर्थित नाही."
    },

    "anjaneya_speaking": {
        "en": "Anjaneya is speaking...",
        "te": "ఆంజనేయ మాట్లాడుతోంది...",
        "hi": "आंजनेय बोल रहा है...",
        "mr": "आंजनेय बोलत आहे..."
    },

    "listening_instruction": {
        "en": "Listening... please speak",
        "te": "వినుతోంది...దయచేసి మాట్లాడండి",
        "hi": "सुन रहा हैं... कृपया बोलें",
        "mr": "ऐकत आहे... कृपया बोला"
    },

    "call_ended": {
        "en": "Call ended",
        "te": "కాల్ ముగిసింది",
        "hi": "कॉल खत्म",
        "mr": "कॉल संपली"
    },

    "ok_button": {
        "en": "OK",
        "te": "సరే",
        "hi": "ठीक है",
        "mr": "ठीक आहे"
    },

    "tap_ok_caption": {
        "en": "Tap OK to start the call with Anjaneya.",
        "te": "ఆంజనేయతో కాల్ ప్రారంభించడానికి OK నొక్కండి.",
        "hi": "आंजनेय के साथ कॉल शुरू करने के लिए OK टैप करें।",
        "mr": "आंजनेयसोबत कॉल सुरू करण्यासाठी OK टॅप करा."
    },

    "allow_microphone": {
        "en": "Please allow microphone access when asked.",
        "te": "అభ్యర్థించినప్పుడు మైక్రోఫోన్ యాక్సెస్ అనుమతించండి.",
        "hi": "जब पूछा जाए तो कृपया माइक्रोफ़ोन एक्सेस की अनुमति दें।",
        "mr": "विनंती केली असल्यास कृपया मायक्रोफोन प्रवेश परवानगी द्या."
    },

    "footer_brand": {
        "en": "Anjaneya • Offline AI Voice IVR",
        "te": "ఆంజనేయ • ఆఫ్‌లైన్ AI వాయిస్ IVR",
        "hi": "आंजनेय • ऑफ़लाइन AI वॉइस IVR",
        "mr": "आंजनेय • ऑफलाइन AI व्हॉइस IVR"
    },

    "splash_jai_anjaneya": {
        "en": "🚩 जय अंजनेय 🚩",
        "te": "🚩 జయ్ ఆంజనేయ 🚩",
        "hi": "🚩 जय अंजनेय 🚩",
        "mr": "🚩 जय अंजनेय 🚩"
    },

    "voice_unavailable_message": {
        "en": "Voice input is not supported by this browser. Please try Chrome on Android or desktop.",
        "te": "ఈ బ్రౌజర్‌లో వాయిస్ ఇన్‌పుట్ సపోర్టెడ్ కాదు. Android లేదా డెస్క్‌టాప్‌పై Chrome ప్రయత్నించండి.",
        "hi": "इस ब्राउज़र में वॉइस इनपुट समर्थित नहीं है। Android या डेस्कटॉप पर Chrome आज़माएं।",
        "mr": "या ब्राउझरमध्ये व्हॉइस इनपुट समर्थित नाही. Android किंवा डेस्कटॉपवर Chrome वापरून पहा."
    },

    "mic_blocked_instruction": {
        "en": "Microphone access is blocked. Please allow it and reload.",
        "te": "మైక్రోఫోన్ యాక్సెస్ బ్లాక్ చేయబడింది. దయచేసి అనుమతించండి మరియు రీలోడ్ చేయండి.",
        "hi": "माइक्रोफ़ोन एक्सेस ब्लॉक है। कृपया इसे अनुमति दें और पुनः लोड करें।",
        "mr": "मायक्रोफोन प्रवेश प्रतिबंधित आहे. कृपया ते परवानगी द्या आणि पुन्हा लोड करा."
    },

    "voice_installed": {
        "en": "voice: ",
        "te": "వాయిస్: ",
        "hi": "वॉइस: ",
        "mr": "व्हॉइस: "
    },

    "no_recent_observation": {
        "en": "No recent AI observation is available.",
        "te": "ఇటీవల AI పరిశీలన అందుబాటులో లేదు.",
        "hi": "कोई हालिया AI अवलोकन उपलब्ध नहीं है।",
        "mr": "अलीकडील AI निरीक्षण उपलब्ध नाही."
    },

    "open_crop_raksha": {
        "en": "Open Crop Raksha in the main application to create the first observation.",
        "te": "మొదటి పరిశీలనను సృష్టించడానికి ప్రధాన అప్లికేషన్‌లో క్రాప్ రక్షను తెరవండి.",
        "hi": "पहला अवलोकन बनाने के लिए मुख्य एप्लिकेशन में क्रॉप रक्षा खोलें।",
        "mr": "पहिले निरीक्षण तयार करण्यासाठी मुख्य अनुप्रयोगात क्रॉप रक्षा उघडा."
    },

    "latest_observation_day": {
        "en": "Latest observation: Day {day}",
        "te": "తాజా పరిశీలన: డే {day}",
        "hi": "नवीनतम अवलोकन: दिन {day}",
        "mr": "नवीनतम निरीक्षण: दिवस {day}"
    },

    "ai_result": {
        "en": "AI result: ",
        "te": "AI ఫలితం: ",
        "hi": "AI परिणाम: ",
        "mr": "AI परिणाम: "
    },

    "confidence": {
        "en": "Confidence: ",
        "te": "నమ్మకం: ",
        "hi": "विश्वास: ",
        "mr": "विश्वास: "
    },

    "recorded": {
        "en": "Recorded: ",
        "te": "రికార్డ్ చేయబడింది: ",
        "hi": "दर्ज: ",
        "mr": "दर्ज केले: "
    },

    "use_clear_photo": {
        "en": "Use a clear photo of the leaf or affected plant part.",
        "te": "ఆకు లేదా ప్రభావిత మొక్క భాగం యొక్క స్పష్టమైన ఫోటోను ఉపయోగించండి.",
        "hi": "पत्ते या प्रभावित पौधे के भाग की साफ तस्वीर का उपयोग करें।",
        "mr": "पानाची किंवा प्रभावित वनस्पती भागाची स्पष्ट छायाचित्र वापरा."
    },

    "help_number_diagnosis": {
        "en": "1 = Diagnosis",
        "te": "1 = నిర్ధారణ",
        "hi": "1 = निदान",
        "mr": "1 = निदान"
    },

    "help_number_status": {
        "en": "2 = Crop Status",
        "te": "2 = పంట స్థితి",
        "hi": "2 = फसल स्थिति",
        "mr": "2 = पीक स्थिती"
    },

    "help_number_raksha": {
        "en": "3 = Crop Raksha AI",
        "te": "3 = క్రాప్ రక్ష AI",
        "hi": "3 = क्रॉप रक्षा AI",
        "mr": "3 = क्रॉप रक्षा AI"
    },

    "help_number_help": {
        "en": "4 = Help",
        "te": "4 = సహాయం",
        "hi": "4 = मदद",
        "mr": "4 = मदत"
    },

    "help_number_repeat": {
        "en": "9 = Repeat",
        "te": "9 = మళ్ళీ",
        "hi": "9 = दोहराएं",
        "mr": "9 = पुन्हा"
    },

    "help_number_end": {
        "en": "0 = End",
        "te": "0 = ముగించు",
        "hi": "0 = समाप्त",
        "mr": "0 = समाप्त"
    },

    "heard": {
        "en": "Heard: ",
        "te": "వినబడింది: ",
        "hi": "सुना: ",
        "mr": "ऐकले: "
    },

    "say_crop_number": {
        "en": "Say the crop number or its name.",
        "te": "పంట నంబర్ లేదా పేరు చెప్పండి.",
        "hi": "फसल का नंबर या नाम बोलें।",
        "mr": "पिकाचा क्रमांक किंवा नाव सांगा."
    },

    "ivr_how_it_works_title": {
        "en": "ℹ️ IVR Demo — How it works",
        "te": "ℹ️ IVR డెమో — ఇది ఎలా పనిచేస్తుంది",
        "hi": "ℹ️ IVR डेमो — यह कैसे काम करता है",
        "mr": "ℹ️ IVR डेमो — हे कसे काम करते"
    },

    "ivr_how_it_works_intro": {
        "en": "Anjaneya is a local, voice-only AI assistant — no keypad.",
        "te": "ఆంజనేయ ఒక లోకల్, వాయిస్-మాత్రమైన AI అసిస్టెంట్ — కీప్యాడ్ లేదు.",
        "hi": "आंजनेय एक स्थानीय, वॉइस-ओनली AI असिस्टेंट है — कोई कीपैड नहीं।",
        "mr": "आंजनेय हा एक लोकल, व्हॉइस-ओनली AI असिस्टंट आहे — कीपैड नाही."
    },

    "ivr_tap_ok_instruction": {
        "en": "Tap **OK** to start the call, allow microphone access, then just talk — like a real phone call:",
        "te": "**OK** నొక్కండి, మైక్రోఫోన్ యాక్సెస్ అనుమతించండి, ఆపై మాట్లాడండి — నిజమైన ఫోన్ కాల్ లాగా:",
        "hi": "कॉल शुरू करने के लिए **OK** टैप करें, माइक्रोफ़ोन एक्सेस की अनुमति दें, फिर बस बोलें — असली फोन कॉल की तरह:",
        "mr": "कॉल सुरू करण्यासाठी **OK** टॅप करा, मायक्रोफोन प्रवेश परवानगी द्या, नंतर फक्त बोला — खर्‍या फोन कॉलप्रमाणे:"
    },

    "ivr_step_ok": {
        "en": "🕉️ Tap OK, wait for the gada splash, then speak",
        "te": "🕉️ OK నొక్కండి, గడ స్ప్లాష్ కోసం వేచి ఉండండి, ఆపై మాట్లాడండి",
        "hi": "🕉️ OK टैप करें, गदा स्प्लैश का इंतज़ार करें, फिर बोलें",
        "mr": "🕉️ OK टॅप करा, गदा स्प्लॅशची वाट पाहा, नंतर बोला"
    },

    "ivr_step_language": {
        "en": "🗣️ Say your language: English, Telugu, Hindi or Marathi",
        "te": "🗣️ మీ భాష చెప్పండి: ఇంగ్లీష్, తెలుగు, హిందీ లేదా మరాఠీ",
        "hi": "🗣️ अपनी भाषा बोलें: अंग्रेज़ी, तेलुगु, हिंदी या मराठी",
        "mr": "🗣️ तुमची भाषा बोला: इंग्रजी, तेलुगू, हिंदी किंवा मराठी"
    },

    "ivr_step_diagnosis": {
        "en": "🩺 Say \"diagnosis\" for Crop Diagnosis",
        "te": "🩺 పంట వ్యాధి నిర్ధారణ కోసం \"నిర్ధారణ\" అని చెప్పండి",
        "hi": "🩺 फसल रोग पहचान के लिए \"निदान\" कहें",
        "mr": "🩺 पीक रोग निदानासाठी \"निदान\" म्हणा"
    },

    "ivr_step_status": {
        "en": "🌱 Say \"status\" for Crop Status",
        "te": "🌱 పంట స్థితి కోసం \"స్థితి\" అని చెప్పండి",
        "hi": "🌱 फसल स्थिति के लिए \"स्थिति\" कहें",
        "mr": "🌱 पीक स्थितीसाठी \"स्थिती\" म्हणा"
    },

    "ivr_step_raksha": {
        "en": "🛡️ Say \"raksha\" for Crop Raksha AI",
        "te": "🛡️ క్రాప్ రక్ష AI కోసం \"రక్ష\" అని చెప్పండి",
        "hi": "🛡️ क्रॉप रक्षा AI के लिए \"रक्षा\" कहें",
        "mr": "🛡️ क्रॉप रक्षा AI साठी \"रक्षा\" म्हणा"
    },

    "ivr_step_help": {
        "en": "❓ Say \"help\" for Help",
        "te": "❓ సహాయం కోసం \"సహాయం\" అని చెప్పండి",
        "hi": "❓ मदद के लिए \"मदद\" कहें",
        "mr": "❓ मदतीसाठी \"मदत\" म्हणा"
    },

    "ivr_step_repeat": {
        "en": "🔁 Say \"repeat\" to hear the menu again",
        "te": "🔁 మళ్ళీ మెనూ వినడానికి \"మళ్ళీ\" అని చెప్పండి",
        "hi": "🔁 मेनू फिर से सुनने के लिए \"दोबारा\" कहें",
        "mr": "🔁 पुन्हा मेनू ऐकण्यासाठी \"पुन्हा\" म्हणा"
    },

    "ivr_step_end": {
        "en": "☎️ Say \"end\" or \"stop\" to end the call",
        "te": "☎️ కాల్ ముగించడానికి \"ముగించు\" లేదా \"ఆపు\" అని చెప్పండి",
        "hi": "☎️ कॉल खत्म करने के लिए \"समाप्त\" या \"रुकें\" कहें",
        "mr": "☎️ कॉल संपवण्यासाठी \"समाप्त\" किंवा \"थांबा\" म्हणा"
    },

    "ivr_footer_note": {
        "en": "The assistant listens automatically after it finishes speaking — no buttons to press. It uses the browser's built-in speech recognition and speech voices; no phone network or external telephony service is required.",
        "te": "అసిస్టెంట్ పూర్తయిన తర్వాత స్వయంచాలకంగా వింటుంది — నొక్కవలసిన బటన్లు లేవు. ఇది బ్రౌజర్ యొక్క అంతర్నిర్మిత స్పీచ్ రికగ్నిషన్ మరియు స్పీచ్ వాయిస్‌లను ఉపయోగిస్తుంది; ఫోన్ నెట్‌వర్క్ లేదా బాహ్య టెలిఫోనీ సర్వీస్ అవసరం లేదు.",
        "hi": "असिस्टेंट बोलना खत्म करने के बाद स्वचालित रूप से सुनता है — कोई बटन दबाने की ज़रूरत नहीं। यह ब्राउज़र के अंतर्निहित स्पीच रिकग्निशन और स्पीच वॉइस का उपयोग करता है; कोई फोन नेटवर्क या बाहरी टेलीफोनी सेवा की आवश्यकता नहीं है।",
        "mr": "सहाय्यक बोलणे संपल्यानंतर स्वयंचलितपणे ऐकते — दाबण्यासाठी कोणतेही बटण नाही. हे ब्राउझरच्या अंगभूत स्पीच रिकग्निशन आणि स्पीच व्हॉइस वापरते; कोणतेही फोन नेटवर्क किंवा बाह्य टेलीफोनी सेवेची आवश्यकता नाही."
    },

    "registered_crops": {
        "en": "Registered Crops",
        "te": "నమోదు చేసిన పంటలు",
        "hi": "पंजीकृत फसलें",
        "mr": "नोंदणीकृत पिके"
    },

    "raksha_records": {
        "en": "Raksha Records",
        "te": "క్రాప్ రక్ష రికార్డులు",
        "hi": "क्रॉप रक्षा रिकॉर्ड",
        "mr": "क्रॉप रक्षा रेकॉर्ड"
    },

    "monitoring_records": {
        "en": "Monitoring Records",
        "te": "పర్యవేక్షణ రికార్డులు",
        "hi": "निगरानी रिकॉर्ड",
        "mr": "निरीक्षण रेकॉर्ड"
    },

    # -------------------------------------------------
    # ANJANEYA VOICE UPGRADE - OPENING EXPERIENCE
    # -------------------------------------------------

    "voice_opening_title": {
        "en": "🔱 Talk to Anjaneya",
        "te": "🔱 ఆంజనేయతో మాట్లాడండి",
        "hi": "🔱 आंजनेय से बात करें",
        "mr": "🔱 आंजनेयशी बोला"
    },

    "voice_opening_subtitle": {
        "en": "Your AI Voice Assistant",
        "te": "మీ AI వాయిస్ అసిస్టెంట్",
        "hi": "आपका AI वॉइस असिस्टेंट",
        "mr": "तुमचा AI व्हॉइस असिस्टंट"
    },

    "voice_opening_greeting": {
        "en": "👋 Tap the microphone to start speaking!",
        "te": "👋 మాట్లాడటం ప్రారంభించడానికి మైక్రోఫోన్‌పై నొక్కండి!",
        "hi": "👋 बोलना शुरू करने के लिए माइक्रोफोन पर टैप करें!",
        "mr": "👋 बोलणे सुरू करण्यासाठी मायक्रोफोनवर टॅप करा!"
    },

    "voice_opening_language": {
        "en": "Language: {lang}",
        "te": "భాష: {lang}",
        "hi": "भाषा: {lang}",
        "mr": "भाषा: {lang}"
    },

    "voice_opening_crop": {
        "en": "Crop: {crop}",
        "te": "పంట: {crop}",
        "hi": "फसल: {crop}",
        "mr": "पीक: {crop}"
    },

    # -------------------------------------------------
    # ANJANEYA VOICE - VOICE STATES
    # -------------------------------------------------

    "voice_state_sleeping": {
        "en": "😴 Ready — Tap to start",
        "te": "😴 సిద్ధంగా — ప్రారంభించడానికి నొక్కండి",
        "hi": "😴 तैयार — शुरू करने के लिए टैप करें",
        "mr": "😴 तयार — सुरू करण्यासाठी टॅप करा"
    },

    "voice_state_listening": {
        "en": "🎙️ Listening...",
        "te": "🎙️ వినుతోంది...",
        "hi": "🎙️ सुन रहा है...",
        "mr": "🎙️ ऐकत आहे..."
    },

    "voice_state_processing": {
        "en": "⚙️ Processing...",
        "te": "⚙️ ప్రాసెసింగ్...",
        "hi": "⚙️ प्रोसेसिंग...",
        "mr": "⚙️ प्रोसेसिंग..."
    },

    "voice_state_speaking": {
        "en": "🔊 Speaking...",
        "te": "🔊 మాట్లాడుతోంది...",
        "hi": "🔊 बोल रहा है...",
        "mr": "🔊 बोलत आहे..."
    },

    "voice_state_idle": {
        "en": "😴 Idle",
        "te": "😴 నిష్క్రియంగా",
        "hi": "😴 निष्क्रिय",
        "mr": "😴 निष्क्रिय"
    },

    # -------------------------------------------------
    # ANJANEYA VOICE - TALK BUTTON
    # -------------------------------------------------

    "talk": {
        "en": "TALK",
        "te": "మాట్లాడండి",
        "hi": "बोलें",
        "mr": "बोला"
    },

    "language_selected": {
        "en": "Language selected",
        "te": "భాష ఎంచుకుంది",
        "hi": "भाषा चुनी गई",
        "mr": "भाषा निवडली"
    },

    "tap_talk_to_speak": {
        "en": "Tap Talk to speak",
        "te": "మాట్లాడడానికి Talk నొక్కండి",
        "hi": "बोलने के लिए Talk दबाएं",
        "mr": "बोलण्यासाठी Talk दाबा"
    },

    "language_confirmed": {
        "en": "Language confirmed. Ready to assist.",
        "te": "భాష నిర్ధారించబడింది. సహాయం చేయడానికి సిద్ధంగా ఉంది.",
        "hi": "भाषा पुष्टि हो गई। सहायता के लिए तैयार।",
        "mr": "भाषा खात्री झाली. मदत करण्यासाठी तयार."
    },

    "ready_to_listen": {
        "en": "Ready to listen",
        "te": "వినడానికి సిద్ధంగా ఉంది",
        "hi": "सुनने के लिए तैयार",
        "mr": "ऐकण्यासाठी तयार"
    },

    # -------------------------------------------------
    # ANJANEYA VOICE - END CALL & CONTROLS
    # -------------------------------------------------

    "end_call": {
        "en": "End Call",
        "te": "కాల్ ముగించు",
        "hi": "कॉल खत्म करें",
        "mr": "कॉल संपवा"
    },

    "stop": {
        "en": "Stop",
        "te": "ఆపు",
        "hi": "रुकें",
        "mr": "थांबा"
    },

    "call_ended_message": {
        "en": "Call ended. Tap to start a new call.",
        "te": "కాల్ ముగిసింది. కొత్త కాల్ ప్రారంభించడానికి నొక్కండి.",
        "hi": "कॉल खत्म। नई कॉल शुरू करने के लिए टैप करें।",
        "mr": "कॉल संपली. नवीन कॉल सुरू करण्यासाठी टॅप करा."
    },

    "call_ended_title": {
        "en": "☎️ Call Ended",
        "te": "☎️ కాల్ ముగిసింది",
        "hi": "☎️ कॉल खत्म",
        "mr": "☎️ कॉल संपली"
    },

    "tap_to_restart": {
        "en": "Tap anywhere to start a new call",
        "te": "కొత్త కాల్ ప్రారంభించడానికి ఎక్కడైనా నొక్కండి",
        "hi": "नई कॉल शुरू करने के लिए कहीं भी टैप करें",
        "mr": "नवीन कॉल सुरू करण्यासाठी कुठेही टॅप करा"
    },

    "start_new_call": {
        "en": "Start New Call",
        "te": "కొత్త కాల్ ప్రారంభించు",
        "hi": "नई कॉल शुरू करें",
        "mr": "नवीन कॉल सुरू करा"
    },

    # -------------------------------------------------
    # ANJANEYA VOICE - MICROPHONE STATES
    # -------------------------------------------------

    "mic_tap_to_speak": {
        "en": "Tap to speak",
        "te": "మాట్లాడడానికి నొక్కండి",
        "hi": "बोलने के लिए टैप करें",
        "mr": "बोलण्यासाठी टॅप करा"
    },

    "mic_speaking": {
        "en": "Anjaneya is speaking...",
        "te": "ఆంజనేయ మాట్లాడుతోంది...",
        "hi": "आंजनेय बोल रहा है...",
        "mr": "आंजनेय बोलत आहे..."
    },

    "mic_processing": {
        "en": "Processing your request...",
        "te": "మీ అభ్యర్థనను ప్రాసెస్ చేస్తోంది...",
        "hi": "आपका अनुरोध प्रोसेस हो रहा है...",
        "mr": "तुमची विनंती प्रोसेस होत आहे..."
    },

    # -------------------------------------------------
    # ANJANEYA VOICE - OFFLINE NOTICE
    # -------------------------------------------------

    "offline_notice": {
        "en": "🌿 Works offline — uses your browser's voice",
        "te": "🌿 ఆఫ్‌లైన్‌లో పనిచేస్తుంది — మీ బ్రౌజర్ వాయిస్‌ను ఉపయోగిస్తుంది",
        "hi": "🌿 ऑफलाइन काम करता है — आपके ब्राउज़र की आवाज़ का उपयोग करता है",
        "mr": "🌿 ऑफलाइन काम करते — तुमच्या ब्राउझरच्या आवाज़ाचा वापर करते"
    },

    "browser_voice_notice": {
        "en": "Uses browser's built-in voice (Chrome recommended)",
        "te": "బ్రౌజర్ అంతర్గత వాయిస్‌ను ఉపయోగిస్తుంది (Chrome సిఫార్సు)",
        "hi": "ब्राउज़र की अंतर्निहित आवाज़ का उपयोग करता है (Chrome अनुशंसित)",
        "mr": "ब्राउझरच्या अंगभूत आवाज़ाचा वापर करते (Chrome शिफारसित)"
    },

    # -------------------------------------------------
    # ANJANEYA VOICE - ANIMATION LABELS
    # -------------------------------------------------

    "voice_indicator_ready": {
        "en": "Ready",
        "te": "సిద్ధంగా",
        "hi": "तैयार",
        "mr": "तयार"
    },

    "voice_indicator_waiting": {
        "en": "Waiting for you...",
        "te": "మీ కోసం వేచి ఉంది...",
        "hi": "आपका इंतज़ार...",
        "mr": "तुमची वाट पाहत आहे..."
    },

    "voice_indicator_connected": {
        "en": "Connected",
        "te": "కనెక్ట్ చేయబడింది",
        "hi": "कनेक्ट है",
        "mr": "कनेक्ट केलेले आहे"
    },

    # -------------------------------------------------
    # ANJANEYA VOICE - NO CROP SELECTED
    # -------------------------------------------------

    "no_crop_selected": {
        "en": "No crop selected",
        "te": "పంట ఎంచుకోబడలేదు",
        "hi": "कोई फसल नहीं चुनी",
        "mr": "कोणतेही पीक निवडलेले नाही"
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

    "visual_change_heatmap_about": {
        "en": "🔥 Visual Change Heatmap",
        "te": "🔥 దృశ్య మార్పు హీట్‌మ్యాప్",
        "hi": "🔥 दृश्य परिवर्तन हीटमैप",
        "mr": "🔥 दृश्य बदल हीटमॅप"
    },

    "daily_monitoring_about": {
        "en": "📊 Daily Monitoring",
        "te": "📊 రోజువారీ పర్యవేక్షణ",
        "hi": "📊 दैनिक निगरानी",
        "mr": "📊 दैनिक निरीक्षण"
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

    "about_crop_doctor_description": {
        "en": "Crop Doctor is an AI-powered crop health assistant designed to help identify crop diseases from leaf images.",
        "te": "క్రాప్ డాక్టర్ అనేది ఆకు చిత్రాల నుండి పంట వ్యాధులను గుర్తించడంలో సహాయపడే AI-ఆధారిత పంట ఆరోగ్య సహాయకుడు.",
        "hi": "क्रॉप डॉक्टर एक AI-संचालित फसल स्वास्थ्य सहायक है जो पत्तों की तस्वीरों से फसल रोगों की पहचान करने में मदद करता है।",
        "mr": "क्रॉप डॉक्टर हे एक AI-चालित पीक आरोग्य सहाय्यक आहे जे पानांच्या प्रतिमांमधून पीक रोग ओळखण्यास मदत करते."
    },

    "about_ai_detection_desc": {
        "en": "A trained deep-learning model analyzes uploaded crop leaf images and predicts the most likely disease or healthy class.",
        "te": "శిక్షణ పొందిన డీప్-లెర్నింగ్ మోడల్ అప్‌లోడ్ చేసిన పంట ఆకు చిత్రాలను విశ్లేషించి అత్యంత సంభావ్య వ్యాధి లేదా ఆరోగ్యకరమైన తరగతిని అంచనా వేస్తుంది.",
        "hi": "एक प्रशिक्षित डीप-लर्निंग मॉडल अपलोड की गई फसल पत्ते की तस्वीरों का विश्लेषण करता है और सबसे संभावित रोग या स्वस्थ वर्ग की भविष्यवाणी करता है।",
        "mr": "प्रशिक्षित डीप-लर्निंग मॉडेल अपलोड केलेल्या पीक पानांच्या प्रतिमांचे विश्लेषण करतो आणि सर्वात संभाव्य रोग किंवा निरोगी वर्गाचा अंदाज लावतो."
    },

    "about_crop_raksha": {
        "en": "🛡️ Crop Raksha",
        "te": "🛡️ క్రాప్ రక్ష",
        "hi": "🛡️ क्रॉप रक्षा",
        "mr": "🛡️ क्रॉप रक्षा"
    },

    "about_crop_raksha_desc": {
        "en": "Crop Raksha monitors registered crops through daily observations, remembers previous observations and looks for changes that may require attention.",
        "te": "క్రాప్ రక్ష నమోదు చేసిన పంటలను రోజువారీ పరిశీలనల ద్వారా పర్యవేక్షిస్తుంది, గత పరిశీలనలను గుర్తుంచుకుంటుంది మరియు శ్రద్ధ అవసరమయ్యే మార్పుల కోసం చూస్తుంది.",
        "hi": "क्रॉप रक्षा दैनिक अवलोकन के माध्यम से पंजीकृत फसलों की निगरानी करता है, पिछले अवलोकनों को याद रखता है और उन परिवर्तनों की तलाश करता है जिन पर ध्यान देने की आवश्यकता हो सकती है।",
        "mr": "क्रॉप रक्षा नोंदणीकृत पिकांचे दैनंदिन निरीक्षणाद्वारे निरीक्षण करतो, मागील निरीक्षणे लक्षात ठेवतो आणि लक्ष देणे आवश्यक असलेले बदल शोधतो."
    },

    "about_visual_change_desc": {
        "en": "Crop Raksha compares consecutive crop photographs and generates a visual difference heatmap showing areas where the crop image has changed.",
        "te": "క్రాప్ రక్ష వరుస పంట ఫోటోలను పోల్చి, పంట చిత్రం మారిన ప్రాంతాలను చూపించే దృశ్య తేడా హీట్‌మ్యాప్‌ను రూపొందిస్తుంది.",
        "hi": "क्रॉप रक्षा लगातार फसल तस्वीरों की तुलना करता है और एक दृश्य अंतर हीटमैप बनाता है जो उन क्षेत्रों को दिखाता है जहां फसल की तस्वीर बदल गई है।",
        "mr": "क्रॉप रक्षा सलग पीक फोटोंची तुलना करतो आणि पीक प्रतिमा बदललेली असलेली क्षेत्रे दर्शविणारा दृश्य फरक हीटमॅप तयार करतो."
    },

    "about_daily_monitoring_desc": {
        "en": "Diagnosis results and Crop Raksha observations are stored locally, allowing users to track crop health over multiple observations.",
        "te": "నిర్ధారణ ఫలితాలు మరియు క్రాప్ రక్ష పరిశీలనలు స్థానికంగా నిల్వ చేయబడతాయి, ఇది వినియోగదారులను అనేక పరిశీలనలలో పంట ఆరోగ్యాన్ని ట్రాక్ చేయడానికి అనుమతిస్తుంది.",
        "hi": "निदान परिणाम और क्रॉप रक्षा अवलोकन स्थानीय रूप से संग्रहीत किए जाते हैं, जिससे उपयोगकर्ता कई अवलोकनों में फसल स्वास्थ्य को ट्रैक कर सकते हैं।",
        "mr": "निदान निष्कर्ष आणि क्रॉप रक्षा निरीक्षणे स्थानिक पातळीवर साठवली जातात, ज्यामुळे वापरकर्त्यांना अनेक निरीक्षणांमध्ये पीक आरोग्याचा मागोवा घेता येतो."
    },

    "about_sih_title": {
        "en": "🏆 Built for SIH 2025",
        "te": "🏆 SIH 2025 కోసం నిర్మించబడింది",
        "hi": "🏆 SIH 2025 के लिए निर्मित",
        "mr": "🏆 SIH 2025 साठी बांधलेले"
    },

    "about_sih_why_crop_doctor_wins": {
        "en": "**Why Crop Doctor wins for SIH judges:**",
        "te": "**SIH న్యాయమూర్తుల కోసం క్రాప్ డాక్టర్ ఎందుకు గెలుస్తుంది:**",
        "hi": "**SIH जजों के लिए क्रॉप डॉक्टर क्यों जीतता है:**",
        "mr": "**SIH न्यायाधीशांसाठी क्रॉप डॉक्टर का जिंकतो:**"
    },

    "about_sih_real_farmer_value": {
        "en": "✅ **Real farmer value** — instant disease diagnosis from any leaf photo",
        "te": "✅ **నిజమైన రైతు విలువ** — ఏదైనా ఆకు ఫోటో నుండి తక్షణ వ్యాధి నిర్ధారణ",
        "hi": "✅ **वास्तविक किसान मूल्य** — किसी भी पत्ते की तस्वीर से तत्काल रोग निदान",
        "mr": "✅ **खरे शेतकरी मूल्य** — कोणत्याही पानाच्या फोटोवरून त्वरित रोग निदान"
    },

    "about_sih_multilingual": {
        "en": "✅ **Multilingual** — English, Telugu, Hindi, Marathi (UI + AI explanations)",
        "te": "✅ **బహుభాష** — ఆంగ్లం, తెలుగు, హిందీ, మరాఠీ (UI + AI వివరణలు)",
        "hi": "✅ **बहुभाषी** — अंग्रेज़ी, तेलुगू, हिंदी, मराठी (UI + AI व्याख्या)",
        "mr": "✅ **बहुभाषिक** — इंग्रजी, तेलुगू, हिंदी, मराठी (UI + AI स्पष्टीकरण)"
    },

    "about_sih_voice_first": {
        "en": "✅ **Voice-first** — Anjaneya IVR works on any phone browser, no app needed",
        "te": "✅ **వాయిస్-ఫస్ట్** — ఆంజనేయ IVR ఏదైనా ఫోన్ బ్రౌజర్‌లో పనిచేస్తుంది, యాప్ అవసరం లేదు",
        "hi": "✅ **वॉइस-फर्स्ट** — आंजनेय IVR किसी भी फोन ब्राउज़र पर काम करता है, ऐप की आवश्यकता नहीं",
        "mr": "✅ **व्हॉइस-फर्स्ट** — आंजनेय IVR कोणत्याही फोन ब्राउझरवर काम करतो, ॲपची गरज नाही"
    },

    "about_sih_offline_first": {
        "en": "✅ **Offline-first** — runs without internet for rural reliability",
        "te": "✅ **ఆఫ్‌లైన్-ఫస్ట్** — గ్రామీణ విశ్వసనీయత కోసం ఇంటర్‌నెట్ లేకుండా నడుస్తుంది",
        "hi": "✅ **ऑफलाइन-फर्स्ट** — ग्रामीण विश्वसनीयता के लिए बिना इंटरनेट के चलता है",
        "mr": "✅ **ऑफलाइन-फर्स्ट** — ग्रामीण विश्वासार्हतेसाठी इंटरनेटशिवाय चालते"
    },

    "about_sih_time_aware": {
        "en": "✅ **Time-aware** — Crop Raksha tracks changes day by day with heatmap",
        "te": "✅ **సమయ-అవగాహన** — క్రాప్ రక్ష హీట్‌మ్యాప్‌తో రోజువారీ మార్పులను ట్రాక్ చేస్తుంది",
        "hi": "✅ **समय-जागरूक** — क्रॉप रक्षा हीटमैप के साथ दिन-प्रतिदिन के बदलावों को ट्रैक करता है",
        "mr": "✅ **वेळ-जाणकार** — क्रॉप रक्षा हीटमॅपसह दिवसेंदिवस बदल ट्रॅक करतो"
    },

    "about_sih_honest_ai": {
        "en": "✅ **Honest AI** — confidence scores + top-5 explanations, not just yes/no",
        "te": "✅ **నిజాయితీ AI** — నమ్మకం స్కోర్లు + టాప్-5 వివరణలు, కేవలం అవును/కాదు కాదు",
        "hi": "✅ **ईमानदार AI** — विश्वास स्कोर + शीर्ष-5 व्याख्या, सिर्फ हाँ/ना नहीं",
        "mr": "✅ **प्रामाणिक AI** — विश्वास गुण + टॉप-5 स्पष्टीकरण, फक्त हो/नाही नाही"
    },

    "about_sih_exportable": {
        "en": "✅ **Exportable** — CSV download for extension officers, agroscientists",
        "te": "✅ **ఎగుమతి చేయదగినది** — విస్తరణ అధికారులు, వ్యవసాయ శాస్త్రవేత్తల కోసం CSV డౌన్‌లోడ్",
        "hi": "✅ **निर्यात योग्य** — विस्तार अधिकारियों, कृषि वैज्ञानिकों के लिए CSV डाउनलोड",
        "mr": "✅ **एक्सपोर्ट करण्यायोग्य** — विस्तार अधिकाऱ्यांसाठी, कृषी शास्त्रज्ञांसाठी CSV डाउनलोड"
    },

    "about_sih_production_grade": {
        "en": "✅ **Production-grade** — TensorFlow 2.17, Streamlit, custom heatmap (no matplotlib)",
        "te": "✅ **ప్రొడక్షన్-గ్రేడ్** — TensorFlow 2.17, Streamlit, కస్టమ్ హీట్‌మ్యాప్ (matplotlib లేదు)",
        "hi": "✅ **प्रोडक्शन-ग्रेड** — TensorFlow 2.17, Streamlit, कस्टम हीटमैप (कोई matplotlib नहीं)",
        "mr": "✅ **प्रोडक्शन-ग्रेड** — TensorFlow 2.17, Streamlit, कस्टम हीटमॅप (matplotlib नाही)"
    },

    "about_tech_stack": {
        "en": "🛠️ Technology Stack",
        "te": "🛠️ సాంకేతిక స్టాక్",
        "hi": "🛠️ तकनीकी स्टैक",
        "mr": "🛠️ तंत्रज्ञान स्टॅक"
    },

    "about_tech_ai_model": {
        "en": "- **AI Model:** TensorFlow 2.17 / Keras — 38 disease classes",
        "te": "- **AI మోడల్:** TensorFlow 2.17 / Keras — 38 వ్యాధి తరగతులు",
        "hi": "- **AI मॉडल:** TensorFlow 2.17 / Keras — 38 रोग वर्ग",
        "mr": "- **AI मॉडेल:** TensorFlow 2.17 / Keras — 38 रोग वर्ग"
    },

    "about_tech_ui": {
        "en": "- **UI:** Streamlit + streamlit-option-menu",
        "te": "- **UI:** Streamlit + streamlit-option-menu",
        "hi": "- **UI:** Streamlit + streamlit-option-menu",
        "mr": "- **UI:** Streamlit + streamlit-option-menu"
    },

    "about_tech_voice_ivr": {
        "en": "- **Voice IVR:** Browser Web Speech API (no external services)",
        "te": "- **వాయిస్ IVR:** బ్రౌజర్ Web Speech API (బాహ్య సేవలు లేవు)",
        "hi": "- **वॉइस IVR:** ब्राउज़र Web Speech API (कोई बाहरी सेवा नहीं)",
        "mr": "- **व्हॉइस IVR:** ब्राउझर Web Speech API (कोणतीही बाह्य सेवा नाही)"
    },

    "about_tech_image": {
        "en": "- **Image processing:** PIL + custom numpy heatmap",
        "te": "- **ఇమేజ్ ప్రాసెసింగ్:** PIL + కస్టమ్ numpy హీట్‌మ్యాప్",
        "hi": "- **इमेज प्रोसेसिंग:** PIL + कस्टम numpy हीटमैप",
        "mr": "- **इमेज प्रोसेसिंग:** PIL + कस्टम numpy हीटमॅप"
    },

    "about_tech_languages": {
        "en": "- **Languages:** Python 3.11",
        "te": "- **భాషలు:** Python 3.11",
        "hi": "- **भाषाएँ:** Python 3.11",
        "mr": "- **भाषा:** Python 3.11"
    },

    "about_tech_storage": {
        "en": "- **Storage:** Local JSON (offline-first)",
        "te": "- **నిల్వ:** స్థానిక JSON (ఆఫ్‌లైన్-ఫస్ట్)",
        "hi": "- **स्टोरेज:** स्थानीय JSON (ऑफलाइन-फर्स्ट)",
        "mr": "- **स्टोरेज:** स्थानिक JSON (ऑफलाइन-फर्स्ट)"
    },

    "daily_crop_check": {
        "en": "📸 {day} — Daily Crop Check",
        "te": "📸 {day} — రోజువారీ పంట తనిఖీ",
        "hi": "📸 {day} — दैनिक फसल जांच",
        "mr": "📸 {day} — दैनंदिन पीक तपासणी"
    },

    # -------------------------------------------------
    # SIH DEMO MODE
    # -------------------------------------------------

    "sih_demo_mode": {
        "en": "🏆 SIH Demo Mode",
        "te": "🏆 SIH డెమో మోడ్",
        "hi": "🏆 SIH डेमो मोड",
        "mr": "🏆 SIH डेमो मोड"
    },

    "sih_click_start_tour": {
        "en": "Click \"Start Guided Tour\" below",
        "te": "కింద \"గైడెడ్ టూర్ ప్రారంభించండి\" క్లిక్ చేయండి",
        "hi": "नीचे \"गाइडेड टूर शुरू करें\" पर क्लिक करें",
        "mr": "खाली \"गाइडेड टूर सुरू करा\" वर क्लिक करा"
    },

    "sih_step_indicator": {
        "en": "STEP {current} of {total}",
        "te": "దశ {current} / {total}",
        "hi": "चरण {current} / {total}",
        "mr": "चरण {current} / {total}"
    },

    "demo_prev": {
        "en": "⬅️ Prev",
        "te": "⬅️ మునుపు",
        "hi": "⬅️ पिछला",
        "mr": "⬅️ मागे"
    },

    "demo_next": {
        "en": "Next ➡️",
        "te": "తరువాత ➡️",
        "hi": "अगला ➡️",
        "mr": "पुढे ➡️"
    },

    "demo_exit": {
        "en": "🚪 Exit Demo",
        "te": "🚪 డెమో నుండి నిష్క్రమించండి",
        "hi": "🚪 डेमो से बाहर निकलें",
        "mr": "🚪 डेमोमधून बाहर पडा"
    },

    # -------------------------------------------------
    # SAMPLE IMAGES GALLERY
    # -------------------------------------------------

    "sample_gallery_heading": {
        "en": "🖼️ Quick Demo — Try Sample Images",
        "te": "🖼️ త్వరిత డెమో — నమూనా చిత్రాలను ప్రయత్నించండి",
        "hi": "🖼️ त्वरित डेमो — नमूना चित्र देखें",
        "mr": "🖼️ जल्दी डेमो — नमूना प्रतिमा पहा"
    },

    "sample_gallery_instructions": {
        "en": "**Click any image below for an instant AI diagnosis demo.**\nNo upload needed — the AI will analyze the sample immediately.",
        "te": "**తక్షణ AI నిర్ధారణ డెమో కోసం కింద ఏదైనా చిత్రంపై క్లిక్ చేయండి.**\nఅప్‌లోడ్ అవసరం లేదు — AI నమూనాను తక్షణం విశ్లేషిస్తుంది.",
        "hi": "**तुरंत AI निदान डेमो के लिए नीचे किसी भी छवि पर क्लिक करें।**\nअपलोड की जरूरत नहीं — AI तुरंत नमूने का विश्लेषण करेगा।",
        "mr": "**त्वरित AI निदान डेमोसाठी खाली कोणत्याही प्रतिमेवर क्लिक करा.**\nअपलोडची गरज नाही — AI त्वरित नमुन्याचे विश्लेषण करेल."
    },

    "crop_samples_count": {
        "en": "🌱 {crop} Samples ({count})",
        "te": "🌱 {crop} నమూనాలు ({count})",
        "hi": "🌱 {crop} नमूने ({count})",
        "mr": "🌱 {crop} नमूने ({count})"
    },

    "sample_image_caption_fallback": {
        "en": "Sample",
        "te": "నమూనా",
        "hi": "नमूना",
        "mr": "नमूना"
    },

    "sample_label_format": {
        "en": "{emoji} {crop} — {disease}",
        "te": "{emoji} {crop} — {disease}",
        "hi": "{emoji} {crop} — {disease}",
        "mr": "{emoji} {crop} — {disease}"
    },

    "diagnose_observation_healthy": {
        "en": "No significant visual change detected. AI result: Healthy ({confidence:.2f}%).",
        "te": "గణనీయమైన దృశ్య మార్పు గుర్తించబడలేదు. AI ఫలితం: ఆరోగ్యకరమైనది ({confidence:.2f}%).",
        "hi": "कोई महत्वपूर्ण दृश्य परिवर्तन नहीं पाया गया। AI परिणाम: स्वस्थ ({confidence:.2f}%)।",
        "mr": "कोणताही लक्षणीय दृश्य बदल आढळला नाही. AI निष्कर्ष: निरोगी ({confidence:.2f}%)."
    },

    "diagnose_observation_minor_healthy": {
        "en": "A minor visual change was detected. AI currently predicts Healthy ({confidence:.2f}%). Continue monitoring.",
        "te": "స్వల్ప దృశ్య మార్పు గుర్తించబడింది. AI ప్రస్తుతం ఆరోగ్యకరమైనదని అంచనా వేస్తోంది ({confidence:.2f}%). పర్యవేక్షణ కొనసాగించండి.",
        "hi": "एक मामूली दृश्य परिवर्तन पाया गया। AI वर्तमान में स्वस्थ ({confidence:.2f}%) की भविष्यवाणी करता है। निगरानी जारी रखें।",
        "mr": "किरकोळ दृश्य बदल आढळला. AI सध्या निरोगी ({confidence:.2f}%) अंदाज करतो. निरीक्षण सुरू ठेवा."
    },

    "diagnose_observation_significant_healthy": {
        "en": "A significant visual change was detected, but the AI currently predicts Healthy ({confidence:.2f}%). Further monitoring is recommended.",
        "te": "గణనీయమైన దృశ్య మార్పు గుర్తించబడింది, కానీ AI ప్రస్తుతం ఆరోగ్యకరమైనదని అంచనా వేస్తోంది ({confidence:.2f}%). మరింత పర్యవేక్షణ సిఫార్సు చేయబడింది.",
        "hi": "एक महत्वपूर्ण दृश्य परिवर्तन पाया गया, लेकिन AI वर्तमान में स्वस्थ ({confidence:.2f}%) की भविष्यवाणी करता है। आगे निगरानी की सिफारिश की जाती है।",
        "mr": "लक्षणीय दृश्य बदल आढळला, परंतु AI सध्या निरोगी ({confidence:.2f}%) अंदाज करतो. पुढील निरीक्षण शिफारसीय आहे."
    },

    "diagnose_observation_disease_detected": {
        "en": "AI detected {disease} with {confidence:.2f}% confidence.",
        "te": "AI {disease}ను {confidence:.2f}% నమ్మకంతో గుర్తించింది.",
        "hi": "AI ने {disease} को {confidence:.2f}% विश्वास के साथ पहचाना।",
        "mr": "AI ने {disease} {confidence:.2f}% विश्वासाने ओळखले."
    },

    "diagnose_observation_low_confidence": {
        "en": "AI result: {disease} ({confidence:.2f}%). Further observation is recommended.",
        "te": "AI ఫలితం: {disease} ({confidence:.2f}%). మరింత పరిశీలన సిఫార్సు చేయబడింది.",
        "hi": "AI परिणाम: {disease} ({confidence:.2f}%)। आगे अवलोकन की सिफारिश की जाती है।",
        "mr": "AI निष्कर्ष: {disease} ({confidence:.2f}%). पुढील निरीक्षण शिफारसीय आहे."
    },

    "diagnose_observation_baseline": {
        "en": "Baseline observation recorded. AI result: {disease} ({confidence:.2f}%).",
        "te": "ప్రాథమిక పరిశీలన నమోదు చేయబడింది. AI ఫలితం: {disease} ({confidence:.2f}%).",
        "hi": "प्रारंभिक अवलोकन दर्ज किया गया। AI परिणाम: {disease} ({confidence:.2f}%)।",
        "mr": "प्रारंभिक निरीक्षण नोंदवले. AI निष्कर्ष: {disease} ({confidence:.2f}%)."
    },

    "diagnose_unknown": {
        "en": "Unknown",
        "te": "తెలియదు",
        "hi": "अज्ञात",
        "mr": "अज्ञात"
    },

    "sample_diagnose": {
        "en": "🩺 Diagnose",
        "te": "🩺 వ్యాధి నిర్ధారణ",
        "hi": "🩺 रोग पहचान",
        "mr": "🩺 रोग निदान"
    },

    "sample_load_error": {
        "en": "Could not load {id}",
        "te": "{id} లోడ్ కాలేకపోయింది",
        "hi": "{id} लोड नहीं हो सका",
        "mr": "{id} लोड होऊ शकला नाही"
    },

    # -------------------------------------------------
    # AI EXPLANATION
    # -------------------------------------------------

    "ai_high_confidence": {
        "en": "🟢 High Confidence",
        "te": "🟢 అధిక నమ్మకం",
        "hi": "🟢 उच्च विश्वास",
        "mr": "🟢 उच्च विश्वास"
    },

    "ai_medium_confidence": {
        "en": "🟡 Medium Confidence",
        "te": "🟡 మధ్యమ నమ్మకం",
        "hi": "🟡 मध्यम विश्वास",
        "mr": "🟡 मध्यम विश्वास"
    },

    "ai_lower_confidence": {
        "en": "🟠 Lower Confidence",
        "te": "🟠 తక్కువ నమ్మకం",
        "hi": "🟠 कम विश्वास",
        "mr": "🟠 कम विश्वास"
    },

    "ai_high_confidence_desc": {
        "en": "The AI model is highly confident ({confidence}%) in this prediction. This is a strong signal that the diagnosis is likely correct.",
        "te": "AI మోడల్ ఈ అంచనాలో అత్యధిక నమ్మకం ({confidence}%) కలిగి ఉంది. ఇది నిర్ధారణ సరిగ్గా ఉండవచ్చని బలమైన సంకేతం.",
        "hi": "AI मॉडल इस पूर्वानुमान में अत्यधिक विश्वास ({confidence}%) रखता है। यह एक मजबूत संकेत है कि निदान सही होने की संभावना है।",
        "mr": "AI मॉडेल या अंदाजात अत्यंत विश्वास ({confidence}%) ठेवतो. हे एक मजबूत सूचना आहे की निदान बरोबर असण्याची शक्यता आहे."
    },

    "ai_medium_confidence_desc": {
        "en": "The AI model has moderate confidence ({confidence}%). This suggests the image shows features matching this disease, but a second opinion or clearer photo would be useful.",
        "te": "AI మోడల్‌కు మధ్యమ నమ్మకం ({confidence}%) ఉంది. ఇమేజ్‌లో ఈ వ్యాధికి సరిపోయే లక్షణాలు కనిపిస్తున్నాయని ఇది సూచిస్తుంది, కానీ మరొక అభిప్రాయం లేదా స్పష్టమైన ఫోటో ఉపయోగకరమైనది.",
        "hi": "AI मॉडल को मध्यम विश्वास ({confidence}%) है। इससे पता चलता है कि छवि में इस रोग से मेल खाती विशेषताएं हैं, लेकिन दूसरी राय या स्पष्ट फोटो उपयोगी होगी।",
        "mr": "AI मॉडेलला मध्यम विश्वास ({confidence}%) आहे. याचा अर्थ असा की प्रतिमेत या रोगाशी जुळणाऱ्या वैशिष्ट्ये दिसत आहेत, परंतु दुसरी किंमत किंवा स्पष्ट फोटो उपयोगी असेल."
    },

    "ai_lower_confidence_desc": {
        "en": "The AI model has lower confidence ({confidence}%) in this prediction. Consider taking a clearer photo with better lighting and trying again.",
        "te": "AI మోడల్‌కు ఈ అంచనాలో తక్కువ నమ్మకం ({confidence}%) ఉంది. మెరుగైన కాంతితో స్పష్టమైన ఫోటో తీసుకుని మళ్ళీ ప్రయత్నించడం �考虑一下.",
        "hi": "AI मॉडल इस पूर्वानुमान में कम विश्वास ({confidence}%) रखता है। बेहतर रोशनी में स्पष्ट फोटो लें और फिर से प्रयास करें।",
        "mr": "AI मॉडेल या अंदाजात कमी विश्वास ({confidence}%) आहे. चांगल्या प्रकाशासह स्पष्ट फोटो घेणे आणि पुन्हा प्रयत्न करणे विचारात घ्या."
    },

    "ai_looked_for": {
        "en": "🤖 What the AI Looked For",
        "te": "🤖 AI ఏమి చూసింది",
        "hi": "🤖 AI ने क्या देखा",
        "mr": "🤖 AI ने काय पाहिले"
    },

    "ai_looked_for_desc": {
        "en": "The model analyzed the **color patterns**, **texture features**, and **spot characteristics** in your image against **38 disease classes** across **10 crops**.",
        "te": "మోడల్ మీ ఇమేజ్‌లోని **రంగు నమూనాలు**, **వర్థమాన లక్షణాలు** మరియు **మచ్చల లక్షణాలను** **10 పంటలలోని **38 వ్యాధి తరగతుల**పై విశ్లేషించింది.",
        "hi": "मॉडल ने आपकी छवि में **रंग पैटर्न**, **बनावट विशेषताओं** और **धब्बों की विशेषताओं** का विश्लेषण **10 फसलों** में **38 रोग वर्गों** के आधार पर किया।",
        "mr": "मॉडेलने तुमच्या प्रतिमेतील **रंग नमुने**, **बनावट वैशिष्ट्ये** आणि **ठिपके वैशिष्ट्यांचे** **10 पिकांमधील **38 रोग वर्गां**विरुद्ध विश्लेषण केले."
    },

    "ai_healthy_label": {
        "en": "Healthy 🌱",
        "te": "ఆరోగ్యంగా 🌱",
        "hi": "स्वस्थ 🌱",
        "mr": "निरोगी 🌱"
    },

    # -------------------------------------------------
    # RAKSHA INSIGHTS
    # -------------------------------------------------

    "raksha_just_started": {
        "en": "🌱 **Crop Raksha journey has just begun.** This is the first observation for {farmer}'s {crop}. Continue daily monitoring to build a health timeline.",
        "te": "🌱 **క్రాప్ రక్ష ప్రయాణం ఇప్పుడే ప్రారంభమైంది.** {farmer} {crop} యొక్క మొదటి పరిశీలన ఇది. ఆరోగ్య టైమ్‌లైన్‌ను నిర్మించడానికి రోజువారీ పర్యవేక్షణ కొనసాగించండి.",
        "hi": "🌱 **क्रॉप रक्षा यात्रा अभी शुरू हुई है।** {farmer} की {crop} के लिए यह पहला अवलोकन है। स्वास्थ्य टाइमलाइन बनाने के लिए दैनिक निगरानी जारी रखें।",
        "mr": "🌱 **क्रॉप रक्षा प्रवास अगदी सुरू झाला आहे.** {farmer} च्या {crop} साठी हे पहिले निरीक्षण आहे. आरोग्य टाइमलाइन बनवण्यासाठी दैनिक निरीक्षण सुरू ठेवा."
    },

    "raksha_alert": {
        "en": "🚨 **Attention needed!** Recent observations show a significant visual change or detected issue in the {crop} crop. Review the latest AI result and consider using Crop Diagnosis for a deeper assessment.",
        "te": "🚨 **శ్రద్ధ అవసరం!** ఇటీవలి పరిశీలనలు {crop} పంటలో గణనీయమైన దృశ్య మార్పు లేదా గుర్తించిన సమస్యను చూపిస్తున్నాయి. తాజా AI ఫలితంను సమీక్షించండి మరియు গভীর মূল্যায়নের জন্য Crop Diagnosis ఉపయోగించడం గురించి ఆలోచించండి.",
        "hi": "🚨 **ध्यान दें!** हाल के अवलोकनों में {crop} फसल में महत्वपूर्ण दृश्य परिवर्तन या पाई गई समस्या दिखाई दे रही है। नवीनतम AI परिणाम की समीक्षा करें और गहन मूल्यांकन के लिए Crop Diagnosis का उपयोग करने पर विचार करें।",
        "mr": "🚨 **लक्ष द्या!** अलीकडील निरीक्षणांमध्ये {crop} पिकामध्ये लक्षणीय दृश्य बदल किंवा आढळलेली समस्या दिसत आहे. नवीनतम AI परिणामाचे पुनरिक्षण करा आणि खोल मूल्यांकनासाठी Crop Diagnosis वापरण्याचा विचार करा."
    },

    "raksha_watch": {
        "en": "👀 **Minor change detected.** A small visual difference was noticed in the latest observation of {farmer}'s {crop}. This doesn't mean disease — continue monitoring daily. {total} observations recorded so far.",
        "te": "👀 **స్వల్ప మార్పు గుర్తించబడింది.** {farmer} {crop} యొక్క తాజా పరిశీలనలో చిన్న విచక్షణ తేడా గుర్తించబడింది. ఇది వ్యాధిని సూచించదు — రోజువారీ పర్యవేక్షణ కొనసాగించండి. ఇప్పటివరకు {total} పరిశీలనలు నమోదు చేయబడ్డాయి.",
        "hi": "👀 **मामूली बदल पाया गया।** {farmer} की {crop} के नवीनतम अवलोकन में थोड़ा दृश्य अंतर देखा गया। इसका मतलब बीमारी नहीं है — दैनिक निगरानी जारी रखें। अब तक {total} अवलोकन दर्ज किए गए।",
        "mr": "👀 **किरकोळ बदल ओळखला.** {farmer} च्या {crop} च्या नवीनतम निरीक्षणात छोटा दृश्य फरक लक्षात आला. याचा अर्थ रोग नाही — दैनिक निरीक्षण सुरू ठेवा. आतापर्यंत {total} निरीक्षणे नोंदली गेली आहेत."
    },

    "raksha_stable": {
        "en": "✅ **Stable progress.** {farmer}'s {crop} has shown no significant visual changes across {total} daily observations. AI results: {healthy}/{total} days showed healthy status. Keep up the daily monitoring routine!",
        "te": "✅ **స్థిర పురోగతి.** {farmer} {crop} {total} రోజువారీ పరిశీలనలలో గణనీయమైన విచక్షణ మార్పులను చూపలేదు. AI ఫలితాలు: {total} రోజులలో {healthy} రోజులు ఆరోగ్యకరమైన స్థితిని చూపాయి. రోజువారీ పర్యవేక్షణ పద్ధతిని కొనసాగించండి!",
        "hi": "✅ **स्थिर प्रगति।** {farmer} की {crop} में {total} दैनिक अवलोकनों में कोई महत्वपूर्ण दृश्य परिवर्तन नहीं दिखा। AI परिणाम: {total} दिनों में {healthy} दिन स्वस्थ स्थिति दिखाई दी। दैनिक निगरानी दिनचर्या जारी रखें!",
        "mr": "✅ **स्थिर प्रगती.** {farmer} च्या {crop} ने {total} दैनिक निरीक्षणांमध्ये कोणतेही लक्षणीय दृश्य बदल दाखवले नाहीत. AI परिणाम: {total} दिवसांपैकी {healthy} दिवस निरोगी स्थिती दर्शवली. दैनिक निरीक्षण दिनचर्या कायम ठेवा!"
    },

    "raksha_today": {
        "en": "Today",
        "te": "ఈ రోజు",
        "hi": "आज",
        "mr": "आज"
    },

    "raksha_yesterday": {
        "en": "Yesterday",
        "te": "నిన్న",
        "hi": "कल",
        "mr": "काल"
    },

    "raksha_days_ago": {
        "en": "{n} days ago",
        "te": "{n} రోజుల క్రితం",
        "hi": "{n} दिन पहले",
        "mr": "{n} दिवसांपूर्वी"
    },

    "raksha_last_observation": {
        "en": "Last observation: **{time}** ({date})",
        "te": "చివరి పరిశీలన: **{time}** ({date})",
        "hi": "अंतिम अवलोकन: **{time}** ({date})",
        "mr": "शेवटचे निरीक्षण: **{time}** ({date})"
    },

    "raksha_last_observation_date": {
        "en": "Last observation: **{date}**",
        "te": "చివరి పరిశీలన: **{date}**",
        "hi": "अंतिम अवलोकन: **{date}**",
        "mr": "शेवटचे निरीक्षण: **{date}**"
    },

    "raksha_no_date": {
        "en": "No date recorded",
        "te": "తేదీ నమోదు చేయలేదు",
        "hi": "तारीख दर्ज नहीं",
        "mr": "तारीख नोंद नाही"
    },

    "raksha_no_observations": {
        "en": "No observations yet",
        "te": "ఇంకా పరిశీలనలు లేవు",
        "hi": "अभी तक कोई अवलोकन नहीं",
        "mr": "अद्याप कोणतीही निरीक्षणे नाहीतत"
    },

    "raksha_no_date": {
        "en": "No date recorded",
        "te": "తేదీ నమోదు చేయలేదు",
        "hi": "तारीख दर्ज नहीं",
        "mr": "तारीख नोंद नाही"
    },

    "raksha_days_ago": {
        "en": "{n} days ago",
        "te": "{n} రోజుల క్రితం",
        "hi": "{n} दिन पहले",
        "mr": "{n} दिवसांपूर्वी"
    },

    "raksha_last_observation_time": {
        "en": "Last observation: **{time}** ({date})",
        "te": "చివరి పరిశీలన: **{time}** ({date})",
        "hi": "अंतिम अवलोकन: **{time}** ({date})",
        "mr": "शेवटचे निरीक्षण: **{time}** ({date})"
    },

    "raksha_last_observation_only": {
        "en": "Last observation: **{date}**",
        "te": "చివరి పరిశీలన: **{date}**",
        "hi": "अंतिम अवलोकन: **{date}**",
        "mr": "शेवटचे निरीक्षण: **{date}**"
    },

    "raksha_no_observation_available": {
        "en": "No observation available.",
        "te": "పరిశీలన అందుబాటులో లేదు.",
        "hi": "कोई अवलोकन उपलब्ध नहीं।",
        "mr": "कोणतेही निरीक्षण उपलब्ध नाही."
    },

    "raksha_insight_summary": {
        "en": "AI Insight Summary",
        "te": "AI అంతర్దృష్టి సారాంశం",
        "hi": "AI अंतर्दृष्टि सारांश",
        "mr": "AI आंतर्दृष्टी सारांश"
    },

    "raksha_observations_count": {
        "en": "{n} observation(s)",
        "te": "{n} పరిశీలన(లు)",
        "hi": "{n} अवलोकन",
        "mr": "{n} निरीक्षण(ने)"
    },

    "raksha_day": {
        "en": "Day",
        "te": "రోజు",
        "hi": "दिन",
        "mr": "दिवस"
    },

    "raksha_visual_status": {
        "en": "Visual status",
        "te": "దృశ్య స్థితి",
        "hi": "दृश्य स्थिति",
        "mr": "दृश्य स्थिती"
    },

    "raksha_latest_result": {
        "en": "Latest AI Result",
        "te": "తాజా AI ఫలితం",
        "hi": "नवीनतम AI परिणाम",
        "mr": "नवीनतम AI परिणाम"
    },

    "raksha_result_label": {
        "en": "AI result",
        "te": "AI ఫలితం",
        "hi": "AI परिणाम",
        "mr": "AI परिणाम"
    },

    "raksha_confidence_label": {
        "en": "Confidence",
        "te": "నమ్మకం",
        "hi": "विश्वास",
        "mr": "विश्वास"
    },

    "raksha_total_observations": {
        "en": "Total observations",
        "te": "మొత్తం పరిశీలనలు",
        "hi": "कुल अवलोकन",
        "mr": "एकूण निरीक्षणे"
    },

    "raksha_latest_observation": {
        "en": "Latest observation",
        "te": "తాజా పరిశీలన",
        "hi": "नवीनतम अवलोकन",
        "mr": "नवीनतम निरीक्षण"
    },

    "raksha_first_observation": {
        "en": "First observation",
        "te": "మొదటి పరిశీలన",
        "hi": "पहला अवलोकन",
        "mr": "पहिले निरीक्षण"
    },

    "raksha_talk_placeholder": {
        "en": "💬 Talk to Crop Raksha...",
        "te": "💬 క్రాప్ రక్షతో మాట్లాడండి...",
        "hi": "💬 क्रॉप रक्षा से बात करें...",
        "mr": "💬 क्रॉप रक्षाशी बोला..."
    },

    "raksha_compare_select_different": {
        "en": "⚠️ Please select two different observations to compare.",
        "te": "⚠️ పోలించడానికి భిన్నమైన రెండు పరిశీలనలను ఎంచుకోండి.",
        "hi": "⚠️ कृपया तुलना के लिए दो अलग-अलग अवलोकन चुनें।",
        "mr": "⚠️ कृपया तुलनेसाठी दोन वेगळी निरीक्षणे निवडा."
    },

    "raksha_compare_no_images": {
        "en": "No observation images found.",
        "te": "పరిశీలన చిత్రాలు కనుగొనబడలేదు.",
        "hi": "कोई अवलोकन छवियाँ नहीं मिलीं।",
        "mr": "कोणतीही निरीक्षण प्रतिमा आढळल्या नाहीत."
    },

    "raksha_compare_no_observations": {
        "en": "📸 No observations yet. Upload at least one crop photograph to enable comparison.",
        "te": "📸 ఇంకా పరిశీలనలు లేవు. పోలికను ప్రారంభించడానికి కనీసం ఒక పంట ఫోటోను అప్‌లోడ్ చేయండి.",
        "hi": "📸 अभी तक कोई अवलोकन नहीं। तुलना सक्षम करने के लिए कम से कम एक फसल तस्वीर अपलोड करें।",
        "mr": "📸 अद्याप निरीक्षणे नाहीत. तुलना सक्षम करण्यासाठी कमीतकमी एक पीक फोटो अपलोड करा."
    },

    "raksha_compare_explanation": {
        "en": "Compare any two observations of your crop to see how it has changed over time. Pick two days and view them side-by-side with a visual change heatmap.",
        "te": "కాలక్రమేణా మీ పంట ఎలా మారిందో చూడటానికి ఏవైనా రెండు పరిశీలనలను పోల్చండి. రెండు రోజులను ఎంచుకుని వాటిని విజువల్ చేంజ్ హీట్‌మ్యాప్‌తో పక్కపక్కన చూడండి.",
        "hi": "अपनी फसल के किसी भी दो अवलोकनों की तुलना करें और देखें कि समय के साथ यह कैसे बदल गई है। दो दिन चुनें और उन्हें विज़ुअल चेंज हीटमैप के साथ साथ-साथ देखें।",
        "mr": "कालांतराने आपले पीक कसे बदलले आहे ते पाहण्यासाठी आपल्या पिकाची कोणतीही दोन निरीक्षणे तुलना करा. दोन दिवस निवडा आणि त्यांना विज्युअल चेंज हीटमॅपसह जवळजवळ पहा."
    },

    "raksha_observation_caption": {
        "en": "Day {day} — {disease}",
        "te": "రోజు {day} — {disease}",
        "hi": "दिन {day} — {disease}",
        "mr": "दिवस {day} — {disease}"
    },

    "raksha_compare_heatmap_caption": {
        "en": "Hotter/brighter areas show where the After image differs most from the Before image",
        "te": "వేడి/ప్రకాశవంతమైన ప్రాంతాలు తర్వాత చిత్రం ముందు చిత్రం నుండి ఎక్కువగా భిన్నంగా ఉన్న ప్రాంతాలను చూపుతాయి",
        "hi": "अधिक चमकीले/तेज क्षेत्र दिखाते हैं कि बाद की छवि पहली छवि से कहाँ सबसे अधिक भिन्न है",
        "mr": "उष्ण/प्रकाशमान भाग दर्शवितात की नंतरची प्रतिमा आधी प्रतिमापेक्षा कुठे सर्वात जास्त वेगळी आहे"
    },

    "raksha_compare_day_option": {
        "en": "Day {day} — {date} ({disease})",
        "te": "రోజు {day} — {date} ({disease})",
        "hi": "दिन {day} — {date} ({disease})",
        "mr": "दिवस {day} — {date} ({disease})"
    },

    "raksha_compare_load_error": {
        "en": "Could not load images: {error}",
        "te": "చిత్రాలను లోడ్ చేయలేకపోయింది: {error}",
        "hi": "छवियाँ लोड नहीं हो सकीं: {error}",
        "mr": "प्रतिमा लोड होऊ शकल्या नाहीत: {error}"
    },

    "raksha_compare_pick_days": {
        "en": "📸 Before / After — Pick Any Two Days",
        "te": "📸 ముందు / తర్వాత — ఏవైనా రెండు రోజులను ఎంచుకోండి",
        "hi": "📸 पहले / बाद — कोई भी दो दिन चुनें",
        "mr": "📸 आधी / नंतर — कोणतेही दोन दिवस निवडा"
    },

    "raksha_compare_instructions": {
        "en": "Select any two observations to compare them side-by-side.",
        "te": "ఏవైనా రెండు పరిశీలనలను పక్కపక్కన చూడడానికి ఎంచుకోండి.",
        "hi": "कोई भी दो अवलोकन चुनें और उन्हें आस-पास देखें।",
        "mr": "कोणतीही दोन निरीक्षणे निवडा आणि ती जवळजवळ पहा."
    },

    # -------------------------------------------------
    # VOICE FEEDBACK
    # -------------------------------------------------

    "voice_healthy_msg": {
        "en": "Good news! Your {crop} crop is healthy. The AI analyzed the image with {confidence:.0f} percent confidence. Continue your daily monitoring routine.",
        "te": "శుభవార్త! మీ {crop} పంట ఆరోగ్యంగా ఉంది. AI {confidence:.0f} శాతం నమ్మకంతో ఇమేజ్‌ను విశ్లేషించింది. మీ రోజువారీ పర్యవేక్షణ పద్ధతిని కొనసాగించండి.",
        "hi": "अच्छी खबर! आपकी {crop} फसल स्वस्थ है। AI ने {confidence:.0f} प्रतिशत विश्वास के साथ छवि का विश्लेषण किया। अपनी दैनिक निगरानी दिनचर्या जारी रखें।",
        "mr": "छान बातमी! तुमचे {crop} पीक निरोगी आहे. AI ने {confidence:.0f} टक्के विश्वासाने प्रतिमेचे विश्लेषण केले. तुमची दैनिक निरीक्षण दिनचर्या कायम ठेवा."
    },

    "voice_disease_msg": {
        "en": "Attention! The AI detected {disease} in your {crop} crop. Confidence is {confidence:.0f} percent. Please review the management recommendations. Continue monitoring daily with Crop Raksha.",
        "te": "శ్రద్ధ! AI మీ {crop} పంటలో {disease} గుర్తించింది. నమ్మకం {confidence:.0f} శాతం.దయచేసి నిర్వహణ సిఫార్సులను సమీక్షించండి. క్రాప్ రక్షతో రోజువారీ పర్యవేక్షణ కొనసాగించండి.",
        "hi": "ध्यान दें! AI ने आपकी {crop} फसल में {disease} का पता लगाया। विश्वास {confidence:.0f} प्रतिशत है। कृपया प्रबंधन सिफारिशों की समीक्षा करें। क्रॉप रक्षा के साथ दैनिक निगरानी जारी रखें।",
        "mr": "लक्ष द्या! AI ने तुमच्या {crop} पिकामध्ये {disease} आढळला. विश्वास {confidence:.0f} टक्के आहे. कृपया व्यवस्थापन शिफारसींचे पुनरिक्षण करा. क्रॉप रक्षा सह दैनिक निरीक्षण कायम ठेवा."
    },

    "voice_listen_btn": {
        "en": "🔊 Listen to Diagnosis",
        "te": "🔊 నిర్ధారణ వినండి",
        "hi": "🔊 निदान सुनें",
        "mr": "🔊 निदान ऐका"
    },

    # -------------------------------------------------
    # CROP NAMES
    # -------------------------------------------------

    "crop_banana": {
        "en": "Banana",
        "te": "అరటి",
        "hi": "केला",
        "mr": "केळी"
    },

    "crop_corn": {
        "en": "Corn",
        "te": "మొక్కజొన్న",
        "hi": "मक्का",
        "mr": "मका"
    },

    "crop_cotton": {
        "en": "Cotton",
        "te": "పత్తి",
        "hi": "कपास",
        "mr": "कापूस"
    },

    "crop_grape": {
        "en": "Grape",
        "te": "ద్రాక్ష",
        "hi": "अंगूर",
        "mr": "द्राक्षे"
    },

    "crop_mango": {
        "en": "Mango",
        "te": "మామిడి",
        "hi": "आम",
        "mr": "आंबा"
    },

    "crop_paddy": {
        "en": "Paddy",
        "te": "వరి",
        "hi": "धान",
        "mr": "भात"
    },

    "crop_potato": {
        "en": "Potato",
        "te": "బంగాళాదుంప",
        "hi": "आलू",
        "mr": "बटाटा"
    },

    "crop_soybean": {
        "en": "Soybean",
        "te": "సోయాబీన్",
        "hi": "सोयाबीन",
        "mr": "सोयाबीन"
    },

    "crop_tomato": {
        "en": "Tomato",
        "te": "టమాటా",
        "hi": "टमाटर",
        "mr": "टोमॅटो"
    },

    "crop_wheat": {
        "en": "Wheat",
        "te": "గోధుమ",
        "hi": "गेहूं",
        "mr": "गहू"
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
    # DISEASE LIBRARY — DISEASE NAMES
    # (Internal IDs in disease_info.py remain unchanged.
    #  These keys translate the visible disease name only.)
    # -------------------------------------------------

    "disease_cordana_leaf_spot": {
        "en": "Cordana Leaf Spot",
        "te": "కార్డానా ఆకు మచ్చ",
        "hi": "कॉर्डाना पत्ती धब्बा",
        "mr": "कॉर्डाना पानावरील डाग"
    },

    "disease_pestalotiopsis_leaf_spot": {
        "en": "Pestalotiopsis Leaf Spot",
        "te": "పెస్టలోటియోప్సిస్ ఆకు మచ్చ",
        "hi": "पेस्टालोटियोप्सिस पत्ती धब्बा",
        "mr": "पेस्टालोटियोप्सिस पानावरील डाग"
    },

    "disease_sigatoka_leaf_spot": {
        "en": "Sigatoka Leaf Spot",
        "te": "సిగాటోకా ఆకు మచ్చ",
        "hi": "सिगाटोका पत्ती धब्बा",
        "mr": "सिगाटोका पानावरील डाग"
    },

    "disease_common_rust": {
        "en": "Common Rust",
        "te": "సాధారణ తుప్పు",
        "hi": "सामान्य रतुआ",
        "mr": "सामान्य तांबेरा"
    },

    "disease_gray_leaf_spot": {
        "en": "Gray Leaf Spot",
        "te": "బూడిచ ఆకు మచ్చ",
        "hi": "ग्रे पत्ती धब्बा",
        "mr": "राखाडी पानावरील डाग"
    },

    "disease_northern_corn_leaf_blight": {
        "en": "Northern Corn Leaf Blight",
        "te": "ఉత్తర మొక్కజొన్న ఆకు కుళ్ళు",
        "hi": "उत्तरी मक्का पत्ती झुलसा",
        "mr": "उत्तर मका पानावरील करपा"
    },

    "disease_bacterial_blight": {
        "en": "Bacterial Blight",
        "te": "బ్యాక్టీరియల్ బ్లైట్",
        "hi": "जीवाणु झुलसा",
        "mr": "जीवाणूजन्य करपा"
    },

    "disease_cotton_leaf_curl": {
        "en": "Cotton Leaf Curl Disease",
        "te": "పత్తి ఆకు ముడత వ్యాధి",
        "hi": "कपास पत्ती मोड़ रोग",
        "mr": "कापूस पाने वळण रोग"
    },

    "disease_fusarium_wilt": {
        "en": "Fusarium Wilt",
        "te": "ఫ్యూజేరియం విల్ట్",
        "hi": "फ्यूजेरियम उकठा",
        "mr": "फ्यूझेरियम मर"
    },

    "disease_black_measles": {
        "en": "Black Measles",
        "te": "నల్ల మీజిల్స్",
        "hi": "काली खसरा",
        "mr": "काळा गोवर"
    },

    "disease_black_rot": {
        "en": "Black Rot",
        "te": "నల్ల కుళ్ళు",
        "hi": "काला सड़न",
        "mr": "काळी कुज"
    },

    "disease_isariopsis_leaf_spot": {
        "en": "Isariopsis Leaf Spot",
        "te": "ఇసారియోప్సిస్ ఆకు మచ్చ",
        "hi": "आइसारियोप्सिस पत्ती धब्बा",
        "mr": "आयसॅरिओप्सिस पानावरील डाग"
    },

    "disease_anthracnose": {
        "en": "Anthracnose",
        "te": "ఆంత్రాక్నోస్",
        "hi": "एन्थ्रेक्नोज",
        "mr": "अँथ्रॅकनोज"
    },

    "disease_bacterial_canker": {
        "en": "Bacterial Canker",
        "te": "బ్యాక్టీరియల్ క్యాంకర్",
        "hi": "जीवाणु कैंकर",
        "mr": "जीवाणूजन्य कॅन्कर"
    },

    "disease_powdery_mildew": {
        "en": "Powdery Mildew",
        "te": "బూడిచ తెగులు",
        "hi": "चूर्णिल आसिता",
        "mr": "भुरी रोग"
    },

    "disease_bacterial_leaf_blight": {
        "en": "Bacterial Leaf Blight",
        "te": "బ్యాక్టీరియల్ ఆకు ఎండు తెగులు",
        "hi": "जीवाणु पत्ती झुलसा",
        "mr": "जीवाणूजन्य पानावरील करपा"
    },

    "disease_brown_spot": {
        "en": "Brown Spot",
        "te": "బ్రౌన్ స్పాట్",
        "hi": "भूरा धब्बा",
        "mr": "तपकिरी डाग"
    },

    "disease_rice_leaf_blast": {
        "en": "Rice Leaf Blast",
        "te": "వరి ఆకు బ్లాస్ట్",
        "hi": "धान का पत्ती ब्लास्ट",
        "mr": "भात पानावरील ब्लास्ट"
    },

    "disease_early_blight": {
        "en": "Early Blight",
        "te": "ముందస్తు ఎండు తెగులు",
        "hi": "अगेती झुलसा",
        "mr": "लवकर करपा"
    },

    "disease_late_blight": {
        "en": "Late Blight",
        "te": "ఆలస్య ఎండు తెగులు",
        "hi": "पछेती झुलसा",
        "mr": "उशिरा करपा"
    },

    "disease_caterpillar_damage": {
        "en": "Caterpillar Damage",
        "te": "గొంగళి పురుగు నష్టం",
        "hi": "सुंडी द्वारा नुकसान",
        "mr": "अळीचे नुकसान"
    },

    "disease_diabrotica_speciosa": {
        "en": "Diabrotica speciosa Damage",
        "te": "డయాబ్రోటికా స్పెసియోసా నష్టం",
        "hi": "डायब्रोटिका स्पेसिओसा द्वारा नुकसान",
        "mr": "डायाब्रोटिका स्पेशिओसा नुकसान"
    },

    "disease_bacterial_spot": {
        "en": "Bacterial Spot",
        "te": "బ్యాక్టీరియల్ మచ్చ",
        "hi": "जीवाणु धब्बा",
        "mr": "जीवाणूजन्य डाग"
    },

    "disease_septoria_leaf_spot": {
        "en": "Septoria Leaf Spot",
        "te": "సెప్టోరియా ఆకు మచ్చ",
        "hi": "सेप्टोरिया पत्ती धब्बा",
        "mr": "सेप्टोरिया पानावरील डाग"
    },

    "disease_yellow_rust": {
        "en": "Yellow Rust",
        "te": "పసుపు తుప్పు",
        "hi": "पीला रतुआ",
        "mr": "पिवळा तांबेरा"
    },

    "disease_healthy": {
        "en": "Healthy",
        "te": "ఆరోగ్యంగా ఉంది",
        "hi": "स्वस्थ",
        "mr": "निरोगी"
    },

    # -------------------------------------------------
    # DISEASE LIBRARY — DISEASE DESCRIPTIONS
    # (Short description shown in the card body)
    # -------------------------------------------------

    "disease_desc_banana_cordana": {
        "en": "A fungal leaf disease that causes spots and lesions on banana leaves.",
        "te": "అరటి ఆకులపై మచ్చలు మరియు గాయాలను కలిగించే శిలీంధ్ర ఆకు వ్యాధి.",
        "hi": "केले के पत्तों पर धब्बे और घाव पैदा करने वाला एक कवक पत्ती रोग।",
        "mr": "केळीच्या पानांवर डाग आणि जखमा निर्माण करणारा बुरशीजन्य पानावरील रोग."
    },

    "disease_desc_banana_pestalotiopsis": {
        "en": "A fungal disease that causes necrotic spots on banana leaves.",
        "te": "అరటి ఆకులపై మృత కణజాల మచ్చలను కలిగించే శిలీంధ్ర వ్యాధి.",
        "hi": "केले की पत्तियों पर मृत ऊतक धब्बे पैदा करने वाला कवक रोग।",
        "mr": "केळीच्या पानांवर मृत पेशी डाग निर्माण करणारा बुरशीजन्य रोग."
    },

    "disease_desc_banana_sigatoka": {
        "en": "A fungal leaf disease that can reduce the photosynthetic area of banana plants.",
        "te": "అరటి మొక్కల కిరణజన్య సంయోగక్రియ ప్రాంతాన్ని తగ్గించే శిలీంధ్ర ఆకు వ్యాధి.",
        "hi": "केले के पौधों के प्रकाश संश्लेषण क्षेत्र को कम करने वाला कवक पत्ती रोग।",
        "mr": "केळीच्या झाडांचा प्रकाशसंश्लेषण भाग कमी करणारा बुरशीजन्य पानावरील रोग."
    },

    "disease_desc_corn_common_rust": {
        "en": "A fungal disease that produces rust-colored pustules on corn leaves.",
        "te": "మొక్కజొన్న ఆకులపై తుప్పు రంగు పొక్కులను ఉత్పత్తి చేసే శిలీంధ్ర వ్యాధి.",
        "hi": "मक्के की पत्तियों पर जंग रंग के पुटिकाएं पैदा करने वाला कवक रोग।",
        "mr": "मका पानांवर तांबेरा रंगाचे पुटके तयार करणारा बुरशीजन्य रोग."
    },

    "disease_desc_corn_gray_leaf_spot": {
        "en": "A fungal disease that produces elongated lesions on corn leaves.",
        "te": "మొక్కజొన్న ఆకులపై పొడిగిన గాయాలను ఉత్పత్తి చేసే శిలీంధ్ర వ్యాధి.",
        "hi": "मक्के की पत्तियों पर लंबे घाव पैदा करने वाला कवक रोग।",
        "mr": "मका पानांवर लांबट जखमा निर्माण करणारा बुरशीजन्य रोग."
    },

    "disease_desc_corn_northern_leaf_blight": {
        "en": "A fungal disease that produces large elongated lesions on corn leaves.",
        "te": "మొక్కజొన్న ఆకులపై పెద్ద పొడిగిన గాయాలను ఉత్పత్తి చేసే శిలీంధ్ర వ్యాధి.",
        "hi": "मक्के की पत्तियों पर बड़े लंबे घाव पैदा करने वाला कवक रोग।",
        "mr": "मका पानांवर मोठ्या लांब जखमा निर्माण करणारा बुरशीजन्य रोग."
    },

    "disease_desc_cotton_bacterial_blight": {
        "en": "A bacterial disease that can affect cotton leaves, stems and other plant parts.",
        "te": "పత్తి ఆకులు, కాండం మరియు ఇతర మొక్క భాగాలను ప్రభావితం చేసే బ్యాక్టీరియా వ్యాధి.",
        "hi": "कपास की पत्तियों, तनों और अन्य पौधे के हिस्सों को प्रभावित करने वाला जीवाणु रोग।",
        "mr": "कापसाची पाने, खोड आणि इतर झाडाचे भाग प्रभावित करणारा जीवाणूजन्य रोग."
    },

    "disease_desc_cotton_cotton_leaf_curl": {
        "en": "A viral disease of cotton commonly associated with leaf curling and abnormal plant growth.",
        "te": "ఆకు ముడత మరియు అసాధారణ మొక్క పెరుగుదలతో సంబంధం ఉన్న పత్తి యొక్క వైరల్ వ్యాధి.",
        "hi": "कपास का एक विषाणु रोग जो आमतौर पर पत्तियों के मोड़ और असामान्य पौधे की वृद्धि से जुड़ा होता है।",
        "mr": "कापसाचा एक विषाणूजन्य रोग जो सामान्यतः पानांच्या वळणे आणि असामान्य वाढीशी संबंधित असतो."
    },

    "disease_desc_cotton_fusarium_wilt": {
        "en": "A soil-borne fungal disease that affects the vascular system of cotton plants.",
        "te": "పత్తి మొక్కల నాళీయ వ్యవస్థను ప్రభావితం చేసే నేల ద్వారా వ్యాపించే శిలీంధ్ర వ్యాధి.",
        "hi": "कपास के पौधों के संवहनी तंत्र को प्रभावित करने वाला मृदा जनित कवक रोग।",
        "mr": "कापसाच्या झाडांची वाहिनी प्रणाली प्रभावित करणारा मातीतून येणारा बुरशीजन्य रोग."
    },

    "disease_desc_grape_black_measles": {
        "en": "A fungal disease complex that can affect grape leaves, shoots and fruit.",
        "te": "ద్రాక్ష ఆకులు, రెమ్మలు మరియు పండ్లను ప్రభావితం చేయగల శిలీంధ్ర వ్యాధి సముదాయం.",
        "hi": "अंगूर की पत्तियों, शाखाओं और फलों को प्रभावित करने वाला कवक रोगों का एक समूह।",
        "mr": "द्राक्षांची पाने, फांद्या आणि फळे प्रभावित करणारा बुरशीजन्य रोगांचा संच."
    },

    "disease_desc_grape_black_rot": {
        "en": "A fungal disease that can affect grape leaves, shoots and fruit.",
        "te": "ద్రాక్ష ఆకులు, రెమ్మలు మరియు పండ్లను ప్రభావితం చేయగల శిలీంధ్ర వ్యాధి.",
        "hi": "अंगूर की पत्तियों, शाखाओं और फलों को प्रभावित करने वाला कवक रोग।",
        "mr": "द्राक्षांची पाने, फांद्या आणि फळे प्रभावित करणारा बुरशीजन्य रोग."
    },

    "disease_desc_grape_isariopsis_leaf_spot": {
        "en": "A fungal leaf-spot disease that can cause dark lesions on grape leaves.",
        "te": "ద్రాక్ష ఆకులపై ముదురు గాయాలను కలిగించే శిలీంధ్ర ఆకు మచ్చ వ్యాధి.",
        "hi": "अंगूर की पत्तियों पर गहरे घाव पैदा करने वाला कवक पत्ती धब्बा रोग।",
        "mr": "द्राक्षांच्या पानांवर गडद जखमा निर्माण करणारा बुरशीजन्य पानावरील डाग रोग."
    },

    "disease_desc_mango_anthracnose": {
        "en": "A fungal disease that can affect mango leaves, flowers, twigs and fruit.",
        "te": "మామిడి ఆకులు, పూలు, రెమ్మలు మరియు పండ్లను ప్రభావితం చేయగల శిలీంధ్ర వ్యాధి.",
        "hi": "आम की पत्तियों, फूलों, टहनियों और फलों को प्रभावित करने वाला कवक रोग।",
        "mr": "आंब्याची पाने, फुले, फांद्या आणि फळे प्रभावित करणारा बुरशीजन्य रोग."
    },

    "disease_desc_mango_bacterial_canker": {
        "en": "A bacterial disease that can cause lesions and cankers on mango leaves, stems and fruit.",
        "te": "మామిడి ఆకులు, కాండం మరియు పండ్లపై గాయాలు మరియు క్యాంకర్లను కలిగించే బ్యాక్టీరియా వ్యాధి.",
        "hi": "आम की पत्तियों, तनों और फलों पर घाव और कैंकर पैदा करने वाला जीवाणु रोग।",
        "mr": "आंब्याची पाने, खोड आणि फळांवर जखमा आणि कॅन्कर निर्माण करणारा जीवाणूजन्य रोग."
    },

    "disease_desc_mango_powdery_mildew": {
        "en": "A fungal disease that commonly affects young mango leaves, flowers and shoots.",
        "te": "యువ మామిడి ఆకులు, పూలు మరియు రెమ్మలను సాధారణంగా ప్రభావితం చేసే శిలీంధ్ర వ్యాధి.",
        "hi": "एक कवक रोग जो आमतौर पर युवा आम की पत्तियों, फूलों और शाखाओं को प्रभावित करता है।",
        "mr": "एक बुरशीजन्य रोग जो सामान्यपणे तरुण आंब्याची पाने, फुले आणि फांद्या प्रभावित करतो."
    },

    "disease_desc_paddy_bacterial_leaf_blight": {
        "en": "A bacterial disease that can cause severe leaf damage in rice plants.",
        "te": "వరి మొక్కలలో తీవ్రమైన ఆకు నష్టాన్ని కలిగించే బ్యాక్టీరియా వ్యాధి.",
        "hi": "चावल के पौधों में गंभीर पत्ती क्षति पैदा करने वाला जीवाणु रोग।",
        "mr": "भाताच्या झाडांमध्ये तीव्र पानांचे नुकसान करणारा जीवाणूजन्य रोग."
    },

    "disease_desc_paddy_brown_spot": {
        "en": "A fungal disease of rice that produces characteristic brown lesions on leaves.",
        "te": "ఆకులపై ప్రత్యేక బ్రౌన్ గాయాలను ఉత్పత్తి చేసే వరి యొక్క శిలీంధ్ర వ్యాధి.",
        "hi": "चावल का एक कवक रोग जो पत्तियों पर विशिष्ट भूरे घाव पैदा करता है।",
        "mr": "भातावरील एक बुरशीजन्य रोग जो पानांवर ठळक तपकिरी जखमा निर्माण करतो."
    },

    "disease_desc_paddy_leaf_blast": {
        "en": "A fungal disease that can cause characteristic lesions on rice leaves.",
        "te": "వరి ఆకులపై ప్రత్యేక గాయాలను కలిగించే శిలీంధ్ర వ్యాధి.",
        "hi": "चावल की पत्तियों पर विशिष्ट घाव पैदा करने वाला कवक रोग।",
        "mr": "भाताच्या पानांवर ठळक जखमा निर्माण करणारा बुरशीजन्य रोग."
    },

    "disease_desc_potato_early_blight": {
        "en": "A fungal disease that commonly affects potato leaves and can reduce plant vigor.",
        "te": "బంగాళాదుంప ఆకులను సాధారణంగా ప్రభావితం చేసి మొక్క బలాన్ని తగ్గించే శిలీంధ్ర వ్యాధి.",
        "hi": "एक कवक रोग जो आमतौर पर आलू की पत्तियों को प्रभावित करता है और पौधे की शक्ति को कम कर सकता है।",
        "mr": "एक बुरशीजन्य रोग जो सामान्यपणे बटाट्याची पाने प्रभावित करतो आणि झाडाची ताकद कमी करू शकतो."
    },

    "disease_desc_potato_late_blight": {
        "en": "A destructive disease that can rapidly affect potato foliage and tubers under favorable conditions.",
        "te": "అనుకూల పరిస్థితులలో బంగాళాదుంప ఆకులు మరియు దుంపలను త్వరగా ప్రభావితం చేసే వినాశక శిలీంధ్ర వ్యాధి.",
        "hi": "एक विनाशकारी रोग जो अनुकूल परिस्थितियों में आलू की पत्तियों और कंदों को तेजी से प्रभावित कर सकता है।",
        "mr": "एक विध्वंसक रोग जो अनुकूल परिस्थितींमध्ये बटाट्याची पाने आणि कंद त्वरीत प्रभावित करू शकतो."
    },

    "disease_desc_soybean_caterpillar": {
        "en": "The model detected symptoms associated with caterpillar feeding damage on soybean foliage.",
        "te": "సోయాబీన్ ఆకులపై గొంగళి పురుగు తినే నష్టంతో సంబంధం ఉన్న లక్షణాలను మోడల్ గుర్తించింది.",
        "hi": "मॉडल ने सोयाबीन की पत्तियों पर सुंडी के भक्षण क्षति से जुड़े लक्षणों का पता लगाया।",
        "mr": "मॉडेलने सोयाबीनच्या पानांवर अळीच्या खाण्याच्या नुकसानीशी संबंधित लक्षणे ओळखली."
    },

    "disease_desc_soybean_diabrotica_speciosa": {
        "en": "The model detected symptoms associated with feeding damage from a leaf-feeding beetle.",
        "te": "ఆకు తినే బీటిల్ యొక్క ఆహార నష్టంతో సంబంధం ఉన్న లక్షణాలను మోడల్ గుర్తించింది.",
        "hi": "मॉडल ने पत्ती खाने वाले भृंग के भक्षण क्षति से जुड़े लक्षणों का पता लगाया।",
        "mr": "मॉडेलने पाने खाणाऱ्या भुंग्याच्या खाण्याच्या नुकसानीशी संबंधित लक्षणे ओळखली."
    },

    "disease_desc_tomato_bacterial_spot": {
        "en": "A bacterial disease that can cause spots on tomato leaves, stems and fruit.",
        "te": "టమాటా ఆకులు, కాండం మరియు పండ్లపై మచ్చలను కలిగించే బ్యాక్టీరియా వ్యాధి.",
        "hi": "एक जीवाणु रोग जो टमाटर की पत्तियों, तनों और फलों पर धब्बे पैदा कर सकता है।",
        "mr": "एक जीवाणूजन्य रोग जो टोमॅटोची पाने, खोड आणि फळांवर डाग निर्माण करू शकतो."
    },

    "disease_desc_tomato_early_blight": {
        "en": "A fungal disease that commonly affects tomato leaves, stems and fruit.",
        "te": "టమాటా ఆకులు, కాండం మరియు పండ్లను సాధారణంగా ప్రభావితం చేసే శిలీంధ్ర వ్యాధి.",
        "hi": "एक कवक रोग जो आमतौर पर टमाटर की पत्तियों, तनों और फलों को प्रभावित करता है।",
        "mr": "एक बुरशीजन्य रोग जो सामान्यपणे टोमॅटोची पाने, खोड आणि फळे प्रभावित करतो."
    },

    "disease_desc_tomato_late_blight": {
        "en": "A disease that can rapidly damage tomato foliage and fruit under favorable conditions.",
        "te": "అనుకూల పరిస్థితులలో టమాటా ఆకులు మరియు పండ్లను త్వరగా దెబ్బతీసే వ్యాధి.",
        "hi": "एक रोग जो अनुकूल परिस्थितियों में टमाटर की पत्तियों और फलों को तेजी से नुकसान पहुंचा सकता है।",
        "mr": "एक रोग जो अनुकूल परिस्थितींमध्ये टोमॅटोची पाने आणि फळे त्वरीत नुकसान करू शकतो."
    },

    "disease_desc_wheat_mildew": {
        "en": "A fungal disease that produces powdery fungal growth on wheat leaves and stems.",
        "te": "గోధుమ ఆకులు మరియు కాండంపై బూడిచ శిలీంధ్ర పెరుగుదలను ఉత్పత్తి చేసే వ్యాధి.",
        "hi": "गेहूं की पत्तियों और तनों पर पाउडर जैसी कवक वृद्धि पैदा करने वाला एक कवक रोग।",
        "mr": "गहूच्या पाने व खोडांवर भुरीसारखी बुरशी वाढ निर्माण करणारा रोग."
    },

    "disease_desc_wheat_septoria": {
        "en": "A fungal disease that produces leaf lesions and can reduce photosynthetic leaf area.",
        "te": "ఆకు గాయాలను ఉత్పత్తి చేసి కిరణజన్య సంయోగక్రియ ఆకు ప్రాంతాన్ని తగ్గించగల శిలీంధ్ర వ్యాధి.",
        "hi": "एक कवक रोग जो पत्ती घाव पैदा करता है और प्रकाश संश्लेषक पत्ती क्षेत्र को कम कर सकता है।",
        "mr": "एक बुरशीजन्य रोग जो पानांवर जखमा निर्माण करतो आणि प्रकाशसंश्लेषक पानांचे क्षेत्र कमी करू शकतो."
    },

    "disease_desc_wheat_yellowrust": {
        "en": "A fungal rust disease that produces yellow or orange-yellow pustules on wheat leaves.",
        "te": "గోధుమ ఆకులపై పసుపు లేదా నారింజ-పసుపు పొక్కులను ఉత్పత్తి చేసే శిలీంధ్ర తుప్పు వ్యాధి.",
        "hi": "एक कवक रतुआ रोग जो गेहूं की पत्तियों पर पीले या नारंगी-पीले पुटिकाएं पैदा करता है।",
        "mr": "एक बुरशीजन्य तांबेरा रोग जो गहूच्या पानांवर पिवळे किंवा नारिंगी-पिवळे पुटके निर्माण करतो."
    },

    # -------------------------------------------------
    # DISEASE LIBRARY — SYMPTOMS (as dict of lists)
    # -------------------------------------------------

    "disease_symptoms_banana_cordana": {
        "en": ["Brown or reddish-brown leaf spots", "Spots may enlarge and develop darker margins", "Severely affected leaves may lose healthy green tissue"],
        "te": ["ఆకులపై గోధుమ లేదా ఎరుపు-గోధుమ మచ్చలు", "మచ్చలు పెద్దవవడం మరియు ముదురు అంచులు వికసించడం", "తీవ్రంగా ప్రభావితమైన ఆకులు ఆరోగ్యకరమైన ఆకు కణజాలాన్ని కోల్పోవచ్చు"],
        "hi": ["भूरे या लाल-भूरे पत्ती धब्बे", "धब्बे बड़े हो सकते हैं और गहरे किनारे विकसित कर सकते हैं", "बुरंग प्रभावित पत्तियां स्वस्थ हरे ऊतक खो सकती हैं"],
        "mr": ["पानांवर तपकिरी किंवा तांबूस-तपकिरी डाग", "डाग मोठे होऊ शकतात आणि गडद कडा विकसित करू शकतात", "गंभीर प्रभावित पाने आरोग्यपूर्ण हिरवा ऊतक गमावू शकतात"]
    },

    "disease_symptoms_banana_pestalotiopsis": {
        "en": ["Small brown spots on leaves", "Spots can enlarge over time", "Affected tissue may become dry and necrotic"],
        "te": ["ఆకులపై చిన్న గోధుమ మచ్చలు", "కాలక్రమేణా మచ్చలు పెద్దవవు", "ప్రభావిత కణజాలం పొడిగా మరియు నెక్రోటిక్ అవ్వవచ్చు"],
        "hi": ["पत्तियों पर छोटे भूरे धब्बे", "धब्बे समय के साथ बड़े हो सकते हैं", "प्रभावित ऊतक सूखा और मृत हो सकता है"],
        "mr": ["पानांवर लहान तपकिरी डाग", "काळ्यानुसार डाग मोठे होऊ शकतात", "प्रभावित ऊतक कोरडा आणि मृत होऊ शकतो"]
    },

    "disease_symptoms_banana_sigatoka": {
        "en": ["Small streaks or spots on leaves", "Spots become darker as they develop", "Severe infection can cause leaf yellowing and drying"],
        "te": ["ఆకులపై చిన్న గీతలు లేదా మచ్చలు", "అభివృద్ధి చెందుతున్నప్పుడు మచ్చలు ముదురుగా అవుతాయి", "తీవ్రమైన infeection ఆకు పసుపుగా అవడం మరియు ఎండిపోవడం కలిగించవచ్చు"],
        "hi": ["पत्तियों पर छोटी धारियां या धब्बे", "विकसित होने पर धब्बे गहरे हो जाते हैं", "गंभीर संक्रमण पत्ती पीले होने और सूखने का कारण बन सकता है"],
        "mr": ["पानांवर लहान रेषा किंवा डाग", "विकसित होताना डाग गडद होतात", "गंभीर संसर्गामुळे पान पिवळे होणे आणि वाळणे होऊ शकते"]
    },

    "disease_symptoms_corn_common_rust": {
        "en": ["Rust-colored spots or pustules", "Pustules may appear on both sides of leaves", "Severe infection can reduce healthy leaf area"],
        "te": ["తుప్పు-రంగు మచ్చలు లేదా పొక్కులు", "ఆకులు రెండు వైపులా పొక్కులు కనిపించవచ్చు", "తీవ్రమైన infeection ఆరోగ्यకరమైన ఆకు ప్రాంతాన్ని తగ్గించవచ్చు"],
        "hi": ["जंग रंग के धब्बे या पुटिकाएं", "पुटिकाएं पत्तियों के दोनों तरफ दिखाई दे सकती हैं", "गंभीर संक्रमण स्वस्थ पत्ती क्षेत्र को कम कर सकता है"],
        "mr": ["तांबेरा रंगाचे डाग किंवा पुटके", "पुटके पानांच्या दोन्ही बाजूंनी दिसू शकतात", "गंभीर संसर्गामुळे आरोग्यपूर्ण पानांचे क्षेत्र कमी होऊ शकते"]
    },

    "disease_symptoms_corn_gray_leaf_spot": {
        "en": ["Gray or tan rectangular lesions", "Lesions may expand and merge", "Lower leaves may show symptoms first"],
        "te": ["బూడిచ లేదా టాన్ దీర్ఘచతురస్ర గాయాలు", "గాయాలు విస్తరించి విలీనమవవచ్చు", "కింది ఆకులు మొదట లక్షణాలను చూపవచ్చు"],
        "hi": ["सलेटी या टैन आयताकार घाव", "घाव फैल सकते हैं और मिल सकते हैं", "निचली पत्तियों पर पहले लक्षण दिखाई दे सकते हैं"],
        "mr": ["राखाडी किंवा तपकिरी आयताकार जखमा", "जखमा विस्तारून एकत्र होऊ शकतात", "खालची पाने प्रथम लक्षणे दाखवू शकतात"]
    },

    "disease_symptoms_corn_northern_leaf_blight": {
        "en": ["Long gray-green or tan lesions", "Lesions may become large and elongated", "Severe infection can reduce leaf area"],
        "te": ["పొడవైన బూడిచ-ఆకుపచ్చ లేదా టాన్ గాయాలు", "గాయాలు పెద్దవవడం మరియు పొడిగినవవవచ్చు", "తీవ్రమైన infeection ఆకు ప్రాంతాన్ని తగ్గించవచ్చు"],
        "hi": ["लंबे सलेटी-हरे या टैन घाव", "घाव बड़े और लंबे हो सकते हैं", "गंभीर संक्रमण पत्ती क्षेत्र को कम कर सकता है"],
        "mr": ["लांब राखाडी-हिरवे किंवा तपकिरी जखमा", "जखमा मोठे आणि लांब होऊ शकतात", "गंभीर संसर्गामुळे पानांचे क्षेत्र कमी होऊ शकते"]
    },

    "disease_symptoms_cotton_bacterial_blight": {
        "en": ["Dark water-soaked or angular leaf spots", "Leaf spots may become brown or black", "Affected tissue may dry and fall out"],
        "te": ["ముదురు నీటితో తడిసిన లేదా కోణీయ ఆకు మచ్చలు", "ఆకు మచ్చలు గోధుమ లేదా నలుపు అవవచ్చు", "ప్రభావిత కణజాలం ఎండిపోవడం మరియు రాలిపోవడం జరగవచ్చు"],
        "hi": ["गहरे पानी में भीगे या कोणीय पत्ती धब्बे", "पत्ती धब्बे भूरे या काले हो सकते हैं", "प्रभावित ऊतक सूख सकता है और गिर सकता है"],
        "mr": ["गडद पाण्याने भिजलेले किंवा कोनीय पानांचे डाग", "पानांचे डाग तपकिरी किंवा काळे होऊ शकतात", "प्रभावित ऊतक कोरडा होऊन पडू शकतो"]
    },

    "disease_symptoms_cotton_cotton_leaf_curl": {
        "en": ["Upward or downward curling of leaves", "Leaf thickening or distortion", "Reduced plant growth may occur"],
        "te": ["ఆకుల పైకి లేదా కిందకు ముడత పెట్టడం", "ఆకు మందం లేదా వికృతి", "తగ్గిన మొక్క పెరుగుదల సంభవించవచ్చు"],
        "hi": ["पत्तियों का ऊपर या नीचे मुड़ना", "पत्ती का मोटा होना या विकृत होना", "पौधे की वृद्धि में कमी हो सकती है"],
        "mr": ["पानांचे वर किंवा खाली वळणे", "पानांचे जाड होणे किंवा विकृत होणे", "झाडांची वाढ मंदावू शकते"]
    },

    "disease_symptoms_cotton_fusarium_wilt": {
        "en": ["Yellowing or wilting leaves", "Stunted plant growth", "Discoloration of vascular tissue may occur"],
        "te": ["ఆకులు పసుపుగా మారడం లేదా ఎండిపోవడం", "ఆశించిన మొక్క పెరుగుదల", "నాళీయ కణజాలం వివర్ణీకరణ సంభవించవచ్చు"],
        "hi": ["पत्तियों का पीला होना या मुरझाना", "पौधे की वृद्धि रुकना", "संवहनी ऊतक का रंग बदलना हो सकता है"],
        "mr": ["पानांचे पिवळे पडणे किंवा मळणे", "झाडांची वाढ खुंटणे", "वाहिनी ऊतकाचे रंग बदलणे होऊ शकते"]
    },

    "disease_symptoms_grape_black_measles": {
        "en": ["Small dark spots on leaves", "Leaf discoloration may develop", "Fruit may show dark symptoms in affected vines"],
        "te": ["ఆకులపై చిన్న ముదురు మచ్చలు", "ఆకు వివర్ణీకరణ అభివృద్ధి చెందవచ్చు", "పండ్లపై ప్రభావిత తంత్రాలలో ముదురు లక్షణాలు కనిపించవచ్చు"],
        "hi": ["पत्तियों पर छोटे गहरे धब्बे", "पत्ती का रंग बदलना विकसित हो सकता है", "प्रभावित बेलों पर फलों में गहरे लक्षण दिखाई दे सकते हैं"],
        "mr": ["पानांवर लहान गडद डाग", "पानांचे रंग बदलणे विकसित होऊ शकते", "प्रभावित द्राक्षाबेलांवर फळांवर गडद लक्षणे दिसू शकतात"]
    },

    "disease_symptoms_grape_black_rot": {
        "en": ["Brown or reddish leaf spots", "Dark lesions may develop on plant tissue", "Fruit can develop dark rot symptoms"],
        "te": ["బ్రౌన్ లేదా ఎరుపు-బ్రౌన్ ఆకు మచ్చలు", "మొక్క కణజాలంపై ముదురు గాయాలు అభివృద్ధి చెందవచ్చు", "పండ్లపై ముదురు కుళ్ళు లక్షణాలు అభివృద్ధి చెందవచ్చు"],
        "hi": ["भूरे या लाल-भूरे पत्ती धब्बे", "पौधे के ऊतक पर गहरे घाव विकसित हो सकते हैं", "फलों पर गहरा सड़न लक्षण विकसित हो सकता है"],
        "mr": ["तपकिरी किंवा तांबूस-तपकिरी पानांचे डाग", "झाडाच्या ऊतकावर गडद जखमा विकसित होऊ शकतात", "फळांवर काळ्या सडण्याची लक्षणे विकसित होऊ शकतात"]
    },

    "disease_symptoms_grape_isariopsis_leaf_spot": {
        "en": ["Dark spots on leaves", "Spots may enlarge over time", "Severely affected leaves may yellow or fall"],
        "te": ["ఆకులపై ముదురు మచ్చలు", "కాలక్రమేణా మచ్చలు పెద్దవవవచ్చు", "తీవ్రంగా ప్రభావితమైన ఆకులు పసుపుగా లేదా రాలవచ్చు"],
        "hi": ["पत्तियों पर गहरे धब्बे", "धब्बे समय के साथ बड़े हो सकते हैं", "बुरंग प्रभावित पत्तियां पीली हो सकती हैं या गिर सकती हैं"],
        "mr": ["पानांवर गडद डाग", "काळ्यानुसार डाग मोठे होऊ शकतात", "गंभीर प्रभावित पाने पिवळी होऊन पडू शकतात"]
    },

    "disease_symptoms_mango_anthracnose": {
        "en": ["Dark spots on leaves", "Lesions may appear on flowers and young shoots", "Fruit may develop dark sunken spots"],
        "te": ["ఆకులపై ముదురు మచ్చలు", "పూలు మరియు యువ రెమ్మలపై గాయాలు కనిపించవచ్చు", "పండ్లపై ముదురు గుంతలు కనిపించవచ్చు"],
        "hi": ["पत्तियों पर गहरे धब्बे", "फूलों और युवा शाखाओं पर घाव दिख सकते हैं", "फलों पर गहरे धंसे हुए धब्बे विकसित हो सकते हैं"],
        "mr": ["पानांवर गडद डाग", "फुलांवर आणि तरुण फांद्यांवर जखमा दिसू शकतात", "फळांवर गडद बुडालेले डाग विकसित होऊ शकतात"]
    },

    "disease_symptoms_mango_bacterial_canker": {
        "en": ["Dark leaf spots", "Cankers may develop on stems or branches", "Fruit may show dark lesions"],
        "te": ["ముదురు ఆకు మచ్చలు", "కాండం లేదా కొమ్మలపై క్యాంకర్లు అభివృద్ధి చెందవచ్చు", "పండ్లపై ముదురు గాయాలు కనిపించవచ్చు"],
        "hi": ["गहरे पत्ती धब्बे", "तनों या शाखाओं पर कैंकर विकसित हो सकते हैं", "फलों पर गहरे घाव दिख सकते हैं"],
        "mr": ["गडद पानांचे डाग", "खोड किंवा फांद्यांवर कॅन्कर विकसित होऊ शकतात", "फळांवर गडद जखमा दिसू शकतात"]
    },

    "disease_symptoms_mango_powdery_mildew": {
        "en": ["White powdery growth on plant surfaces", "Young leaves may become distorted", "Flowers may be affected"],
        "te": ["మొక్క ఉపరితలాలపై తెలుపు బూడిచ పెరుగుదల", "యువ ఆకులు వికృతమవవచ్చు", "పూలు ప్రభావితమవవచ్చు"],
        "hi": ["पौधों की सतहों पर सफेद पाउडर जैसी वृद्धि", "युवा पत्तियां विकृत हो सकती हैं", "फूल प्रभावित हो सकते हैं"],
        "mr": ["झाडांच्या पृष्ठभागावर पांढरा भुरी सारखा विकास", "तरुण पाने विकृत होऊ शकतात", "फुले प्रभावित होऊ शकतात"]
    },

    "disease_symptoms_paddy_bacterial_leaf_blight": {
        "en": ["Water-soaked lesions near leaf margins", "Leaves may develop yellow or straw-colored areas", "Severely affected leaves may dry"],
        "te": ["ఆకు అంచుల సమీపంలో నీటితో తడిసిన గాయాలు", "ఆకులపై పసుపు లేదా బెరడు-రంగు ప్రాంతాలు అభివృద్ధి చెందవచ్చు", "తీవ్రంగా ప్రభావితమైన ఆకులు ఎండిపోవవచ్చు"],
        "hi": ["पत्ती के किनारों के पास पानी में भीगे घाव", "पत्तियों पर पीले या पुआल रंग के क्षेत्र विकसित हो सकते हैं", "बुरंग प्रभावित पत्तियां सूख सकती हैं"],
        "mr": ["पानांच्या कडांजवळ पाण्याने भिजलेल्या जखमा", "पानांवर पिवळे किंवा काडीच्या रंगाचे प्रदेश विकसित होऊ शकतात", "गंभीर प्रभावित पाने कोरडी होऊ शकतात"]
    },

    "disease_symptoms_paddy_brown_spot": {
        "en": ["Small brown circular or oval spots", "Spots may develop darker margins", "Severe infection can reduce leaf health"],
        "te": ["చిన్న గోధుమ వృత్తాకార లేదా అండాకార మచ్చలు", "మచ్చలు ముదురు అంచులు వికసించవచ్చు", "తీవ్రమైన infeection ఆకు ఆరోగ్యాన్ని తగ్గించవచ్చు"],
        "hi": ["छोटे भूरे गोलाकार या अंडाकार धब्बे", "धब्बे गहरे किनारे विकसित कर सकते हैं", "गंभीर संक्रमण पत्ती के स्वास्थ्य को कम कर सकता है"],
        "mr": ["लहान तपकिरी गोलाकार किंवा अंडाकार डाग", "डाग गडद कडा विकसित करू शकतात", "गंभीर संसर्गामुळे पानांचे आरोग्य कमी होऊ शकते"]
    },

    "disease_symptoms_paddy_leaf_blast": {
        "en": ["Spindle-shaped or diamond-shaped leaf lesions", "Lesions may have gray centers", "Severe infection can damage large areas of leaves"],
        "te": ["మొక్కజొన్న-ఆకార లేదా వజ్ర-ఆకార ఆకు గాయాలు", "గాయాలకు బూడిచ కేంద్రాలు ఉండవచ్చు", "తీవ్రమైన infeection ఆకుల పెద్ద ప్రాంతాలను గాయపరచవచ్చు"],
        "hi": ["तंतु आकार या हीरे के आकार के पत्ती घाव", "घावों के केंद्र सलेटी हो सकते हैं", "गंभीर संक्रमण पत्तियों के बड़े क्षेत्रों को नुकसान पहुंचा सकता है"],
        "mr": ["सूताकार किंवा हिरम्याच्या आकाराच्या पानांच्या जखमा", "जखमांची केंद्रे राखाडी असू शकतात", "गंभीर संसर्गामुळे पानांच्या मोठ्या प्रदेशांना नुकसान होऊ शकतो"]
    },

    "disease_symptoms_potato_early_blight": {
        "en": ["Dark brown leaf spots", "Concentric ring patterns may appear", "Older leaves are often affected first"],
        "te": ["ముదురు గోధుమ ఆకు మచ్చలు", "ఏకకేంద్రీయ వలయం నమూనాలు కనిపించవచ్చు", "పాత ఆకులు తరచుగా మొదట ప్రభావితమవుతాయి"],
        "hi": ["गहरे भूरे पत्ती धब्बे", "एककेंद्रीय वलय पैटर्न दिखाई दे सकते हैं", "पुरानी पत्तियां अक्सर पहले प्रभावित होती हैं"],
        "mr": ["गडद तपकिरी पानांचे डाग", "एककेंद्रीय वलय पैटर्न दिसू शकतात", "जुन्या पानांवर प्रथम प्रभाव होतो"]
    },

    "disease_symptoms_potato_late_blight": {
        "en": ["Dark irregular leaf lesions", "Affected leaves may rapidly deteriorate", "Tuber infection can cause internal discoloration"],
        "te": ["ముదురు అనియత ఆకు గాయాలు", "ప్రభావిత ఆకులు త్వరగా క్షీణించవచ్చు", "కండ అంటు అంతర వివర్ణీకరణకు కారణమవవచ్చు"],
        "hi": ["गहरे अनियमित पत्ती घाव", "प्रभावित पत्तियां तेजी से खराब हो सकती हैं", "कंद संक्रमण आंतरिक रंग बदलाव का कारण बन सकता है"],
        "mr": ["गडद अनियमित पानांच्या जखमा", "प्रभावित पाने लवकर खराब होऊ शकतात", "कंदाच्या संसर्गामुळे आंतरिक रंग बदल होऊ शकतो"]
    },

    "disease_symptoms_soybean_caterpillar": {
        "en": ["Irregular holes in leaves", "Leaf tissue may be consumed", "Heavy feeding can reduce leaf area"],
        "te": ["ఆకులపై అనియత రంధ్రాలు", "ఆకు కణజాలం వినియోగించబడవచ్చు", "భారీ తినడం ఆకు ప్రాంతాన్ని తగ్గించవచ్చు"],
        "hi": ["पत्तियों में अनियमित छेद", "पत्ती का ऊतक खाया जा सकता है", "भारी खिलाने से पत्ती क्षेत्र कम हो सकता है"],
        "mr": ["पानांमध्ये अनियमित छिद्रे", "पानांचा ऊतक खाण्यात आला असू शकतो", "जास्त खाल्यामुळे पानांचे क्षेत्र कमी होऊ शकते"]
    },

    "disease_symptoms_soybean_diabrotica_speciosa": {
        "en": ["Small holes or damaged areas on leaves", "Leaf tissue may be consumed", "Heavy feeding can reduce healthy leaf area"],
        "te": ["ఆకులపై చిన్న రంధ్రాలు లేదా గాయపడిన ప్రాంతాలు", "ఆకు కణజాలం వినియోగించబడవచ్చు", "భారీ తినడం ఆరోగ్యకరమైన ఆకు ప్రాంతాన్ని తగ్గించవచ్చు"],
        "hi": ["पत्तियों पर छोटे छेद या क्षतिग्रस्त क्षेत्र", "पत्ती का ऊतक खाया जा सकता है", "भारी खिलाने से स्वस्थ पत्ती क्षेत्र कम हो सकता है"],
        "mr": ["पानांवर लहान छिद्रे किंवा क्षतिग्रस्त क्षेत्रे", "पानांचा ऊतक खाण्यात आला असू शकतो", "जास्त खाल्यामुळे आरोग्यपूर्ण पानांचे क्षेत्र कमी होऊ शकते"]
    },

    "disease_symptoms_tomato_bacterial_spot": {
        "en": ["Small dark spots on leaves", "Spots may have yellow halos", "Fruit can develop small raised or dark lesions"],
        "te": ["ఆకులపై చిన్న ముదురు మచ్చలు", "మచ్చలకు పసుపు హాలోలు ఉండవచ్చు", "పండ్లపై చిన్న ఎత్తైన లేదా ముదురు గాయాలు అభివృద్ధి చెందవచ్చు"],
        "hi": ["पत्तियों पर छोटे गहरे धब्बे", "धब्बों के चारों ओर पीले हलो हो सकते हैं", "फलों पर छोटे उभरे या गहरे घाव विकसित हो सकते हैं"],
        "mr": ["पानांवर लहान गडद डाग", "डागांभोवती पिवळ्या हॅलो असू शकतात", "फळांवर लहान उंच किंवा गडद जखमा विकसित होऊ शकतात"]
    },

    "disease_symptoms_tomato_early_blight": {
        "en": ["Dark spots on older leaves", "Concentric ring patterns may develop", "Affected leaves may yellow and fall"],
        "te": ["పాత ఆకులపై ముదురు మచ్చలు", "ఏకకేంద్రీయ వలయం నమూనాలు అభివృద్ధి చెందవచ్చు", "ప్రభావిత ఆకులు పసుపుగా మారి రాలవచ్చు"],
        "hi": ["पुरानी पत्तियों पर गहरे धब्बे", "एककेंद्रीय वलय पैटर्न विकसित हो सकते हैं", "प्रभावित पत्तियां पीली हो सकती हैं और गिर सकती हैं"],
        "mr": ["जुन्या पानांवर गडद डाग", "एककेंद्रीय वलय पैटर्न विकसित होऊ शकतात", "प्रभावित पाने पिवळी होऊन पडू शकतात"]
    },

    "disease_symptoms_tomato_late_blight": {
        "en": ["Dark irregular leaf lesions", "Rapid leaf deterioration may occur", "Fruit can develop dark firm lesions"],
        "te": ["ముదురు అనియత ఆకు గాయాలు", "త్వరిత ఆకు క్షీణత సంభవించవచ్చు", "పండ్లపై ముదురు గట్టి గాయాలు అభివృద్ధి చెందవచ్చు"],
        "hi": ["गहरे अनियमित पत्ती घाव", "पत्ती का तेजी से क्षरण हो सकता है", "फलों पर गहरे कठोर घाव विकसित हो सकते हैं"],
        "mr": ["गडद अनियमित पानांच्या जखमा", "पानांचे लवकर ऱ्हास होऊ शकते", "फळांवर गडद घट्ट जखमा विकसित होऊ शकतात"]
    },

    "disease_symptoms_wheat_mildew": {
        "en": ["White powdery patches", "Affected leaves may yellow", "Severe infection can reduce healthy leaf area"],
        "te": ["తెలుపు బూడిచ పాచీలు", "ప్రభావిత ఆకులు పసుపుగా మారవచ్చు", "తీవ్రమైన infeection ఆరోగ్యకరమైన ఆకు ప్రాంతాన్ని తగ్గించవచ్చు"],
        "hi": ["सफेद पाउडर जैसे पैच", "प्रभावित पत्तियां पीली हो सकती हैं", "गंभीर संक्रमण स्वस्थ पत्ती क्षेत्र को कम कर सकता है"],
        "mr": ["पांढरे भुरीसारखे पatch", "प्रभावित पाने पिवळी होऊ शकतात", "गंभीर संसर्गामुळे आरोग्यपूर्ण पानांचे क्षेत्र कमी होऊ शकते"]
    },

    "disease_symptoms_wheat_septoria": {
        "en": ["Brown or gray leaf lesions", "Small dark structures may occur within lesions", "Older leaves may be affected first"],
        "te": ["బ్రౌన్ లేదా బూడిచ ఆకు గాయాలు", "ఘన గాయాల లోపల చిన్న ముదురు నిర్మాణాలు సంభవించవచ్చు", "పాత ఆకులు మొదట ప్రభావితమవవచ్చు"],
        "hi": ["भूरे या सलेटी पत्ती घाव", "घावों के भीतर छोटी गहरी संरचनाएं हो सकती हैं", "पुरानी पत्तियां पहले प्रभावित हो सकती हैं"],
        "mr": ["तपकिरी किंवा राखाडी पानांच्या जखमा", "जखमांच्या आत लहान गडद रचना असू शकतात", "जुन्या पानांवर प्रथम प्रभाव होऊ शकतो"]
    },

    "disease_symptoms_wheat_yellowrust": {
        "en": ["Yellow or orange-yellow stripe-like pustules", "Pustules commonly follow leaf veins", "Severe infection can reduce leaf function"],
        "te": ["పసుపు లేదా నారింజ-పసుపు పట్టీ-ఆకార పొక్కులు", "పొక్కులు సాధారణంగా ఆకు నాళాలను అనుసరిస్తాయి", "తీవ్రమైన infeection ఆకు పనిని తగ్గించవచ్చు"],
        "hi": ["पीले या नारंगी-पीले धारीदार पुटिकाएं", "पुटिकाएं आमतौर पर पत्ती की नसों का अनुसरण करती हैं", "गंभीर संक्रमण पत्ती के कार्य को कम कर सकता है"],
        "mr": ["पिवळे किंवा नारिंगी-पिवळे रेषेसारखे पुटके", "पुटके सामान्यतः पानांच्या शिरांचे अनुसरण करतात", "गंभीर संसर्गामुळे पानांचे कार्य कमी होऊ शकते"]
    },

    # -------------------------------------------------
    # DISEASE LIBRARY — MANAGEMENT (as dict of lists)
    # -------------------------------------------------

    "disease_management_banana_cordana": {
        "en": ["Remove severely affected leaves where practical", "Maintain good field sanitation", "Improve air circulation around plants", "Use appropriate fungicide management when recommended"],
        "te": ["ఆచరణాత్మకమైనప్పుడు తీవ్రంగా ప్రభావితమైన ఆకులను తొలగించండి", "మంచి ఫీల్డ్ శుభ్రతను నిర్వహించండి", "మొక్కల చు�around air circulationను మెరుగుపరచండి", "సిఫార్సు చేసినప్పుడు సరిపడే fungicide నిర్వహణను ఉపయోగించండి"],
        "hi": ["जहां व्यावहारिक हो वहां बुरंग प्रभावित पत्तियों को हटाएं", "अच्छा खेत स्वच्छता बनाए रखें", "पौधों के आसपास हवा का संचार सुधारें", "जब अनुशंसित हो तब उचित कवकनाशी प्रबंधन का उपयोग करें"],
        "mr": ["जेथे शक्य असेल तेथे गंभीर प्रभावित पाने काढून टाका", "चांगले शेती स्वच्छता राखा", "झाडांभोवती हवा प्रवाह सुधारा", "शिफारस केल्यावर योग्य बुरशीनाशक वापरा"]
    },

    "disease_management_banana_pestalotiopsis": {
        "en": ["Remove severely affected leaves", "Improve field sanitation", "Reduce prolonged leaf wetness", "Use appropriate fungicide management when recommended"],
        "te": ["తీవ్రంగా ప్రభావితమైన ఆకులను తొలగించండి", "ఫీల్డ్ శుభ్రతను మెరుగుపరచండి", "ఆకు తడిని పొడిగి ఉండకుండా తగ్గించండి", "సిఫార్సు చేసినప్పుడు సరిపడే fungicide నిర్వహణను ఉపయోగించండి"],
        "hi": ["बुरंग प्रभावित पत्तियों को हटाएं", "खेत की स्वच्छता में सुधार करें", "पत्ती के लंबे समय तक गीला रहने को कम करें", "जब अनुशंसित हो तब उचित कवकनाशी प्रबंधन का उपयोग करें"],
        "mr": ["गंभीर प्रभावित पाने काढून टाका", "शेताची स्वच्छता सुधारा", "पानांचा दीर्घकाळ ओला राहणा टाळा", "शिफारस केल्यावर योग्य बुरशीनाशक वापरा"]
    },

    "disease_management_banana_sigatoka": {
        "en": ["Remove severely affected leaves where practical", "Maintain field sanitation", "Improve airflow", "Use recommended fungicide programs when appropriate"],
        "te": ["ఆచరణాత్మకమైనప్పుడు తీవ్రంగా ప్రభావితమైన ఆకులను తొలగించండి", "ఫీల్డ్ శుభ్రతను నిర్వహించండి", "ఎయిర్flowను మెరుగుపరచండి", "ఉచితమైనప్పుడు సిఫార్సు చేసిన fungicide కార్యక్రమాలను ఉపయోగించండి"],
        "hi": ["जहां व्यावहारिक हो वहां बुरंग प्रभावित पत्तियों को हटाएं", "खेत स्वच्छता बनाए रखें", "हवा के प्रवाह में सुधार करें", "जब उचित हो तब अनुशंसित कवकनाशी कार्यक्रमों का उपयोग करें"],
        "mr": ["जेथे शक्य असेल तेथे गंभीर प्रभावित पाने काढून टाका", "शेताची स्वच्छता राखा", "हवा प्रवाह सुधारा", "योग्य असताना शिफारस केलेल्या बुरशीनाशक कार्यक्रम वापरा"]
    },

    "disease_management_corn_common_rust": {
        "en": ["Use resistant varieties when available", "Monitor fields regularly", "Maintain good crop management", "Use fungicides when recommended for the situation"],
        "te": ["అందుబాటులో ఉన్నప్పుడు నిరోధక రకాలను ఉపయోగించండి", "నియమితంగా ఫీల్డ్‌లను పర్యవేక్షించండి", "మంచి పంట నిర్వహణను నిర్వహించండి", "పరిస్థితికి సిఫార్సు చేసినప్పుడు fungicidesను ఉపయోగించండి"],
        "hi": ["जब उपलब्ध हो प्रतिरोधी किस्मों का उपयोग करें", "नियमित रूप से खेतों की निगरानी करें", "अच्छा फसल प्रबंधन बनाए रखें", "स्थिति के लिए अनुशंसित होने पर कवकनाशी का उपयोग करें"],
        "mr": ["उपलब्ध असताना प्रतिरोधी जाती वापरा", "नियमितपणे शेतांचे निरीक्षण करा", "चांगले पीक व्यवस्थापन राखा", "परिस्थितीसाठी शिफारस केल्यावर बुरशीनाशक वापरा"]
    },

    "disease_management_corn_gray_leaf_spot": {
        "en": ["Use resistant hybrids", "Manage crop residue appropriately", "Monitor disease development", "Use fungicide management when recommended"],
        "te": ["నిరోధక హైబ్రిడ్‌లను ఉపయోగించండి", "పంట అవశేషాన్ని సరిగ్గా నిర్వహించండి", "వ్యాధి అభివృద్ధిని పర్యవేక్షించండి", "సిఫార్సు చేసినప్పుడు fungicide నిర్వహణను ఉపయోగించండి"],
        "hi": ["प्रतिरोधी संकरों का उपयोग करें", "फसल अवशेषों को उचित रूप से प्रबंधित करें", "रोग विकास की निगरानी करें", "जब अनुशंसित हो तब कवकनाशी प्रबंधन का उपयोग करें"],
        "mr": ["प्रतिरोधी संकर वापरा", "पीक अवशेष योग्यरित्या व्यवस्थापित करा", "रोग विकासाचे निरीक्षण करा", "शिफारस केल्यावर बुरशीनाशक व्यवस्थापन वापरा"]
    },

    "disease_management_corn_northern_leaf_blight": {
        "en": ["Use resistant hybrids", "Monitor fields regularly", "Manage crop residue", "Use fungicides when recommended"],
        "te": ["నిరోధక హైబ్రిడ్‌లను ఉపయోగించండి", "నియమితంగా ఫీల్డ్‌లను పర్యవేక్షించండి", "పంట అవశేషాన్ని నిర్వహించండి", "సిఫార్సు చేసినప్పుడు fungicidesను ఉపయోగించండి"],
        "hi": ["प्रतिरोधी संकरों का उपयोग करें", "नियमित रूप से खेतों की निगरानी करें", "फसल अवशेषों का प्रबंधन करें", "जब अनुशंसित हो तब कवकनाशी का उपयोग करें"],
        "mr": ["प्रतिरोधी संकर वापरा", "नियमितपणे शेतांचे निरीक्षण करा", "पीक अवशेष व्यवस्थापित करा", "शिफारस केल्यावर बुरशीनाशक वापरा"]
    },

    "disease_management_cotton_bacterial_blight": {
        "en": ["Use resistant varieties when available", "Remove or manage infected crop residue", "Use clean seed", "Follow locally recommended disease-management practices"],
        "te": ["అందుబాటులో ఉన్నప్పుడు నిరోధక రకాలను ఉపయోగించండి", "అంటు చేసిన పంట అవశేషాన్ని తొలగించండి లేదా నిర్వహించండి", "శుభ్రమైన విత్తనాలను ఉపయోగించండి", "స్థానికంగా సిఫార్సు చేసిన వ్యాధి-నిర్వహణ పద్ధతులను అనుసరించండి"],
        "hi": ["जब उपलब्ध हो प्रतिरोधी किस्मों का उपयोग करें", "संक्रमित फसल अवशेषों को हटाएं या प्रबंधित करें", "साफ बीज का उपयोग करें", "स्थानीय रूप से अनुशंसित रोग-प्रबंधन प्रथाओं का पालन करें"],
        "mr": ["उपलब्ध असताना प्रतिरोधी जाती वापरा", "संक्रमित पीक अवशेष काढून टाका किंवा व्यवस्थापित करा", "शुद्ध बियाणे वापरा", "स्थानिकदृष्ट्या शिफारस केलेल्या रोग-व्यवस्थापन पद्धती अनुसरण करा"]
    },

    "disease_management_cotton_cotton_leaf_curl": {
        "en": ["Monitor plants and vector populations", "Remove severely affected plants where recommended", "Use resistant varieties when available", "Follow local integrated pest-management practices"],
        "te": ["మొక్కలు మరియు వెక్టర్ జనాభాపర్యవేక్షించండి", "సిఫార్సు చేసినప్పుడు తీవ్రంగా ప్రభావితమైన మొక్కలను తొలగించండి", "అందుబాటులో ఉన్నప్పుడు నిరోధక రకాలను ఉపయోగించండి", "స్థానిక ఇంటిగ్రేటెడ్ pest-నిర్వహణ పద్ధతులను అనుసరించండి"],
        "hi": ["पौधों और वाहक आबादी की निगरानी करें", "जहां अनुशंसित हो वहां बुरंग प्रभावित पौधों को हटाएं", "जब उपलब्ध हो प्रतिरोधी किस्मों का उपयोग करें", "स्थानीय एकीकृत कीट-प्रबंधन प्रथाओं का पालन करें"],
        "mr": ["झाडे आणि वाहक लोकसंख्येचे निरीक्षण करा", "शिफारस केल्यावर गंभीर प्रभावित झाडे काढून टाका", "उपलब्ध असताना प्रतिरोधी जाती वापरा", "स्थानिक सर्वेक्षण कीट-व्यवस्थापन पद्धती अनुसरण करा"]
    },

    "disease_management_cotton_fusarium_wilt": {
        "en": ["Use resistant varieties when available", "Maintain good field management", "Remove severely affected plants where practical", "Avoid moving contaminated soil between fields"],
        "te": ["అందుబాటులో ఉన్నప్పుడు నిరోధక రకాలను ఉపయోగించండి", "మంచి ఫీల్డ్ నిర్వహణను నిర్వహించండి", "ఆచరణాత్మకమైనప్పుడు తీవ్రంగా ప్రభావితమైన మొక్కలను తొలగించండి", "కలుషిత నేలను ఫీల్డ్‌ల మధ్య తరలించకుండా �avoid"],
        "hi": ["जब उपलब्ध हो प्रतिरोधी किस्मों का उपयोग करें", "अच्छा खेत प्रबंधन बनाए रखें", "जहां व्यावहारिक हो वहां बुरंग प्रभावित पौधों को हटाएं", "संदूषित मिट्टी को खेतों के बीच ले जाने से बचें"],
        "mr": ["उपलब्ध असताना प्रतिरोधी जाती वापरा", "चांगले शेत व्यवस्थापन राखा", "जेथे शक्य असेल तेथे गंभीर प्रभावित झाडे काढून टाका", "दूषित माती शेतांमध्ये हलविणे टाळा"]
    },

    "disease_management_grape_black_measles": {
        "en": ["Remove affected plant material where practical", "Maintain vineyard sanitation", "Prune and manage vines appropriately", "Follow locally recommended disease-management practices"],
        "te": ["ఆచరణాత్మకమైనప్పుడు ప్రభావిత మొక్క పదార్థాన్ని తొలగించండి", "వైన్‌యార్డ్ శుభ్రతను నిర్వహించండి", "తంత్రాలను తగినవిధంగా छेदన మరియు నిర్వహించండి", "స్థానికంగా సిఫార్సు చేసిన వ్యాధి-నిర్వహణ పద్ధతులను అనుసరించండి"],
        "hi": ["जहां व्यावहारिक हो वहां प्रभावित पौधे की सामग्री को हटाएं", "अंगूर बाग की स्वच्छता बनाए रखें", "बेलों को उचित रूप से छंदित और प्रबंधित करें", "स्थानीय रूप से अनुशंसित रोग-प्रबंधन प्रथाओं का पालन करें"],
        "mr": ["जेथे शक्य असेल तेथे प्रभावित झाड सामग्री काढून टाका", "द्राक्षावgarden शुद्धता राखा", "बेलांची योग्य तरीकेने छाटणी करा आणि व्यवस्थापित करा", "स्थानिकदृष्ट्या शिफारस केलेल्या रोग-व्यवस्थापन पद्धती अनुसरण करा"]
    },

    "disease_management_grape_black_rot": {
        "en": ["Remove infected fruit and plant debris", "Improve canopy airflow", "Monitor vines regularly", "Use appropriate fungicide management when recommended"],
        "te": ["అంటు చేసిన పండు మరియు మొక్క క్షీణతను తొలగించండి", "కేనపీ airflowను మెరుగుపరచండి", "తంత్రాలను నియమితంగా పర్యవేక్షించండి", "సిఫార్సు చేసినప్పుడు సరిపడే fungicide నిర్వహణను ఉపయోగించండి"],
        "hi": ["संक्रमित फल और पौधे के अवशेषों को हटाएं", "छत के हवा के प्रवाह में सुधार करें", "नियमित रूप से बेलों की निगरानी करें", "जब अनुशंसित हो तब उचित कवकनाशी प्रबंधन का उपयोग करें"],
        "mr": ["संक्रमित फळ आणि झाड अवशेष काढून टाका", "कॅनोपी हवा प्रवाह सुधारा", "नियमितपणे बेलांचे निरीक्षण करा", "शिफारस केल्यावर योग्य बुरशीनाशक वापरा"]
    },

    "disease_management_grape_isariopsis": {
        "en": ["Remove severely affected leaves where practical", "Maintain vineyard sanitation", "Improve canopy airflow", "Use appropriate fungicide management when recommended"],
        "te": ["ఆచరణాత్మకమైనప్పుడు తీవ్రంగా ప్రభావితమైన ఆకులను తొలగించండి", "వైన్‌యార్డ్ శుభ్రతను నిర్వహించండి", "కేనపీ airflowను మెరుగుపరచండి", "సిఫార్సు చేసినప్పుడు సరిపడే fungicide నిర్వహణను ఉపయోగించండి"],
        "hi": ["जहां व्यावहारिक हो वहां बुरंग प्रभावित पत्तियों को हटाएं", "अंगूर बाग की स्वच्छता बनाए रखें", "छत के हवा के प्रवाह में सुधार करें", "जब अनुशंसित हो तब उचित कवकनाशी प्रबंधन का उपयोग करें"],
        "mr": ["जेथे शक्य असेल तेथे गंभीर प्रभावित पाने काढून टाका", "द्राक्षावgarden शुद्धता राखा", "कॅनोपी हवा प्रवाह सुधारा", "शिफारस केल्यावर योग्य बुरशीनाशक वापरा"]
    },

    "disease_management_mango_anthracnose": {
        "en": ["Remove infected plant material where practical", "Maintain good orchard sanitation", "Improve canopy airflow", "Use appropriate fungicide management when recommended"],
        "te": ["ఆచరణాత్మకమైనప్పుడు అంటు చేసిన మొక్క పదార్థాన్ని తొలగించండి", "మంచి ఆర్చర్డ్ శుభ్రతను నిర్వహించండి", "కేనపీ airflowను మెరుగుపరచండి", "సిఫార్సు చేసినప్పుడు సరిపడే fungicide నిర్వహణను ఉపయోగించండి"],
        "hi": ["जहां व्यावहारिक हो वहां संक्रमित पौधे की सामग्री को हटाएं", "अच्छे बाग की स्वच्छता बनाए रखें", "छत के हवा के प्रवाह में सुधार करें", "जब अनुशंसित हो तब उचित कवकनाशी प्रबंधन का उपयोग करें"],
        "mr": ["जेथे शक्य असेल तेथे संक्रमित झाड सामग्री काढून टाका", "चांगले बागेची स्वच्छता राखा", "कॅनोपी हवा प्रवाह सुधारा", "शिफारस केल्यावर योग्य बुरशीनाशक वापरा"]
    },

    "disease_management_mango_bacterial_canker": {
        "en": ["Remove severely infected plant parts where practical", "Maintain orchard sanitation", "Avoid unnecessary plant injuries", "Follow locally recommended management practices"],
        "te": ["ఆచరణాత్మకమైనప్పుడు తీవ్రంగా అంటు చేసిన మొక్క భాగాలను తొలగించండి", "ఆర్చర్డ్ శుభ్రతను నిర్వహించండి", "అనవసరమైన మొక్క గాయాలను avoid", "స్థానికంగా సిఫార్సు చేసిన నిర్వహణ పద్ధతులను అనుసరించండి"],
        "hi": ["जहां व्यावहारिक हो वहां बुरंग संक्रमित पौधों के भागों को हटाएं", "बाग की स्वच्छता बनाए रखें", "अनावश्यक पौधे की चोटों से बचें", "स्थानीय रूप से अनुशंसित प्रबंधन प्रथाओं का पालन करें"],
        "mr": ["जेथे शक्य असेल तेथे गंभीर संक्रमित झाड भाग काढून टाका", "बागेची स्वच्छता राखा", "आवश्यक नसताना झाडांच्या जखमा टाळा", "स्थानिकदृष्ट्या शिफारस केलेल्या व्यवस्थापन पद्धती अनुसरण करा"]
    },

    "disease_management_mango_powdery_mildew": {
        "en": ["Monitor flowering and young growth", "Improve canopy airflow", "Remove severely affected material where practical", "Use recommended fungicide management when appropriate"],
        "te": ["పూలు మరియు యువ పెరుగుదలను పర్యవేక్షించండి", "కేనపీ airflowను మెరుగుపరచండి", "ఆచరణాత్మకమైనప్పుడు తీవ్రంగా ప్రభావితమైన పదార్థాన్ని తొలగించండి", "ఉచితమైనప్పుడు సిఫార్సు చేసిన fungicide నిర్వహణను ఉపయోగించండి"],
        "hi": ["फूल और युवा विकास की निगरानी करें", "छत के हवा के प्रवाह में सुधार करें", "जहां व्यावहारिक हो वहां बुरंग प्रभावित सामग्री को हटाएं", "जब उचित हो तब अनुशंसित कवकनाशी प्रबंधन का उपयोग करें"],
        "mr": ["फुले आणि तरुण वाढीचे निरीक्षण करा", "कॅनोपी हवा प्रवाह सुधारा", "जेथे शक्य असेल तेथे गंभीर प्रभावित सामग्री काढून टाका", "योग्य असताना शिफारस केलेल्या बुरशीनाशक वापरा"]
    },

    "disease_management_paddy_bacterial_leaf_blight": {
        "en": ["Use resistant varieties when available", "Maintain balanced nitrogen management", "Avoid excessive irrigation practices", "Follow locally recommended bacterial disease management"],
        "te": ["అందుబాటులో ఉన్నప్పుడు నిరోధక రకాలను ఉపయోగించండి", "సమతుల్య నైట్రోజన్ నిర్వహణను నిర్వహించండి", "అతిసారమైన నీటిపారుదల పద్ధతులను avoid", "స్థానికంగా సిఫార్సు చేసిన బ్యాక్టీరియల్ వ్యాధి నిర్వహణను అనుసరించండి"],
        "hi": ["जब उपलब्ध हो प्रतिरोधी किस्मों का उपयोग करें", "संतुलित नाइट्रोजन प्रबंधन बनाए रखें", "अत्यधिक सिंचाई प्रथाओं से बचें", "स्थानीय रूप से अनुशंसित जीवाणु रोग प्रबंधन का पालन करें"],
        "mr": ["उपलब्ध असताना प्रतिरोधी जाती वापरा", "संतुलित नायट्रोजन व्यवस्थापन राखा", "जास्त सिंचाई टाळा", "स्थानिकदृष्ट्या शिफारस केलेल्या जीवाणूजन्य रोग व्यवस्थापन अनुसरण करा"]
    },

    "disease_management_paddy_brown_spot": {
        "en": ["Maintain balanced plant nutrition", "Avoid plant stress where possible", "Use healthy seed", "Use appropriate fungicide management when recommended"],
        "te": ["సమతుల్య మొక్క పోషణను నిర్వహించండి", "ఏకఃన ఆశించినప్పుడు మొక్క ఒత్తిడిని avoid", "ఆరోగ్యకరమైన విత్తనాలను ఉపయోగించండి", "సిఫార్సు చేసినప్పుడు సరిపడే fungicide నిర్వహణను ఉపయోగించండి"],
        "hi": ["संतुलित पौध पोषण बनाए रखें", "जहां संभव हो पौधे के तनाव से बचें", "स्वस्थ बीज का उपयोग करें", "जब अनुशंसित हो तब उचित कवकनाशी प्रबंधन का उपयोग करें"],
        "mr": ["संतुलित झाड पोषण राखा", "जेथे शक्य तेथे झाड तणाव टाळा", "आरोग्यपूर्ण बियाणे वापरा", "शिफारस केल्यावर योग्य बुरशीनाशक वापरा"]
    },

    "disease_management_paddy_leaf_blast": {
        "en": ["Use resistant varieties when available", "Avoid excessive nitrogen application", "Maintain balanced crop nutrition", "Use recommended fungicide management when appropriate"],
        "te": ["అందుబాటులో ఉన్నప్పుడు నిరోధక రకాలను ఉపయోగించండి", "అతిసారమైన నైట్రోజన్ అప్లికేషన్ avoid", "సమతుల్య పంట పోషణను నిర్వహించండి", "ఉచితమైనప్పుడు సిఫార్సు చేసిన fungicide నిర్వహణను ఉపయోగించండి"],
        "hi": ["जब उपलब्ध हो प्रतिरोधी किस्मों का उपयोग करें", "अत्यधिक नाइट्रोजन के प्रयोग से बचें", "संतुलित फसल पोषण बनाए रखें", "जब उचित हो तब अनुशंसित कवकनाशी प्रबंधन का उपयोग करें"],
        "mr": ["उपलब्ध असताना प्रतिरोधी जाती वापरा", "जास्त नायट्रोजन खत टाळा", "संतुलित पीक पोषण राखा", "योग्य असताना शिफारस केलेल्या बुरशीनाशक वापरा"]
    },

    "disease_management_potato_early_blight": {
        "en": ["Remove severely affected foliage where practical", "Maintain good field sanitation", "Avoid prolonged leaf wetness", "Use appropriate fungicide management when recommended"],
        "te": ["ఆచరణాత్మకమైనప్పుడు తీవ్రంగా ప్రభావితమైన ఆకులను తొలగించండి", "మంచి ఫీల్డ్ శుభ్రతను నిర్వహించండి", "ఆకు తడిని పొడిగి ఉండకుండా తగ్గించండి", "సిఫార్సు చేసినప్పుడు సరిపడే fungicide నిర్వహణను ఉపయోగించండి"],
        "hi": ["जहां व्यावहारिक हो वहां बुरंग प्रभावित पत्तियों को हटाएं", "अच्छी खेत स्वच्छता बनाए रखें", "पत्ती के लंबे समय तक गीला रहने से बचें", "जब अनुशंसित हो तब उचित कवकनाशी प्रबंधन का उपयोग करें"],
        "mr": ["जेथे शक्य असेल तेथे गंभीर प्रभावित पाने काढून टाका", "चांगली शेत स्वच्छता राखा", "पानांचा दीर्घकाळ ओला राहणा टाळा", "शिफारस केल्यावर योग्य बुरशीनाशक वापरा"]
    },

    "disease_management_potato_late_blight": {
        "en": ["Monitor fields closely during cool and wet conditions", "Remove or manage infected plant material appropriately", "Use resistant varieties where available", "Follow recommended fungicide programs"],
        "te": ["చలి మరియు తడి పరిస్థితులలో ఫీల్డ్‌లను గట్టిగా పర్యవేక్షించండి", "అంటు చేసిన మొక్క పదార్థాన్ని సరిగ్గా తొలగించండి లేదా నిర్వహించండి", "అందుబాటులో ఉన్నప్పుడు నిరోధక రకాలను ఉపయోగించండి", "సిఫార్సు చేసిన fungicide కార్యక్రమాలను అనుసరించండి"],
        "hi": ["ठंडी और गीली परिस्थितियों के दौरान खेतों की बारीकी से निगरानी करें", "संक्रमित पौधे की सामग्री को उचित रूप से हटाएं या प्रबंधित करें", "जहां उपलब्ध हो प्रतिरोधी किस्मों का उपयोग करें", "अनुशंसित कवकनाशी कार्यक्रमों का पालन करें"],
        "mr": ["थंड आणि ओल्या परिस्थितींमध्ये शेतांचे जवळून निरीक्षण करा", "संक्रमित झाड सामग्री योग्यरित्या काढून टाका किंवा व्यवस्थापित करा", "उपलब्ध असताना प्रतिरोधी जाती वापरा", "शिफारस केलेल्या बुरशीनाशक कार्यक्रम अनुसरण करा"]
    },

    "disease_management_soybean_caterpillar": {
        "en": ["Inspect plants for caterpillars and feeding damage", "Monitor pest population levels", "Use integrated pest-management practices", "Use appropriate control measures when economic thresholds are reached"],
        "te": ["గొంగళి పురుగులు మరియు తినడం గాయం కోసం మొక్కలను inspect", "పిత్త పరమైన జనాభా స్థాయిలను పర్యవేక్షించండి", "Интегрированная pest-నిర్వహణ పద్ధతులను ఉపయోగించండి", "ఆర్థిక thresholds చేరుకున్నప్పుడు సరిపడే నియంత్రణ చర్యలను ఉపయోగించండి"],
        "hi": ["सुंडियों और खिलाने की क्षति के लिए पौधों की जांच करें", "कीट आबादी के स्तर की निगरानी करें", "एकीकृत कीट-प्रबंधन प्रथाओं का उपयोग करें", "जब आर्थिक सीमाएं पूरी हो जाएं तब उचित नियंत्रण उपायों का उपयोग करें"],
        "mr": ["अळ्या आणि खाण्याच्या नुकसानीसाठी झाडांची तपासणी करा", "किट लोकसंख्या पातळीचे निरीक्षण करा", "एकीकृत कीट-व्यवस्थापन पद्धती वापरा", "आर्थिक मर्यादा गाठल्या गेल्या असताना योग्य नियंत्रण उपाय वापरा"]
    },

    "disease_management_soybean_diabrotica": {
        "en": ["Scout plants for beetles and feeding damage", "Monitor pest populations", "Use integrated pest-management practices", "Use locally recommended control measures when necessary"],
        "te": ["బీటిల్‌లు మరియు తినడం గాయం కోసం మొక్కలను scout", "పిత్త పరమైన జనాభాపర్యవేక్షణ", "Интегрированная pest-నిర్వహణ పద్ధతులను ఉపయోగించండి", "అవసరమైనప్పుడు స్థానికంగా సిఫార్సు చేసిన నియంత్రణ చర్యలను ఉపయోగించండి"],
        "hi": ["भृंगों और खिलाने की क्षति के लिए पौधों की टोह लें", "कीट आबादी की निगरानी करें", "एकीकृत कीट-प्रबंधन प्रथाओं का उपयोग करें", "जब आवश्यक हो तब स्थानीय रूप से अनुशंसित नियंत्रण उपायों का उपयोग करें"],
        "mr": ["भुंगे आणि खाण्याच्या नुकसानीसाठी झाडांची टोह घ्या", "किट लोकसंख्येचे निरीक्षण करा", "एकीकृत कीट-व्यवस्थापन पद्धती वापरा", "आवश्यक असताना स्थानिक शिफारस केलेल्या नियंत्रण उपाय वापरा"]
    },

    "disease_management_tomato_bacterial_spot": {
        "en": ["Use healthy seed and transplants", "Remove severely affected plant material where practical", "Avoid unnecessary handling of wet plants", "Follow locally recommended disease-management practices"],
        "te": ["ఆరోగ్యకరమైన విత్తనాలు మరియు అంటుకోలును ఉపయోగించండి", "ఆచరణాత్మకమైనప్పుడు తీవ్రంగా ప్రభావితమైన మొక్క పదార్థాన్ని తొలగించండి", "తడి మొక్కలను అనవసరంగా handle గాకుండా ఉండండి", "స్థానికంగా సిఫార్సు చేసిన వ్యాధి-నిర్వహణ పద్ధతులను అనుసరించండి"],
        "hi": ["स्वस्थ बीज और पौधों का उपयोग करें", "जहां व्यावहारिक हो वहां बुरंग प्रभावित पौधे की सामग्री को हटाएं", "गीले पौधों के अनावश्यक हैंडलिंग से बचें", "स्थानीय रूप से अनुशंसित रोग-प्रबंधन प्रथाओं का पालन करें"],
        "mr": ["आरोग्यपूर्ण बियाणे आणि रोपे वापरा", "जेथे शक्य असेल तेथे गंभीर प्रभावित झाड सामग्री काढून टाका", "ओल्या झाडांचे अनावश्यक हाताळणे टाळा", "स्थानिकदृष्ट्या शिफारस केलेल्या रोग-व्यवस्थापन पद्धती अनुसरण करा"]
    },

    "disease_management_tomato_early_blight": {
        "en": ["Remove severely affected leaves", "Maintain good airflow", "Avoid prolonged leaf wetness", "Use appropriate fungicide management when recommended"],
        "te": ["తీవ్రంగా ప్రభావితమైన ఆకులను తొలగించండి", "మంచి airflowను నిర్వహించండి", "ఆకు తడిని పొడిగి ఉండకుండా తగ్గించండి", "సిఫార్సు చేసినప్పుడు సరిపడే fungicide నిర్వహణను ఉపయోగించండి"],
        "hi": ["बुरंग प्रभावित पत्तियों को हटाएं", "अच्छा हवा का प्रवाह बनाए रखें", "पत्ती के लंबे समय तक गीला रहने से बचें", "जब अनुशंसित हो तब उचित कवकनाशी प्रबंधन का उपयोग करें"],
        "mr": ["गंभीर प्रभावित पाने काढून टाका", "चांगला हवा प्रवाह राखा", "पानांचा दीर्घकाळ ओला राहणा टाळा", "शिफारस केल्यावर योग्य बुरशीनाशक वापरा"]
    },

    "disease_management_tomato_late_blight": {
        "en": ["Monitor plants closely during cool and wet conditions", "Remove severely infected material where practical", "Improve airflow", "Use recommended fungicide management when appropriate"],
        "te": ["చలి మరియు తడి పరిస్థితులలో మొక్కలను గట్టిగా పర్యవేక్షించండి", "ఆచరణాత్మకమైనప్పుడు తీవ్రంగా అంటు చేసిన పదార్థాన్ని తొలగించండి", "airflowను మెరుగుపరచండి", "ఉచితమైనప్పుడు సిఫార్సు చేసిన fungicide నిర్వహణను ఉపయోగించండి"],
        "hi": ["ठंडी और गीली परिस्थितियों के दौरान पौधों की बारीकी से निगरानी करें", "जहां व्यावहारिक हो वहां बुरंग संक्रमित सामग्री को हटाएं", "हवा के प्रवाह में सुधार करें", "जब उचित हो तब अनुशंसित कवकनाशी प्रबंधन का उपयोग करें"],
        "mr": ["थंड आणि ओल्या परिस्थितींमध्ये झाडांचे जवळून निरीक्षण करा", "जेथे शक्य असेल तेथे गंभीर संक्रमित सामग्री काढून टाका", "हवा प्रवाह सुधारा", "योग्य असताना शिफारस केलेल्या बुरशीनाशक वापरा"]
    },

    "disease_management_wheat_mildew": {
        "en": ["Use resistant varieties when available", "Avoid excessive nitrogen application", "Monitor fields regularly", "Use appropriate fungicide management when recommended"],
        "te": ["అందుబాటులో ఉన్నప్పుడు నిరోధక రకాలను ఉపయోగించండి", "అతిసారమైన నైట్రోజన్ అప్లికేషన్ avoid", "నియమితంగా ఫీల్డ్‌లను పర్యవేక్షించండి", "సిఫార్సు చేసినప్పుడు సరిపడే fungicide నిర్వహణను ఉపయోగించండి"],
        "hi": ["जब उपलब्ध हो प्रतिरोधी किस्मों का उपयोग करें", "अत्यधिक नाइट्रोजन के प्रयोग से बचें", "नियमित रूप से खेतों की निगरानी करें", "जब अनुशंसित हो तब उचित कवकनाशी प्रबंधन का उपयोग करें"],
        "mr": ["उपलब्ध असताना प्रतिरोधी जाती वापरा", "जास्त नायट्रोजन खत टाळा", "नियमितपणे शेतांचे निरीक्षण करा", "शिफारस केल्यावर योग्य बुरशीनाशक वापरा"]
    },

    "disease_management_wheat_septoria": {
        "en": ["Use resistant varieties where available", "Monitor disease development", "Manage crop residue appropriately", "Use fungicides when recommended"],
        "te": ["అందుబాటులో ఉన్నప్పుడు నిరోధక రకాలను ఉపయోగించండి", "వ్యాధి అభివృద్ధిని పర్యవేక్షించండి", "పంట అవశేషాన్ని సరిగ్గా నిర్వహించండి", "సిఫార్సు చేసినప్పుడు fungicidesను ఉపయోగించండి"],
        "hi": ["जहां उपलब्ध हो प्रतिरोधी किस्मों का उपयोग करें", "रोग विकास की निगरानी करें", "फसल अवशेषों को उचित रूप से प्रबंधित करें", "जब अनुशंसित हो तब कवकनाशी का उपयोग करें"],
        "mr": ["उपलब्ध असताना प्रतिरोधी जाती वापरा", "रोग विकासाचे निरीक्षण करा", "पीक अवशेष योग्यरित्या व्यवस्थापित करा", "शिफारस केल्यावर बुरशीनाशक वापरा"]
    },

    "disease_management_wheat_yellowrust": {
        "en": ["Use resistant varieties when available", "Monitor crops regularly", "Apply recommended fungicide management when appropriate", "Follow local disease forecasting where available"],
        "te": ["అందుబాటులో ఉన్నప్పుడు నిరోధక రకాలను ఉపయోగించండి", "నియమితంగా పంటలను పర్యవేక్షించండి", "ఉచితమైనప్పుడు సిఫార్సు చేసిన fungicide నిర్వహణను వర్తింపజేయండి", "అందుబాటులో ఉన్నప్పుడు స్థానిక వ్యాధి पूर्वानुमान అనుసరించండి"],
        "hi": ["जब उपलब्ध हो प्रतिरोधी किस्मों का उपयोग करें", "नियमित रूप से फसलों की निगरानी करें", "जब उचित हो तब अनुशंसित कवकनाशी प्रबंधन लागू करें", "जहां उपलब्ध हो वहां स्थानीय रोग पूर्वानुमान का पालन करें"],
        "mr": ["उपलब्ध असताना प्रतिरोधी जाती वापरा", "नियमितपणे पिकांचे निरीक्षण करा", "योग्य असताना शिफारस केलेल्या बुरशीनाशक व्यवस्थापन लागू करा", "उपलब्ध असताना स्थानिक रोग अंदाज अनुसरण करा"]
    },

    # -------------------------------------------------
    # DISEASE LIBRARY — PREVENTION (as dict of lists)
    # -------------------------------------------------

    "disease_prevention_banana_cordana": {
        "en": ["Monitor leaves regularly", "Remove infected plant debris", "Avoid prolonged leaf wetness", "Use healthy planting material"],
        "te": ["ఆకులను నియమితంగా పర్యవేక్షించండి", "అంటు చేసిన మొక్క క్షీణతను తొలగించండి", "ఆకు తడిని పొడిగి ఉండకుండా avoid", "ఆరోగ్యకరమైన నాటడం పదార్థాన్ని ఉపయోగించండి"],
        "hi": ["नियमित रूप से पत्तियों की निगरानी करें", "संक्रमित पौधे के अवशेषों को हटाएं", "पत्ती के लंबे समय तक गीला रहने से बचें", "स्वस्थ रोपण सामग्री का उपयोग करें"],
        "mr": ["नियमितपणे पानांचे निरीक्षण करा", "संक्रमित झाड अवशेष काढून टाका", "पानांचा दीर्घकाळ ओला राहणा टाळा", "आरोग्यपूर्ण लागवड सामग्री वापरा"]
    },

    "disease_prevention_banana_pestalotiopsis": {
        "en": ["Monitor leaves frequently", "Remove infected plant debris", "Maintain good airflow", "Use healthy planting material"],
        "te": ["ఆకులను తరచుగా పర్యవేక్షించండి", "అంటు చేసిన మొక్క క్షీణతను తొలగించండి", "మంచి airflowను నిర్వహించండి", "ఆరోగ్యకరమైన నాటడం పదార్థాన్ని ఉపయోగించండి"],
        "hi": ["बार-बार पत्तियों की निगरानी करें", "संक्रमित पौधे के अवशेषों को हटाएं", "अच्छा हवा का प्रवाह बनाए रखें", "स्वस्थ रोपण सामग्री का उपयोग करें"],
        "mr": ["वारंवार पानांचे निरीक्षण करा", "संक्रमित झाड अवशेष काढून टाका", "चांगला हवा प्रवाह राखा", "आरोग्यपूर्ण लागवड सामग्री वापरा"]
    },

    "disease_prevention_banana_sigatoka": {
        "en": ["Regularly inspect leaves", "Remove infected debris", "Avoid excessive leaf wetness", "Use suitable disease-management practices"],
        "te": ["ఆకులను నియమితంగా inspect", "అంటు చేసిన debrisను తొలగించండి", "అతిసారమైన ఆకు తడిని avoid", "సరిపడే వ్యాధి-నిర్వహణ పద్ధతులను ఉపయోగించండి"],
        "hi": ["नियमित रूप से पत्तियों की जांच करें", "संक्रमित अवशेषों को हटाएं", "अत्यधिक पत्ती गीलेपन से बचें", "उचित रोग-प्रबंधन प्रथाओं का उपयोग करें"],
        "mr": ["नियमितपणे पानांची तपासणी करा", "संक्रमित अवशेष काढून टाका", "जास्त पानांचा ओलेपणा टाळा", "योग्य रोग-व्यवस्थापन पद्धती वापरा"]
    },

    "disease_prevention_corn_common_rust": {
        "en": ["Plant resistant hybrids", "Monitor plants during favorable disease conditions", "Maintain healthy crop growth"],
        "te": ["నిరోధక హైబ్రిడ్‌లను నాటండి", "అనుకూలమైన వ్యాధి పరిస్థితులలో మొక్కలను పర్యవేక్షించండి", "ఆరోగ్యకరమైన పంట పెరుగుదలను నిర్వహించండి"],
        "hi": ["प्रतिरोधी संकर रोपें", "अनुकूल रोग परिस्थितियों के दौरान पौधों की निगरानी करें", "स्वस्थ फसल विकास बनाए रखें"],
        "mr": ["प्रतिरोधी संकर लावा", "अनुकूल रोग परिस्थितींदरम्यान झाडांचे निरीक्षण करा", "आरोग्यपूर्ण पीक वाढ राखा"]
    },

    "disease_prevention_corn_gray_leaf_spot": {
        "en": ["Use resistant varieties", "Practice suitable crop rotation", "Monitor fields regularly"],
        "te": ["నిరోధక రకాలను ఉపయోగించండి", "సరిపడే పంట పర్యాయ నిర్వహణను practice", "నియమితంగా ఫీల్డ్‌లను పర్యవేక్షించండి"],
        "hi": ["प्रतिरोधी किस्मों का उपयोग करें", "उचित फसल चक्र का अभ्यास करें", "नियमित रूप से खेतों की निगरानी करें"],
        "mr": ["प्रतिरोधी जाती वापरा", "योग्य पीक आवर्तन सराव करा", "नियमितपणे शेतांचे निरीक्षण करा"]
    },

    "disease_prevention_corn_northern_leaf_blight": {
        "en": ["Plant resistant hybrids", "Use appropriate crop rotation", "Maintain field sanitation"],
        "te": ["నిరోధక హైబ్రిడ్‌లను నాటండి", "సరిపడే పంట పర్యాయ నిర్వహణను ఉపయోగించండి", "ఫీల్డ్ శుభ్రతను నిర్వహించండి"],
        "hi": ["प्रतिरोधी संकर रोपें", "उचित फसल चक्र का उपयोग करें", "खेत स्वच्छता बनाए रखें"],
        "mr": ["प्रतिरोधी संकर लावा", "योग्य पीक आवर्तन वापरा", "शेताची स्वच्छता राखा"]
    },

    "disease_prevention_cotton_bacterial_blight": {
        "en": ["Use certified healthy seed", "Maintain field sanitation", "Avoid unnecessary leaf wetness", "Monitor plants regularly"],
        "te": ["ధృవీకరించబడిన ఆరోగ్యకరమైన విత్తనాలను ఉపయోగించండి", "ఫీల్డ్ శుభ్రతను నిర్వహించండి", "అనవసరమైన ఆకు తడిని avoid", "మొక్కలను నియమితంగా పర్యవేక్షించండి"],
        "hi": ["प्रमाणित स्वस्थ बीज का उपयोग करें", "खेत स्वच्छता बनाए रखें", "अनावश्यक पत्ती गीलेपन से बचें", "नियमित रूप से पौधों की निगरानी करें"],
        "mr": ["प्रमाणित आरोग्यपूर्ण बियाणे वापरा", "शेताची स्वच्छता राखा", "अनावश्यक पानांचा ओलेपणा टाळा", "नियमितपणे झाडांचे निरीक्षण करा"]
    },

    "disease_prevention_cotton_leaf_curl": {
        "en": ["Use healthy planting material", "Control disease vectors according to local recommendations", "Remove volunteer cotton plants", "Monitor fields regularly"],
        "te": ["ఆరోగ్యకరమైన నాటడం పదార్థాన్ని ఉపయోగించండి", "స్థానిక సిఫార్సుల ప్రకారం వ్యాధి వెక్టర్లను నియంత్రించండి", "స్వచ్ఛంద కాటన్ మొక్కలను remove", "నియమితంగా ఫీల్డ్‌లను పర్యవేక్షించండి"],
        "hi": ["स्वस्थ रोपण सामग्री का उपयोग करें", "स्थानीय अनुशंसाओं के अनुसार रोग वाहकों को नियंत्रित करें", "स्वयंसेवी कपास के पौधों को हटाएं", "नियमित रूप से खेतों की निगरानी करें"],
        "mr": ["आरोग्यपूर्ण लागवड सामग्री वापरा", "स्थानिक शिफारसीनुसार रोग वाहकांचे नियंत्रण करा", "स्वयंसेवी कापूस झाडे काढून टाका", "नियमितपणे शेतांचे निरीक्षण करा"]
    },

    "disease_prevention_cotton_fusarium_wilt": {
        "en": ["Use disease-free planting material", "Use resistant varieties", "Maintain field sanitation", "Practice suitable crop rotation"],
        "te": ["వ్యాధి-శూన్య నాటడం పదార్థాన్ని ఉపయోగించండి", "నిరోధక రకాలను ఉపయోగించండి", "ఫీల్డ్ శుభ్రతను నిర్వహించండి", "సరిపడే పంట crop rotationను practice"],
        "hi": ["रोग-मुक्त रोपण सामग्री का उपयोग करें", "प्रतिरोधी किस्मों का उपयोग करें", "खेत स्वच्छता बनाए रखें", "उचित फसल चक्र का अभ्यास करें"],
        "mr": ["रोग-मुक्त लागवड सामग्री वापरा", "प्रतिरोधी जाती वापरा", "शेताची स्वच्छता राखा", "योग्य पीक आवर्तन सराव करा"]
    },

    "disease_prevention_grape_black_measles": {
        "en": ["Maintain good vineyard sanitation", "Monitor vines regularly", "Remove diseased plant material", "Use healthy planting material"],
        "te": ["మంచి వైన్‌యార్డ్ శుభ్రతను నిర్వహించండి", "తంత్రాలను నియమితంగా పర్యవేక్షించండి", "వ్యాధి గ్రస్త మొక్క పదార్థాన్ని remove", "ఆరోగ్యకరమైన నాటడం పదార్థాన్ని ఉపయోగించండి"],
        "hi": ["अच्छी अंगूर बाग की स्वच्छता बनाए रखें", "नियमित रूप से बेलों की निगरानी करें", "रोगग्रस्त पौधे की सामग्री को हटाएं", "स्वस्थ रोपण सामग्री का उपयोग करें"],
        "mr": ["चांगली द्राक्षावgarden शुद्धता राखा", "नियमितपणे बेलांचे निरीक्षण करा", "रोगग्रस्त झाड सामग्री काढून टाका", "आरोग्यपूर्ण लागवड सामग्री वापरा"]
    },

    "disease_prevention_grape_black_rot": {
        "en": ["Maintain vineyard sanitation", "Remove mummified fruit", "Improve airflow through canopy management", "Monitor during favorable weather"],
        "te": ["వైన్‌యార్డ్ శుభ్రతను నిర్వహించండి", "mummified fruitను remove", "కేనపీ నిర్వహణ through airflowను improve", "అనుకూలమైన వాతావరణంలో నియమితంగా అనుసరించండి"],
        "hi": ["अंगूर बाग स्वच्छता बनाए रखें", "ममीकृत फलों को हटाएं", "छत प्रबंधन के माध्यम से हवा के प्रवाह में सुधार करें", "अनुकूल मौसम के दौरान निगरानी करें"],
        "mr": ["द्राक्षावgarden शुद्धता राखा", "ममी झालेली फळे काढून टाका", "कॅनोपी व्यवस्थापनाद्वारे हवा प्रवाह सुधारा", "अनुकूल हवामानात निरीक्षण करा"]
    },

    "disease_prevention_grape_isariopsis": {
        "en": ["Monitor leaves regularly", "Remove infected plant debris", "Maintain good airflow", "Avoid prolonged leaf wetness"],
        "te": ["ఆకులను నియమితంగా పర్యవేక్షించండి", "అంటు చేసిన మొక్క క్షీణతను remove", "మంచి airflowను maintain", "ఆకు తడిని prolonged avoid"],
        "hi": ["नियमित रूप से पत्तियों की निगरानी करें", "संक्रमित पौधे के अवशेषों को हटाएं", "अच्छा हवा का प्रवाह बनाए रखें", "पत्ती के लंबे समय तक गीला रहने से बचें"],
        "mr": ["नियमितपणे पानांचे निरीक्षण करा", "संक्रमित झाड अवशेष काढून टाका", "चांगला हवा प्रवाह राखा", "पानांचा दीर्घकाळ ओला राहणा टाळा"]
    },

    "disease_prevention_mango_anthracnose": {
        "en": ["Remove infected debris", "Maintain good canopy management", "Monitor during humid or wet conditions", "Use healthy planting material"],
        "te": ["అంటు చేసిన debrisను remove", "మంచి canopy నిర్వహణను maintain", "ఆర్ద్ర లేదా తడి పరిస్థితులలో monitor", "ఆరోగ్యకరమైన నాటడం పదార్థాన్ని ఉపయోగించండి"],
        "hi": ["संक्रमित अवशेषों को हटाएं", "अच्छा छत प्रबंधन बनाए रखें", "आर्द्र या गीली परिस्थितियों के दौरान निगरानी करें", "स्वस्थ रोपण सामग्री का उपयोग करें"],
        "mr": ["संक्रमित अवशेष काढून टाका", "चांगले कॅनोपी व्यवस्थापन राखा", "ओल्या किंवा ओल्या परिस्थितींमध्ये निरीक्षण करा", "आरोग्यपूर्ण लागवड सामग्री वापरा"]
    },

    "disease_prevention_mango_bacterial_canker": {
        "en": ["Use healthy planting material", "Maintain orchard sanitation", "Monitor plants regularly", "Manage irrigation to avoid prolonged wetness"],
        "te": ["ఆరోగ్యకరమైన నాటడం పదార్థాన్ని ఉపయోగించండి", "ఆర్చర్డ్ శుభ్రతను maintain", "మొక్కలను నియమితంగా monitor", "పొడిగిన తడిని avoid చేయడానికి నీటి పారుదలను manage"],
        "hi": ["स्वस्थ रोपण सामग्री का उपयोग करें", "बाग की स्वच्छता बनाए रखें", "नियमित रूप से पौधों की निगरानी करें", "लंबे समय तक गीलेपन से बचने के लिए सिंचाई का प्रबंधन करें"],
        "mr": ["आरोग्यपूर्ण लागवड सामग्री वापरा", "बागेची स्वच्छता राखा", "नियमितपणे झाडांचे निरीक्षण करा", "दीर्घकाळ ओलेपणा टाळण्यासाठी सिंचाई व्यवस्थापित करा"]
    },

    "disease_prevention_mango_powdery_mildew": {
        "en": ["Maintain good canopy ventilation", "Monitor during favorable weather", "Maintain orchard sanitation"],
        "te": ["మంచి canopy ventilationను maintain", "అనుకూలమైన వాతావరణంలో monitor", "ఆర్చర్డ్ శుభ్రతను maintain"],
        "hi": ["अच्छा छत वेंटिलेशन बनाए रखें", "अनुकूल मौसम के दौरान निगरानी करें", "बाग की स्वच्छता बनाए रखें"],
        "mr": ["चांगला कॅनोपी वेंटिलेशन राखा", "अनुकूल हवामानात निरीक्षण करा", "बागेची स्वच्छता राखा"]
    },

    "disease_prevention_paddy_bacterial_leaf_blight": {
        "en": ["Use healthy seed", "Use resistant varieties", "Maintain field sanitation", "Monitor fields regularly"],
        "te": ["ఆరోగ్యకరమైన seedను ఉపయోగించండి", "నిరోధక రకాలను ఉపయోగించండి", "ఫీల్డ్ శుభ్రతను maintain", "నియమితంగా ఫీల్డ్‌లను monitor"],
        "hi": ["स्वस्थ बीज का उपयोग करें", "प्रतिरोधी किस्मों का उपयोग करें", "खेत स्वच्छता बनाए रखें", "नियमित रूप से खेतों की निगरानी करें"],
        "mr": ["आरोग्यपूर्ण बियाणे वापरा", "प्रतिरोधी जाती वापरा", "शेताची स्वच्छता राखा", "नियमितपणे शेतांचे निरीक्षण करा"]
    },

    "disease_prevention_paddy_brown_spot": {
        "en": ["Use good-quality seed", "Maintain balanced fertilization", "Monitor fields regularly", "Maintain appropriate water management"],
        "te": ["మంచి-నాణ్యత seedను ఉపయోగించండి", "సమతుల్య fertilizationను maintain", "నియమితంగా ఫీల్డ్‌లను monitor", "సరిపడే నీటి నిర్వహణను maintain"],
        "hi": ["अच्छी गुणवत्ता वाले बीज का उपयोग करें", "संतुलित उर्वरकता बनाए रखें", "नियमित रूप से खेतों की निगरानी करें", "उचित जल प्रबंधन बनाए रखें"],
        "mr": ["चांगल्या दर्जाचे बियाणे वापरा", "संतुलित खत व्यवस्थापन राखा", "नियमितपणे शेतांचे निरीक्षण करा", "योग्य पाणी व्यवस्थापन राखा"]
    },

    "disease_prevention_paddy_leaf_blast": {
        "en": ["Use resistant varieties", "Use healthy seed", "Monitor fields regularly", "Maintain balanced fertilization"],
        "te": ["నిరోధక రకాలను ఉపయోగించండి", "ఆరోగ్యకరమైన seedను ఉపయోగించండి", "నియమితంగా ఫీల్డ్‌లను monitor", "సమతుల్య fertilizationను maintain"],
        "hi": ["प्रतिरोधी किस्मों का उपयोग करें", "स्वस्थ बीज का उपयोग करें", "नियमित रूप से खेतों की निगरानी करें", "संतुलित उर्वरकता बनाए रखें"],
        "mr": ["प्रतिरोधी जाती वापरा", "आरोग्यपूर्ण बियाणे वापरा", "नियमितपणे शेतांचे निरीक्षण करा", "संतुलित खत व्यवस्थापन राखा"]
    },

    "disease_prevention_potato_early_blight": {
        "en": ["Use healthy seed tubers", "Practice suitable crop rotation", "Remove infected crop debris", "Monitor plants regularly"],
        "te": ["ఆరోగ్యకరమైన seed tubersను ఉపయోగించండి", "సరిపడే పంట crop rotationను practice", "అంటు చేసిన crop debrisను remove", "మొక్కలను నియమితంగా monitor"],
        "hi": ["स्वस्थ बीज कंदों का उपयोग करें", "उचित फसल चक्र का अभ्यास करें", "संक्रमित फसल अवशेषों को हटाएं", "नियमित रूप से पौधों की निगरानी करें"],
        "mr": ["आरोग्यपूर्ण बियाणे कंद वापरा", "योग्य पीक आवर्तन सराव करा", "संक्रमित पीक अवशेष काढून टाका", "नियमितपणे झाडांचे निरीक्षण करा"]
    },

    "disease_prevention_potato_late_blight": {
        "en": ["Use healthy seed tubers", "Monitor weather and disease risk", "Maintain field sanitation", "Use resistant varieties when available"],
        "te": ["ఆరోగ్యకరమైన seed tubersను ఉపయోగించండి", "వాతావరణం మరియు వ్యాధి riskను monitor", "ఫీల్డ్ శుభ్రతను maintain", "అందుబాటులో ఉన్నప్పుడు నిరోధక రకాలను ఉపయోగించండి"],
        "hi": ["स्वस्थ बीज कंदों का उपयोग करें", "मौसम और रोग जोखिम की निगरानी करें", "खेत स्वच्छता बनाए रखें", "जब उपलब्ध हो प्रतिरोधी किस्मों का उपयोग करें"],
        "mr": ["आरोग्यपूर्ण बियाणे कंद वापरा", "हवामान आणि रोग धोक्याचे निरीक्षण करा", "शेताची स्वच्छता राखा", "उपलब्ध असताना प्रतिरोधी जाती वापरा"]
    },

    "disease_prevention_soybean_caterpillar": {
        "en": ["Scout fields regularly", "Monitor pest populations", "Encourage beneficial insects where appropriate", "Use integrated pest management"],
        "te": ["ఫీల్డ్‌లను తరచుగా scout", "పిత్త populationsను monitor", "ఉచితమైనప్పుడు మేలు చేసే insectsను ప్రోత్సహించండి", "Интегрированная pest managementను ఉపయోగించండి"],
        "hi": ["नियमित रूप से खेतों की टोह लें", "कीट आबादी की निगरानी करें", "जहां उचित हो वहां लाभकारी कीटों को प्रोत्साहित करें", "एकीकृत कीट प्रबंधन का उपयोग करें"],
        "mr": ["नियमितपणे शेतांची टोह घ्या", "किट लोकसंख्येचे निरीक्षण करा", "जेथे योग्य असेल तेथे सुपरिणामकारी कीटांना प्रोत्साहित करा", "एकीकृत कीट व्यवस्थापन वापरा"]
    },

    "disease_prevention_soybean_diabrotica": {
        "en": ["Regular field scouting", "Monitor pest populations", "Maintain healthy crop growth", "Use integrated pest management"],
        "te": ["నియమిత field scouting", "పిత్త populationsను monitor", "ఆరోగ్యకరమైన crop growthను maintain", "Интегрированная pest managementను ఉపయోగించండి"],
        "hi": ["नियमित खेत टोह", "कीट आबादी की निगरानी करें", "स्वस्थ फसल विकास बनाए रखें", "एकीकृत कीट प्रबंधन का उपयोग करें"],
        "mr": ["नियमित शेत टोह", "किट लोकसंख्येचे निरीक्षण करा", "आरोग्यपूर्ण पीक वाढ राखा", "एकीकृत कीट व्यवस्थापन वापरा"]
    },

    "disease_prevention_tomato_bacterial_spot": {
        "en": ["Use disease-free seed", "Maintain field sanitation", "Avoid overhead irrigation where possible", "Monitor plants regularly"],
        "te": ["వ్యాధి-శూన్య seedను ఉపయోగించండి", "ఫీల్డ్ శుభ్రతను maintain", "ఉచితమైనప్పుడు overhead irrigationను avoid", "మొక్కలను నియమితంగా monitor"],
        "hi": ["रोग-मुक्त बीज का उपयोग करें", "खेत स्वच्छता बनाए रखें", "जहां संभव हो वहां ऊंची सिंचाई से बचें", "नियमित रूप से पौधों की निगरानी करें"],
        "mr": ["रोग-मुक्त बियाणे वापरा", "शेताची स्वच्छता राखा", "जेथे शक्य तेथा वरच्या सिंचाई टाळा", "नियमितपणे झाडांचे निरीक्षण करा"]
    },

    "disease_prevention_tomato_early_blight": {
        "en": ["Provide adequate plant spacing", "Remove infected plant debris", "Avoid overhead watering", "Practice suitable crop rotation"],
        "te": ["చరిత్రకమైన plant spacingను provide", "అంటు చేసిన plant debrisను remove", "overhead wateringను avoid", "సరిపడే crop rotationను practice"],
        "hi": ["पर्याप्त पौध दूरी प्रदान करें", "संक्रमित पौधे के अवशेषों को हटाएं", "ऊंची सिंचाई से बचें", "उचित फसल चक्र का अभ्यास करें"],
        "mr": ["पुरेसे झाड अंतर द्या", "संक्रमित झाड अवशेष काढून टाका", "वरची सिंचाई टाळा", "योग्य पीक आवर्तन सराव करा"]
    },

    "disease_prevention_tomato_late_blight": {
        "en": ["Avoid prolonged leaf wetness", "Use healthy planting material", "Monitor weather conditions", "Maintain good field sanitation"],
        "te": ["prolonged ఆకు తడిని avoid", "ఆరోగ్యకరమైన planting materialను ఉపయోగించండి", "వాతావరణం conditionsను monitor", "మంచి field sanitationను maintain"],
        "hi": ["पत्ती के लंबे समय तक गीला रहने से बचें", "स्वस्थ रोपण सामग्री का उपयोग करें", "मौसम की स्थिति की निगरानी करें", "अच्छी खेत स्वच्छता बनाए रखें"],
        "mr": ["पानांचा दीर्घकाळ ओला राहणा टाळा", "आरोग्यपूर्ण लागवड सामग्री वापरा", "हवामान परिस्थितींचे निरीक्षण करा", "चांगली शेत स्वच्छता राखा"]
    },

    "disease_prevention_wheat_mildew": {
        "en": ["Use resistant varieties", "Maintain balanced crop nutrition", "Monitor crops regularly", "Avoid excessive plant density where applicable"],
        "te": ["నిరోధక రకాలను ఉపయోగించండి", "సమతుల్య crop nutritionను maintain", "నియమితంగా cropsను monitor", "అనుకూలమైనప్పుడు అతిసారమైన plant densityను avoid"],
        "hi": ["प्रतिरोधी किस्मों का उपयोग करें", "संतुलित फसल पोषण बनाए रखें", "नियमित रूप से फसलों की निगरानी करें", "जहां लागू हो वहां अत्यधिक पौध घनत्व से बचें"],
        "mr": ["प्रतिरोधी जाती वापरा", "संतुलित पीक पोषण राखा", "नियमितपणे पिकांचे निरीक्षण करा", "जेथे लागू असेल तेथे जास्त झाड घनता टाळा"]
    },

    "disease_prevention_wheat_septoria": {
        "en": ["Use healthy seed", "Practice suitable crop rotation", "Maintain field sanitation", "Monitor crops regularly"],
        "te": ["ఆరోగ్యకరమైన seedను ఉపయోగించండి", "సరిపడే crop rotationను practice", "ఫీల్డ్ శుభ్రతను maintain", "నియమితంగా cropsను monitor"],
        "hi": ["स्वस्थ बीज का उपयोग करें", "उचित फसल चक्र का अभ्यास करें", "खेत स्वच्छता बनाए रखें", "नियमित रूप से फसलों की निगरानी करें"],
        "mr": ["आरोग्यपूर्ण बियाणे वापरा", "योग्य पीक आवर्तन सराव करा", "शेताची स्वच्छता राखा", "नियमितपणे पिकांचे निरीक्षण करा"]
    },

    "disease_prevention_wheat_yellowrust": {
        "en": ["Use resistant varieties", "Use healthy seed", "Monitor fields during favorable conditions", "Maintain balanced crop management"],
        "te": ["నిరోధక రకాలను ఉపయోగించండి", "ఆరోగ్యకరమైన seedను ఉపయోగించండి", "అనుకూలమైన conditionsలో ఫీల్డ్‌లను monitor", "సమతుల్య crop managementను maintain"],
        "hi": ["प्रतिरोधी किस्मों का उपयोग करें", "स्वस्थ बीज का उपयोग करें", "अनुकूल परिस्थितियों के दौरान खेतों की निगरानी करें", "संतुलित फसल प्रबंधन बनाए रखें"],
        "mr": ["प्रतिरोधी जाती वापरा", "आरोग्यपूर्ण बियाणे वापरा", "अनुकूल परिस्थितींदरम्यान शेतांचे निरीक्षण करा", "संतुलित पीक व्यवस्थापन राखा"]
    },

}




TEXT_TRANSLATIONS = {'AI-assisted crop health monitoring': {'en': 'AI-assisted crop health monitoring', 'te': 'AI సహాయంతో పంట ఆరోగ్య పర్యవేక్షణ', 'hi': 'AI-सहायित फसल स्वास्थ्य निगरानी', 'mr': 'AI-सहाय्यित पीक आरोग्य निरीक्षण'}, 'Navigation': {'en': 'Navigation', 'te': 'నావిగేషన్', 'hi': 'नेविगेशन', 'mr': 'नेव्हिगेशन'}, '🚀 Crop Doctor Features': {'en': '🚀 Crop Doctor Features', 'te': '🚀 క్రాప్ డాక్టర్ ఫీచర్లు', 'hi': '🚀 क्रॉप डॉक्टर सुविधाएँ', 'mr': '🚀 क्रॉप डॉक्टर वैशिष्ट्ये'}, '🌱 Healthy': {'en': '🌱 Healthy', 'te': '🌱 ఆరోగ్యంగా', 'hi': '🌱 स्वस्थ', 'mr': '🌱 निरोगी'}, '🦠 Issues': {'en': '🦠 Issues', 'te': '🦠 సమస్యలు', 'hi': '🦠 समस्याएँ', 'mr': '🦠 समस्या'}, 'Your AI crop companion for continuous daily monitoring.': {'en': 'Your AI crop companion for continuous daily monitoring.', 'te': 'నిరంతర రోజువారీ పర్యవేక్షణ కోసం మీ AI పంట సహాయకుడు.', 'hi': 'निरंतर दैनिक निगरानी के लिए आपका AI फसल सहायक।', 'mr': 'सतत दैनंदिन निरीक्षणासाठी तुमचा AI पीक सहाय्यक.'}, '🌱 No crops registered yet.': {'en': '🌱 No crops registered yet.', 'te': '🌱 ఇంకా పంటలు నమోదు కాలేదు.', 'hi': '🌱 अभी तक कोई फसल पंजीकृत नहीं है।', 'mr': '🌱 अद्याप कोणतीही पिके नोंदलेली नाहीत.'}, 'Go to Crop Registration and register your crop first.': {'en': 'Go to Crop Registration and register your crop first.', 'te': 'పంట నమోదు విభాగానికి వెళ్లి ముందుగా మీ పంటను నమోదు చేయండి.', 'hi': 'फसल पंजीकरण में जाकर पहले अपनी फसल पंजीकृत करें।', 'mr': 'पीक नोंदणीमध्ये जाऊन प्रथम तुमचे पीक नोंदवा.'}, 'No active crops found.': {'en': 'No active crops found.', 'te': 'క్రియాశీల పంటలు ఏవీ కనుగొనబడలేదు.', 'hi': 'कोई सक्रिय फसल नहीं मिली।', 'mr': 'कोणतीही सक्रिय पिके आढळली नाहीत.'}, '🌾 Select your crop': {'en': '🌾 Select your crop', 'te': '🌾 మీ పంటను ఎంచుకోండి', 'hi': '🌾 अपनी फसल चुनें', 'mr': '🌾 तुमचे पीक निवडा'}, '🌱 Crop Profile': {'en': '🌱 Crop Profile', 'te': '🌱 పంట వివరాలు', 'hi': '🌱 फसल प्रोफ़ाइल', 'mr': '🌱 पीक प्रोफाइल'}, "Let's record today's condition.": {'en': "Let's record today's condition.", 'te': 'ఈరోజు పంట పరిస్థితిని నమోదు చేద్దాం.', 'hi': 'आज की स्थिति दर्ज करें।', 'mr': 'आजची स्थिती नोंदवूया.'}, "📸 Upload today's crop photograph": {'en': "📸 Upload today's crop photograph", 'te': '📸 ఈరోజు పంట ఫోటోను అప్\u200cలోడ్ చేయండి', 'hi': '📸 आज की फसल की तस्वीर अपलोड करें', 'mr': '📸 आजच्या पिकाचा फोटो अपलोड करा'}, '🔬 AI Analysis': {'en': '🔬 AI Analysis', 'te': '🔬 AI విశ్లేషణ', 'hi': '🔬 AI विश्लेषण', 'mr': '🔬 AI विश्लेषण'}, '⚠️ Please upload a valid RGB leaf image — analysis could not be completed.': {'en': '⚠️ Please upload a valid RGB leaf image — analysis could not be completed.', 'te': '⚠️ చెల్లుబాటు అయ్యే RGB ఆకు చిత్రాన్ని అప్\u200cలోడ్ చేయండి — విశ్లేషణ పూర్తికాలేదు.', 'hi': '⚠️ मान्य RGB पत्ते की तस्वीर अपलोड करें — विश्लेषण पूरा नहीं हो सका।', 'mr': '⚠️ वैध RGB पानाचा फोटो अपलोड करा — विश्लेषण पूर्ण होऊ शकले नाही.'}, '📊 Visual Difference': {'en': '📊 Visual Difference', 'te': '📊 దృశ్య తేడా', 'hi': '📊 दृश्य अंतर', 'mr': '📊 दृश्य फरक'}, '🟢 Normal': {'en': '🟢 Normal', 'te': '🟢 సాధారణం', 'hi': '🟢 सामान्य', 'mr': '🟢 सामान्य'}, '🟠 Minor Change': {'en': '🟠 Minor Change', 'te': '🟠 స్వల్ప మార్పు', 'hi': '🟠 मामूली बदलाव', 'mr': '🟠 किरकोळ बदल'}, '🔴 Significant Change': {'en': '🔴 Significant Change', 'te': '🔴 గణనీయమైన మార్పు', 'hi': '🔴 महत्वपूर्ण बदलाव', 'mr': '🔴 लक्षणीय बदल'}, '🤖 Crop Raksha Assessment': {'en': '🤖 Crop Raksha Assessment', 'te': '🤖 క్రాప్ రక్ష అంచనా', 'hi': '🤖 क्रॉप रक्षा आकलन', 'mr': '🤖 क्रॉप रक्षा मूल्यांकन'}, '🤖 Crop Raksha AI Assessment': {'en': '🤖 Crop Raksha AI Assessment', 'te': '🤖 క్రాప్ రక్ష AI అంచనా', 'hi': '🤖 क्रॉप रक्षा AI आकलन', 'mr': '🤖 क्रॉप रक्षा AI मूल्यांकन'}, 'Hotter/brighter areas show where the current image differs most from the previous observation.': {'en': 'Hotter/brighter areas show where the current image differs most from the previous observation.', 'te': 'వేడి/ప్రకాశవంతమైన ప్రాంతాలు ప్రస్తుత చిత్రం మునుపటి పరిశీలనతో ఎక్కువగా భిన్నంగా ఉన్న ప్రాంతాలను చూపుతాయి.', 'hi': 'अधिक चमकीले क्षेत्र दिखाते हैं कि वर्तमान तस्वीर पिछली तस्वीर से कहाँ सबसे अधिक अलग है।', 'mr': 'उष्ण/प्रकाशमान भाग वर्तमान फोटो मागील निरीक्षणापेक्षा कुठे जास्त वेगळा आहे ते दाखवतात.'}, 'The previous observation image could not be loaded, so the visual heatmap could not be created.': {'en': 'The previous observation image could not be loaded, so the visual heatmap could not be created.', 'te': 'మునుపటి పరిశీలన చిత్రం లోడ్ కాలేదు, కాబట్టి దృశ్య హీట్\u200cమ్యాప్ రూపొందించలేకపోయాం.', 'hi': 'पिछली तस्वीर लोड नहीं हो सकी, इसलिए दृश्य हीटमैप नहीं बनाया जा सका।', 'mr': 'मागील निरीक्षणाचा फोटो लोड झाला नाही, त्यामुळे दृश्य हीटमॅप तयार करता आला नाही.'}, '🟠 Crop Raksha noticed a visual change, but the AI currently considers the crop healthy.': {'en': '🟠 Crop Raksha noticed a visual change, but the AI currently considers the crop healthy.', 'te': '🟠 క్రాప్ రక్ష దృశ్య మార్పును గుర్తించింది, కానీ AI ప్రస్తుతం పంటను ఆరోగ్యంగా పరిగణిస్తోంది.', 'hi': '🟠 क्रॉप रक्षा ने दृश्य परिवर्तन देखा, लेकिन AI अभी फसल को स्वस्थ मानता है।', 'mr': '🟠 क्रॉप रक्षा ने दृश्य बदल लक्षात घेतला, पण AI सध्या पीक निरोगी मानतो.'}, '🟢 Crop Raksha currently sees no major health concern.': {'en': '🟢 Crop Raksha currently sees no major health concern.', 'te': '🟢 క్రాప్ రక్ష ప్రస్తుతం పెద్ద ఆరోగ్య సమస్యను చూడడం లేదు.', 'hi': '🟢 क्रॉप रक्षा को अभी कोई बड़ी स्वास्थ्य चिंता नहीं दिख रही है।', 'mr': '🟢 क्रॉप रक्षा ला सध्या मोठी आरोग्याची चिंता दिसत नाही.'}, '🟠 The AI detected a possible issue. Consider using the Diagnose section for confirmation.': {'en': '🟠 The AI detected a possible issue. Consider using the Diagnose section for confirmation.', 'te': '🟠 AI ఒక సాధ్యమైన సమస్యను గుర్తించింది. నిర్ధారణ కోసం డయాగ్నోసిస్ విభాగాన్ని ఉపయోగించండి.', 'hi': '🟠 AI ने संभावित समस्या पहचानी। पुष्टि के लिए निदान अनुभाग का उपयोग करें।', 'mr': '🟠 AI ने संभाव्य समस्या ओळखली. पुष्टीसाठी निदान विभाग वापरा.'}, '🚨 Crop Raksha detected a significant visual change and the AI identified a possible crop health issue.': {'en': '🚨 Crop Raksha detected a significant visual change and the AI identified a possible crop health issue.', 'te': '🚨 క్రాప్ రక్ష గణనీయమైన దృశ్య మార్పును గుర్తించింది మరియు AI పంట ఆరోగ్య సమస్యను సూచించింది.', 'hi': '🚨 क्रॉप रक्षा ने महत्वपूर्ण दृश्य परिवर्तन पाया और AI ने संभावित फसल स्वास्थ्य समस्या पहचानी।', 'mr': '🚨 क्रॉप रक्षा ने लक्षणीय दृश्य बदल ओळखला आणि AI ने संभाव्य पीक आरोग्य समस्या दर्शवली.'}, '🩺 Please open the Diagnose section for a detailed assessment.': {'en': '🩺 Please open the Diagnose section for a detailed assessment.', 'te': '🩺 వివరమైన అంచనా కోసం నిర్ధారణ విభాగాన్ని తెరవండి.', 'hi': '🩺 विस्तृत जांच के लिए निदान अनुभाग खोलें।', 'mr': '🩺 सविस्तर तपासणीसाठी निदान विभाग उघडा.'}}

TEXT_TRANSLATIONS["🌾 Link diagnosis to a registered crop"] = {"en":"🌾 Link diagnosis to a registered crop","te":"🌾 నిర్ధారణను నమోదు చేసిన పంటకు లింక్ చేయండి","hi":"🌾 निदान को पंजीकृत फसल से जोड़ें","mr":"🌾 निदान नोंदणीकृत पिकाशी जोडा"}
TEXT_TRANSLATIONS["— General diagnosis (not linked to a crop) —"] = {"en":"— General diagnosis (not linked to a crop) —","te":"— సాధారణ నిర్ధారణ (పంటకు లింక్ చేయలేదు) —","hi":"— सामान्य जांच (फसल से लिंक नहीं) —","mr":"— सामान्य निदान (पिकाशी जोडलेले नाही) —"}
TEXT_TRANSLATIONS.update({'Your AI crop companion remembers your monitoring history and helps you understand what is happening over time.': {'en': 'Your AI crop companion remembers your monitoring history and helps you understand what is happening over time.', 'te': 'మీ AI పంట సహాయకుడు మీ పర్యవేక్షణ చరిత్రను గుర్తుంచుకుని కాలక్రమేణా ఏమి జరుగుతుందో అర్థం చేసుకోవడంలో సహాయపడుతుంది.', 'hi': 'आपका AI फसल सहायक आपकी निगरानी का इतिहास याद रखता है और समय के साथ क्या हो रहा है यह समझने में मदद करता है।', 'mr': 'तुमचा AI पीक सहाय्यक तुमचा निरीक्षण इतिहास लक्षात ठेवतो आणि कालांतराने काय घडत आहे हे समजून घेण्यास मदत करतो.'}, 'I understand this will permanently delete all diagnosis history.': {'en': 'I understand this will permanently delete all diagnosis history.', 'te': 'నా నిర్ధారణ చరిత్ర మొత్తం శాశ్వతంగా తొలగించబడుతుందని నాకు తెలుసు.', 'hi': 'मैं समझता हूँ कि इससे पूरा निदान इतिहास स्थायी रूप से हट जाएगा।', 'mr': 'मला समजते की यामुळे संपूर्ण निदान इतिहास कायमचा हटवला जाईल.'}, '🔥 Visual Change Analysis': {'en': '🔥 Visual Change Analysis', 'te': '🔥 దృశ్య మార్పు విశ్లేషణ', 'hi': '🔥 दृश्य परिवर्तन विश्लेषण', 'mr': '🔥 दृश्य बदल विश्लेषण'}, 'Information for this disease is not available yet.': {'en': 'Information for this disease is not available yet.', 'te': 'ఈ వ్యాధికి సంబంధించిన సమాచారం ఇంకా అందుబాటులో లేదు.', 'hi': 'इस रोग की जानकारी अभी उपलब्ध नहीं है।', 'mr': 'या रोगाची माहिती अद्याप उपलब्ध नाही.'}, "Let's record today's condition.": {'en': "Let's record today's condition.", 'te': 'ఈరోజు పంట పరిస్థితిని నమోదు చేద్దాం.', 'hi': 'आज की स्थिति दर्ज करें।', 'mr': 'आजची स्थिती नोंदवूया.'}, 'No crops registered yet.': {'en': 'No crops registered yet.', 'te': 'ఇంకా పంటలు నమోదు కాలేదు.', 'hi': 'అభీ తక ఫసల్ పంజీకృత్ లేద్।', 'mr': 'अद्याप कोणतीही पिके नोंदलेली नाहीत.'}, 'Please enter the farmer name.': {'en': 'Please enter the farmer name.', 'te': 'దయచేసి రైతు పేరు నమోదు చేయండి.', 'hi': 'कृपया किसान का नाम दर्ज करें।', 'mr': 'कृपया शेतकऱ्याचे नाव नोंदवा.'}, 'The date of sowing cannot be in the future.': {'en': 'The date of sowing cannot be in the future.', 'te': 'విత్తిన తేదీ భవిష్యంలో ఉండకూడదు.', 'hi': 'बुवाई की तारीख भविष्य में नहीं हो सकती।', 'mr': 'पेरणीची तारीख भविष्यात असू शकत नाही.'}})

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

def t(key, language=None, **variables):
    """
    Offline translation function.

    Example:
        t("dashboard", "te")
        t("day_observation", day=3)

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
        # Fall back to key as the rendered text
        result = key
    else:
        result = translation.get(
            language,
            translation.get("en", key)
        )

    # Apply variable substitution
    if variables:
        try:
            result = result.format(**variables)
        except (KeyError, IndexError, AttributeError):
            # If formatting fails, do simple replacement
            for name, value in variables.items():
                result = result.replace("{" + str(name) + "}", str(value))

    return result


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


# =====================================================
# CROP NAME TRANSLATION
# =====================================================

CROP_NAME_MAP = {
    "banana": "crop_banana",
    "corn": "crop_corn",
    "cotton": "crop_cotton",
    "grape": "crop_grape",
    "mango": "crop_mango",
    "paddy": "crop_paddy",
    "rice": "crop_paddy",
    "potato": "crop_potato",
    "soybean": "crop_soybean",
    "tomato": "crop_tomato",
    "wheat": "crop_wheat",
}


def translate_crop_name(crop_name, language=None):
    """
    Translate a crop name to the selected language.

    Args:
        crop_name: English crop name (e.g. "Tomato", "Paddy")
        language: target language code; defaults to current

    Returns:
        Translated crop name, or original if no mapping exists.
    """
    if not crop_name:
        return crop_name

    key = CROP_NAME_MAP.get(crop_name.lower().strip())
    if key:
        return t(key, language)

    return crop_name


# =====================================================
# DISEASE LIBRARY — TRANSLATION HELPERS
# =====================================================

def translate_disease_name(class_name, language=None):
    """
    Translate a disease name using its class ID.

    Uses the class_name (e.g. "banana_cordana") to find the
    translation key, falling back to the English disease
    name from disease_info.py if no translation exists.

    Internal disease IDs in disease_info.py are NOT modified.

    Args:
        class_name:  Internal class ID from class_names.json
                     (e.g. "banana_cordana", "tomato_early_blight")
        language:    target language code; defaults to current

    Returns:
        Translated disease name, or English fallback.
    """
    # Normalize "healthy" class names
    disease_key = class_name.lower().strip()
    if "healthy" in disease_key:
        return t("disease_healthy", language)

    # Map class_name to the translation key. The translation keys use
    # a stable name (e.g. "disease_cordana_leaf_spot") rather than
    # the internal class ID, so the storage is never modified.
    name_to_key = {
        "banana_cordana": "disease_cordana_leaf_spot",
        "banana_pestalotiopsis": "disease_pestalotiopsis_leaf_spot",
        "banana_sigatoka": "disease_sigatoka_leaf_spot",
        "corn_common_rust": "disease_common_rust",
        "corn_gray_leaf_spot": "disease_gray_leaf_spot",
        "corn_northern_leaf_blight": "disease_northern_corn_leaf_blight",
        "cotton_bacterial_blight": "disease_bacterial_blight",
        "cotton_cotton_leaf_curl": "disease_cotton_leaf_curl",
        "cotton_fusarium_wilt": "disease_fusarium_wilt",
        "grape_black_measles": "disease_black_measles",
        "grape_black_rot": "disease_black_rot",
        "grape_isariopsis_leaf_spot": "disease_isariopsis_leaf_spot",
        "mango_anthracnose": "disease_anthracnose",
        "mango_bacterial_canker": "disease_bacterial_canker",
        "mango_powdery_mildew": "disease_powdery_mildew",
        "paddy_bacterial_leaf_blight": "disease_bacterial_leaf_blight",
        "paddy_brown_spot": "disease_brown_spot",
        "paddy_leaf_blast": "disease_rice_leaf_blast",
        "potato_early_blight": "disease_early_blight",
        "potato_late_blight": "disease_late_blight",
        "soybean_caterpillar": "disease_caterpillar_damage",
        "soybean_diabrotica_speciosa": "disease_diabrotica_speciosa",
        "tomato_bacterial_spot": "disease_bacterial_spot",
        "tomato_early_blight": "disease_early_blight",
        "tomato_late_blight": "disease_late_blight",
        "wheat_mildew": "disease_powdery_mildew",
        "wheat_septoria": "disease_septoria_leaf_spot",
        "wheat_yellowrust": "disease_yellow_rust",
    }

    trans_key = name_to_key.get(disease_key)
    if trans_key:
        translated = t(trans_key, language)
        if translated != trans_key:
            return translated

    # Fall back to English from disease_info.py
    from disease_info import DISEASE_INFO
    info = DISEASE_INFO.get(class_name)
    if info:
        return info.get("disease", class_name.replace("_", " ").title())

    return class_name.replace("_", " ").title()


def get_translated_disease_info(class_name, language=None):
    """
    Return disease info (description, symptoms, management, prevention)
    translated into the selected language.

    Falls back to English from disease_info.py if no translation
    is available for the current language. Internal disease IDs
    in disease_info.py are NOT modified.

    Args:
        class_name: Internal class ID (e.g. "banana_cordana")
        language:    target language code; defaults to current

    Returns:
        dict with keys: description, symptoms (list), management (list),
        prevention (list) — all in the target language.
    """
    if language is None:
        # Use streamlit session state lazily to avoid ImportError at module load
        try:
            import streamlit as st
            language = st.session_state.get("language", "en")
        except Exception:
            language = "en"

    if language not in ["en", "te", "hi", "mr"]:
        language = "en"

    # Build translation key for disease description
    # e.g. "banana_cordana" -> "disease_desc_banana_cordana"
    disease_key = class_name.lower().strip()

    # Check if we have translations for this disease
    desc_key = f"disease_desc_{disease_key}"
    translated_desc = t(desc_key, language)

    if translated_desc != desc_key:
        # We have translations for this disease
        # Get symptom, management, prevention from TRANSLATIONS
        symptoms_key = f"disease_symptoms_{disease_key}"
        management_key = f"disease_management_{disease_key}"
        prevention_key = f"disease_prevention_{disease_key}"

        symptoms = TRANSLATIONS.get(symptoms_key, {}).get(language, [])
        management = TRANSLATIONS.get(management_key, {}).get(language, [])
        prevention = TRANSLATIONS.get(prevention_key, {}).get(language, [])

        # If no translated lists found, fall back to English from disease_info
        from disease_info import DISEASE_INFO
        info = DISEASE_INFO.get(class_name, {})
        if not symptoms:
            symptoms = info.get("symptoms", [])
        if not management:
            management = info.get("management", [])
        if not prevention:
            prevention = info.get("prevention", [])

        return {
            "description": translated_desc,
            "symptoms": symptoms,
            "management": management,
            "prevention": prevention,
        }

    # No translated description found — fall back to English
    from disease_info import DISEASE_INFO
    info = DISEASE_INFO.get(class_name)
    if info:
        return {
            "description": info.get("description", ""),
            "symptoms": info.get("symptoms", []),
            "management": info.get("management", []),
            "prevention": info.get("prevention", []),
        }

    return None
