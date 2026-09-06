import streamlit as st
import streamlit.components.v1 as components
import json
import os
import sys
import base64
import urllib.parse

# Add parent directory to path so we can import language.py
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from language import t, translate_crop_name




# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

CROPS_FILE = os.path.join(
    BASE_DIR,
    "crops.json"
)

RAKSHA_FILE = os.path.join(
    BASE_DIR,
    "crop_raksha_history.json"
)

MONITORING_FILE = os.path.join(
    BASE_DIR,
    "monitoring_history.json"
)


# ============================================================
# JSON LOADER
# ============================================================

def load_json(path, default):

    if not os.path.exists(path):
        return default

    try:
        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception:
        return default


# ============================================================
# LOAD PROJECT DATA
# ============================================================

crops_data = load_json(
    CROPS_FILE,
    []
)

raksha_history = load_json(
    RAKSHA_FILE,
    []
)

monitoring_history = load_json(
    MONITORING_FILE,
    []
)


# ============================================================
# NORMALIZE CROPS
# ============================================================

def normalize_crops(data):

    if isinstance(data, dict):

        if isinstance(
            data.get("crops"),
            list
        ):
            data = data["crops"]

        else:
            data = []

    if not isinstance(data, list):
        return []

    result = []

    for index, crop in enumerate(data):

        if not isinstance(crop, dict):
            continue

        crop_id = (
            crop.get("id")
            or crop.get("crop_id")
            or index + 1
        )

        crop_name = (
            crop.get("crop_name")
            or crop.get("crop")
            or crop.get("name")
            or "Unknown Crop"
        )

        farmer_name = (
            crop.get("farmer_name")
            or crop.get("farmer")
            or "Farmer"
        )

        field_label = (
            crop.get("field_label")
            or crop.get("field")
            or "Field"
        )

        sowing_date = (
            crop.get("sowing_date")
            or ""
        )

        result.append(
            {
                "id": str(crop_id),
                "crop_name": str(crop_name),
                "farmer_name": str(farmer_name),
                "field_label": str(field_label),
                "sowing_date": str(sowing_date)
            }
        )

    return result


crops = normalize_crops(crops_data)


if not isinstance(
    raksha_history,
    list
):
    raksha_history = []


if not isinstance(
    monitoring_history,
    list
):
    monitoring_history = []


# ============================================================
# BUILD CROP RECORDS
# ============================================================

crop_records = []


for crop in crops:

    crop_id = crop["id"]

    raksha_records = [
        record
        for record in raksha_history
        if str(
            record.get("crop_id", "")
        ) == crop_id
    ]

    monitoring_records = [
        record
        for record in monitoring_history
        if (
            str(record.get("crop_id", "")) == crop_id
            or (
                not record.get("crop_id")
                and str(record.get("crop", "")).strip().lower()
                == str(crop["crop_name"]).strip().lower()
            )
        )
    ]

    latest_raksha = None

    if raksha_records:

        latest_raksha = sorted(
            raksha_records,
            key=lambda x: str(
                x.get("date", "")
            )
        )[-1]

    latest_monitoring = None

    if monitoring_records:

        latest_monitoring = sorted(
            monitoring_records,
            key=lambda x: str(
                x.get("date")
                or x.get("timestamp")
                or ""
            )
        )[-1]

    crop_records.append(
        {
            "id": crop_id,
            "crop_name": crop["crop_name"],
            "farmer_name": crop["farmer_name"],
            "field_label": crop["field_label"],
            "sowing_date": crop["sowing_date"],
            "raksha_count": len(
                raksha_records
            ),
            "monitoring_count": len(
                monitoring_records
            ),
            "latest_raksha": latest_raksha,
            "latest_monitoring": latest_monitoring
        }
    )


# ============================================================
# TRANSLATIONS
# ============================================================

translations = {

    "en": {

        "name": "English",

        "welcome":
            "Welcome to Anjaneya. "
            "I am your AI agricultural assistant.",

        "choose_language":
            "Please say your language. "
            "Say English, Telugu, Hindi, "
            "or Marathi.",

        "main_menu":
            "Main menu. "
            "Say diagnosis for Crop Diagnosis. "
            "Say status for Crop Status. "
            "Say raksha for Crop Raksha AI. "
            "Say casual for Casual Talk. "
            "Say help for Help. "
            "Say repeat to hear this again. "
            "Say end to end the call.",

        "diagnosis":
            "Crop Diagnosis selected. "
            "Please open the Crop Doctor diagnosis section "
            "and upload a clear photograph of the affected crop. "
            "The AI will analyze the photograph.",

        "choose_crop":
            "Please say the name of your crop.",

        "status":
            "I am checking your crop status.",

        "raksha":
            "Crop Raksha AI selected. "
            "I will use your previous observations "
            "to monitor changes in your crop.",

        "help":
            "You can speak to me anytime. "
            "Say status to check crop status, "
            "say raksha to use Crop Raksha, "
            "or say diagnosis to start a crop diagnosis.",

        "no_crops":
            "No registered crops were found. "
            "Please register a crop in Crop Doctor first.",

        "repeat":
            "Repeating the current menu.",

        "goodbye":
            "Thank you for using Crop Doctor. "
            "Take care of your crops. Goodbye.",

        "invalid":
            "I did not understand that choice. "
            "Please try again.",

        "status_summary":
            "Your latest AI observation was {disease}, "
            "with {confidence} percent confidence.",

        "raksha_summary":
            "Crop Raksha has recorded {count} observations "
            "for this crop.",

        "no_history":
            "There are no Crop Raksha observations "
            "for this crop yet."
    },


    "te": {

        "name": "తెలుగు",

        "welcome":
            "క్రాప్ డాక్టర్‌కు స్వాగతం. "
            "నేను మీ AI వ్యవసాయ సహాయకుడిని.",

        "choose_language":
            "మీ భాషను చెప్పండి. "
            "ఇంగ్లీష్ కోసం 'ఇంగ్లీష్', "
            "తెలుగు కోసం 'తెలుగు', "
            "హిందీ కోసం 'హిందీ', "
            "మరాఠీ కోసం 'మరాఠీ' అని చెప్పండి.",

        "main_menu":
            "ప్రధాన మెనూ. "
            "వ్యాధి నిర్ధారణ కోసం 'నిర్ధారణ' అని చెప్పండి. "
            "పంట స్థితి కోసం 'స్థితి' అని చెప్పండి. "
            "క్రాప్ రక్ష కోసం 'రక్ష' అని చెప్పండి. "
            "సాధారణ సంభాషణ కోసం 'సంభాషణ' అని చెప్పండి. "
            "సహాయం కోసం 'సహాయం' అని చెప్పండి. "
            "మళ్లీ వినడానికి 'మళ్లీ' అని చెప్పండి. "
            "ముగించడానికి 'ముగించు' అని చెప్పండి.",

        "diagnosis":
            "పంట వ్యాధి నిర్ధారణ ఎంపిక చేయబడింది. "
            "క్రాప్ డాక్టర్ డయాగ్నోసిస్ విభాగాన్ని తెరిచి "
            "పంటకు సంబంధించిన స్పష్టమైన ఫోటోను అప్‌లోడ్ చేయండి. "
            "AI ఫోటోను విశ్లేషిస్తుంది.",

        "choose_crop":
            "దయచేసి మీ పంట పేరు చెప్పండి.",

        "status":
            "మీ పంట స్థితిని పరిశీలిస్తున్నాను.",

        "raksha":
            "క్రాప్ రక్ష AI ఎంపిక చేయబడింది. "
            "మీ పంటలో మార్పులను గమనించడానికి "
            "మునుపటి పరిశీలనలను ఉపయోగిస్తాను.",

        "help":
            "మీరు ఎప్పుడైనా మాట్లాడవచ్చు. "
            "పంట స్థితి కోసం 'స్థితి', "
            "క్రాప్ రక్ష కోసం 'రక్ష', "
            "వ్యాధి నిర్ధారణ కోసం 'నిర్ధారణ' అని చెప్పండి.",

        "no_crops":
            "రిజిస్టర్ చేసిన పంటలు ఏవీ కనుగొనబడలేదు. "
            "ముందుగా క్రాప్ డాక్టర్‌లో పంటను రిజిస్టర్ చేయండి.",

        "repeat":
            "ప్రస్తుత మెనూను మళ్ళీ చెబుతున్నాను.",

        "goodbye":
            "క్రాప్ డాక్టర్‌ను ఉపయోగించినందుకు ధన్యవాదాలు. "
            "మీ పంటలను జాగ్రత్తగా చూసుకోండి. నమస్కారం.",

        "invalid":
            "మీ ఎంపిక అర్థం కాలేదు. "
            "దయచేసి మళ్ళీ ప్రయత్నించండి.",

        "status_summary":
            "మీ తాజా AI పరిశీలనలో {disease} గుర్తించబడింది. "
            "నమ్మక స్థాయి {confidence} శాతం.",

        "raksha_summary":
            "ఈ పంటకు క్రాప్ రక్షలో {count} పరిశీలనలు ఉన్నాయి.",

        "no_history":
            "ఈ పంటకు ఇంకా క్రాప్ రక్ష పరిశీలనలు లేవు."
    },


    "hi": {

        "name": "हिन्दी",

        "welcome":
            "क्रॉप डॉक्टर में आपका स्वागत है। "
            "मैं आपका AI कृषि सहायक हूँ।",

        "choose_language":
            "अपनी भाषा बोलें। "
            "अंग्रेज़ी के लिए 'अंग्रेज़ी', "
            "तेलुगु के लिए 'तेलुगु', "
            "हिंदी के लिए 'हिंदी', "
            "और मराठी के लिए 'मराठी' कहें।",

        "main_menu":
            "मुख्य मेनू। "
            "रोग पहचान के लिए 'पहचान' कहें। "
            "फसल की स्थिति के लिए 'स्थिति' कहें। "
            "क्रॉप रक्षा के लिए 'रक्षा' कहें। "
            "सामान्य बातचीत के लिए 'बातचीत' कहें। "
            "मदद के लिए 'मदद' कहें। "
            "दोबारा सुनने के लिए 'दोबारा' कहें। "
            "समाप्त करने के लिए 'समाप्त' कहें।",

        "diagnosis":
            "फसल रोग पहचान चुना गया है। "
            "कृपया क्रॉप डॉक्टर के डायग्नोसिस सेक्शन में जाकर "
            "फसल की साफ तस्वीर अपलोड करें। "
            "AI तस्वीर का विश्लेषण करेगा।",

        "choose_crop":
            "कृपया अपनी फसल का नाम बोलें।",

        "status":
            "मैं आपकी फसल की स्थिति जाँच रहा हूँ।",

        "raksha":
            "क्रॉप रक्षा AI चुना गया है। "
            "मैं आपकी फसल में बदलावों की निगरानी के लिए "
            "पिछली जानकारी का उपयोग करूँगा।",

        "help":
            "आप कभी भी मुझसे बोल सकते हैं। "
            "फसल की स्थिति के लिए 'स्थिति', "
            "क्रॉप रक्षा के लिए 'रक्षा', "
            "रोग पहचान के लिए 'पहचान' कहें।",

        "no_crops":
            "कोई पंजीकृत फसल नहीं मिली। "
            "कृपया पहले क्रॉप डॉक्टर में फसल पंजीकृत करें।",

        "repeat":
            "मैं वर्तमान मेनू दोबारा बता रहा हूँ।",

        "goodbye":
            "क्रॉप डॉक्टर का उपयोग करने के लिए धन्यवाद। "
            "अपनी फसल का ध्यान रखें। नमस्कार।",

        "invalid":
            "मैं आपकी पसंद समझ नहीं पाया। "
            "कृपया फिर से प्रयास करें।",

        "status_summary":
            "आपकी नवीनतम AI जाँच में {disease} पाया गया। "
            "विश्वास स्तर {confidence} प्रतिशत है।",

        "raksha_summary":
            "इस फसल के लिए क्रॉप रक्षा में {count} निरीक्षण दर्ज हैं।",

        "no_history":
            "इस फसल के लिए अभी कोई क्रॉप रक्षा निरीक्षण नहीं है।"
    },


    "mr": {

        "name": "मराठी",

        "welcome":
            "क्रॉप डॉक्टरमध्ये आपले स्वागत आहे. "
            "मी तुमचा AI कृषी सहाय्यक आहे.",

        "choose_language":
            "तुमची भाषा बोला. "
            "इंग्रजीसाठी 'इंग्रजी', "
            "तेलुगूसाठी 'तेलुगू', "
            "हिंदीसाठी 'हिंदी', "
            "आणि मराठीसाठी 'मराठी' म्हणा.",

        "main_menu":
            "मुख्य मेनू. "
            "रोग निदानासाठी 'निदान' म्हणा. "
            "पिकाची स्थिती पाहण्यासाठी 'स्थिती' म्हणा. "
            "क्रॉप रक्षासाठी 'रक्षा' म्हणा. "
            "सामान्य संभाषणासाठी 'संभाषण' म्हणा. "
            "मदतीसाठी 'मदत' म्हणा. "
            "पुन्हा ऐकण्यासाठी 'पुन्हा' म्हणा. "
            "समाप्त करण्यासाठी 'समाप्त' म्हणा.",

        "diagnosis":
            "पीक रोग निदान निवडले आहे. "
            "कृपया क्रॉप डॉक्टरमधील डायग्नोसिस विभाग उघडा "
            "आणि पिकाचा स्पष्ट फोटो अपलोड करा. "
            "AI फोटोचे विश्लेषण करेल.",

        "choose_crop":
            "कृपया तुमच्या पिकाचे नाव सांगा.",

        "status":
            "मी तुमच्या पिकाची स्थिती तपासत आहे.",

        "raksha":
            "क्रॉप रक्षा AI निवडले आहे. "
            "तुमच्या पिकातील बदल पाहण्यासाठी "
            "आधीच्या निरीक्षणांचा उपयोग केला जाईल.",

        "help":
            "तुम्ही केव्हाही माइयाशी बोलू शकता. "
            "पिकाच्या स्थितीसाठी 'स्थिती', "
            "क्रॉप रक्षासाठी 'रक्षा', "
            "रोग निदानासाठी 'निदान' म्हणा.",

        "no_crops":
            "नोंदणीकृत पिके आढळली नाहीत. "
            "कृपया प्रथम क्रॉप डॉक्टरमध्ये पीक नोंदणी करा.",

        "repeat":
            "मी सध्याचा मेनू पुन्हा सांगत आहे.",

        "goodbye":
            "क्रॉप डॉक्टर वापरल्याबद्दल धन्यवाद. "
            "तुमच्या पिकांची काळजी घ्या. नमस्कार.",

        "invalid":
            "मला तुमची निवड समजली नाही. "
            "कृपया पुन्हा प्रयत्न करा.",

        "status_summary":
            "तुमच्या नवीनतम AI तपासणीत {disease} आढळले. "
            "विश्वास पातळी {confidence} टक्के आहे.",

        "raksha_summary":
            "या पिकासाठी क्रॉप रक्षा मध्ये {count} निरीक्षणे नोंदली आहेत.",

        "no_history":
            "या पिकासाठी अद्याप क्रॉप रक्षा निरीक्षणे नाहीत."
    }
}



