# ============================================================
# CROP DOCTOR - OFFLINE IVR LOGIC
# ============================================================

import os
import json
import numpy as np
from PIL import Image


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "models",
    "best_crop_doctor.keras"
)

CLASS_PATH = os.path.join(
    PROJECT_ROOT,
    "class_names.json"
)

CROPS_FILE = os.path.join(
    PROJECT_ROOT,
    "crops.json"
)

RAKSHA_HISTORY_FILE = os.path.join(
    PROJECT_ROOT,
    "crop_raksha_history.json"
)

MONITORING_HISTORY_FILE = os.path.join(
    PROJECT_ROOT,
    "monitoring_history.json"
)


# ============================================================
# LANGUAGES
# ============================================================

LANGUAGES = {
    "en": "English",
    "te": "తెలుగు",
    "hi": "हिन्दी",
    "mr": "मराठी"
}


# ============================================================
# IVR TRANSLATIONS
# ============================================================

TEXT = {

    # ========================================================
    # ENGLISH
    # ========================================================

    "en": {

        "welcome":
            "Welcome to Crop Doctor. "
            "Your AI powered crop health assistant.",

        "language":
            "Please select your language.",

        "main_menu":
            "Main Menu",

        "select":
            "Please select an option.",

        "diagnose":
            "Crop Diagnosis",

        "status":
            "Crop Health Status",

        "raksha":
            "Crop Raksha",

        "help":
            "Help",

        "back":
            "Back to Main Menu",

        "repeat":
            "Repeat",

        "end":
            "End Call",

        "upload":
            "Please upload a clear photograph of your crop.",

        "analyzing":
            "Crop Doctor is analyzing your crop image.",

        "result":
            "Diagnosis Result",

        "healthy":
            "Your crop appears healthy.",

        "confidence":
            "AI Confidence",

        "unknown":
            "The crop condition could not be determined.",

        "status_title":
            "Crop Health Status",

        "no_records":
            "No crop monitoring records are available yet.",

        "records":
            "Monitoring observations",

        "raksha_title":
            "Crop Raksha",

        "raksha_message":
            "Crop Raksha monitors your crop over time and "
            "looks for unusual visual changes.",

        "help_message":
            "Crop Doctor can diagnose crop diseases from images, "
            "monitor crop health, and track changes over time.",

        "call_ended":
            "Thank you for using Crop Doctor. Goodbye.",

        "new_call":
            "Start New Call",

        "select_crop":
            "Please select a crop.",

        "no_crops":
            "No registered crops were found.",

        "latest":
            "Latest Observation",

        "day":
            "Day",

        "disease":
            "Disease",

        "status_value":
            "Status",

        "observation":
            "Observation",

        "early_warning":
            "Early Warning",

        "warning_message":
            "An unusual change may require further inspection.",

        "no_warning":
            "No major warning is currently available.",

        "call_log":
            "Call Transcript",

        "connected":
            "CALL CONNECTED",

        "offline":
            "OFFLINE IVR",

        "diagnosis_complete":
            "Diagnosis completed.",

        "return_menu":
            "Returning to the main menu."
    },


    # ========================================================
    # TELUGU
    # ========================================================

    "te": {

        "welcome":
            "క్రాప్ డాక్టర్‌కు స్వాగతం. "
            "మీ AI పంట ఆరోగ్య సహాయకుడు.",

        "language":
            "దయచేసి మీ భాషను ఎంచుకోండి.",

        "main_menu":
            "ప్రధాన మెనూ",

        "select":
            "దయచేసి ఒక ఎంపికను ఎంచుకోండి.",

        "diagnose":
            "పంట వ్యాధి నిర్ధారణ",

        "status":
            "పంట ఆరోగ్య స్థితి",

        "raksha":
            "క్రాప్ రక్ష",

        "help":
            "సహాయం",

        "back":
            "ప్రధాన మెనూకు తిరిగి వెళ్ళండి.",

        "repeat":
            "మళ్లీ వినండి",

        "end":
            "కాల్ ముగించండి",

        "upload":
            "దయచేసి మీ పంట యొక్క స్పష్టమైన ఫోటోను అప్‌లోడ్ చేయండి.",

        "analyzing":
            "క్రాప్ డాక్టర్ మీ పంట చిత్రాన్ని విశ్లేషిస్తోంది.",

        "result":
            "నిర్ధారణ ఫలితం",

        "healthy":
            "మీ పంట ఆరోగ్యంగా కనిపిస్తోంది.",

        "confidence":
            "AI నమ్మక స్థాయి",

        "unknown":
            "పంట పరిస్థితిని గుర్తించలేకపోయాము.",

        "status_title":
            "పంట ఆరోగ్య స్థితి",

        "no_records":
            "ఇంకా పంట పర్యవేక్షణ రికార్డులు లేవు.",

        "records":
            "పర్యవేక్షణ పరిశీలనలు",

        "raksha_title":
            "క్రాప్ రక్ష",

        "raksha_message":
            "క్రాప్ రక్ష మీ పంటను కాలక్రమేణా పర్యవేక్షించి "
            "అసాధారణ దృశ్య మార్పులను గుర్తించడంలో సహాయపడుతుంది.",

        "help_message":
            "క్రాప్ డాక్టర్ చిత్రాల ద్వారా పంట వ్యాధులను గుర్తించి, "
            "పంట ఆరోగ్యాన్ని పర్యవేక్షించి, మార్పులను ట్రాక్ చేస్తుంది.",

        "call_ended":
            "క్రాప్ డాక్టర్‌ను ఉపయోగించినందుకు ధన్యవాదాలు. నమస్కారం.",

        "new_call":
            "కొత్త కాల్ ప్రారంభించండి",

        "select_crop":
            "దయచేసి ఒక పంటను ఎంచుకోండి.",

        "no_crops":
            "నమోదు చేసిన పంటలు ఏవీ కనుగొనబడలేదు.",

        "latest":
            "తాజా పరిశీలన",

        "day":
            "రోజు",

        "disease":
            "వ్యాధి",

        "status_value":
            "స్థితి",

        "observation":
            "పరిశీలన",

        "early_warning":
            "ముందస్తు హెచ్చరిక",

        "warning_message":
            "అసాధారణ మార్పు కనిపించింది. "
            "మరింత పరిశీలన అవసరం కావచ్చు.",

        "no_warning":
            "ప్రస్తుతం ముఖ్యమైన హెచ్చరిక లేదు.",

        "call_log":
            "కాల్ సంభాషణ",

        "connected":
            "కాల్ కనెక్ట్ అయింది",

        "offline":
            "ఆఫ్‌లైన్ IVR",

        "diagnosis_complete":
            "నిర్ధారణ పూర్తయింది.",

        "return_menu":
            "ప్రధాన మెనూకు తిరిగి వెళ్తున్నాము."
    },


    # ========================================================
    # HINDI
    # ========================================================

    "hi": {

        "welcome":
            "क्रॉप डॉक्टर में आपका स्वागत है। "
            "आपका AI फसल स्वास्थ्य सहायक।",

        "language":
            "कृपया अपनी भाषा चुनें।",

        "main_menu":
            "मुख्य मेनू",

        "select":
            "कृपया एक विकल्प चुनें।",

        "diagnose":
            "फसल रोग पहचान",

        "status":
            "फसल स्वास्थ्य स्थिति",

        "raksha":
            "क्रॉप रक्षा",

        "help":
            "सहायता",

        "back":
            "मुख्य मेनू पर वापस जाएं।",

        "repeat":
            "दोबारा सुनें",

        "end":
            "कॉल समाप्त करें",

        "upload":
            "कृपया अपनी फसल की एक स्पष्ट तस्वीर अपलोड करें।",

        "analyzing":
            "क्रॉप डॉक्टर आपकी फसल की तस्वीर का विश्लेषण कर रहा है।",

        "result":
            "जांच का परिणाम",

        "healthy":
            "आपकी फसल स्वस्थ दिखाई दे रही है।",

        "confidence":
            "AI विश्वास स्तर",

        "unknown":
            "फसल की स्थिति निर्धारित नहीं की जा सकी।",

        "status_title":
            "फसल स्वास्थ्य स्थिति",

        "no_records":
            "अभी कोई फसल निगरानी रिकॉर्ड उपलब्ध नहीं है।",

        "records":
            "निगरानी अवलोकन",

        "raksha_title":
            "क्रॉप रक्षा",

        "raksha_message":
            "क्रॉप रक्षा समय के साथ आपकी फसल की निगरानी करता है "
            "और असामान्य दृश्य परिवर्तनों को पहचानने में मदद करता है।",

        "help_message":
            "क्रॉप डॉक्टर तस्वीरों से फसल रोगों की पहचान करता है, "
            "फसल स्वास्थ्य की निगरानी करता है और बदलावों को ट्रैक करता है।",

        "call_ended":
            "क्रॉप डॉक्टर का उपयोग करने के लिए धन्यवाद। नमस्कार।",

        "new_call":
            "नई कॉल शुरू करें",

        "select_crop":
            "कृपया एक फसल चुनें।",

        "no_crops":
            "कोई पंजीकृत फसल नहीं मिली।",

        "latest":
            "नवीनतम अवलोकन",

        "day":
            "दिन",

        "disease":
            "रोग",

        "status_value":
            "स्थिति",

        "observation":
            "अवलोकन",

        "early_warning":
            "प्रारंभिक चेतावनी",

        "warning_message":
            "असामान्य बदलाव दिखाई दे रहा है। "
            "आगे निरीक्षण आवश्यक हो सकता है।",

        "no_warning":
            "अभी कोई बड़ी चेतावनी उपलब्ध नहीं है।",

        "call_log":
            "कॉल वार्तालाप",

        "connected":
            "कॉल कनेक्ट है",

        "offline":
            "ऑफलाइन IVR",

        "diagnosis_complete":
            "जांच पूरी हुई।",

        "return_menu":
            "मुख्य मेनू पर वापस जा रहे हैं।"
    },


    # ========================================================
    # MARATHI
    # ========================================================

    "mr": {

        "welcome":
            "क्रॉप डॉक्टरमध्ये आपले स्वागत आहे. "
            "आपला AI पीक आरोग्य सहाय्यक.",

        "language":
            "कृपया आपली भाषा निवडा.",

        "main_menu":
            "मुख्य मेनू",

        "select":
            "कृपया एक पर्याय निवडा.",

        "diagnose":
            "पीक रोग निदान",

        "status":
            "पीक आरोग्य स्थिती",

        "raksha":
            "क्रॉप रक्षा",

        "help":
            "मदत",

        "back":
            "मुख्य मेनूवर परत जा.",

        "repeat":
            "पुन्हा ऐका",

        "end":
            "कॉल समाप्त करा",

        "upload":
            "कृपया आपल्या पिकाचा स्पष्ट फोटो अपलोड करा.",

        "analyzing":
            "क्रॉप डॉक्टर आपल्या पिकाच्या फोटोचे विश्लेषण करत आहे.",

        "result":
            "निदानाचा निकाल",

        "healthy":
            "आपले पीक निरोगी दिसत आहे.",

        "confidence":
            "AI विश्वास पातळी",

        "unknown":
            "पिकाची स्थिती निश्चित करता आली नाही.",

        "status_title":
            "पीक आरोग्य स्थिती",

        "no_records":
            "अद्याप कोणतेही पीक निरीक्षण रेकॉर्ड उपलब्ध नाहीत.",

        "records":
            "निरीक्षण नोंदी",

        "raksha_title":
            "क्रॉप रक्षा",

        "raksha_message":
            "क्रॉप रक्षा आपल्या पिकाचे कालांतराने निरीक्षण करते "
            "आणि असामान्य दृश्य बदल ओळखण्यास मदत करते.",

        "help_message":
            "क्रॉप डॉक्टर फोटोमधून पीक रोग ओळखतो, "
            "पिकाच्या आरोग्यावर लक्ष ठेवतो आणि बदल ट्रॅक करतो.",

        "call_ended":
            "क्रॉप डॉक्टर वापरल्याबद्दल धन्यवाद. नमस्कार.",

        "new_call":
            "नवीन कॉल सुरू करा",

        "select_crop":
            "कृपया एक पीक निवडा.",

        "no_crops":
            "नोंदणीकृत पीक आढळले नाही.",

        "latest":
            "नवीनतम निरीक्षण",

        "day":
            "दिवस",

        "disease":
            "रोग",

        "status_value":
            "स्थिती",

        "observation":
            "निरीक्षण",

        "early_warning":
            "पूर्व सूचना",

        "warning_message":
            "असामान्य बदल दिसत आहे. "
            "पुढील तपासणी आवश्यक असू शकते.",

        "no_warning":
            "सध्या कोणतीही मोठी चेतावणी नाही.",

        "call_log":
            "कॉल संभाषण",

        "connected":
            "कॉल कनेक्ट झाला",

        "offline":
            "ऑफलाइन IVR",

        "diagnosis_complete":
            "निदान पूर्ण झाले.",

        "return_menu":
            "मुख्य मेनूवर परत जात आहोत."
    }
}


