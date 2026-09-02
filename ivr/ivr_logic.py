import json
import os


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
# LANGUAGES
# ============================================================

LANGUAGES = {
    "en": {
        "name": "English",
        "speech": "en-IN"
    },

    "te": {
        "name": "తెలుగు",
        "speech": "te-IN"
    },

    "hi": {
        "name": "हिन्दी",
        "speech": "hi-IN"
    },

    "mr": {
        "name": "मराठी",
        "speech": "mr-IN"
    }
}


# ============================================================
# IVR SCRIPT
# ============================================================

SCRIPT = {

    "en": {

        "welcome":
            "Welcome to Crop Doctor. "
            "I am your agricultural AI assistant. "
            "I can help you check your crop, "
            "understand its health, and use Crop Raksha.",

        "language":
            "Please select your language.",

        "menu":
            "Main menu. "
            "Press 1 for AI crop diagnosis. "
            "Press 2 for crop health status. "
            "Press 3 for Crop Raksha. "
            "Press 4 for help. "
            "Press 9 to repeat. "
            "Press 0 to end the call.",

        "diagnosis":
            "AI crop diagnosis requires a photograph. "
            "For the full AI diagnosis, please open the Crop Doctor "
            "diagnosis page and upload a clear photograph of your crop. "
            "The existing Crop Doctor model will analyze the image. "
            "You can also describe your symptoms to me.",

        "status":
            "I can check the latest monitoring information "
            "recorded for your crop.",

        "raksha":
            "Crop Raksha is your daily crop monitoring companion. "
            "It remembers your previous observations and helps "
            "you notice changes over time.",

        "help":
            "You can use the keypad or your voice. "
            "Press 1 for diagnosis, "
            "2 for crop health status, "
            "3 for Crop Raksha, "
            "9 to repeat the menu, "
            "or 0 to end the call.",

        "invalid":
            "I did not understand that. "
            "Please try again.",

        "goodbye":
            "Thank you for using Crop Doctor. "
            "Keep monitoring your crop. Goodbye.",

        "no_data":
            "I do not have monitoring information for this crop yet.",

        "choose_crop":
            "Please select your crop using the keypad.",

        "next_action":
            "Please continue monitoring your crop and upload "
            "another photograph when the next observation is due."
    },


    "te": {

        "welcome":
            "క్రాప్ డాక్టర్‌కు స్వాగతం. "
            "నేను మీ వ్యవసాయ AI సహాయకుడిని. "
            "మీ పంట ఆరోగ్యాన్ని తెలుసుకోవడంలో మరియు క్రాప్ రక్షతో "
            "పంటను పర్యవేక్షించడంలో నేను సహాయపడతాను.",

        "language":
            "దయచేసి మీ భాషను ఎంచుకోండి.",

        "menu":
            "ప్రధాన మెనూ. "
            "AI పంట నిర్ధారణ కోసం 1 నొక్కండి. "
            "పంట ఆరోగ్య స్థితి కోసం 2 నొక్కండి. "
            "క్రాప్ రక్ష కోసం 3 నొక్కండి. "
            "సహాయం కోసం 4 నొక్కండి. "
            "మళ్లీ వినడానికి 9 నొక్కండి. "
            "కాల్ ముగించడానికి 0 నొక్కండి.",

        "diagnosis":
            "AI పంట నిర్ధారణకు పంట ఫోటో అవసరం. "
            "పూర్తి AI నిర్ధారణ కోసం క్రాప్ డాక్టర్ డయాగ్నోసిస్ పేజీలో "
            "స్పష్టమైన పంట ఫోటోను అప్లోడ్ చేయండి. "
            "మీరు మీ పంట లక్షణాలను నాకు చెప్పవచ్చు.",

        "status":
            "మీ పంటకు సంబంధించిన తాజా పర్యవేక్షణ సమాచారాన్ని "
            "నేను చెప్పగలను.",

        "raksha":
            "క్రాప్ రక్ష మీ రోజువారీ పంట పర్యవేక్షణ సహాయకుడు. "
            "ఇది గత పరిశీలనలను గుర్తుంచుకుని పంటలో మార్పులను "
            "గుర్తించడంలో సహాయపడుతుంది.",

        "help":
            "మీరు కీప్యాడ్ లేదా మీ వాయిస్ ఉపయోగించవచ్చు. "
            "నిర్ధారణ కోసం 1, ఆరోగ్య స్థితి కోసం 2, "
            "క్రాప్ రక్ష కోసం 3, మళ్లీ వినడానికి 9, "
            "కాల్ ముగించడానికి 0 నొక్కండి.",

        "invalid":
            "మీ ఎంపిక అర్థం కాలేదు. దయచేసి మళ్లీ ప్రయత్నించండి.",

        "goodbye":
            "క్రాప్ డాక్టర్‌ను ఉపయోగించినందుకు ధన్యవాదాలు. "
            "మీ పంటను పర్యవేక్షిస్తూ ఉండండి. వీడ్కోలు.",

        "no_data":
            "ఈ పంటకు ఇంకా పర్యవేక్షణ సమాచారం లేదు.",

        "choose_crop":
            "దయచేసి కీప్యాడ్ ద్వారా మీ పంటను ఎంచుకోండి.",

        "next_action":
            "మీ పంటను పర్యవేక్షించడం కొనసాగించండి మరియు "
            "తదుపరి పరిశీలన సమయంలో మరొక ఫోటోను అప్లోడ్ చేయండి."
    },


    "hi": {

        "welcome":
            "क्रॉप डॉक्टर में आपका स्वागत है। "
            "मैं आपका कृषि AI सहायक हूँ। "
            "मैं आपकी फसल के स्वास्थ्य को समझने और "
            "क्रॉप रक्षा के माध्यम से निगरानी करने में मदद करूंगा।",

        "language":
            "कृपया अपनी भाषा चुनें।",

        "menu":
            "मुख्य मेनू। "
            "AI फसल जांच के लिए 1 दबाएं। "
            "फसल स्वास्थ्य स्थिति के लिए 2 दबाएं। "
            "क्रॉप रक्षा के लिए 3 दबाएं। "
            "मदद के लिए 4 दबाएं। "
            "दोबारा सुनने के लिए 9 दबाएं। "
            "कॉल समाप्त करने के लिए 0 दबाएं।",

        "diagnosis":
            "AI फसल जांच के लिए फसल की तस्वीर आवश्यक है। "
            "पूरी AI जांच के लिए क्रॉप डॉक्टर के डायग्नोसिस पेज पर "
            "एक साफ तस्वीर अपलोड करें। "
            "आप अपने पौधे के लक्षण मुझे बता सकते हैं।",

        "status":
            "मैं आपकी फसल की नवीनतम निगरानी जानकारी बता सकता हूं।",

        "raksha":
            "क्रॉप रक्षा आपका दैनिक फसल निगरानी सहायक है। "
            "यह पिछली टिप्पणियों को याद रखता है और समय के साथ "
            "फसल में बदलाव पहचानने में मदद करता है।",

        "help":
            "आप कीपैड या अपनी आवाज का उपयोग कर सकते हैं। "
            "जांच के लिए 1, स्वास्थ्य स्थिति के लिए 2, "
            "क्रॉप रक्षा के लिए 3, दोबारा सुनने के लिए 9, "
            "और कॉल समाप्त करने के लिए 0 दबाएं।",

        "invalid":
            "मैं आपकी पसंद समझ नहीं पाया। कृपया फिर कोशिश करें।",

        "goodbye":
            "क्रॉप डॉक्टर का उपयोग करने के लिए धन्यवाद। "
            "अपनी फसल की निगरानी करते रहें। नमस्ते।",

        "no_data":
            "इस फसल के लिए अभी कोई निगरानी जानकारी उपलब्ध नहीं है।",

        "choose_crop":
            "कृपया कीपैड से अपनी फसल चुनें।",

        "next_action":
            "अपनी फसल की निगरानी जारी रखें और "
            "अगली जांच के समय एक और तस्वीर अपलोड करें।"
    },


    "mr": {

        "welcome":
            "क्रॉप डॉक्टरमध्ये आपले स्वागत आहे. "
            "मी तुमचा कृषी AI सहाय्यक आहे. "
            "मी तुमच्या पिकाचे आरोग्य समजून घेण्यास आणि "
            "क्रॉप रक्षा द्वारे निरीक्षण करण्यास मदत करतो.",

        "language":
            "कृपया तुमची भाषा निवडा.",

        "menu":
            "मुख्य मेनू. "
            "AI पीक निदानासाठी 1 दाबा. "
            "पीक आरोग्य स्थितीसाठी 2 दाबा. "
            "क्रॉप रक्षा साठी 3 दाबा. "
            "मदतीसाठी 4 दाबा. "
            "पुन्हा ऐकण्यासाठी 9 दाबा. "
            "कॉल समाप्त करण्यासाठी 0 दाबा.",

        "diagnosis":
            "AI पीक निदानासाठी पिकाचा फोटो आवश्यक आहे. "
            "पूर्ण AI निदानासाठी क्रॉप डॉक्टरच्या डायग्नोसिस पेजवर "
            "पिकाचा स्पष्ट फोटो अपलोड करा. "
            "तुम्ही तुमच्या पिकाची लक्षणे मला सांगू शकता.",

        "status":
            "मी तुमच्या पिकाची नवीनतम निरीक्षण माहिती सांगू शकतो.",

        "raksha":
            "क्रॉप रक्षा हा तुमचा दैनंदिन पीक निरीक्षण सहाय्यक आहे. "
            "तो मागील निरीक्षणे लक्षात ठेवतो आणि वेळेनुसार "
            "होणारे बदल ओळखण्यास मदत करतो.",

        "help":
            "तुम्ही कीपॅड किंवा तुमचा आवाज वापरू शकता. "
            "निदानासाठी 1, आरोग्य स्थितीसाठी 2, "
            "क्रॉप रक्षा साठी 3, पुन्हा ऐकण्यासाठी 9, "
            "आणि कॉल समाप्त करण्यासाठी 0 दाबा.",

        "invalid":
            "तुमची निवड समजली नाही. कृपया पुन्हा प्रयत्न करा.",

        "goodbye":
            "क्रॉप डॉक्टर वापरल्याबद्दल धन्यवाद. "
            "तुमच्या पिकाचे निरीक्षण करत रहा. नमस्कार.",

        "no_data":
            "या पिकासाठी अद्याप निरीक्षणाची माहिती उपलब्ध नाही.",

        "choose_crop":
            "कृपया कीपॅडद्वारे तुमचे पीक निवडा.",

        "next_action":
            "तुमच्या पिकाचे निरीक्षण सुरू ठेवा आणि "
            "पुढील निरीक्षणाच्या वेळी आणखी एक फोटो अपलोड करा."
    }
}


