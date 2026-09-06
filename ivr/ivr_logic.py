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
            "Say diagnosis for AI crop diagnosis. "
            "Say status for crop health status. "
            "Say raksha for Crop Raksha. "
            "Say help for help. "
            "Say repeat to hear this again. "
            "Say end to end the call.",

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
            "This is a voice call — just speak to me. "
            "Say diagnosis, "
            "status, "
            "raksha, "
            "repeat to hear the menu again, "
            "or end to end the call.",

        "invalid":
            "I did not understand that. "
            "Please try again.",

        "goodbye":
            "Thank you for using Crop Doctor. "
            "Keep monitoring your crop. Goodbye.",

        "no_data":
            "I do not have monitoring information for this crop yet.",

        "choose_crop":
            "Please say the name of your crop.",

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
            "దయచేసి మీ భాషను చెప్పండి.",

        "menu":
            "ప్రధాన మెనూ. "
            "AI పంట నిర్ధారణ కోసం 'నిర్ధారణ' అని చెప్పండి. "
            "పంట ఆరోగ్య స్థితి కోసం 'స్థితి' అని చెప్పండి. "
            "క్రాప్ రక్ష కోసం 'రక్ష' అని చెప్పండి. "
            "సహాయం కోసం 'సహాయం' అని చెప్పండి. "
            "మళ్లీ వినడానికి 'మళ్లీ' అని చెప్పండి. "
            "కాల్ ముగించడానికి 'ముగించు' అని చెప్పండి.",

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
            "ఇది వాయిస్ కాల్ — మీరు నాతో నేరుగా మాట్లాడవచ్చు. "
            "నిర్ధారణ కోసం 'నిర్ధారణ', ఆరోగ్య స్థితి కోసం 'స్థితి', "
            "క్రాప్ రక్ష కోసం 'రక్ష', మళ్లీ వినడానికి 'మళ్లీ', "
            "కాల్ ముగించడానికి 'ముగించు' అని చెప్పండి.",

        "invalid":
            "మీ ఎంపిక అర్థం కాలేదు. దయచేసి మళ్లీ ప్రయత్నించండి.",

        "goodbye":
            "క్రాప్ డాక్టర్‌ను ఉపయోగించినందుకు ధన్యవాదాలు. "
            "మీ పంటను పర్యవేక్షిస్తూ ఉండండి. వీడ్కోలు.",

        "no_data":
            "ఈ పంటకు ఇంకా పర్యవేక్షణ సమాచారం లేదు.",

        "choose_crop":
            "దయచేసి మీ పంట పేరు చెప్పండి.",

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
            "कृपया अपनी भाषा बोलें।",

        "menu":
            "मुख्य मेनू। "
            "AI फसल जांच के लिए 'जांच' कहें। "
            "फसल स्वास्थ्य स्थिति के लिए 'स्थिति' कहें। "
            "क्रॉप रक्षा के लिए 'रक्षा' कहें। "
            "मदद के लिए 'मदद' कहें। "
            "दोबारा सुनने के लिए 'दोबारा' कहें। "
            "कॉल समाप्त करने के लिए 'समाप्त' कहें।",

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
            "यह एक वॉइस कॉल है — आप सीधे मुझसे बोल सकते हैं। "
            "जांच के लिए 'जांच', स्वास्थ्य स्थिति के लिए 'स्थिति', "
            "क्रॉप रक्षा के लिए 'रक्षा', दोबारा सुनने के लिए 'दोबारा', "
            "और कॉल समाप्त करने के लिए 'समाप्त' कहें।",

        "invalid":
            "मैं आपकी पसंद समझ नहीं पाया। कृपया फिर कोशिश करें।",

        "goodbye":
            "क्रॉप डॉक्टर का उपयोग करने के लिए धन्यवाद। "
            "अपनी फसल की निगरानी करते रहें। नमस्ते।",

        "no_data":
            "इस फसल के लिए अभी कोई निगरानी जानकारी उपलब्ध नहीं है।",

        "choose_crop":
            "कृपया अपनी फसल का नाम बोलें।",

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
            "कृपया तुमची भाषा बोला.",

        "menu":
            "मुख्य मेनू. "
            "AI पीक निदानासाठी 'निदान' म्हणा. "
            "पीक आरोग्य स्थितीसाठी 'स्थिती' म्हणा. "
            "क्रॉप रक्षासाठी 'रक्षा' म्हणा. "
            "मदतीसाठी 'मदत' म्हणा. "
            "पुन्हा ऐकण्यासाठी 'पुन्हा' म्हणा. "
            "कॉल समाप्त करण्यासाठी 'समाप्त' म्हणा.",

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
            "ही एक व्हॉइस कॉल आहे — तुम्ही थेट माझ्याशी बोलू शकता. "
            "निदानासाठी 'निदान', आरोग्य स्थितीसाठी 'स्थिती', "
            "क्रॉप रक्षासाठी 'रक्षा', पुन्हा ऐकण्यासाठी 'पुन्हा', "
            "आणि कॉल समाप्त करण्यासाठी 'समाप्त' म्हणा.",

        "invalid":
            "तुमची निवड समजली नाही. कृपया पुन्हा प्रयत्न करा.",

        "goodbye":
            "क्रॉप डॉक्टर वापरल्याबद्दल धन्यवाद. "
            "तुमच्या पिकाचे निरीक्षण करत रहा. नमस्कार.",

        "no_data":
            "या पिकासाठी अद्याप निरीक्षणाची माहिती उपलब्ध नाही.",

        "choose_crop":
            "कृपया तुमच्या पिकाचे नाव सांगा.",

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

        "diagnosis": "1",
        "diagnose": "1",
        "ai diagnosis": "1",
        "crop diagnosis": "1",
        "check my crop": "1",
        "निदान": "1",
        "जांच": "1",
        "पहचान": "1",
        "నిర్ధారణ": "1",
        "వ్యాధి": "1",

        "status": "2",
        "crop status": "2",
        "health": "2",
        "health status": "2",
        "स्थिति": "2",
        "स्थिती": "2",
        "స్థితి": "2",

        "raksha": "3",
        "crop raksha": "3",
        "crop protection": "3",
        "रक्षा": "3",
        "రక్ష": "3",

        "help": "4",
        "मदद": "4",
        "मदत": "4",
        "సహాయం": "4",

        "repeat": "9",
        "again": "9",
        "दोबारा": "9",
        "पुन्हा": "9",
        "మళ్లీ": "9",

        "exit": "0",
        "quit": "0",
        "stop": "0",
        "end": "0",
        "समाप्त": "0",
        "ముగించు": "0"
    }

    for phrase, value in mappings.items():

        if phrase in command:
            return value

    return None