# ============================================================
# TRANSLATION FUNCTION
# ============================================================

def t(key, language="en"):

    if language not in TEXT:
        language = "en"

    if key in TEXT[language]:
        return TEXT[language][key]

    return TEXT["en"].get(key, key)


# ============================================================
# MODEL CLASS NAMES
# ============================================================

def load_class_names():

    if not os.path.exists(CLASS_PATH):
        return []

    try:

        with open(
            CLASS_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        if isinstance(data, list):
            return data

        if isinstance(data, dict):

            if "class_names" in data:
                return data["class_names"]

            return list(data.values())

    except Exception:
        return []

    return []


# ============================================================
# MODEL DIAGNOSIS
# ============================================================

def analyze_image(
    image,
    model,
    class_names
):

    if image is None:
        return None

    try:

        image = image.convert("RGB")

        image = image.resize(
            (224, 224)
        )

        image_array = np.array(
            image
        ).astype(
            np.float32
        )

        image_array = np.expand_dims(
            image_array,
            axis=0
        )

        predictions = model.predict(
            image_array,
            verbose=0
        )

        probabilities = predictions[0]

        index = int(
            np.argmax(probabilities)
        )

        confidence = (
            float(probabilities[index])
            * 100
        )

        if index < len(class_names):

            class_name = class_names[index]

        else:

            class_name = "Unknown"

        return {
            "class_name": class_name,
            "confidence": confidence
        }

    except Exception as error:

        return {
            "class_name": "Unknown",
            "confidence": 0,
            "error": str(error)
        }


# ============================================================
# READABLE DISEASE NAME
# ============================================================

def clean_disease_name(class_name):

    if not class_name:
        return "Unknown"

    if class_name.lower() == "healthy":
        return "Healthy"

    return (
        class_name
        .replace("_", " ")
        .replace("-", " ")
        .title()
    )


# ============================================================
# LOAD REGISTERED CROPS
# ============================================================

def load_registered_crops():

    if not os.path.exists(CROPS_FILE):
        return []

    try:

        with open(
            CROPS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        if isinstance(data, list):
            return data

        if isinstance(data, dict):

            if "crops" in data:
                return data["crops"]

            return list(data.values())

    except Exception:
        return []

    return []


# ============================================================
# HISTORY LOADER
# ============================================================

def load_history_file(path):

    if not os.path.exists(path):
        return []

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        if isinstance(data, list):
            return data

    except Exception:
        pass

    return []


# ============================================================
# GET ALL MONITORING HISTORY
# ============================================================

def get_crop_history(crop_id=None):

    raksha_history = load_history_file(
        RAKSHA_HISTORY_FILE
    )

    monitoring_history = load_history_file(
        MONITORING_HISTORY_FILE
    )

    history = []

    history.extend(
        raksha_history
    )

    history.extend(
        monitoring_history
    )

    if crop_id is not None:

        history = [
            record
            for record in history
            if str(
                record.get("crop_id")
            ) == str(crop_id)
        ]

    history.sort(
        key=lambda record:
        record.get("date", "")
    )

    return history


# ============================================================
# GET LATEST RECORD
# ============================================================

def get_latest_record(crop_id=None):

    history = get_crop_history(
        crop_id
    )

    if not history:
        return None

    return history[-1]


# ============================================================
# GET CROP NAME
# ============================================================

def get_crop_name(crop):

    if not crop:
        return "Unknown Crop"

    return (
        crop.get("crop_name")
        or crop.get("crop")
        or crop.get("name")
        or "Unknown Crop"
    )


# ============================================================
# GET CROP ID
# ============================================================

def get_crop_id(crop):

    if not crop:
        return None

    return crop.get("id")


# ============================================================
# GET STATUS SUMMARY
# ============================================================

def get_status_summary(crop_id=None):

    history = get_crop_history(
        crop_id
    )

    if not history:

        return {
            "count": 0,
            "latest": None
        }

    return {
        "count": len(history),
        "latest": history[-1]
    }


# ============================================================
# DIAGNOSIS DESCRIPTION
# ============================================================

def diagnosis_summary(
    class_name,
    confidence
):

    disease = clean_disease_name(
        class_name
    )

    if disease.lower() == "healthy":

        return {
            "disease": disease,
            "confidence": confidence,
            "healthy": True
        }

    return {
        "disease": disease,
        "confidence": confidence,
        "healthy": False
    }