# ============================================================
# JSON LOADING
# ============================================================

def load_json(path):

    if not os.path.exists(path):
        return []

    try:
        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except Exception:
        return []


def get_project_data():

    crops = load_json(
        CROPS_FILE
    )

    raksha = load_json(
        RAKSHA_FILE
    )

    monitoring = load_json(
        MONITORING_FILE
    )

    return {
        "crops": crops,
        "raksha": raksha,
        "monitoring": monitoring
    }


# ============================================================
# DATA NORMALIZATION
# ============================================================

def crop_name(crop):

    return (
        crop.get("crop_name")
        or crop.get("crop")
        or crop.get("name")
        or "Unknown crop"
    )


def crop_identifier(crop):

    return (
        crop.get("id")
        or crop.get("crop_id")
        or crop.get("registration_id")
    )


def get_records(crop, data):

    crop_id = crop_identifier(crop)

    records = []

    for record in (
        data.get("raksha", [])
        + data.get("monitoring", [])
    ):

        record_id = (
            record.get("crop_id")
            or record.get("cropId")
        )

        if (
            crop_id is not None
            and str(record_id) == str(crop_id)
        ):
            records.append(record)

    records.sort(
        key=lambda x: x.get(
            "date",
            ""
        )
    )

    return records


def build_crop_status(
    crop,
    data
):

    records = get_records(
        crop,
        data
    )

    if not records:

        return {
            "available": False
        }

    latest = records[-1]

    return {
        "available": True,

        "crop": crop_name(crop),

        "day": latest.get(
            "day",
            len(records)
        ),

        "date": latest.get(
            "date",
            ""
        ),

        "disease": latest.get(
            "disease",
            "Unknown"
        ),

        "confidence": latest.get(
            "confidence",
            0
        ),

        "status": latest.get(
            "status",
            "unknown"
        ),

        "observation": latest.get(
            "observation",
            "No observation recorded."
        ),

        "observations": len(records)
    }


# ============================================================
# SPEECH COMMAND NORMALIZATION
# ============================================================

def interpret_command(command):

    if not command:
        return None

    command = command.lower().strip()

    mappings = {

        "1": "1",
        "one": "1",
        "diagnosis": "1",
        "diagnose": "1",
        "ai diagnosis": "1",
        "crop diagnosis": "1",
        "check my crop": "1",

        "2": "2",
        "two": "2",
        "status": "2",
        "crop status": "2",
        "health": "2",
        "health status": "2",

        "3": "3",
        "three": "3",
        "raksha": "3",
        "crop raksha": "3",
        "crop protection": "3",

        "4": "4",
        "four": "4",
        "help": "4",

        "9": "9",
        "nine": "9",
        "repeat": "9",
        "again": "9",

        "0": "0",
        "zero": "0",
        "exit": "0",
        "quit": "0",
        "stop": "0",
        "end": "0"
    }

    for phrase, value in mappings.items():

        if phrase in command:
            return value

    return None