_EXTRA_TRANSLATIONS = {
    "visual_status": {"en":"Visual status: {status}","te":"దృశ్య స్థితి: {status}","hi":"दृश्य स्थिति: {status}","mr":"दृश्य स्थिती: {status}"},
    "last_observation": {"en":"Last observation: {date}","te":"చివరి పరిశీలన: {date}","hi":"अंतिम अवलोकन: {date}","mr":"शेवटचे निरीक्षण: {date}"},
    "raksha_count": {"en":"Crop Raksha observations: {count}","te":"క్రాప్ రక్ష పరిశీలనలు: {count}","hi":"क्रॉप रक्षा अवलोकन: {count}","mr":"क्रॉप रक्षा निरीक्षणे: {count}"},
    "monitoring_count": {"en":"Monitoring records: {count}","te":"పర్యవేక్షణ రికార్డులు: {count}","hi":"निगरानी रिकॉर्ड: {count}","mr":"निरीक्षण रेकॉर्ड: {count}"},

    # ── TALK button ─────────────────────────────────
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
    "offline_notice": {
        "en": "🌿 Works offline — uses your browser's voice",
        "te": "🌿 ఆఫ్‌లైన్‌లో పనిచేస్తుంది — మీ బ్రౌజర్ వాయిస్‌ను ఉపయోగిస్తుంది",
        "hi": "🌿 ऑफलाइन काम करता है — आपके ब्रॉउज़र की आवाज़ का उपयोग करता है",
        "mr": "🌿 ऑफलाइन काम करते — तुमच्या ब्रॉझरच्या आवाज़ाचा वापर करते"
    },
    "browser_voice_notice": {
        "en": "Uses browser's built-in voice (Chrome recommended)",
        "te": "బ్రౌజర్ అంతర్గత వాయిస్‌ను ఉపయోగిస్తుంది (Chrome సిఫార్సు)",
        "hi": "ब्रॉउज़र की अंतर्निहित आवाज़ का उपयोग करता है (Chrome अनुशंसित)",
        "mr": "ब्रॉझरच्या अंगभूत आवाज़ाचा वापर करते (Chrome शिफारसित)"
    },
    "voice_unavailable_message": {
        "en": "Voice input is not supported by this browser. Please try Chrome on Android or desktop.",
        "te": "ఈ బ్రౌజర్‌లో వాయిస్ ఇన్‌పుట్ సపోర్టెడ్ కాదు. Android లేదా డెస్క్‌టాప్‌పై Chrome ప్రయత్నించండి.",
        "hi": "इस ब्रॉउज़र में वॉइस इनपुट समर्थित नहीं है। Android या डेस्कटॉप पर Chrome आज़माएं।",
        "mr": "या ब्रॉझरमध्ये व्हॉइस इनपुट समर्थित नाही. Android किंवा डेस्कटॉपवर Chrome वापरा."
    },
    "mic_blocked_instruction": {
        "en": "Microphone access is blocked. Please allow it and reload.",
        "te": "మైక్రోఫోన్ యాక్సెస్ బ్లాక్ చేయబడింది.దయచేసి అనుమతించండి మరియు రీలోడ్ చేయండి.",
        "hi": "माइक्रोफ़ोन एक्सेस ब्लॉक है। कृपया इसे अनुमति दें और पुनः लोड करें।",
        "mr": "मायक्रोफोन प्रवेश ब्लॉक आहे. कृपया ते परवानगी द्या आणि पुन्हा लोड करा."
    },
    "voice_not_installed": {
        "en": "voice not installed in this browser.",
        "te": "ఈ బ్రౌజర్‌లో వాయిస్ ఇన్‌స్టాల్ చేయబడలేదు.",
        "hi": "इस ब्रॉउज़र में वॉइस इंस्टॉल नहीं है।",
        "mr": "या ब्रॉझरमध्ये व्हॉइस इंस्टॉल नाही."
    },
    "online_tts_notice": {
        "en": "🌐 Telugu & Marathi use online TTS — internet required",
        "te": "🌐 ఆన్‌లైన్ TTS — ఇంటర్నెట్ అవసరం",
        "hi": "🌐 तेलुगु और मराठी के लिए ऑनलाइन TTS — इंटरनेट आवश्यक",
        "mr": "🌐 तेलुगू आणि मराठीसाठी ऑनलाइन TTS — इंटरनेट आवश्यक"
    },
    "checking_language_voices": {
        "en": "Checking language voices...",
        "te": "భాష వాయిస్‌లను తనిఖీ చేస్తోంది...",
        "hi": "भाषा वॉइस की जाँच हो रही है...",
        "mr": "भाषा व्हॉइस तपासत आहे..."
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
    "ok_button": {
        "en": "OK",
        "te": "సరే",
        "hi": "ठीक है",
        "mr": "ठीक आहे"
    },
    "tap_ok_caption": {
        "en": "Tap to start your voice session with Anjaneya",
        "te": "ఆంజనేయతో వాయిస్ సెషన్ ప్రారంభించడానికి నొక్కండి",
        "hi": "आंजनेय के साथ अपना वॉइस सेशन शुरू करने के लिए टैप करें",
        "mr": "आंजनेयशी तुमचे व्हॉइस सेशन सुरू करण्यासाठी टॅप करा"
    },
    "footer_brand": {
        "en": "Crop Doctor — Anjaneya Voice",
        "te": "క్రాప్ డాక్టర్ — ఆంజనేయ వాయిస్",
        "hi": "क्रॉप डॉक्टर — आंजनेय वॉइस",
        "mr": "क्रॉप डॉक्टर — आंजनेय व्हॉइस"
    },
    "splash_jai_anjaneya": {
        "en": "🙏 जय श्री अंजनेय 🙏",
        "te": "🙏 జయ శ్రీ అంజనేయ 🙏",
        "hi": "🙏 जय श्री अंजनेय 🙏",
        "mr": "🙏 जय श्री अंजनेय 🙏"
    },
    "anjaneya_title": {
        "en": "🔱 ANJANEYA",
        "te": "🔱 ఆంజనేయ",
        "hi": "🔱 आंजनेय",
        "mr": "🔱 आंजनेय"
    },
    "anjaneya_subtitle": {
        "en": "Multilingual Offline AI Voice Assistant",
        "te": "బహుభాషా ఆఫ్‌లైన్ AI వాయిస్ అసిస్టెంట్",
        "hi": "बहुभाषी ऑफ़लाइन AI वॉइस असिस्टेंट",
        "mr": "बहुभाषी ऑफलाइन AI व्हॉइस असिस्टंट"
    },
    "status_connecting": {
        "en": "Connecting",
        "te": "కనెక్ట్ చేస్తోంది",
        "hi": "कनेक्ट हो रहा है",
        "mr": "कनेक्ट होत आहे"
    },
    "status_voice_unavailable": {
        "en": "Voice input unavailable",
        "te": "వాయిస్ ఇన్‌పుట్ అందుబాటులో లేదు",
        "hi": "वॉइस इनपुट उपलब्ध नहीं",
        "mr": "व्हॉइस इनपुट उपलब्ध नाही"
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
    "select_language": {
        "en": "Select Language",
        "te": "భాషను ఎంచుకోండి",
        "hi": "भाषा चुनें",
        "mr": "भाषा निवडा"
    },
    "no_crop_selected": {
        "en": "No crop selected",
        "te": "పంట ఎంచుకోబడలేదు",
        "hi": "कोई फसल नहीं चुनी",
        "mr": "कोणतेही पीक निवडलेले नाही"
    },
    "registered_crops_metric": {
        "en": "Registered Crops",
        "te": "నమోదు చేసిన పంటలు",
        "hi": "पंजीकृत फसलें",
        "mr": "नोंदणीकृत पिके"
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
    "heard": {
        "en": "Heard: ",
        "te": "వినబడింది: ",
        "hi": "सुना: ",
        "mr": "ऐकले: "
    },
    "invalid": {
        "en": "I did not understand that. Please try again.",
        "te": "నాకు అది అర్థం కాలేదు.దయచేసి మళ్ళీ ప్రయత్నించండి.",
        "hi": "मुझे समझ नहीं आया। कृपया फिर से प्रयास करें।",
        "mr": "मला समजले नाही. कृपया पुन्हा प्रयत्न करा."
    },

    # ── CASUAL TALK ─────────────────────────────────
    "casual_talk": {
        "en": "Casual Talk",
        "te": "సాధారణ సంభాషణ",
        "hi": "सामान्य बातचीत",
        "mr": "सामान्य संभाषण"
    },
    "casual_talk_intro": {
        "en": "Casual Talk mode. Ask me anything about your day, your crop, or the weather. I will do my best to help.",
        "te": "సాధారణ సంభాషణ విధానం. మీ రోజు, పంట లేదా వాతావరణం గురించి ఏదైనా అడగండి. నేను సహాయం చేయడానికి ప్రయత్నిస్తాను.",
        "hi": "सामान्य बातचीत मोड। अपने दिन, फसल या मौसम के बारे में कुछ भी पूछें। मैं मदद करने की पूरी कोशिश करूँगा।",
        "mr": "सामान्य संभाषण मोड. तुमच्या दिवसाबद्दल, पिकाबद्दल किंवा हवामानाबद्दल काहीही विचारा. मी मदत करण्याचा पूर्ण प्रयत्न करेन."
    },
    "greeting_morning": {
        "en": "Good morning! I hope you and your farm are doing well today.",
        "te": "శుభోదయం! మీరు మరియు మీ పొలం ఈరోజు బాగున్నారని ఆశిస్తున్నాను.",
        "hi": "सुप्रभात! मुझे उम्मीद है आप और आपका खेत आज ठीक हैं।",
        "mr": "शुभ सकाळ! तुम्ही आणि तुमचे शेत आज ठीक आहेत अशी मला आशा आहे."
    },
    "greeting_afternoon": {
        "en": "Good afternoon! How is your crop holding up in today's weather?",
        "te": "శుభ మధ్యాహ్నం! ఈరోజు వాతావరణంలో మీ పంట ఎలా ఉంది?",
        "hi": "नमस्कार! आज के मौसम में आपकी फसल कैसी है?",
        "mr": "शुभ दुपार! आजच्या हवामानात तुमचे पीक कसे आहे?"
    },
    "greeting_evening": {
        "en": "Good evening! It's been a long day in the field. How may I help you?",
        "te": "శుభ సాయంత్రం! పొలంలో చాలా సుదీర్ఘమైన రోజు. నేను మీకు ఎలా సహాయం చేయగలను?",
        "hi": "शुभ संध्या! खेत में लंबा दिन रहा। मैं आपकी कैसे मदद कर सकता हूँ?",
        "mr": "शुभ संध्या! शेतात खूप दिवस गेला. मी तुम्हाला कशी मदत करू शकतो?"
    },
    "greeting_thanks": {
        "en": "You're very welcome. I'm always here to help you and your farm.",
        "te": "మీకు ఎప్పుడూ స్వాగతం. నేను ఎప్పుడూ మీకు మరియు మీ పొలానికి సహాయం చేయడానికి ఇక్కడ ఉన్నాను.",
        "hi": "आपका स्वागत है। मैं हमेशा आपकी और आपके खेत की मदद के लिए यहाँ हूँ।",
        "mr": "तुमचे स्वागत आहे. मी नेहमी तुम्हाला आणि तुमच्या शेताला मदत करण्यासाठी इथे आहे."
    },
    "casual_crop_today": {
        "en": "Today is a good day to check your fields. If you can, take a fresh photo of your crop and we will compare it with your previous observations.",
        "te": "ఈరోజు మీ పొలాలను తనిఖీ చేయడానికి మంచి రోజు. మీరు చేయగలిగితే, మీ పంట యొక్క కొత్త ఫోటో తీసి, మునుపటి పరిశీలనలతో పోల్చవచ్చు.",
        "hi": "आज आपके खेतों की जाँच करने का अच्छा दिन है। यदि आप कर सकें, तो अपनी फसल की एक ताज़ा तस्वीर लें और हम उसे पिछली टिप्पणियों से तुलना करेंगे।",
        "mr": "आज तुमच्या शेतांची तपासणी करण्यासाठी चांगला दिवस आहे. तुम्ही शकत असाल तर, तुमच्या पिकाचा ताजा फोटो घ्या आणि आम्ही तो मागील निरीक्षणांशी तुलना करू."
    },
    "casual_yesterday": {
        "en": "Yesterday I have no new observation recorded for you. If something looked different in the field, please make a fresh Crop Raksha observation today.",
        "te": "నిన్న మీ కోసం కొత్త పరిశీలన నమోదు కాలేదు. పొలంలో ఏదైనా భిన్నంగా కనిపించినట్లయితే, దయచేసి ఈరోజు కొత్త క్రాప్ రక్ష పరిశీలన చేయండి.",
        "hi": "कल मेरे पास आपके लिए कोई नई टिप्पणी दर्ज नहीं है। यदि खेत में कुछ अलग दिखा, तो कृपया आज एक नई क्रॉप रक्षा टिप्पणी करें।",
        "mr": "काल माझ्याकडे तुमच्यासाठी नवीन निरीक्षण नोंदवलेले नाही. शेतात काहीतरी वेगळे दिसल्यास, कृपया आज एक नवीन क्रॉप रक्षा निरीक्षण करा."
    },
    "casual_how_to_help": {
        "en": "I can help you with crop health questions, Crop Raksha observations, disease diagnosis, and a friendly chat about your farm. What would you like to do?",
        "te": "పంట ఆరోగ్య ప్రశ్నలు, క్రాప్ రక్ష పరిశీలనలు, వ్యాధి నిర్ధారణ మరియు మీ పొలం గురించి స్నేహపూర్వక చర్చలో నేను మీకు సహాయం చేయగలను. మీరు ఏమి చేయాలనుకుంటున్నారు?",
        "hi": "मैं फसल स्वास्थ्य प्रश्नों, क्रॉप रक्षा टिप्पणियों, रोग निदान और आपके खेत के बारे में मित्रवत बातचीत में आपकी मदद कर सकता हूँ। आप क्या करना चाहेंगे?",
        "mr": "मी पीक आरोग्य प्रश्न, क्रॉप रक्षा निरीक्षणे, रोग निदान आणि तुमच्या शेताबद्दल मैत्रीपूर्ण संभाषणात तुम्हाला मदत करू शकतो. तुम्हाला काय करायचे आहे?"
    },
    "casual_latest_observation": {
        "en": "Your latest Crop Raksha observation is on Day {day}, dated {date}.",
        "te": "మీ తాజా క్రాప్ రక్ష పరిశీలన రోజు {day}న, తేదీ {date}న నమోదైంది.",
        "hi": "आपका नवीनतम क्रॉप रक्षा अवलोकन दिन {day} पर, तारीख {date} को है।",
        "mr": "तुमचे नवीनतम क्रॉप रक्षा निरीक्षण दिवस {day} रोजी, दिनांक {date} रोजी आहे."
    },
    "casual_no_observation_yet": {
        "en": "No Crop Raksha observations have been recorded yet. You can add your first one in the Crop Raksha section.",
        "te": "ఇంకా క్రాప్ రక్ష పరిశీలనలు నమోదు కాలేదు. మీరు క్రాప్ రక్ష విభాగంలో మీ మొదటి పరిశీలనను జోడించవచ్చు.",
        "hi": "अभी तक कोई क्रॉप रक्षा अवलोकन दर्ज नहीं किया गया है। आप क्रॉप रक्षा अनुभाग में अपना पहला अवलोकन जोड़ सकते हैं।",
        "mr": "अद्याप कोणतेही क्रॉप रक्षा निरीक्षण नोंदवलेले नाही. तुम्ही क्रॉप रक्षा विभागात तुमचे पहिले निरीक्षण जोडू शकता."
    },
    "casual_diagnose_open": {
        "en": "To diagnose your crop with the AI, open the Diagnose section in the side menu and upload a clear leaf photo.",
        "te": "AI తో మీ పంటను నిర్ధారించడానికి, సైడ్ మెనూలోని డయాగ్నోసిస్ విభాగాన్ని తెరిచి స్పష్టమైన ఆకు ఫోటోను అప్‌లోడ్ చేయండి.",
        "hi": "AI से अपनी फसल का निदान करने के लिए, साइड मेनू में डायग्नोसिस अनुभाग खोलें और एक साफ पत्ते की तस्वीर अपलोड करें।",
        "mr": "AI सह तुमच्या पिकाचे निदान करण्यासाठी, साइड मेनूमधील निदान विभाग उघडा आणि स्पष्ट पानाचा फोटो अपलोड करा."
    },
    "casual_open_raksha": {
        "en": "To see your full Raksha history, open the Raksha section in the side menu.",
        "te": "మీ పూర్తి రక్ష చరిత్ర చూడటానికి, సైడ్ మెనూలోని రక్ష విభాగాన్ని తెరవండి.",
        "hi": "अपना पूरा रक्षा इतिहास देखने के लिए, साइड मेनू में रक्षा अनुभाग खोलें।",
        "mr": "तुमचा संपूर्ण रक्षा इतिहास पाहण्यासाठी, साइड मेनूमधील रक्षा विभाग उघडा."
    },
    "casual_dont_understand": {
        "en": "I can help with crop health, Raksha, diagnosis, and friendly farm talk. You can also tap the TALK button anytime.",
        "te": "పంట ఆరోగ్యం, రక్ష, నిర్ధారణ మరియు స్నేహపూర్వక పొలం సంభాషణతో నేను సహాయం చేయగలను. మీరు ఎప్పుడైనా TALK బటన్‌ను నొక్కవచ్చు.",
        "hi": "मैं फसल स्वास्थ्य, रक्षा, निदान और मित्रवत खेत बातचीत में मदद कर सकता हूँ। आप कभी भी TALK बटन दबा सकते हैं।",
        "mr": "मी पीक आरोग्य, रक्षा, निदान आणि मैत्रीपूर्ण शेत संभाषणात मदत करू शकतो. तुम्ही कधीही TALK बटण दाबू शकता."
    },

    # ── CROP / SAY-CROP TRANSLATIONS ─────────────────
    "say_crop_number": {
        "en": "Say the crop number or name.",
        "te": "పంట సంఖ్య లేదా పేరు చెప్పండి.",
        "hi": "फसल संख्या या नाम बोलें।",
        "mr": "पीक क्रमांक किंवा नाव सांगा."
    },
    "no_recent_observation": {
        "en": "No recent AI observation available for this crop.",
        "te": "ఈ పంట కోసం ఇటీవలి AI పరిశీలన అందుబాటులో లేదు.",
        "hi": "इस फसल के लिए हाल का AI अवलोकन उपलब्ध नहीं है।",
        "mr": "या पिकासाठी अलीकडील AI निरीक्षण उपलब्ध नाही."
    },
    "no_raksha_history": {
        "en": "There are no Raksha observations for this crop yet. Open Raksha in the side menu to record your first observation.",
        "te": "ఈ పంట కోసం ఇంకా రక్ష పరిశీలనలు లేవు. మీ మొదటి పరిశీలనను రికార్డ్ చేయడానికి సైడ్ మెనూలోని రక్షను తెరవండి.",
        "hi": "इस फसल के लिए अभी कोई रक्षा अवलोकन नहीं है। अपना पहला अवलोकन दर्ज करने के लिए साइड मेनू में रक्षा खोलें।",
        "mr": "या पिकासाठी अद्याप कोणतेही रक्षा निरीक्षण नाही. तुमचे पहिले निरीक्षण नोंदवण्यासाठी साइड मेनूमधील रक्षा उघडा."
    },
    "open_raksha_hint": {
        "en": "Open the Raksha section in the side menu to add your first observation.",
        "te": "మీ మొదటి పరిశీలనను జోడించడానికి సైడ్ మెనూలోని రక్ష విభాగాన్ని తెరవండి.",
        "hi": "अपना पहला अवलोकन जोड़ने के लिए साइड मेनू में रक्षा अनुभाग खोलें।",
        "mr": "तुमचे पहिले निरीक्षण जोडण्यासाठी साइड मेनूमधील रक्षा विभाग उघडा."
    },

    # ── UI MICROCOPY ──────────────────────────────────
    "crop_label": {
        "en": "Crop",
        "te": "పంట",
        "hi": "फसल",
        "mr": "पीक"
    },
    "language_label": {
        "en": "Language",
        "te": "భాష",
        "hi": "भाषा",
        "mr": "भाषा"
    },
    "open_raksha_action": {
        "en": "Open Raksha",
        "te": "రక్ష తెరవండి",
        "hi": "रक्षा खोलें",
        "mr": "रक्षा उघडा"
    },
    "check_raksha_action": {
        "en": "Check Raksha",
        "te": "రక్ష తనిఖీ చేయండి",
        "hi": "रक्षा जाँचें",
        "mr": "रक्षा तपासा"
    },
    "show_raksha_action": {
        "en": "Show Raksha observations",
        "te": "రక్ష పరిశీలనలు చూపించు",
        "hi": "रक्षा अवलोकन दिखाएँ",
        "mr": "रक्षा निरीक्षणे दाखवा"
    },

    # ── LATEST DAY / DATE TEXT (used in Casual Talk) ───
    "casual_latest_day": {
        "en": "Day {day}",
        "te": "రోజు {day}",
        "hi": "दिन {day}",
        "mr": "दिवस {day}"
    },

    # ── OPENING GUIDANCE ───────────────────────────────
    "guidance_title": {
        "en": "HOW TO USE",
        "te": "ఎలా ఉపయోగించాలి",
        "hi": "कैसे उपयोग करें",
        "mr": "कसे वापरावे"
    },
    "guidance_diagnosis_label": {
        "en": "🩺 Diagnosis",
        "te": "🩺 నిర్ధారణ",
        "hi": "🩺 रोग पहचान",
        "mr": "🩺 रोग निदान"
    },
    "guidance_diagnosis_desc": {
        "en": "Open Diagnosis → Upload a crop image → Get disease result",
        "te": "నిర్ధారణ తెరవండి → పంట చిత్రం అప్‌లోడ్ చేయండి → వ్యాధి ఫలితం పొందండి",
        "hi": "निदान खोलें → फसल की तस्वीर अपलोड करें → रोग परिणाम देखें",
        "mr": "निदान उघडा → पिकाचा फोटो अपलोड करा → रोग निकाल पाहा"
    },
    "guidance_raksha_label": {
        "en": "🌱 Crop Raksha",
        "te": "🌱 క్రాప్ రక్ష",
        "hi": "🌱 क्रॉप रक्षा",
        "mr": "🌱 क्रॉप रक्षा"
    },
    "guidance_raksha_desc": {
        "en": "Open Crop Raksha → Record daily observations → Track crop health",
        "te": "క్రాప్ రక్ష తెరవండి → ప్రతిరోజు పరిశీలనలు రికార్డ్ చేయండి → పంట ఆరోగ్యం ట్రాక్ చేయండి",
        "hi": "क्रॉप रक्षा खोलें → रोज़ाना अवलोकन दर्ज करें → फसल स्वास्थ्य ट्रैक करें",
        "mr": "क्रॉप रक्षा उघडा → दैनिक निरीक्षणे नोंदवा → पीक आरोग्य ट्रॅक कर"
    },

    # ── "WHAT CAN I SAY?" — VOICE COMMAND EXAMPLES ────
    # These are the natural phrases the existing handleVoiceInput()
    # recognition logic already understands. The opening screen shows
    # these to the farmer so they know exactly what to say.
    "what_can_i_say": {
        "en": "What can I say?",
        "te": "నేను ఏమి చెప్పగలను?",
        "hi": "मैं क्या बोल सकता हूँ?",
        "mr": "मी काय बोलू शकतो?"
    },
    "cmd_open_raksha": {
        "en": "Open Crop Raksha",
        "te": "క్రాప్ రక్ష తెరవండి",
        "hi": "क्रॉप रक्षा खोलें",
        "mr": "क्रॉप रक्षा उघडा"
    },
    "cmd_open_diagnosis": {
        "en": "Open Diagnosis",
        "te": "నిర్ధారణ తెరవండి",
        "hi": "निदान खोलें",
        "mr": "निदान उघडा"
    },
    "cmd_check_crop": {
        "en": "Check my crop",
        "te": "నా పంట తనిఖీ చేయండి",
        "hi": "मेरी फसल जाँचें",
        "mr": "माझे पीक तपासा"
    },
    "cmd_help": {
        "en": "Help",
        "te": "సహాయం",
        "hi": "मदद",
        "mr": "मदत"
    },
    "cmd_end_call": {
        "en": "End call",
        "te": "కాల్ ముగించండి",
        "hi": "कॉल समाप्त",
        "mr": "कॉल समाप्त करा"
    },
    "cmd_casual_talk": {
        "en": "How is my crop today?",
        "te": "ఈరోజు నా పంట ఎలా ఉంది?",
        "hi": "आज मेरी फसल कैसी है?",
        "mr": "आज माझे पीक कसे आहे?"
    },

    # ── RAKSHA STATUS VALUES (translated labels) ──────
    # These map raw status values stored in the raksha record
    # (e.g. "Healthy", "Minor Change", "Significant Change")
    # into the user's selected language. Unknown values
    # fall back to the original raw value via the renderer.
    "raksha_status_healthy": {
        "en": "Healthy",
        "te": "ఆరోగ్యంగా ఉంది",
        "hi": "स्वस्थ है",
        "mr": "निरोगी आहे"
    },
    "raksha_status_normal": {
        "en": "Normal",
        "te": "సాధారణం",
        "hi": "सामान्य",
        "mr": "सामान्य"
    },
    "raksha_status_minor_change": {
        "en": "Minor Change",
        "te": "స్వల్ప మార్పు",
        "hi": "मामूली बदलाव",
        "mr": "किरकोळ बदल"
    },
    "raksha_status_significant_change": {
        "en": "Significant Change",
        "te": "గణనీయమైన మార్పు",
        "hi": "महत्वपूर्ण बदलाव",
        "mr": "लक्षणीय बदल"
    },
    "raksha_status_label": {
        "en": "Status: {status}",
        "te": "స్థితి: {status}",
        "hi": "स्थिति: {status}",
        "mr": "स्थिती: {status}"
    },
    "raksha_day_label": {
        "en": "Day: {day}",
        "te": "రోజు: {day}",
        "hi": "दिन: {day}",
        "mr": "दिवस: {day}"
    },
    "raksha_date_label": {
        "en": "Date: {date}",
        "te": "తేదీ: {date}",
        "hi": "तारीख: {date}",
        "mr": "दिनांक: {date}"
    },
    "raksha_disease_label": {
        "en": "Disease: {disease}",
        "te": "వ్యాధి: {disease}",
        "hi": "रोग: {disease}",
        "mr": "रोग: {disease}"
    },
}
for _code in translations:
    translations[_code].update({k: v[_code] for k, v in _EXTRA_TRANSLATIONS.items()})

# ============================================================
# SERIALIZE DATA FOR JAVASCRIPT
# ============================================================

translations_json = json.dumps(
    translations,
    ensure_ascii=False
)

crops_json = json.dumps(
    crop_records,
    ensure_ascii=False
)


# ============================================================
# CROP NAME TRANSLATION MAP FOR JAVASCRIPT
# Mirrors CROP_NAME_MAP in language.py so the JS layer can
# use translate_crop_name() behavior without reimplementing.
# ============================================================

CROP_DISPLAY_MAP = {
    "en": {
        "banana": "Banana", "corn": "Corn", "cotton": "Cotton",
        "grape": "Grape", "mango": "Mango", "paddy": "Paddy",
        "rice": "Paddy", "potato": "Potato", "soybean": "Soybean",
        "tomato": "Tomato", "wheat": "Wheat"
    },
    "te": {
        "banana": "అరటి", "corn": "మొక్కజొన్న", "cotton": "పత్తి",
        "grape": "ద్రాక్ష", "mango": "మామిడి", "paddy": "వరి",
        "rice": "వరి", "potato": "బంగాళాదుంప", "soybean": "సోయాబీన్",
        "tomato": "టమాటా", "wheat": "గోధుమ"
    },
    "hi": {
        "banana": "केला", "corn": "मक्का", "cotton": "कपास",
        "grape": "अंगूर", "mango": "आम", "paddy": "धान",
        "rice": "धान", "potato": "आलू", "soybean": "सोयाबीन",
        "tomato": "टमाटर", "wheat": "गेहूं"
    },
    "mr": {
        "banana": "केळी", "corn": "मका", "cotton": "कापूस",
        "grape": "द्राक्षे", "mango": "आंबा", "paddy": "भात",
        "rice": "भात", "potato": "बटाटा", "soybean": "सोयाबीन",
        "tomato": "टोमॅटो", "wheat": "गहू"
    }
}

crop_display_map_json = json.dumps(
    CROP_DISPLAY_MAP,
    ensure_ascii=False
)


# ============================================================
# GADA / MACE — POWERFUL WARRIOR SYMBOL
# Pure gada (mace) visual — NO character image.
# Heavy metallic/bronze head, divine golden aura,
# strong silhouette, mature warrior aesthetic.
# ============================================================

ANJANEYA_SYMBOL_SVG = r"""
<svg viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" width="200" height="320">
  <defs>
    <!-- Outer divine aura -->
    <radialGradient id="gadaAura" cx="50%" cy="40%" r="60%">
      <stop offset="0%"  stop-color="#FFD700" stop-opacity="0.55"/>
      <stop offset="45%" stop-color="#FF8C00" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#FF4500" stop-opacity="0"/>
    </radialGradient>

    <!-- Gada head — heavy bronze / dark metal -->
    <radialGradient id="gadaHead" cx="35%" cy="30%" r="80%">
      <stop offset="0%"  stop-color="#5a4528"/>
      <stop offset="35%" stop-color="#3a2a18"/>
      <stop offset="100%" stop-color="#0a0604"/>
    </radialGradient>

    <!-- Highlight on gada head -->
    <radialGradient id="gadaHi" cx="30%" cy="25%" r="40%">
      <stop offset="0%"  stop-color="#d4a050" stop-opacity="0.85"/>
      <stop offset="60%" stop-color="#7a5020" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>

    <!-- Shaft — dark polished wood with golden caps -->
    <linearGradient id="shaftGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"  stop-color="#1a0e08"/>
      <stop offset="50%" stop-color="#3a2410"/>
      <stop offset="100%" stop-color="#1a0e08"/>
    </linearGradient>

    <!-- Gold band gradient -->
    <linearGradient id="goldBand" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"  stop-color="#7a5018"/>
      <stop offset="40%" stop-color="#FFD700"/>
      <stop offset="60%" stop-color="#FFD700"/>
      <stop offset="100%" stop-color="#7a5018"/>
    </linearGradient>

    <!-- Spike gradient -->
    <linearGradient id="spikeGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%"  stop-color="#E0B040"/>
      <stop offset="50%" stop-color="#A07820"/>
      <stop offset="100%" stop-color="#4a3008"/>
    </linearGradient>

    <!-- Soft inner glow filter -->
    <filter id="gadaGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Strong aura glow -->
    <filter id="auraBlur" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Outer aura (radiant backdrop) -->
  <ellipse cx="100" cy="130" rx="95" ry="125" fill="url(#gadaAura)"/>
  <circle cx="100" cy="110" r="78" fill="none" stroke="#FF8C00" stroke-width="0.8" opacity="0.35"/>
  <circle cx="100" cy="110" r="68" fill="none" stroke="#FFD700" stroke-width="0.4" opacity="0.55"/>

  <!--
    GADA / MACE — centered, vertical, imposing.
    Shaft: long vertical handle, dark wood with golden caps.
    Head: massive rounded bronze mace head with golden spikes.
  -->

  <!-- Shaft (long handle) -->
  <rect x="92" y="120" width="16" height="170" fill="url(#shaftGrad)" filter="url(#gadaGlow)"/>
  <!-- Shaft highlight line -->
  <rect x="96" y="120" width="3" height="170" fill="#5a3818" opacity="0.85"/>
  <rect x="93.5" y="120" width="1" height="170" fill="#a07040" opacity="0.6"/>

  <!-- Lower gold cap / pommel at base of shaft -->
  <ellipse cx="100" cy="292" rx="14" ry="6" fill="url(#goldBand)" filter="url(#gadaGlow)"/>
  <ellipse cx="100" cy="290" rx="11" ry="3" fill="#FFD700" opacity="0.9"/>
  <!-- Tiny base spike -->
  <polygon points="100,310 96,295 104,295" fill="url(#spikeGrad)" filter="url(#gadaGlow)"/>
  <polygon points="100,316 93,300 107,300" fill="url(#spikeGrad)" filter="url(#gadaGlow)"/>

  <!-- Mid-shaft gold band -->
  <rect x="90" y="180" width="20" height="6" fill="url(#goldBand)"/>
  <rect x="91" y="180" width="2" height="6" fill="#FFE680" opacity="0.9"/>

  <!-- Upper collar (where head meets shaft) -->
  <rect x="88" y="118" width="24" height="10" fill="url(#goldBand)" filter="url(#gadaGlow)"/>
  <rect x="88" y="118" width="3" height="10" fill="#FFE680" opacity="0.85"/>

  <!-- Gada head — massive rounded bronze mace head -->
  <!-- Outer dark rim -->
  <ellipse cx="100" cy="95" rx="62" ry="58" fill="url(#gadaHead)" filter="url(#gadaGlow)"/>
  <!-- Head body (slightly inset) -->
  <ellipse cx="100" cy="95" rx="56" ry="52" fill="#1a0e08"/>
  <!-- Head highlight -->
  <ellipse cx="78" cy="72" rx="32" ry="22" fill="url(#gadaHi)"/>
  <!-- Subtle vertical seam -->
  <line x1="100" y1="40" x2="100" y2="150" stroke="#000" stroke-width="0.5" opacity="0.6"/>
  <line x1="100" y1="40" x2="100" y2="150" stroke="#FFD700" stroke-width="0.3" opacity="0.25"/>

  <!-- Equatorial gold band across the head -->
  <ellipse cx="100" cy="95" rx="58" ry="6" fill="url(#goldBand)" opacity="0.85"/>
  <ellipse cx="100" cy="93" rx="55" ry="2" fill="#FFE680" opacity="0.6"/>

  <!-- Mace spikes — radiating outward (heavy, golden, dangerous) -->
  <g filter="url(#gadaGlow)">
    <!-- Top spikes -->
    <polygon points="100,32 92,50 108,50" fill="url(#spikeGrad)"/>
    <polygon points="100,28 89,48 111,48" fill="url(#spikeGrad)" opacity="0.85"/>
    <!-- Top-left & top-right spikes -->
    <polygon points="60,45 70,62 56,58" fill="url(#spikeGrad)"/>
    <polygon points="140,45 130,62 144,58" fill="url(#spikeGrad)"/>
    <!-- Side spikes (left & right) -->
    <polygon points="38,95 56,90 56,100" fill="url(#spikeGrad)"/>
    <polygon points="162,95 144,90 144,100" fill="url(#spikeGrad)"/>
    <polygon points="36,92 55,85 55,98" fill="url(#spikeGrad)" opacity="0.9"/>
    <polygon points="164,92 145,85 145,98" fill="url(#spikeGrad)" opacity="0.9"/>
    <!-- Bottom-left & bottom-right spikes -->
    <polygon points="60,145 70,128 56,132" fill="url(#spikeGrad)"/>
    <polygon points="140,145 130,128 144,132" fill="url(#spikeGrad)"/>
    <!-- Bottom spike -->
    <polygon points="100,158 92,140 108,140" fill="url(#spikeGrad)"/>
    <polygon points="100,162 89,142 111,142" fill="url(#spikeGrad)" opacity="0.85"/>
  </g>

  <!-- Tiny dot highlights on each spike tip -->
  <g fill="#FFE680" opacity="0.85">
    <circle cx="100" cy="28" r="1.6"/>
    <circle cx="56" cy="44" r="1.4"/>
    <circle cx="144" cy="44" r="1.4"/>
    <circle cx="36" cy="92" r="1.4"/>
    <circle cx="164" cy="92" r="1.4"/>
    <circle cx="56" cy="146" r="1.4"/>
    <circle cx="144" cy="146" r="1.4"/>
    <circle cx="100" cy="162" r="1.6"/>
  </g>

  <!-- Inner golden core glow -->
  <ellipse cx="100" cy="95" rx="22" ry="20" fill="#FFD700" opacity="0.18" filter="url(#auraBlur)"/>
  <ellipse cx="100" cy="95" rx="10" ry="9" fill="#FFE680" opacity="0.45"/>

  <!-- Top tip ornament -->
  <circle cx="100" cy="22" r="3" fill="#FFD700" filter="url(#auraBlur)"/>
  <circle cx="100" cy="22" r="1.5" fill="#FFFFFF" opacity="0.9"/>
</svg>
"""


# ============================================================
# IVR HTML
# ============================================================

page_html = r"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>Anjaneya Voice</title>


<style>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    margin: 0;
    padding: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: linear-gradient(160deg, #050d08, #0a1a0e, #071209);
    min-height: 100vh;
    color: white;
    -webkit-font-smoothing: antialiased;
}

.wrapper {
    width: 100%;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

/* ── Phone Frame ──────────────────────────────── */
.phone {
    width: 440px;
    max-width: 100%;
    min-height: 880px;
    border-radius: 38px;
    background: linear-gradient(160deg, #0c0c0c, #181818);
    border: 5px solid #252525;
    box-shadow:
        0 30px 80px rgba(0,0,0,0.8),
        0 0 60px rgba(0,0,0,0.5),
        inset 0 1px 0 rgba(255,255,255,0.05);
    overflow: hidden;
    position: relative;
}

/* ── Notch ───────────────────────────────────── */
.notch {
    width: 145px;
    height: 27px;
    background: #050505;
    border-radius: 0 0 18px 18px;
    margin: 0 auto;
}

/* ── Keyframe Animations ─────────────────────── */
@keyframes fadeSlideUp {
    0%   { opacity: 0; transform: translateY(24px); }
    100% { opacity: 1; transform: translateY(0); }
}

@keyframes fadeIn {
    0%   { opacity: 0; }
    100% { opacity: 1; }
}

@keyframes wavePulse {
    0%, 100% { transform: scaleY(0.25); }
    50%       { transform: scaleY(1.0); }
}

@keyframes spinWheel {
    0%   { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

@keyframes blinkReady {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.4; }
}

@keyframes glowRing {
    0%, 100% { box-shadow: 0 0 8px rgba(255,165,0,0.3); }
    50%       { box-shadow: 0 0 20px rgba(255,140,0,0.7); }
}

@keyframes titleGlow {
    0%, 100% { text-shadow: 0 0 10px rgba(255,165,0,0.4); }
    50%       { text-shadow: 0 0 20px rgba(255,140,0,0.8); }
}

/* ── Animation Classes ────────────────────────── */
.anim-1 { animation: fadeSlideUp 0.45s ease-out 0.1s both; }
.anim-2 { animation: fadeSlideUp 0.45s ease-out 0.25s both; }
.anim-3 { animation: fadeSlideUp 0.45s ease-out 0.40s both; }
.anim-4 { animation: fadeSlideUp 0.45s ease-out 0.55s both; }
.anim-5 { animation: fadeSlideUp 0.45s ease-out 0.70s both; }
.anim-fade { animation: fadeIn 0.4s ease-out both; }

/* ── Header ──────────────────────────────────── */
.header {
    padding: 18px 25px 12px;
    text-align: center;
}

.anjaneya-title {
    font-size: 28px;
    font-weight: bold;
    color: #FFD700;
    letter-spacing: 2px;
    animation: titleGlow 3s ease-in-out infinite;
}

.anjaneya-subtitle {
    font-size: 13px;
    color: #9a8a6a;
    margin-top: 4px;
    letter-spacing: 0.5px;
}

/* ── Info Bar ─────────────────────────────────── */
.info-bar {
    margin: 0 20px 8px;
    padding: 10px 16px;
    border-radius: 14px;
    background: linear-gradient(135deg, #0f1e12, #162414);
    border: 1px solid #1e3820;
    font-size: 12px;
    color: #9abf9c;
    line-height: 1.8;
}

.info-bar .info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.info-bar .info-label {
    color: #5a9e64;
    font-weight: 600;
}

.info-bar .info-value {
    color: #c8e8c4;
    font-weight: 500;
}

/* ── Status Bar ──────────────────────────────── */
.status-bar {
    margin: 0 20px 8px;
    padding: 10px 16px;
    border-radius: 12px;
    text-align: center;
    font-size: 13px;
    font-weight: 600;
    transition: all 0.35s ease;
}

.status-bar.sleeping {
    color: #7ad89e;
    background: #0e1e12;
    border: 1px solid #1a3822;
}
.status-bar.listening {
    color: #ff7070;
    background: #1e0c0c;
    border: 1px solid #3a1515;
}
.status-bar.processing {
    color: #f0c050;
    background: #1e160a;
    border: 1px solid #3a2a10;
}
.status-bar.speaking {
    color: #80c8ff;
    background: #0a1420;
    border: 1px solid #142038;
}
.status-bar.ended {
    color: #888;
    background: #141414;
    border: 1px solid #2a2a2a;
}

/* ── Voice Status Line ───────────────────────── */
.voice-status {
    margin: 0 20px 10px;
    padding: 8px 14px;
    border-radius: 10px;
    background: #0a120b;
    border: 1px solid #1a2e1c;
    color: #5a8a60;
    font-size: 11px;
    text-align: center;
    min-height: 34px;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* ── Main Screen ──────────────────────────────── */
.screen {
    margin: 0 18px 12px;
    min-height: 220px;
    border-radius: 24px;
    background: linear-gradient(160deg, #070d07, #0c170d);
    border: 1px solid #1a3020;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.3s ease;
}

.screen-label {
    color: #3d7a4a;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.message {
    font-size: 15px;
    line-height: 1.6;
    white-space: pre-line;
    color: #d0e8d5;
    min-height: 60px;
}

.selected {
    margin-top: 8px;
    min-height: 18px;
    color: #4a8a58;
    font-size: 11px;
}

/* ── Center Area ──────────────────────────────── */
.center-area {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 14px 0 8px;
    min-height: 140px;
}

/* TALK Button */
.talk-btn {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: none;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
    transition: all 0.2s ease;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: white;
    position: relative;
    overflow: hidden;
}

.talk-btn.ready {
    background: linear-gradient(145deg, #1a8f42, #0e5c2a);
    box-shadow: 0 8px 30px rgba(30,160,60,0.35), 0 0 0 2px rgba(255,255,255,0.1);
    animation: glowRing 2.5s ease-in-out infinite;
}

.talk-btn.listening {
    background: linear-gradient(145deg, #c03030, #8a1a1a);
    box-shadow: 0 0 0 0 rgba(255,60,60,0.7);
    animation: pulseListen 1.1s ease-in-out infinite;
}

@keyframes pulseListen {
    0%   { box-shadow: 0 0 0 0 rgba(255,60,60,0.7); transform: scale(1); }
    70%  { box-shadow: 0 0 0 22px rgba(255,60,60,0); transform: scale(1.04); }
    100% { box-shadow: 0 0 0 0 rgba(255,60,60,0); transform: scale(1); }
}

.talk-btn.processing {
    background: linear-gradient(145deg, #c09020, #8a6010);
    animation: spinWheel 1.5s linear infinite;
}

.talk-btn.speaking {
    background: linear-gradient(145deg, #2060c0, #103080);
    box-shadow: 0 8px 30px rgba(40,100,220,0.4);
}

.talk-btn.ended {
    background: linear-gradient(145deg, #3a3a3a, #1a1a1a);
    cursor: default;
    box-shadow: none;
    opacity: 0.6;
}

.talk-btn:not(.listening):not(.processing):not(.ended):hover {
    transform: scale(1.05);
}

.talk-btn:active:not(.ended) {
    transform: scale(0.96);
}

.talk-icon {
    font-size: 32px;
    line-height: 1;
}

.talk-label {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
}

.talk-sublabel {
    font-size: 10px;
    opacity: 0.8;
    font-weight: 400;
}

/* Wave bars for listening */
.wave-bars {
    display: flex;
    align-items: center;
    gap: 4px;
    height: 36px;
}

.wave-bar {
    width: 5px;
    background: white;
    border-radius: 3px;
    animation: wavePulse 0.8s ease-in-out infinite;
}

.wave-bar:nth-child(1) { animation-delay: 0s; }
.wave-bar:nth-child(2) { animation-delay: 0.1s; }
.wave-bar:nth-child(3) { animation-delay: 0.2s; }
.wave-bar:nth-child(4) { animation-delay: 0.3s; }
.wave-bar:nth-child(5) { animation-delay: 0.4s; }

/* Spinning gear for processing */
.gear-icon {
    font-size: 36px;
    animation: spinWheel 1.5s linear infinite;
}

/* Waveform for speaking */
.speak-bars {
    display: flex;
    align-items: center;
    gap: 3px;
    height: 32px;
}

.speak-bar {
    width: 4px;
    background: white;
    border-radius: 2px;
    animation: wavePulse 0.6s ease-in-out infinite;
}

.speak-bar:nth-child(1) { animation-delay: 0s; }
.speak-bar:nth-child(2) { animation-delay: 0.08s; }
.speak-bar:nth-child(3) { animation-delay: 0.16s; }
.speak-bar:nth-child(4) { animation-delay: 0.24s; }
.speak-bar:nth-child(5) { animation-delay: 0.32s; }
.speak-bar:nth-child(6) { animation-delay: 0.4s; }
.speak-bar:nth-child(7) { animation-delay: 0.48s; }

/* Mic label */
.mic-label {
    text-align: center;
    color: #6a8a6a;
    font-size: 11px;
    margin-top: 10px;
    min-height: 16px;
    font-weight: 500;
}

/* ── Controls Row ─────────────────────────────── */
.controls-row {
    display: flex;
    justify-content: center;
    padding: 8px 20px 14px;
    gap: 12px;
}

.btn-control {
    flex: 1;
    max-width: 175px;
    padding: 12px 16px;
    border: none;
    border-radius: 14px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    color: white;
    box-shadow: 0 4px 14px rgba(0,0,0,0.4);
}

.btn-end-call {
    background: linear-gradient(145deg, #c03030, #8a1a1a);
    border: 1px solid #7a1010;
}

.btn-end-call:hover {
    background: linear-gradient(145deg, #d84040, #a02020);
    transform: translateY(-1px);
}

.btn-end-call:active {
    transform: translateY(0);
}

.btn-end-call:disabled {
    opacity: 0.35;
    cursor: not-allowed;
}

/* ── Footer ─────────────────────────────────── */
.footer {
    text-align: center;
    padding: 0 20px 20px;
    font-size: 10px;
    color: #3a4a3a;
    line-height: 1.5;
}

.footer .footer-note {
    color: #4a7a4e;
    font-weight: 500;
    margin-top: 3px;
}

.footer .footer-note2 {
    color: #2a3a2a;
    font-size: 9px;
    margin-top: 2px;
}

/* ── Overlays ─────────────────────────────────── */
.overlay {
    position: absolute;
    inset: 0;
    z-index: 20;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 30px;
    background: radial-gradient(ellipse at 50% 30%, #0d2210 0%, #050d07 100%);
}

.ok-button {
    width: 130px;
    height: 130px;
    border-radius: 50%;
    border: none;
    background: linear-gradient(145deg, #1fa050, #0e6830);
    color: white;
    font-size: 26px;
    font-weight: bold;
    letter-spacing: 1px;
    cursor: pointer;
    box-shadow: 0 10px 40px rgba(30,180,70,0.4), 0 0 0 3px rgba(255,255,255,0.08);
    transition: all 0.2s ease;
    animation: glowRing 2.5s ease-in-out infinite;
}

.ok-button:hover {
    transform: scale(1.06);
    box-shadow: 0 14px 50px rgba(30,200,80,0.5), 0 0 0 4px rgba(255,255,255,0.1);
}

.ok-button:active {
    transform: scale(0.95);
}

.overlay-caption {
    margin-top: 22px;
    color: #7aaa7e;
    font-size: 13px;
    max-width: 260px;
    line-height: 1.55;
}

/* Splash overlay */
#splashOverlay {
    display: none;
}

.splash-text {
    margin-top: 18px;
    font-size: 16px;
    color: #FFD700;
    letter-spacing: 2px;
    font-weight: bold;
    animation: titleGlow 1.5s ease-in-out infinite;
}

/* Ended overlay */
#endedOverlay {
    display: none;
}

.ended-icon {
    font-size: 64px;
    margin-bottom: 16px;
}

.ended-title {
    font-size: 22px;
    color: #888;
    font-weight: 600;
    margin-bottom: 12px;
}

.ended-message {
    font-size: 13px;
    color: #555;
    max-width: 260px;
    line-height: 1.5;
    margin-bottom: 24px;
}

.restart-btn {
    width: 170px;
    height: 58px;
    border-radius: 29px;
    border: none;
    background: linear-gradient(145deg, #1a8f42, #0e5c2a);
    color: white;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 8px 30px rgba(30,160,60,0.35);
    transition: all 0.2s ease;
    animation: glowRing 2.5s ease-in-out infinite;
}

.restart-btn:hover {
    transform: scale(1.04);
}

.restart-btn:active {
    transform: scale(0.96);
}

/* ── Language Selection ──────────────────────── */
.lang-section {
    margin: 0 18px 8px;
    animation: fadeSlideUp 0.45s ease-out 0.6s both;
}

.lang-title {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #3d6a40;
    margin-bottom: 8px;
    text-align: center;
}

.lang-buttons {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
}

.lang-btn {
    padding: 10px 8px;
    border-radius: 12px;
    border: 1.5px solid #1a2e1c;
    background: #0c1a0e;
    color: #6a9a6a;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    text-align: center;
}

.lang-btn:hover {
    background: #122214;
    border-color: #2a4a2a;
    color: #8aba8a;
    transform: translateY(-1px);
}

.lang-btn.selected-lang {
    background: linear-gradient(135deg, #0e3018, #1a5028);
    border-color: #3a8a48;
    color: #8ade8a;
    box-shadow: 0 0 10px rgba(50,180,70,0.15);
}

.lang-btn .lang-native {
    display: block;
    font-size: 14px;
    margin-bottom: 2px;
}

.lang-btn .lang-eng {
    font-size: 10px;
    opacity: 0.6;
}

/* ── Crop Selection ───────────────────────────── */
.crop-section {
    margin: 0 18px 8px;
    animation: fadeSlideUp 0.45s ease-out 0.75s both;
}

.crop-title {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #3d6a40;
    margin-bottom: 8px;
    text-align: center;
}

.crop-display {
    text-align: center;
    padding: 8px 14px;
    border-radius: 12px;
    background: #0c1a0e;
    border: 1.5px solid #1a2e1c;
    color: #7aaa7a;
    font-size: 15px;
    font-weight: 600;
}

/* ready blinking dot */
.ready-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #4ade80;
    margin-right: 6px;
    animation: blinkReady 1.8s ease-in-out infinite;
    vertical-align: middle;
}

/* ── What Can I Say — Voice Command Reference ─── */
.commands-section {
    margin: 0 18px 12px;
    padding: 14px 14px 12px;
    border-radius: 16px;
    background: linear-gradient(135deg, #0f1e12, #162414);
    border: 1px solid #1e3820;
    animation: fadeSlideUp 0.45s ease-out 0.6s both;
}

.commands-title {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 2.5px;
    color: #5a9e64;
    font-weight: 700;
    margin-bottom: 14px;
    text-align: center;
}

.commands-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
}

.cmd-row {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    padding: 10px 10px;
    border-radius: 12px;
    background: rgba(7, 17, 10, 0.55);
    border: 1px solid #1a3020;
    transition: all 0.2s ease;
    min-height: 56px;
}

.cmd-row:hover {
    background: rgba(20, 38, 22, 0.75);
    border-color: #2a5a32;
    transform: translateY(-1px);
}

.cmd-icon {
    font-size: 18px;
    line-height: 1.2;
    flex-shrink: 0;
    width: 22px;
    text-align: center;
}

.cmd-content {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.cmd-phrase {
    font-size: 12.5px;
    font-weight: 700;
    color: #d8f0d8;
    line-height: 1.3;
    word-break: break-word;
    hyphens: auto;
}

.cmd-feature {
    font-size: 10px;
    color: #6a9a6e;
    margin-top: 2px;
    letter-spacing: 0.3px;
    text-transform: uppercase;
    font-weight: 600;
}

/* ── Compact Language Mini-Bar ─────────────────── */
.lang-mini-bar {
    margin: 0 18px 8px;
    display: flex;
    justify-content: center;
    animation: fadeSlideUp 0.45s ease-out 0.75s both;
}

.lang-mini-buttons {
    display: flex;
    gap: 6px;
}

.lang-mini-btn {
    padding: 5px 12px;
    border-radius: 8px;
    border: 1px solid #1a2e1c;
    background: #0c1a0e;
    color: #5a8a5e;
    font-size: 11px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    letter-spacing: 0.5px;
}

.lang-mini-btn:hover {
    background: #122214;
    border-color: #2a4a2a;
    color: #8aba8a;
}

.lang-mini-btn.selected-mini {
    background: linear-gradient(135deg, #0e3018, #1a5028);
    border-color: #3a8a48;
    color: #8ade8a;
}

/* ── Responsive Sizing ────────────────────────── */
@media (max-width: 420px) {
    .anjaneya-title {
        font-size: 24px;
    }
    .anjaneya-subtitle {
        font-size: 12px;
    }
}

</style>

</head>


<body>


<div class="wrapper">

<div class="phone" id="phoneContainer">

<!-- Notch -->
<div class="notch"></div>

<!-- Header: Anjaneya Title only (no symbol/character image) -->
<div class="header anim-1">
    <div class="anjaneya-title">__ANJANEYA_WORDMARK__</div>
    <div class="anjaneya-subtitle">__ANJANEYA_SUBTITLE__</div>
</div>

<!-- Info Bar -->
<div class="info-bar anim-2" id="infoBar">
    <div class="info-row">
        <span class="info-label">__LANG_LABEL__</span>
        <span class="info-value" id="currentLang">__LANG_VALUE__</span>
    </div>
    <div class="info-row">
        <span class="info-label">__CROP_LABEL__</span>
        <span class="info-value" id="currentCrop">__CROP_VALUE__</span>
    </div>
</div>

<!-- Status Bar -->
<div class="status-bar sleeping anim-2" id="statusBar">
    <span id="statusText">__STATUS_READY__</span>
</div>

<!-- Voice Status -->
<div class="voice-status anim-3" id="voiceStatusLine">
    __VOICE_STATUS__
</div>

<!-- Main Screen -->
<div class="screen anim-3">

    <div>
        <div class="screen-label">__SCREEN_LABEL__</div>
        <div class="message" id="messageArea">__MESSAGE_INITIAL__</div>
        <div class="selected" id="selectedLine"></div>
    </div>

    <!-- Center: TALK Button -->
    <div class="center-area">
        <button
            class="talk-btn ready"
            id="talkBtn"
            onclick="onTalkTap()"
        >
            <div class="talk-icon" id="talkIcon">__TALK_ICON__</div>
            <div class="talk-label" id="talkLabel">__TALK_LABEL__</div>
            <div class="talk-sublabel" id="talkSublabel">__TALK_SUBLABEL__</div>
        </button>
        <div class="mic-label" id="micLabel">__MIC_LABEL__</div>
    </div>

</div>

<!-- What Can I Say? — Voice Command Reference -->
<div class="commands-section" id="commandsSection">
    <div class="commands-title">__WHAT_CAN_I_SAY__</div>
    <div class="commands-grid">

        <div class="cmd-row" id="cmd-raksha">
            <span class="cmd-icon">🌱</span>
            <div class="cmd-content">
                <div class="cmd-phrase" id="cmd-raksha-text">__CMD_RAKSHA__</div>
                <div class="cmd-feature">Crop Raksha</div>
            </div>
        </div>

        <div class="cmd-row" id="cmd-diagnosis">
            <span class="cmd-icon">🔬</span>
            <div class="cmd-content">
                <div class="cmd-phrase" id="cmd-diagnosis-text">__CMD_DIAGNOSIS__</div>
                <div class="cmd-feature">Diagnosis</div>
            </div>
        </div>

        <div class="cmd-row" id="cmd-status">
            <span class="cmd-icon">📊</span>
            <div class="cmd-content">
                <div class="cmd-phrase" id="cmd-status-text">__CMD_STATUS__</div>
                <div class="cmd-feature">Crop Status</div>
            </div>
        </div>

        <div class="cmd-row" id="cmd-help">
            <span class="cmd-icon">❓</span>
            <div class="cmd-content">
                <div class="cmd-phrase" id="cmd-help-text">__CMD_HELP__</div>
                <div class="cmd-feature">Help</div>
            </div>
        </div>

        <div class="cmd-row" id="cmd-end">
            <span class="cmd-icon">📞</span>
            <div class="cmd-content">
                <div class="cmd-phrase" id="cmd-end-text">__CMD_END__</div>
                <div class="cmd-feature">End Call</div>
            </div>
        </div>

        <div class="cmd-row" id="cmd-talk">
            <span class="cmd-icon">💬</span>
            <div class="cmd-content">
                <div class="cmd-phrase" id="cmd-talk-text">__CMD_TALK__</div>
                <div class="cmd-feature">Casual Talk</div>
            </div>
        </div>

    </div>
</div>

<!-- Language Switcher -->
<div class="lang-mini-bar" id="langMiniBar">
    <div class="lang-mini-buttons">
        <button class="lang-mini-btn" id="lang-mini-en" onclick="selectLang('en')">EN</button>
        <button class="lang-mini-btn" id="lang-mini-te" onclick="selectLang('te')">తె</button>
        <button class="lang-mini-btn" id="lang-mini-hi" onclick="selectLang('hi')">हि</button>
        <button class="lang-mini-btn" id="lang-mini-mr" onclick="selectLang('mr')">म</button>
    </div>
</div>

<!-- Crop Display -->
<div class="crop-section anim-4">
    <div class="crop-title">__CROP_FIELD_TITLE__</div>
    <div class="crop-display" id="cropDisplay">__CROP_DISPLAY__</div>
</div>

<!-- Controls: End Call -->
<div class="controls-row anim-4">
    <button
        class="btn-control btn-end-call"
        id="endCallBtn"
        onclick="onEndCallTap()"
        disabled
    >
        __END_CALL_LABEL__
    </button>
</div>

<!-- Footer -->
<div class="footer anim-5">
    __FOOTER_NOTICE__
    <div class="footer-note">__FOOTER_NOTICE2__</div>
    <div class="footer-note2">__FOOTER_NOTICE3__</div>
</div>

<!-- Start Overlay (first open) -->
<div class="overlay" id="startOverlay">
    <button class="ok-button" id="okButton" onclick="beginFlow()">
        __OPEN_BUTTON__
    </button>
    <div class="overlay-caption">__OPEN_CAPTION__</div>
</div>

<!-- Splash Overlay (after OK) -->
<div class="overlay" id="splashOverlay">
    <div class="splash-text">__SPLASH_TEXT__</div>
</div>

<!-- Ended Overlay -->
<div class="overlay" id="endedOverlay">
    <div class="ended-icon">__PHONE_ICON__</div>
    <div class="ended-title">__ENDED_TITLE__</div>
    <div class="ended-message">__ENDED_MESSAGE__</div>
    <button class="restart-btn" onclick="restartFromEnded()">__RESTART_LABEL__</button>
</div>

</div><!-- /phone -->

</div><!-- /wrapper -->


<script>


// ============================================================
// DATA FROM PYTHON
// ============================================================

const LANGUAGES = __LANGUAGES__;
const CROPS     = __CROPS__;
const CROP_MAP  = __CROP_MAP__;


// ============================================================
// TRANSLATE CROP NAME (for displayed + spoken crop names)
// ============================================================

// Returns the translated crop name for the current UI language.
// Falls back to English if no mapping exists.
function translateCropName(cropName) {
    if (!cropName) return cropName;
    const langMap = CROP_MAP[language] || CROP_MAP["en"] || {};
    const key = cropName.toLowerCase().trim();
    return langMap[key] || cropName;
}


// ============================================================
// LANGUAGE LOCALES (for speech recognition)
// ============================================================

const LANGUAGE_LOCALES = {
    "en": ["en-IN","en-US","en-GB","en"],
    "te": ["te-IN","te"],
    "hi": ["hi-IN","hi"],
    "mr": ["mr-IN","mr"]
};


// ============================================================
// STATE VARIABLES
// ============================================================

let language = "en";        // Current language code
let sessionActive = false;  // True when in a call session
let callEnded = false;      // True when call has ended
let voiceState = "idle";    // idle | listening | processing | speaking

let recognition    = null;
let speechRecAvail = false;
let speechSynAvail = false;
let availableVoices = [];

let listening    = false;
let resultSeen   = false;

let sessionId       = 0;   // Increments on session change — kills stale callbacks
let pendingTimeouts = [];  // setTimeout IDs for safe cancellation


// ============================================================
// ELEMENT REFS
// ============================================================

const statusBar       = document.getElementById("statusBar");
const statusText      = document.getElementById("statusText");
const voiceStatusLine = document.getElementById("voiceStatusLine");
const messageArea     = document.getElementById("messageArea");
const selectedLine    = document.getElementById("selectedLine");
const talkBtn         = document.getElementById("talkBtn");
const talkIcon       = document.getElementById("talkIcon");
const talkLabel      = document.getElementById("talkLabel");
const talkSublabel   = document.getElementById("talkSublabel");
const micLabel       = document.getElementById("micLabel");
const endCallBtn      = document.getElementById("endCallBtn");
const currentLang     = document.getElementById("currentLang");
const currentCrop     = document.getElementById("currentCrop");
const startOverlay    = document.getElementById("startOverlay");
const splashOverlay   = document.getElementById("splashOverlay");
const endedOverlay    = document.getElementById("endedOverlay");
const langBtns        = {
    en: document.getElementById("lang-en"),
    te: document.getElementById("lang-te"),
    hi: document.getElementById("lang-hi"),
    mr: document.getElementById("lang-mr")
};
const langMiniBtns    = {
    en: document.getElementById("lang-mini-en"),
    te: document.getElementById("lang-mini-te"),
    hi: document.getElementById("lang-mini-hi"),
    mr: document.getElementById("lang-mini-mr")
};


// ============================================================
// TRANSLATION (uses Python-translated strings embedded in JS LANGUAGES)
// ============================================================

function T(key, vars) {
    let text = (LANGUAGES[language] && LANGUAGES[language][key]) ||
               (LANGUAGES["en"]      && LANGUAGES["en"][key])      || key;
    if (vars) {
        Object.keys(vars).forEach(function(k) {
            text = text.replace(new RegExp("{"+k+"}","g"), vars[k]);
        });
    }
    return text;
}


// ============================================================
// SPEECH SYNTHESIS
// ============================================================

function loadVoices() {
    if (!("speechSynthesis" in window)) {
        speechSynAvail = false;
        return;
    }
    availableVoices = window.speechSynthesis.getVoices();
    speechSynAvail = true;
}

if ("speechSynthesis" in window) {
    window.speechSynthesis.onvoiceschanged = loadVoices;
    loadVoices();
}

function findVoice(langCode) {
    if (!availableVoices.length) return null;
    const locales = LANGUAGE_LOCALES[langCode] || [];
    for (const loc of locales) {
        const found = availableVoices.find(function(v) {
            return v.lang.toLowerCase() === loc.toLowerCase();
        });
        if (found) return found;
    }
    const prefix = (langCode + "-").toLowerCase();
    const same = availableVoices.find(function(v) {
        return v.lang.toLowerCase().startsWith(prefix);
    });
    if (same) return same;
    const base = availableVoices.find(function(v) {
        return v.lang.toLowerCase() === langCode.toLowerCase();
    });
    return base || null;
}

// ── Online TTS Audio Element ──────────────────────────
// components.html uses srcdoc — window.location.href === "about:blank"
// so we cannot fetch from it.  Instead we navigate window.parent.location
// (same-origin Streamlit page URL) which triggers a Python rerun.
// Python embeds the base64 MP3 audio as window.__TTS_DATA__ in the
// response HTML.  This file reads it synchronously on page load,
// verifies the session ID, and plays the audio.
let ttsAudio = null;
let ttsNavSid = 0;       // sessionId that started the last navigation
let originalPageUrl = ""; // saved pre-navigation URL for returning

function cancelOnlineTTS() {
    if (ttsAudio) {
        ttsAudio.pause();
        ttsAudio.src = "";
        ttsAudio = null;
    }
    ttsNavSid = 0;
}

// Called from window.onload — checks whether Python left TTS data
// in window.__TTS_DATA__ for our session.  Runs synchronously so
// the audio plays immediately when the page loads.
function checkTtsData() {
    const sid = ttsNavSid;
    if (sid !== sessionId || !sessionActive) return;
    const raw = window.__TTS_DATA__;
    if (!raw) return;
    // Verify SID matches the session that requested this audio
    if (String(raw.sid) !== String(sid)) return;
    // Consume and clear — one-shot
    delete window.__TTS_DATA__;
    playOnlineAudio(raw.audio, sid);
}

function playOnlineAudio(b64Audio, sid) {
    if (sid !== sessionId || !sessionActive) return;
    try {
        const binary = atob(b64Audio);
        const bytes  = new Uint8Array(binary.length);
        for (let i = 0; i < binary.length; i++) {
            bytes[i] = binary.charCodeAt(i);
        }
        const blob  = new Blob([bytes], { type: "audio/mpeg" });
        const audioUrl = URL.createObjectURL(blob);
        const audio = new Audio(audioUrl);
        ttsAudio = audio;
        setVoiceState("speaking");
        audio.onended = function() {
            if (sid !== sessionId || !sessionActive) return;
            URL.revokeObjectURL(audioUrl);
            ttsAudio = null;
            // Return to parent page after audio ends
            if (window.parent.location.href !== originalPageUrl) {
                window.parent.location.replace(originalPageUrl);
            }
            setVoiceState("idle");
        };
        audio.onerror = function() {
            if (sid !== sessionId || !sessionActive) return;
            URL.revokeObjectURL(audioUrl);
            ttsAudio = null;
            if (window.parent.location.href !== originalPageUrl) {
                window.parent.location.replace(originalPageUrl);
            }
            setVoiceState("idle");
        };
        audio.play().catch(function() {
            if (sid !== sessionId || !sessionActive) return;
            URL.revokeObjectURL(audioUrl);
            ttsAudio = null;
            if (window.parent.location.href !== originalPageUrl) {
                window.parent.location.replace(originalPageUrl);
            }
            setVoiceState("idle");
        });
    } catch(e) {
        if (sid !== sessionId || !sessionActive) return;
        if (window.parent.location.href !== originalPageUrl) {
            window.parent.location.replace(originalPageUrl);
        }
        setVoiceState("idle");
    }
}

function speak(text) {
    if (!text) return false;
    const sid = sessionId;

    // ── Try browser speechSynthesis first (en, hi) ────────
    if (speechSynAvail) {
        const voice = findVoice(language);
        if (voice) {
            window.speechSynthesis.cancel();
            cancelOnlineTTS();

            const utt = new SpeechSynthesisUtterance(text);
            utt.voice  = voice;
            utt.lang    = voice.lang;
            utt.rate    = 0.88;
            utt.pitch   = 1.0;
            utt.volume  = 1.0;

            utt.onstart = function() {
                if (sid !== sessionId || !sessionActive) return;
                setVoiceState("speaking");
            };

            utt.onend = function() {
                if (sid !== sessionId || !sessionActive) return;
                setVoiceState("idle");
            };

            utt.onerror = function() {
                if (sid !== sessionId || !sessionActive) return;
                setVoiceState("idle");
            };

            window.speechSynthesis.speak(utt);
            return true;
        }
    }

    // ── No browser voice (te, mr) — navigate parent for TTS ─
    // components.html iframe is srcdoc (about:blank).  We navigate
    // window.parent.location to a TTS URL, triggering a Python rerun.
    // Python embeds the base64 MP3 as window.__TTS_DATA__ in the
    // response HTML.  checkTtsData() reads it synchronously on page load.
    if (language !== "te" && language !== "mr") {
        return false;
    }

    cancelOnlineTTS();

    const encodedText = encodeURIComponent(text);
    const baseUrl = window.parent.location.href.replace(/[#?].*$/, "");
    const ttsUrl = (
        baseUrl
        + "?_tts_text=" + encodedText
        + "&_tts_lang=" + language
        + "&_tts_sid=" + sid
    );

    // Remember where we need to return to
    originalPageUrl = window.parent.location.href.replace(/[#?].*$/, "");

    // Track this navigation by sessionId — checkTtsData() uses it on load
    ttsNavSid = sid;

    // Set state immediately — checkTtsData() will play the audio
    setVoiceState("speaking");

    // Navigate parent to TTS URL (same-origin, triggers Python rerun)
    window.parent.location.replace(ttsUrl);

    return true;
}


// ============================================================
// UPDATE VOICE STATUS LINE
// ============================================================

function updateVoiceStatus(noVoice) {
    if (noVoice) {
        voiceStatusLine.textContent = T("voice_not_installed");
        return;
    }
    // Telugu and Marathi use online TTS (no browser voice)
    if (language === "te" || language === "mr") {
        voiceStatusLine.textContent = "🌐 " + LANGUAGES[language].name + " — Online TTS (Internet required)";
        return;
    }
    const v = findVoice(language);
    if (v) {
        voiceStatusLine.textContent = "🔊 " + LANGUAGES[language].name + " — " + v.name + " (" + v.lang + ")";
    } else {
        voiceStatusLine.textContent = "⚠️ " + LANGUAGES[language].name + " — " + T("voice_not_installed");
    }
}

function updateFooterNotice() {
    const notice3 = document.querySelector(".footer .footer-note2");
    if (!notice3) return;
    if (language === "te" || language === "mr") {
        notice3.textContent = T("online_tts_notice");
    } else {
        notice3.textContent = T("voice_unavailable_message");
    }
}


// ============================================================
// VOICE STATE MACHINE
// ============================================================

// States: idle | listening | processing | speaking
// Transitions:
//   idle        --(TALK tap)--> listening
//   listening   --(speech detected)--> processing
//   listening   --(no speech/error)--> idle
//   processing  --(after delay)--> speaking
//   speaking    --(onend)--> idle
//   ANY         --(End Call)--> ended

function setVoiceState(state) {
    if (callEnded) return;

    voiceState = state;

    // Remove all state classes
    statusBar.className = "status-bar";
    talkBtn.className   = "talk-btn";

    if (state === "idle") {
        statusBar.classList.add("sleeping");
        statusText.textContent = "● " + T("voice_state_sleeping");
        talkBtn.classList.add("ready");
        talkIcon.textContent    = "__MIC_ICON__";
        talkLabel.textContent   = T("talk");
        talkSublabel.textContent = T("tap_talk_to_speak");
        micLabel.textContent    = T("mic_tap_to_speak");
        endCallBtn.disabled     = false;
    }
    else if (state === "listening") {
        statusBar.classList.add("listening");
        statusText.textContent = "● " + T("voice_state_listening");
        talkBtn.classList.add("listening");
        talkIcon.textContent    = '<div class="wave-bars"><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div></div>';
        talkLabel.textContent   = T("voice_state_listening");
        talkSublabel.textContent = "";
        micLabel.textContent    = T("voice_state_listening");
        endCallBtn.disabled     = false;
    }
    else if (state === "processing") {
        statusBar.classList.add("processing");
        statusText.textContent = "● " + T("voice_state_processing");
        talkBtn.classList.add("processing");
        talkIcon.textContent    = "⚙️";
        talkLabel.textContent   = T("voice_state_processing");
        talkSublabel.textContent = "";
        micLabel.textContent    = T("mic_processing");
        endCallBtn.disabled     = false;
    }
    else if (state === "speaking") {
        statusBar.classList.add("speaking");
        statusText.textContent = "● " + T("voice_state_speaking");
        talkBtn.classList.add("speaking");
        talkIcon.textContent    = '<div class="speak-bars"><div class="speak-bar"></div><div class="speak-bar"></div><div class="speak-bar"></div><div class="speak-bar"></div><div class="speak-bar"></div><div class="speak-bar"></div><div class="speak-bar"></div></div>';
        talkLabel.textContent   = T("voice_state_speaking");
        talkSublabel.textContent = "";
        micLabel.textContent    = T("mic_speaking");
        endCallBtn.disabled     = false;
    }
}


// ============================================================
// SAFE TIMEOUT MANAGEMENT
// ============================================================

function safeSetTimeout(fn, delay) {
    const sid = sessionId;
    const id  = setTimeout(function() {
        pendingTimeouts = pendingTimeouts.filter(function(tid) { return tid !== id; });
        if (sessionId === sid && sessionActive) fn();
    }, delay);
    pendingTimeouts.push(id);
    return id;
}

function clearAllPending() {
    pendingTimeouts.forEach(function(id) { clearTimeout(id); });
    pendingTimeouts = [];
}


// ============================================================
// LANGUAGE SELECTION
// ============================================================

function selectLang(code) {
    if (callEnded) return;

    language = code;

    // Update language button highlights (mini-bar)
    Object.keys(langMiniBtns).forEach(function(k) {
        if (langMiniBtns[k]) {
            langMiniBtns[k].classList.remove("selected-mini");
        }
    });
    if (langMiniBtns[code]) {
        langMiniBtns[code].classList.add("selected-mini");
    }

    // Legacy large button highlights (kept for safety / fallback)
    Object.keys(langBtns).forEach(function(k) {
        if (langBtns[k]) {
            langBtns[k].classList.remove("selected-lang");
        }
    });
    if (langBtns[code]) {
        langBtns[code].classList.add("selected-lang");
    }

    // Transition from language-selection state to main menu state
    state = "menu";

    // Update header info bar
    currentLang.textContent = LANGUAGES[code].name;

    // Update voice status line
    loadVoices();
    updateVoiceStatus();

    // Update footer notice for online TTS languages
    updateFooterNotice();

    // Update voice-command examples on the opening screen
    updateCommandExamples();

    // Update message to show confirmation
    messageArea.textContent = T("language_confirmed");

    // Update talk button to current language
    if (voiceState === "idle") {
        talkLabel.textContent  = T("talk");
        talkSublabel.textContent = T("tap_talk_to_speak");
        micLabel.textContent   = T("mic_tap_to_speak");
    }

    // Update all UI labels
    endCallBtn.textContent = T("end_call");
    statusText.textContent = "● " + T("voice_state_sleeping");

    // Announce confirmation in selected language
    speak(T("language_confirmed"));
}


// ============================================================
// RAKSHA STATUS TRANSLATION
// Maps raw status values from the database to human-readable
// translated strings in the selected language.
// ============================================================

const STATUS_TRANSLATIONS = {
    "healthy":            "raksha_status_healthy",
    "normal":             "raksha_status_normal",
    "minor change":       "raksha_status_minor_change",
    "minor_change":       "raksha_status_minor_change",
    "significant change": "raksha_status_significant_change",
    "significant_change": "raksha_status_significant_change",
};

function translateStatus(rawStatus) {
    if (!rawStatus) return null;
    const key = STATUS_TRANSLATIONS[rawStatus.toLowerCase()];
    if (key) {
        const translated = T(key);
        // If translation returns the key (missing), fall back to raw value
        return translated === key ? rawStatus : translated;
    }
    return rawStatus;
}


// ============================================================
// UPDATE COMMAND EXAMPLES (language-aware)
// ============================================================

function updateCommandExamples() {
    // Update the voice command phrase examples shown on the opening screen.
    // These change with the selected language so farmers see the
    // exact phrasing they should speak in their own language.
    if (document.getElementById("cmd-raksha-text")) {
        document.getElementById("cmd-raksha-text").textContent = T("cmd_open_raksha");
    }
    if (document.getElementById("cmd-diagnosis-text")) {
        document.getElementById("cmd-diagnosis-text").textContent = T("cmd_open_diagnosis");
    }
    if (document.getElementById("cmd-status-text")) {
        document.getElementById("cmd-status-text").textContent = T("cmd_check_crop");
    }
    if (document.getElementById("cmd-help-text")) {
        document.getElementById("cmd-help-text").textContent = T("cmd_help");
    }
    if (document.getElementById("cmd-end-text")) {
        document.getElementById("cmd-end-text").textContent = T("cmd_end_call");
    }
    if (document.getElementById("cmd-talk-text")) {
        document.getElementById("cmd-talk-text").textContent = T("cmd_casual_talk");
    }
}



// ============================================================
// CROP DISPLAY
// ============================================================

function updateCropDisplay() {
    if (CROPS && CROPS.length > 0) {
        const first = CROPS[0];
        currentCrop.textContent = translateCropName(first.crop_name);
    } else {
        currentCrop.textContent = T("no_crop_selected");
    }
}


// ============================================================
// SPEECH RECOGNITION
// ============================================================

function setupRecognition() {
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) {
        speechRecAvail = false;
        return false;
    }

    recognition = new SR();
    recognition.continuous    = false;
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.onstart = function() {
        if (!sessionActive) return;
        listening    = true;
        resultSeen   = false;
        setVoiceState("listening");
    };

    recognition.onend = function() {
        listening = false;
        if (!sessionActive) return;

        // NO AUTO-RESTART. Return to idle and let user tap TALK again.
        if (!resultSeen) {
            setVoiceState("idle");
        }
    };

    recognition.onerror = function(event) {
        listening = false;
        if (!sessionActive) return;

        const hardErrors = ["not-allowed","audio-capture","service-not-allowed"];
        if (hardErrors.includes(event.error)) {
            speechRecAvail = false;
            setVoiceState("idle");
            micLabel.textContent = T("mic_blocked_instruction");
            return;
        }

        // no-speech, aborted, network — just return to idle
        setVoiceState("idle");
    };

    recognition.onresult = function(event) {
        if (!sessionActive) return;
        resultSeen = true;
        listening  = false;

        const transcript = event.results[0][0].transcript.toLowerCase().trim();

        selectedLine.textContent = T("heard") + transcript;

        // Show processing
        setVoiceState("processing");

        safeSetTimeout(function() {
            if (sessionActive) {
                handleVoiceInput(transcript);
            }
        }, 200);
    };

    speechRecAvail = true;
    return true;
}


// ============================================================
// START LISTENING (called only on TALK tap)
// ============================================================

function startListening() {
    if (!sessionActive || !speechRecAvail || !recognition || listening) return;

    // Don't start if speech synthesis is playing
    if (window.speechSynthesis && window.speechSynthesis.speaking) return;
    // Don't start if online TTS is playing
    if (ttsAudio && !ttsAudio.paused) return;

    const locales = LANGUAGE_LOCALES[language] || ["en-IN"];
    recognition.lang = locales[0];

    try {
        recognition.start();
    } catch(e) {
        // already running — ignore
    }
}


// ============================================================
// VOICE INPUT HANDLER
// ============================================================

function handleVoiceInput(text) {
    if (!sessionActive) return;

    // ── Language selection state ──
    if (state === "language") {

        if (text.includes("english") || text.includes("ఇంగ్లీష్") || text.includes("इंग्लिश") || text.includes("अंग्रेज़ी") || text.includes("अंग्रेजी")) {
            selectLang("en");
            return;
        }
        if (text.includes("telugu") || text.includes("తెలుగు")) {
            selectLang("te");
            return;
        }
        if (text.includes("hindi") || text.includes("हिंदी")) {
            selectLang("hi");
            return;
        }
        if (text.includes("marathi") || text.includes("मराठी")) {
            selectLang("mr");
            return;
        }

        const digit = text.match(/[1-4]/);
        if (digit) {
            const map = {"1":"en","2":"te","3":"hi","4":"mr"};
            if (map[digit[0]]) selectLang(map[digit[0]]);
            return;
        }

        respond(T("invalid"));
        return;
    }

    // ── Crop selection states ──
    if (state === "crop_status" || state === "crop_raksha") {

        const numWords = {
            "one":"1","two":"2","three":"3","four":"4","five":"5",
            "ఒకటి":"1","రెండు":"2","మూడు":"3","నాలుగు":"4","ఐదు":"5",
            "एक":"1","दो":"2","तीन":"3","चार":"4","पाँच":"5"
        };

        for (const w in numWords) {
            if (text.includes(w)) {
                const idx = parseInt(numWords[w], 10) - 1;
                if (idx >= 0 && idx < CROPS.length) {
                    const crop = CROPS[idx];
                    if (state === "crop_status") showCropStatus(crop);
                    else showCropRaksha(crop);
                    return;
                }
            }
        }

        const digit = text.match(/[1-9]/);
        if (digit) {
            const idx = parseInt(digit[0], 10) - 1;
            if (idx >= 0 && idx < CROPS.length) {
                if (state === "crop_status") showCropStatus(CROPS[idx]);
                else showCropRaksha(CROPS[idx]);
                return;
            }
        }

        // Crop name match — check English name AND all translated names
        for (let i = 0; i < CROPS.length; i++) {
            const englishName = CROPS[i].crop_name.toLowerCase();
            if (text.includes(englishName)) {
                if (state === "crop_status") showCropStatus(CROPS[i]);
                else showCropRaksha(CROPS[i]);
                return;
            }
            // Also match translated names for each language
            for (const lang in CROP_MAP) {
                const translated = CROP_MAP[lang][englishName];
                if (translated && text.includes(translated.toLowerCase())) {
                    if (state === "crop_status") showCropStatus(CROPS[i]);
                    else showCropRaksha(CROPS[i]);
                    return;
                }
            }
        }

        respond(T("invalid"));
        return;
    }

    // ── Menu state ──
    if (state === "menu") {

        if (text.includes("diagnosis") || text.includes("diagnose") || text.includes("रोग") ||
            text.includes("पहचान") || text.includes("निदान") || text.includes("వ్యాధి") ||
            text.includes("నిర్ధారణ")) {
            diagnosis();
            return;
        }

        if (text.includes("status") || text.includes("health") || text.includes("स्थिति") ||
            text.includes("స్థితి") || text.includes("स्थिती")) {
            showCropMenu("crop_status");
            return;
        }

        if (text.includes("raksha") || text.includes("रक्षा") || text.includes("రక్ష")) {
            showCropMenu("crop_raksha");
            return;
        }

        // Casual talk — match greetings, gratitude, or any conversational natural language
        if (text.includes("casual") || text.includes("chat") ||
            text.includes("hello") || text.includes("hi ") || text.endsWith("hi") ||
            text.includes("namaste") || text.includes("नमस्ते") ||
            text.includes("good morning") || text.includes("good afternoon") ||
            text.includes("good evening") || text.includes("thank") ||
            text.includes("धन्यवाद") || text.includes("shukriya") ||
            text.includes("ధన్యవాదాలు") || text.includes("आभार") ||
            text.includes("how are you") || text.includes("कैसा है") ||
            text.includes("क्या हाल है") || text.includes("कसे आहात") ||
            text.includes("how is my crop") || text.includes("mera fasal") ||
            text.includes("meri fasal") || text.includes("maza pika") ||
            text.includes("मेरी फसल") || text.includes("तुमचे पीक") ||
            text.includes("yesterday") || text.includes("what should i do") ||
            text.includes("today") || text.includes("weather") ||
            text.includes("mausam") || text.includes("what happened") ||
            text.includes("help me") || text.includes("what to do") ||
            text.includes("నా పంట") || text.includes("मदत")) {
            showCasualTalk(text);
            return;
        }

        if (text.includes("help") || text.includes("मदद") || text.includes("मदत") ||
            text.includes("सहायता") || text.includes("సహాయం")) {
            showHelp();
            return;
        }

        if (text.includes("repeat") || text.includes("again") || text.includes("दोबारा") ||
            text.includes("पुन्हा") || text.includes("మళ్లీ")) {
            showMenu();
            return;
        }

        if (text.includes("end") || text.includes("exit") || text.includes("stop") ||
            text.includes("समाप्त") || text.includes("ముగించు")) {
            endCall();
            return;
        }

        const digit = text.match(/[0-5]/);
        if (digit) {
            const key = digit[0];
            if (key === "1")       { diagnosis(); return; }
            if (key === "2")       { showCropMenu("crop_status"); return; }
            if (key === "3")       { showCropMenu("crop_raksha"); return; }
            if (key === "4")       { showCasualTalk("casual"); return; }
            if (key === "5")       { showHelp(); return; }
            if (key === "0")       { endCall(); return; }
        }

        respond(T("invalid"));
    }
}


// ============================================================
// RESPOND (update message + speak)
// ============================================================

function respond(text, doSpeak) {
    if (doSpeak === undefined) doSpeak = true;
    messageArea.textContent = text;
    if (doSpeak) speak(text);
}


// ============================================================
// MENU / MENU HELPERS
// ============================================================

let state = "language"; // language | crop_status | crop_raksha | menu

function showMenu() {
    state = "menu";
    respond(T("main_menu"));
}

function showHelp() {
    state = "menu";
    let text = T("help") + "\n\n";
    text += "1 = " + T("diagnose") + "\n";
    text += "2 = " + T("status") + "\n";
    text += "3 = " + T("crop_raksha") + "\n";
    text += "4 = " + T("casual_talk") + "\n";
    text += "5 = Help\n";
    text += "9 = Repeat\n";
    text += "0 = End";
    respond(text);
}

function diagnosis() {
    state = "menu";
    respond(T("diagnosis") + "\n\n" + T("casual_diagnose_open"));
}


// ============================================================
// CASUAL TALK
// ============================================================

function showCasualTalk(text) {
    state = "menu";

    // Pick greeting based on time of day
    const hour = new Date().getHours();
    let greeting = "";
    if (hour < 12) {
        greeting = T("greeting_morning");
    } else if (hour < 17) {
        greeting = T("greeting_afternoon");
    } else {
        greeting = T("greeting_evening");
    }

    let response = greeting + "\n\n";
    const textLower = text.toLowerCase();

    // Gratitude
    if (textLower.includes("thank") || textLower.includes("dhanyavaad") ||
        textLower.includes("धन्यवाद") || textLower.includes("shukriya") ||
        textLower.includes("ధన్యవాదాలు") || textLower.includes("आभार") ||
        textLower.includes("abhar") || textLower.includes("grateful")) {
        response = T("greeting_thanks") + "\n\n";
    }

    // Crop / my farm
    else if (textLower.includes("crop") || textLower.includes("fasal") ||
             textLower.includes("pik") || textLower.includes("పంట") ||
             textLower.includes("फसल") || textLower.includes("पीक") ||
             textLower.includes("maza pika") || textLower.includes("meri fasal") ||
             textLower.includes("mera fasal") || textLower.includes("my crop") ||
             textLower.includes("my farm")) {
        if (CROPS && CROPS.length > 0) {
            const crop = CROPS[0];
            const latest = crop.latest_raksha || crop.latest_monitoring;
            if (latest) {
                response += T("casual_latest_observation", {
                    day: latest.day || "?",
                    date: latest.date || "?"
                }) + "\n";
                if (latest.disease) {
                    response += T("status_summary", {
                        disease: latest.disease,
                        confidence: Number(latest.confidence || 0).toFixed(0)
                    }) + "\n";
                }
            } else {
                response += T("casual_no_observation_yet") + "\n";
            }
        } else {
            response += T("casual_no_observation_yet") + "\n";
        }
        response += T("casual_crop_today") + "\n";
    }

    // Yesterday
    else if (textLower.includes("yesterday") || textLower.includes("कल") ||
             textLower.includes("kal ") || textLower.includes(" काल")) {
        response += T("casual_yesterday") + "\n";
        response += T("casual_crop_today") + "\n";
    }

    // Today / what to do
    else if (textLower.includes("today") || textLower.includes("what should") ||
             textLower.includes("what to do") || textLower.includes("आज") ||
             textLower.includes("ఈరోజు") || textLower.includes("आज क्या")) {
        response += T("casual_crop_today") + "\n";
    }

    // Diagnose
    else if (textLower.includes("diagnose") || textLower.includes("निदान") ||
             textLower.includes("पहचान") || textLower.includes("vydhi") ||
             textLower.includes("నిర్ధారణ") || textLower.includes("रोग")) {
        response += T("casual_diagnose_open") + "\n";
        diagnosis();
        return;
    }

    // Weather
    else if (textLower.includes("weather") || textLower.includes("mausam") ||
             textLower.includes("हवामान") || textLower.includes("वातावरण") ||
             textLower.includes("వాతావరణం")) {
        response += T("casual_crop_today") + "\n";
    }

    // Default — fallback
    else {
        response += T("casual_how_to_help") + "\n";
    }

    respond(response);
}

function showCropMenu(nextState) {
    if (!CROPS || CROPS.length === 0) {
        state = "menu";
        respond(T("no_crops"));
        return;
    }
    state = nextState;
    let text = T("choose_crop") + "\n\n";
    CROPS.forEach(function(c, i) {
        text += (i+1) + ". " + translateCropName(c.crop_name) + "\n";
    });
    text += "\n" + T("say_crop_number");
    respond(text);
}

function showCropStatus(crop) {
    state = "menu";
    const cropDisplay = translateCropName(crop.crop_name);
    currentCrop.textContent = cropDisplay;
    let text = T("status") + "\n\n";
    text += cropDisplay + " - " + crop.field_label + "\n\n";

    const latest = crop.latest_raksha || crop.latest_monitoring;
    if (latest) {
        text += T("status_summary", {disease: latest.disease || "Unknown",
            confidence: Number(latest.confidence || 0).toFixed(2)}) + "\n\n";
        if (latest.status) {
            text += T("visual_status", {status: translateStatus(latest.status)}) + "\n";
        }
        if (latest.date)    text += T("last_observation", {date: latest.date}) + "\n";
    } else {
        text += T("no_recent_observation") + "\n";
    }
    text += "\n" + T("raksha_count", {count: crop.raksha_count});
    text += "\n" + T("monitoring_count", {count: crop.monitoring_count});
    respond(text);
}

function showCropRaksha(crop) {
    state = "menu";
    const cropDisplay = translateCropName(crop.crop_name);
    currentCrop.textContent = cropDisplay;
    let text = T("raksha") + "\n\n";
    text += cropDisplay + " - " + crop.field_label + "\n\n";
    if (crop.raksha_count > 0) {
        text += T("raksha_summary", {count: crop.raksha_count}) + "\n\n";
        const latest = crop.latest_raksha;
        if (latest) {
            if (latest.day) {
                text += T("raksha_day_label", {day: latest.day}) + "\n";
            }
            if (latest.status) {
                const statusText = translateStatus(latest.status);
                text += T("raksha_status_label", {status: statusText}) + "\n";
            }
            if (latest.disease) {
                // Disease is a model output / technical name — keep raw.
                text += T("raksha_disease_label", {disease: latest.disease}) + "\n";
            }
            if (latest.date) {
                text += T("raksha_date_label", {date: latest.date}) + "\n";
            }
        }
    } else {
        text += T("no_raksha_history") + "\n\n";
        text += T("open_raksha_hint");
    }
    respond(text);
}


// ============================================================
// TALK BUTTON TAP
// ============================================================

function onTalkTap() {
    if (callEnded) return;
    if (!sessionActive) return;

    if (voiceState === "idle") {
        // Cancel any ongoing speech (both browser and online TTS)
        if (window.speechSynthesis) window.speechSynthesis.cancel();
        cancelOnlineTTS();
        // Start listening
        startListening();
    }
    // If already listening/processing/speaking, ignore tap
}


// ============================================================
// END CALL
// ============================================================

function onEndCallTap() {
    endCall();
}

function endCall() {
    const sid = sessionId;
    callEnded    = true;
    sessionActive = false;

    clearAllPending();

    if (window.speechSynthesis) {
        window.speechSynthesis.cancel();
    }
    cancelOnlineTTS();

    // If a TTS navigation is in progress, return to the original page
    if (originalPageUrl && window.parent.location.href !== originalPageUrl) {
        try {
            window.parent.location.replace(originalPageUrl);
        } catch(e) {}
    }

    if (recognition) {
        try { if (listening) recognition.stop(); } catch(e) {}
    }
    listening  = false;
    resultSeen = false;

    // Update UI to ended state
    statusBar.className = "status-bar ended";
    statusText.textContent = "● " + T("voice_state_idle");
    talkBtn.className   = "talk-btn ended";
    talkIcon.textContent  = "__PHONE_ICON__";
    talkLabel.textContent = "";
    talkSublabel.textContent = "";
    micLabel.textContent   = "";
    endCallBtn.disabled    = true;

    messageArea.textContent = "";
    selectedLine.textContent = "";

    startOverlay.style.display  = "none";
    splashOverlay.style.display = "none";
    endedOverlay.style.display  = "flex";
}


// ============================================================
// START CALL (after OK button)
// ============================================================

function beginFlow() {
    startOverlay.style.display = "none";

    if (!recognition) {
        setupRecognition();
    }

    if (!speechRecAvail) {
        statusBar.className = "status-bar ended";
        statusText.textContent = T("status_voice_unavailable");
        messageArea.textContent = T("voice_unavailable_message");
        return;
    }

    splashOverlay.style.display = "flex";
    statusText.textContent = T("status_connecting");

    // Increment session ID
    sessionId++;
    clearAllPending();

    setTimeout(function() {
        splashOverlay.style.display = "none";
        loadVoices();
        startCall();
    }, 2000);
}


// ============================================================
// START CALL CORE
// ============================================================

function startCall() {
    sessionActive = true;
    callEnded    = false;
    resultSeen   = false;
    state        = "language";

    // Increment session ID
    sessionId++;

    selectedLine.textContent = "";
    messageArea.textContent  = "";

    endCallBtn.disabled = false;

    // Start with language selection
    setVoiceState("idle");

    // Announce the welcome / language prompt
    respond(T("choose_language"));
}


// ============================================================
// RESTART FROM ENDED STATE
// ============================================================

function restartFromEnded() {
    endedOverlay.style.display = "none";
    startOverlay.style.display = "flex";

    // Reset everything
    callEnded     = false;
    sessionActive = false;
    voiceState    = "idle";
    state         = "language";
    language      = "en";
    listening     = false;
    resultSeen    = false;
    cancelOnlineTTS();

    // Reset language button highlights (mini-bar)
    Object.keys(langMiniBtns).forEach(function(k) {
        if (langMiniBtns[k]) {
            langMiniBtns[k].classList.remove("selected-mini");
        }
    });
    if (langMiniBtns["en"]) {
        langMiniBtns["en"].classList.add("selected-mini");
    }

    // Legacy large button highlights (kept for safety / fallback)
    Object.keys(langBtns).forEach(function(k) {
        if (langBtns[k]) {
            langBtns[k].classList.remove("selected-lang");
        }
    });
    if (langBtns["en"]) {
        langBtns["en"].classList.add("selected-lang");
    }

    currentLang.textContent  = LANGUAGES["en"].name;
    messageArea.textContent  = "";
    selectedLine.textContent = "";
    statusText.textContent    = T("voice_state_sleeping");
    statusBar.className      = "status-bar sleeping";
    talkBtn.className        = "talk-btn ready";
    talkIcon.textContent     = "__MIC_ICON__";
    talkLabel.textContent    = T("talk");
    talkSublabel.textContent = T("tap_talk_to_speak");
    micLabel.textContent     = T("mic_tap_to_speak");
    endCallBtn.disabled      = true;
    voiceStatusLine.textContent = T("checking_language_voices");

    // Re-setup recognition (important for clean state)
    if (recognition) {
        recognition.onstart  = null;
        recognition.onend     = null;
        recognition.onerror   = null;
        recognition.onresult  = null;
        recognition = null;
    }
    setupRecognition();
    loadVoices();
    updateVoiceStatus();
    updateFooterNotice();
}


// ============================================================
// WINDOW ONLOAD
// ============================================================

window.onload = function() {
    // Set initial language to English (mini-bar)
    if (langMiniBtns["en"]) {
        langMiniBtns["en"].classList.add("selected-mini");
    }
    // Legacy large button fallback
    if (langBtns["en"]) {
        langBtns["en"].classList.add("selected-lang");
    }
    currentLang.textContent = LANGUAGES["en"].name;

    // Set initial command examples for English
    updateCommandExamples();

    setupRecognition();
    loadVoices();

    // Set initial voice status
    updateVoiceStatus();

    // Set initial footer notice
    updateFooterNotice();

    // Set crop display
    updateCropDisplay();

    // Check whether Python left TTS audio data in window.__TTS_DATA__
    // (injected by _handle_tts_endpoint after a TTS navigation).
    // Runs synchronously so the audio plays as soon as the page loads.
    checkTtsData();

    // Set initial TALK button
    talkLabel.textContent    = T("talk");
    talkSublabel.textContent = T("tap_talk_to_speak");
    micLabel.textContent     = T("mic_tap_to_speak");

    endCallBtn.disabled = true;
};

</script>

</body>

</html>
"""


# ============================================================
# ONLINE TTS — SERVER-SIDE GOOGLE TRANSLATE TTS
# Browser cannot call translate.google.com due to CORS.
# Python backend fetches audio and embeds it as a base64
# data-URI so the iframe can play it without CORS issues.
# ============================================================

_TTS_LANG_MAP = {
    "te": "te-IN",
    "mr": "mr-IN",
}


def _fetch_online_tts(text: str, lang: str) -> bytes | None:
    """
    Fetch MP3 audio from Google Translate TTS for the given text
    and language code.  Returns raw MP3 bytes, or None on failure.
    """
    if not text or lang not in _TTS_LANG_MAP:
        return None
    tl = _TTS_LANG_MAP[lang]
    params = {
        "ie": "UTF-8",
        "q": text,
        "tl": tl,
        "client": "tw-oca",
    }
    try:
        r = requests.get(
            "https://translate.google.com/translate_tts",
            params=params,
            timeout=10,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36"
                )
            },
        )
        if r.status_code == 200 and r.content:
            return r.content
    except Exception:
        pass
    return None


def _handle_tts_endpoint(html: str) -> str:
    """
    When the Streamlit page URL carries TTS query params (set by the
    Anjaneya iframe via window.parent.location), fetch the audio from
    Google Translate TTS and embed it directly as a JavaScript variable
    in the response HTML.

    The iframe's srcdoc runs the same Streamlit page after navigation,
    so window.__TTS_DATA__ is readable synchronously without any
    cross-origin sessionStorage hacks.

    Query params (injected into window.parent.location by the iframe):
      _tts_text  — URL-encoded text to synthesise
      _tts_lang  — language code (te / mr)
      _tts_sid   — session ID for stale-request guard
    """
    try:
        tts_text = st.query_params.get("_tts_text", "")
        tts_lang = st.query_params.get("_tts_lang", "")
        tts_sid  = st.query_params.get("_tts_sid",  "")
    except Exception:
        return html

    if not tts_text or tts_lang not in _TTS_LANG_MAP:
        return html

    audio_bytes = _fetch_online_tts(tts_text, tts_lang)
    if audio_bytes:
        b64 = base64.b64encode(audio_bytes).decode("ascii")
        # Inject TTS data as a global JS variable — iframe reads it
        # synchronously on page load.  Session ID in the payload guards
        # against stale audio from previous interactions.
        tts_marker = (
            f'<script>'
            f'window.__TTS_DATA__ = {{"audio":"{b64}","lang":"{tts_lang}","sid":"{tts_sid}"}};'
            f'</script>'
        )
        # Inject just before </head> so it is available when the page runs
        html = html.replace("</head>", tts_marker + "</head>", 1)
    return html


# ============================================================
# RENDERER
# ============================================================

def render_anjaneya_voice():
    global crops_data, raksha_history, monitoring_history
    global crops, crop_records, translations_json, crops_json, page_html

    # Reload data
    crops_data = load_json(CROPS_FILE, [])
    raksha_history = load_json(RAKSHA_FILE, [])
    monitoring_history = load_json(MONITORING_FILE, [])
    crops = normalize_crops(crops_data)

    crop_records = []
    for crop in crops:
        crop_id = crop["id"]
        raksha_records = [
            r for r in raksha_history
            if str(r.get("crop_id", "")) == crop_id
        ]
        monitoring_records = [
            r for r in monitoring_history
            if str(r.get("crop_id", "")) == crop_id
            or (not r.get("crop_id")
                and str(r.get("crop", "")).strip().lower()
                == str(crop["crop_name"]).strip().lower())
        ]
        latest_raksha = (
            sorted(raksha_records, key=lambda x: str(x.get("date", "")))[-1]
            if raksha_records else None
        )
        latest_monitoring = (
            sorted(
                monitoring_records,
                key=lambda x: str(x.get("date") or x.get("timestamp") or "")
            )[-1]
            if monitoring_records else None
        )
        crop_records.append({
            "id": crop_id,
            "crop_name": crop["crop_name"],
            "farmer_name": crop["farmer_name"],
            "field_label": crop["field_label"],
            "sowing_date": crop["sowing_date"],
            "raksha_count": len(raksha_records),
            "monitoring_count": len(monitoring_records),
            "latest_raksha": latest_raksha,
            "latest_monitoring": latest_monitoring
        })

    translations_json = json.dumps(translations, ensure_ascii=False)
    crops_json = json.dumps(crop_records, ensure_ascii=False)
    crop_map_json = json.dumps(CROP_DISPLAY_MAP, ensure_ascii=False)

    # ── Replace data placeholders ──────────────────────
    html = page_html.replace("__LANGUAGES__", translations_json)
    html = html.replace("__CROPS__", crops_json)
    html = html.replace("__CROP_MAP__", crop_map_json)

    # ── Anjaneya wordmark (stylized text) ──────────────
    html = html.replace("__ANJANEYA_WORDMARK__", t("anjaneya_title"))
    html = html.replace("__ANJANEYA_SUBTITLE__", t("anjaneya_subtitle"))

    # ── Info bar ───────────────────────────────────────
    html = html.replace("__LANG_LABEL__", t("voice_opening_language").split(":")[0] + ":")
    html = html.replace("__LANG_VALUE__", translations["en"]["name"])
    html = html.replace("__CROP_LABEL__", t("voice_opening_crop").split(":")[0] + ":")
    html = html.replace(
        "__CROP_VALUE__",
        translate_crop_name(crop_records[0]["crop_name"])
        if crop_records else t("no_crop_selected")
    )

    # ── Status ─────────────────────────────────────────
    html = html.replace("__STATUS_READY__", t("ready_to_listen"))
    html = html.replace("__VOICE_STATUS__", t("checking_language_voices"))

    # ── Screen ─────────────────────────────────────────
    html = html.replace("__SCREEN_LABEL__", t("screen_label"))
    html = html.replace("__MESSAGE_INITIAL__", t("press_ok_start"))

    # ── TALK button ────────────────────────────────────
    html = html.replace("__TALK_ICON__", "🎙")
    html = html.replace("__TALK_LABEL__", t("talk"))
    html = html.replace("__TALK_SUBLABEL__", t("tap_talk_to_speak"))
    html = html.replace("__MIC_ICON__", "🎙")
    html = html.replace("__MIC_LABEL__", t("mic_tap_to_speak"))

    # ── Voice Command Reference ("What can I say?") ──
    html = html.replace("__WHAT_CAN_I_SAY__", t("what_can_i_say"))
    html = html.replace("__CMD_RAKSHA__", '"' + t("cmd_open_raksha") + '"')
    html = html.replace("__CMD_DIAGNOSIS__", '"' + t("cmd_open_diagnosis") + '"')
    html = html.replace("__CMD_STATUS__", '"' + t("cmd_check_crop") + '"')
    html = html.replace("__CMD_HELP__", '"' + t("cmd_help") + '"')
    html = html.replace("__CMD_END__", '"' + t("cmd_end_call") + '"')
    html = html.replace("__CMD_TALK__", '"' + t("cmd_casual_talk") + '"')

    # ── Crop section ───────────────────────────────────
    html = html.replace("__CROP_FIELD_TITLE__", t("crop_label"))
    html = html.replace(
        "__CROP_DISPLAY__",
        translate_crop_name(crop_records[0]["crop_name"])
        if crop_records else t("no_crop_selected")
    )

    # ── Controls ───────────────────────────────────────
    html = html.replace("__END_CALL_LABEL__", "☎️ " + t("end_call"))

    # ── Footer ─────────────────────────────────────────
    html = html.replace("__FOOTER_NOTICE__", t("offline_notice"))
    html = html.replace("__FOOTER_NOTICE2__", t("browser_voice_notice"))
    html = html.replace("__FOOTER_NOTICE3__", t("voice_unavailable_message"))

    # ── Overlays ────────────────────────────────────────
    html = html.replace("__OPEN_BUTTON__", t("ok_button"))
    html = html.replace("__OPEN_CAPTION__", t("tap_ok_caption"))
    html = html.replace("__SPLASH_TEXT__", t("splash_jai_anjaneya"))
    html = html.replace("__PHONE_ICON__", "☎️")
    html = html.replace("__ENDED_TITLE__", t("call_ended_title"))
    html = html.replace("__ENDED_MESSAGE__", t("call_ended_message"))
    html = html.replace("__RESTART_LABEL__", "🔄 " + t("start_new_call"))

    # ── Streamlit title ────────────────────────────────
    st.markdown(
        """
        <div style="text-align:center; padding:8px 0 4px 0;">
            <h2 style="margin-bottom:0; color:#FFD700;">{title}</h2>
            <p style="color:#888; margin-top:4px;">{subtitle}</p>
        </div>
        """.format(
            title=t("anjaneya_title"),
            subtitle=t("anjaneya_subtitle")
        ),
        unsafe_allow_html=True
    )

    # ── How it works ───────────────────────────────────
    with st.expander(t("ivr_how_it_works_title"), expanded=False):
        st.write(t("ivr_how_it_works_intro"))
        st.write(t("ivr_tap_ok_instruction"))
        st.markdown("""
- {step_ok}
- {step_language}
- {step_diagnosis}
- {step_status}
- {step_raksha}
- {step_help}
- {step_repeat}
- {step_end}

{final_note}
        """.format(
            step_ok=t("ivr_step_ok"),
            step_language=t("ivr_step_language"),
            step_diagnosis=t("ivr_step_diagnosis"),
            step_status=t("ivr_step_status"),
            step_raksha=t("ivr_step_raksha"),
            step_help=t("ivr_step_help"),
            step_repeat=t("ivr_step_repeat"),
            step_end=t("ivr_step_end"),
            final_note=t("ivr_footer_note")
        ))

    # ── Metrics ────────────────────────────────────────
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(t("registered_crops_metric"), len(crop_records))
    with col2:
        st.metric(t("raksha_records_metric"), len(raksha_history))
    with col3:
        st.metric(t("monitoring_records_metric"), len(monitoring_history))

    # ── IVR HTML ───────────────────────────────────────
    # Pass TTS-marked HTML if a TTS fetch request is in flight.
    html = _handle_tts_endpoint(html)
    components.html(html, height=900, scrolling=False)
