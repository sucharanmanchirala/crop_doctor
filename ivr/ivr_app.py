import streamlit as st
import streamlit.components.v1 as components
import json
import os




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
            "Welcome to Crop Doctor. "
            "I am your AI agricultural assistant.",

        "choose_language":
            "Please choose your language. "
            "Press 1 for English, "
            "2 for Telugu, "
            "3 for Hindi, "
            "or 4 for Marathi.",

        "main_menu":
            "Main menu. "
            "Press 1 for Crop Diagnosis. "
            "Press 2 for Crop Status. "
            "Press 3 for Crop Raksha AI. "
            "Press 4 for Help. "
            "Press 9 to Repeat. "
            "Press 0 to End.",

        "diagnosis":
            "Crop Diagnosis selected. "
            "Please open the Crop Doctor diagnosis section "
            "and upload a clear photograph of the affected crop. "
            "The AI will analyze the photograph.",

        "choose_crop":
            "Please select your crop.",

        "status":
            "I am checking your crop status.",

        "raksha":
            "Crop Raksha AI selected. "
            "I will use your previous observations "
            "to monitor changes in your crop.",

        "help":
            "You can use this IVR to check crop status, "
            "use Crop Raksha, "
            "or start a crop diagnosis.",

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
            "మీ భాషను ఎంచుకోండి. "
            "ఇంగ్లీష్ కోసం ఒకటి, "
            "తెలుగు కోసం రెండు, "
            "హిందీ కోసం మూడు, "
            "మరాఠీ కోసం నాలుగు నొక్కండి.",

        "main_menu":
            "ప్రధాన మెనూ. "
            "పంట వ్యాధి నిర్ధారణ కోసం ఒకటి. "
            "పంట స్థితి కోసం రెండు. "
            "క్రాప్ రక్ష AI కోసం మూడు. "
            "సహాయం కోసం నాలుగు. "
            "మళ్లీ వినడానికి తొమ్మిది. "
            "ముగించడానికి సున్నా నొక్కండి.",

        "diagnosis":
            "పంట వ్యాధి నిర్ధారణ ఎంపిక చేయబడింది. "
            "క్రాప్ డాక్టర్ డయాగ్నోసిస్ విభాగాన్ని తెరిచి "
            "పంటకు సంబంధించిన స్పష్టమైన ఫోటోను అప్లోడ్ చేయండి. "
            "AI ఫోటోను విశ్లేషిస్తుంది.",

        "choose_crop":
            "దయచేసి మీ పంటను ఎంచుకోండి.",

        "status":
            "మీ పంట స్థితిని పరిశీలిస్తున్నాను.",

        "raksha":
            "క్రాప్ రక్ష AI ఎంపిక చేయబడింది. "
            "మీ పంటలో మార్పులను గమనించడానికి "
            "మునుపటి పరిశీలనలను ఉపయోగిస్తాను.",

        "help":
            "ఈ IVR ద్వారా పంట స్థితిని చూడవచ్చు, "
            "క్రాప్ రక్షను ఉపయోగించవచ్చు, "
            "లేదా పంట వ్యాధి నిర్ధారణ ప్రారంభించవచ్చు.",

        "no_crops":
            "రిజిస్టర్ చేసిన పంటలు ఏవీ కనుగొనబడలేదు. "
            "ముందుగా క్రాప్ డాక్టర్‌లో పంటను రిజిస్టర్ చేయండి.",

        "repeat":
            "ప్రస్తుత మెనూను మళ్లీ చెబుతున్నాను.",

        "goodbye":
            "క్రాప్ డాక్టర్‌ను ఉపయోగించినందుకు ధన్యవాదాలు. "
            "మీ పంటలను జాగ్రత్తగా చూసుకోండి. నమస్కారం.",

        "invalid":
            "మీ ఎంపిక అర్థం కాలేదు. "
            "దయచేసి మళ్లీ ప్రయత్నించండి.",

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
            "अपनी भाषा चुनें। "
            "अंग्रेज़ी के लिए एक, "
            "तेलुगु के लिए दो, "
            "हिंदी के लिए तीन, "
            "और मराठी के लिए चार दबाएँ।",

        "main_menu":
            "मुख्य मेनू। "
            "फसल रोग पहचान के लिए एक। "
            "फसल की स्थिति के लिए दो। "
            "क्रॉप रक्षा AI के लिए तीन। "
            "मदद के लिए चार। "
            "दोबारा सुनने के लिए नौ। "
            "समाप्त करने के लिए शून्य दबाएँ।",

        "diagnosis":
            "फसल रोग पहचान चुना गया है। "
            "कृपया क्रॉप डॉक्टर के डायग्नोसिस सेक्शन में जाकर "
            "फसल की साफ तस्वीर अपलोड करें। "
            "AI तस्वीर का विश्लेषण करेगा।",

        "choose_crop":
            "कृपया अपनी फसल चुनें।",

        "status":
            "मैं आपकी फसल की स्थिति जाँच रहा हूँ।",

        "raksha":
            "क्रॉप रक्षा AI चुना गया है। "
            "मैं आपकी फसल में बदलावों की निगरानी के लिए "
            "पिछली जानकारी का उपयोग करूँगा।",

        "help":
            "इस IVR से आप फसल की स्थिति देख सकते हैं, "
            "क्रॉप रक्षा का उपयोग कर सकते हैं, "
            "या रोग पहचान शुरू कर सकते हैं।",

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
            "तुमची भाषा निवडा. "
            "इंग्रजीसाठी एक, "
            "तेलुगूसाठी दोन, "
            "हिंदीसाठी तीन, "
            "आणि मराठीसाठी चार दाबा.",

        "main_menu":
            "मुख्य मेनू. "
            "पीक रोग निदानासाठी एक. "
            "पिकाची स्थिती पाहण्यासाठी दोन. "
            "क्रॉप रक्षा AI साठी तीन. "
            "मदतीसाठी चार. "
            "पुन्हा ऐकण्यासाठी नऊ. "
            "समाप्त करण्यासाठी शून्य दाबा.",

        "diagnosis":
            "पीक रोग निदान निवडले आहे. "
            "कृपया क्रॉप डॉक्टरमधील डायग्नोसिस विभाग उघडा "
            "आणि पिकाचा स्पष्ट फोटो अपलोड करा. "
            "AI फोटोचे विश्लेषण करेल.",

        "choose_crop":
            "कृपया तुमचे पीक निवडा.",

        "status":
            "मी तुमच्या पिकाची स्थिती तपासत आहे.",

        "raksha":
            "क्रॉप रक्षा AI निवडले आहे. "
            "तुमच्या पिकातील बदल पाहण्यासाठी "
            "आधीच्या निरीक्षणांचा उपयोग केला जाईल.",

        "help":
            "या IVR द्वारे तुम्ही पिकाची स्थिती पाहू शकता, "
            "क्रॉप रक्षा वापरू शकता "
            "किंवा रोग निदान सुरू करू शकता.",

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

<title>Crop Doctor IVR</title>


<style>

* {
    box-sizing: border-box;
}


body {

    margin: 0;

    padding: 0;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    background:
        linear-gradient(
            135deg,
            #06180f,
            #0b2b1c,
            #102f20
        );

    min-height: 100vh;

    color: white;
}


.wrapper {

    width: 100%;

    min-height: 100vh;

    display: flex;

    justify-content: center;

    align-items: center;

    padding: 25px;
}


.phone {

    width: 440px;

    max-width: 100%;

    min-height: 780px;

    border-radius: 38px;

    background:
        linear-gradient(
            145deg,
            #101010,
            #202020
        );

    border: 5px solid #303030;

    box-shadow:
        0 30px 80px
        rgba(0,0,0,0.65);

    overflow: hidden;

    position: relative;
}


.notch {

    width: 145px;

    height: 27px;

    background: #050505;

    border-radius:
        0 0 18px 18px;

    margin: 0 auto;
}


.header {

    padding:
        20px 25px 12px;

    text-align: center;
}


.logo {

    width: 72px;

    height: 72px;

    margin: auto;

    border-radius: 50%;

    display: flex;

    justify-content: center;

    align-items: center;

    font-size: 38px;

    background:
        linear-gradient(
            135deg,
            #218f4c,
            #58c879
        );

    box-shadow:
        0 8px 30px
        rgba(50,200,100,0.25);
}


.title {

    margin-top: 11px;

    font-size: 25px;

    font-weight: bold;
}


.subtitle {

    margin-top: 5px;

    font-size: 13px;

    color: #999;
}


.status {

    margin:
        10px 25px;

    padding: 10px;

    text-align: center;

    border-radius: 12px;

    background: #18271e;

    color: #72e49a;

    font-size: 12px;
}


.voice-status {

    margin:
        0 25px 10px;

    padding: 9px;

    text-align: center;

    border-radius: 10px;

    background: #111c16;

    border: 1px solid #243d2c;

    color: #aaa;

    font-size: 11px;

}


.screen {

    margin:
        15px 20px;

    min-height: 280px;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            #08120d,
            #0d1d14
        );

    border: 1px solid #254632;

    padding: 20px;

    display: flex;

    flex-direction: column;

    justify-content: space-between;
}


.screen-label {

    color: #66d98b;

    font-size: 11px;

    text-transform: uppercase;

    letter-spacing: 1.5px;
}


.message {

    margin-top: 15px;

    font-size: 17px;

    line-height: 1.55;

    white-space: pre-line;

    color: #f0f5f1;
}


.selected {

    margin-top: 15px;

    min-height: 20px;

    color: #70dd94;

    font-size: 12px;
}


.mic-area {

    display: flex;

    justify-content: center;

    padding:
        8px 0 15px;
}


.mic {

    width: 68px;

    height: 68px;

    border-radius: 50%;

    border: none;

    background:
        linear-gradient(
            145deg,
            #35a95d,
            #177c3d
        );

    color: white;

    font-size: 28px;

    cursor: pointer;

    box-shadow:
        0 8px 30px
        rgba(35,170,85,0.3);

    transition: 0.2s;
}


.mic:hover {

    transform: scale(1.05);
}


.mic.listening {

    background:
        linear-gradient(
            145deg,
            #d64d4d,
            #9e2222
        );

    animation:
        pulse 1s infinite;
}


@keyframes pulse {

    0% {
        box-shadow:
            0 0 0 0
            rgba(255,70,70,0.6);
    }

    70% {
        box-shadow:
            0 0 0 18px
            rgba(255,70,70,0);
    }

    100% {
        box-shadow:
            0 0 0 0
            rgba(255,70,70,0);
    }
}


.mic-label {

    text-align: center;

    color: #888;

    font-size: 10px;

    margin-top: 5px;
}


.keypad {

    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 10px;

    padding:
        10px 25px 25px;
}


.key {

    height: 54px;

    border-radius: 15px;

    border:
        1px solid #303030;

    background:
        linear-gradient(
            145deg,
            #242424,
            #171717
        );

    color: white;

    font-size: 20px;

    cursor: pointer;

    transition: 0.15s;
}


.key:hover {

    background: #303030;

    transform:
        translateY(-2px);
}


.key:active {

    transform:
        scale(0.96);
}


.key.special {

    color: #6ee89a;
}


.footer {

    text-align: center;

    padding:
        0 20px 20px;

    font-size: 10px;

    color: #555;
}

</style>

</head>


<body>


<div class="wrapper">


<div class="phone">


<div class="notch"></div>


<div class="header">

<div class="logo">
🌱
</div>

<div class="title">
Crop Doctor
</div>

<div class="subtitle">
AI Agricultural IVR Assistant
</div>

</div>


<div
    class="status"
    id="status"
>
● Connecting
</div>


<div
    class="voice-status"
    id="voiceStatus"
>
Checking language voices...
</div>


<div class="screen">


<div>

<div class="screen-label">
AI VOICE ASSISTANT
</div>


<div
    class="message"
    id="message"
>
Connecting...
</div>


<div
    class="selected"
    id="selected"
>
</div>

</div>


<div class="mic-area">

<div>

<button
    class="mic"
    id="micButton"
    onclick="toggleListening()"
>
🎙️
</button>

<div class="mic-label">
Tap to speak
</div>

</div>

</div>


</div>


<div class="keypad">


<button
    class="key"
    onclick="pressKey('1')"
>
1
</button>


<button
    class="key"
    onclick="pressKey('2')"
>
2
</button>


<button
    class="key"
    onclick="pressKey('3')"
>
3
</button>


<button
    class="key"
    onclick="pressKey('4')"
>
4
</button>


<button
    class="key"
    onclick="pressKey('5')"
>
5
</button>


<button
    class="key"
    onclick="pressKey('6')"
>
6
</button>


<button
    class="key"
    onclick="pressKey('7')"
>
7
</button>


<button
    class="key"
    onclick="pressKey('8')"
>
8
</button>


<button
    class="key"
    onclick="pressKey('9')"
>
9
</button>


<button
    class="key special"
    onclick="pressKey('*')"
>
*
</button>


<button
    class="key"
    onclick="pressKey('0')"
>
0
</button>


<button
    class="key special"
    onclick="pressKey('#')"
>
#
</button>


</div>


<div class="footer">
Crop Doctor • Offline AI IVR Demonstration
</div>


</div>

</div>


<script>


// ============================================================
// DATA FROM PYTHON
// ============================================================

const LANGUAGES =
__LANGUAGES__;

const CROPS =
__CROPS__;


// ============================================================
// LANGUAGE LOCALES
// ============================================================

const LANGUAGE_LOCALES = {

    "en": [
        "en-IN",
        "en-US",
        "en-GB",
        "en"
    ],

    "te": [
        "te-IN",
        "te"
    ],

    "hi": [
        "hi-IN",
        "hi"
    ],

    "mr": [
        "mr-IN",
        "mr"
    ]

};


// ============================================================
// STATE
// ============================================================

let language = null;

let state = "language";

let selectedCrop = null;

let listening = false;

let recognition = null;

let availableVoices = [];


// ============================================================
// ELEMENTS
// ============================================================

const messageElement =
    document.getElementById(
        "message"
    );

const selectedElement =
    document.getElementById(
        "selected"
    );

const statusElement =
    document.getElementById(
        "status"
    );

const voiceStatusElement =
    document.getElementById(
        "voiceStatus"
    );

const micButton =
    document.getElementById(
        "micButton"
    );


// ============================================================
// VOICE LOADING
// ============================================================

function loadVoices() {

    if (
        !("speechSynthesis" in window)
    ) {

        availableVoices = [];

        voiceStatusElement.textContent =
            "Speech synthesis is not supported.";

        return;

    }


    availableVoices =
        window.speechSynthesis
            .getVoices();


    updateVoiceStatus();

}


// Chrome sometimes loads voices asynchronously.

if (
    "speechSynthesis" in window
) {

    window.speechSynthesis
        .onvoiceschanged =
        function() {

            loadVoices();

        };

}


function updateVoiceStatus() {

    if (!language) {

        voiceStatusElement.textContent =
            "Choose a language to activate its voice.";

        return;

    }


    const voice =
        findVoice(language);


    if (voice) {

        voiceStatusElement.textContent =
            "🔊 "
            + LANGUAGES[language].name
            + " voice: "
            + voice.name
            + " ("
            + voice.lang
            + ")";

    } else {

        voiceStatusElement.textContent =
            "⚠️ "
            + LANGUAGES[language].name
            + " voice not installed in this browser.";

    }

}


// ============================================================
// FIND BEST VOICE
// ============================================================

function findVoice(languageCode) {

    if (
        !availableVoices.length
    ) {

        return null;

    }


    const locales =
        LANGUAGE_LOCALES[
            languageCode
        ] || [];


    // --------------------------------------------------------
    // 1. EXACT LOCALE
    // --------------------------------------------------------

    for (
        const locale of locales
    ) {

        const exact =
            availableVoices.find(
                function(voice) {

                    return (
                        voice.lang
                            .toLowerCase()
                        ===
                        locale.toLowerCase()
                    );

                }
            );

        if (exact) {

            return exact;

        }

    }


    // --------------------------------------------------------
    // 2. SAME LANGUAGE PREFIX
    // --------------------------------------------------------

    const prefix =
        languageCode
            .toLowerCase()
            + "-";


    const sameLanguage =
        availableVoices.find(
            function(voice) {

                return voice.lang
                    .toLowerCase()
                    .startsWith(prefix);

            }
        );


    if (sameLanguage) {

        return sameLanguage;

    }


    // --------------------------------------------------------
    // 3. BASE LANGUAGE
    // --------------------------------------------------------

    const base =
        availableVoices.find(
            function(voice) {

                return voice.lang
                    .toLowerCase()
                    === languageCode
                    .toLowerCase();

            }
        );


    if (base) {

        return base;

    }


    return null;

}


// ============================================================
// DISPLAY
// ============================================================

function setMessage(text) {

    messageElement.textContent =
        text;

}


function setStatus(text) {

    statusElement.textContent =
        "● " + text;

}


function setSelected(text) {

    selectedElement.textContent =
        text;

}


// ============================================================
// SPEAK
// ============================================================

function speak(text) {

    if (
        !("speechSynthesis" in window)
    ) {

        return false;

    }


    const voice =
        findVoice(language);


    if (!voice) {

        voiceStatusElement.textContent =
            "⚠️ No "
            + (
                LANGUAGES[language]
                ? LANGUAGES[language].name
                : "selected language"
            )
            + " voice is available.";

        return false;

    }


    window.speechSynthesis.cancel();


    const utterance =
        new SpeechSynthesisUtterance(
            text
        );


    // IMPORTANT:
    // Use the actual installed voice locale.

    utterance.voice =
        voice;

    utterance.lang =
        voice.lang;


    utterance.rate =
        0.88;

    utterance.pitch =
        1.0;

    utterance.volume =
        1.0;


    utterance.onstart =
        function() {

            setStatus(
                "Speaking"
            );

        };


    utterance.onend =
        function() {

            setStatus(
                "Ready"
            );

        };


    utterance.onerror =
        function() {

            setStatus(
                "Voice error"
            );

        };


    window.speechSynthesis.speak(
        utterance
    );


    return true;

}


// ============================================================
// RESPOND
// ============================================================

function respond(
    text,
    shouldSpeak = true
) {

    setMessage(text);


    if (shouldSpeak) {

        speak(text);

    }

}


// ============================================================
// TRANSLATION
// ============================================================

function t(
    key,
    variables = {}
) {

    if (!language) {

        language = "en";

    }


    let text =
        (
            LANGUAGES[language]
            &&
            LANGUAGES[language][key]
        )
        ||
        (
            LANGUAGES["en"]
            &&
            LANGUAGES["en"][key]
        )
        ||
        key;


    Object.keys(
        variables
    ).forEach(
        function(name) {

            text =
                text.replace(
                    "{" + name + "}",
                    variables[name]
                );

        }
    );


    return text;

}


// ============================================================
// LANGUAGE SELECTION
// ============================================================

function selectLanguage(
    code
) {

    if (
        !LANGUAGES[code]
    ) {

        return;

    }


    language = code;

    state = "menu";

    selectedCrop = null;


    setSelected(
        LANGUAGES[code].name
    );


    loadVoices();

    updateVoiceStatus();


    const text =
        t("main_menu");


    respond(text);

}


// ============================================================
// MAIN MENU
// ============================================================

function showMenu() {

    state = "menu";


    const text =
        t("main_menu");


    respond(text);

}


// ============================================================
// CROP MENU
// ============================================================

function showCropMenu(
    nextState
) {

    if (
        !CROPS.length
    ) {

        state = "menu";

        respond(
            t("no_crops")
        );

        return;

    }


    state =
        nextState;


    let text =
        t("choose_crop")
        + "\n\n";


    CROPS.forEach(
        function(
            crop,
            index
        ) {

            text +=
                (
                    index + 1
                )
                + ". "
                + crop.crop_name
                + "\n";

        }
    );


    text +=
        "\nPress the crop number.";


    respond(text);

}


// ============================================================
// CROP STATUS
// ============================================================

function showStatus(
    crop
) {

    selectedCrop =
        crop;


    state =
        "menu";


    setSelected(
        crop.crop_name
    );


    let text =
        t("status")
        + "\n\n";


    text +=
        crop.crop_name
        + " - "
        + crop.field_label
        + "\n\n";


    let latest =
        crop.latest_raksha;


    if (!latest) {

        latest =
            crop.latest_monitoring;

    }


    if (latest) {

        const disease =
            latest.disease
            || "Unknown";


        const confidence =
            Number(
                latest.confidence
                || 0
            ).toFixed(2);


        text +=
            t(
                "status_summary",
                {
                    disease:
                        disease,

                    confidence:
                        confidence
                }
            );


        text +=
            "\n\n";


        if (
            latest.status
        ) {

            text +=
                "Visual status: "
                + latest.status
                + "\n";

        }


        if (
            latest.date
        ) {

            text +=
                t("last_observation", {date: latest.date});

        }

    } else {

        text +=
            "No recent AI observation "
            + "is available.";

    }


    text +=
        "\n\n"
        + t("raksha_count", {count: crop.raksha_count});

    text +=
        "\n"
        + t("monitoring_count", {count: crop.monitoring_count});


    respond(text);

}


// ============================================================
// CROP RAKSHA
// ============================================================

function showRaksha(
    crop
) {

    selectedCrop =
        crop;


    state =
        "menu";


    setSelected(
        crop.crop_name
    );


    let text =
        t("raksha")
        + "\n\n";


    text +=
        crop.crop_name
        + " - "
        + crop.field_label
        + "\n\n";


    if (
        crop.raksha_count > 0
    ) {

        text +=
            t(
                "raksha_summary",
                {
                    count:
                        crop.raksha_count
                }
            );


        text +=
            "\n\n";


        const latest =
            crop.latest_raksha;


        if (latest) {

            if (
                latest.day
            ) {

                text +=
                    "Latest observation: Day "
                    + latest.day
                    + "\n";

            }


            if (
                latest.status
            ) {

                text +=
                    "Visual status: "
                    + latest.status
                    + "\n";

            }


            if (
                latest.disease
            ) {

                text +=
                    "AI result: "
                    + latest.disease
                    + "\n";

            }


            if (
                latest.confidence !== undefined
            ) {

                text +=
                    "Confidence: "
                    + Number(
                        latest.confidence
                    ).toFixed(2)
                    + "%\n";

            }


            if (
                latest.date
            ) {

                text +=
                    "Recorded: "
                    + latest.date;

            }

        }

    } else {

        text +=
            t("no_history")
            + "\n\n";

        text +=
            "Open Crop Raksha in the "
            + "main application to create "
            + "the first observation.";

    }


    respond(text);

}


// ============================================================
// DIAGNOSIS
// ============================================================

function diagnosis() {

    state =
        "menu";


    const text =
        t("diagnosis")
        + "\n\n"
        + "Use a clear photo of the leaf "
        + "or affected plant part.";


    respond(text);

}


// ============================================================
// HELP
// ============================================================

function showHelp() {

    state =
        "menu";


    let text =
        t("help")
        + "\n\n";


    text +=
        "1 = Diagnosis\n";

    text +=
        "2 = Crop Status\n";

    text +=
        "3 = Crop Raksha AI\n";

    text +=
        "4 = Help\n";

    text +=
        "9 = Repeat\n";

    text +=
        "0 = End";


    respond(text);

}


// ============================================================
// END
// ============================================================

function endCall() {

    state =
        "ended";


    if (
        "speechSynthesis" in window
    ) {

        window.speechSynthesis.cancel();

    }


    setStatus(
        "Call ended"
    );


    respond(
        t("goodbye")
    );

}


// ============================================================
// KEYPAD
// ============================================================

function pressKey(
    value
) {

    if (
        state === "ended"
    ) {

        return;

    }


    // --------------------------------------------------------
    // LANGUAGE
    // --------------------------------------------------------

    if (
        state === "language"
    ) {

        const map = {

            "1": "en",
            "2": "te",
            "3": "hi",
            "4": "mr"

        };


        if (
            map[value]
        ) {

            selectLanguage(
                map[value]
            );

        } else {

            respond(
                "Please press 1, 2, 3 or 4."
            );

        }


        return;

    }


    // --------------------------------------------------------
    // CROP SELECTION
    // --------------------------------------------------------

    if (
        state === "crop_status"
        ||
        state === "crop_raksha"
    ) {

        const index =
            parseInt(
                value,
                10
            ) - 1;


        if (
            !isNaN(index)
            &&
            index >= 0
            &&
            index < CROPS.length
        ) {

            const crop =
                CROPS[index];


            if (
                state === "crop_status"
            ) {

                showStatus(
                    crop
                );

            } else {

                showRaksha(
                    crop
                );

            }

        } else {

            respond(
                t("invalid")
            );

        }


        return;

    }


    // --------------------------------------------------------
    // MAIN MENU
    // --------------------------------------------------------

    if (
        state === "menu"
    ) {

        switch (value) {

            case "1":

                diagnosis();

                break;


            case "2":

                showCropMenu(
                    "crop_status"
                );

                break;


            case "3":

                showCropMenu(
                    "crop_raksha"
                );

                break;


            case "4":

                showHelp();

                break;


            case "9":

                respond(
                    t("repeat")
                );


                setTimeout(
                    function() {

                        showMenu();

                    },
                    900
                );

                break;


            case "0":

                endCall();

                break;


            default:

                respond(
                    t("invalid")
                );

        }

    }

}


// ============================================================
// START CALL
// ============================================================

function startCall() {

    state =
        "language";


    language =
        null;


    selectedCrop =
        null;


    setSelected("");


    setStatus(
        "Connected"
    );


    const text = t("choose_language");


    respond(text);

}


// ============================================================
// SPEECH RECOGNITION
// ============================================================

function setupRecognition() {

    const SpeechRecognition =
        window.SpeechRecognition
        ||
        window.webkitSpeechRecognition;


    if (!SpeechRecognition) {

        recognition =
            null;

        return false;

    }


    recognition =
        new SpeechRecognition();


    recognition.continuous =
        false;


    recognition.interimResults =
        false;


    recognition.maxAlternatives =
        1;


    recognition.onstart =
        function() {

            listening =
                true;


            micButton.classList.add(
                "listening"
            );


            micButton.textContent =
                "⏹️";


            setStatus(
                "Listening..."
            );

        };


    recognition.onend =
        function() {

            listening =
                false;


            micButton.classList.remove(
                "listening"
            );


            micButton.textContent =
                "🎙️";


            setStatus(
                "Ready"
            );

        };


    recognition.onerror =
        function() {

            listening =
                false;


            micButton.classList.remove(
                "listening"
            );


            micButton.textContent =
                "🎙️";


            setStatus(
                "Voice input unavailable"
            );

        };


    recognition.onresult =
        function(event) {

            const transcript =
                event
                    .results[0][0]
                    .transcript
                    .toLowerCase()
                    .trim();


            handleVoiceInput(
                transcript
            );

        };


    return true;

}


// ============================================================
// VOICE INPUT
// ============================================================

function handleVoiceInput(
    text
) {

    setSelected(
        "Heard: " + text
    );


    // --------------------------------------------------------
    // LANGUAGE SELECTION
    // --------------------------------------------------------

    if (
        state === "language"
    ) {

        if (
            text.includes("english")
            ||
            text.includes("इंग्लिश")
            ||
            text.includes("इंग्रजी")
        ) {

            selectLanguage(
                "en"
            );

            return;

        }


        if (
            text.includes("telugu")
            ||
            text.includes("తెలుగు")
        ) {

            selectLanguage(
                "te"
            );

            return;

        }


        if (
            text.includes("hindi")
            ||
            text.includes("हिंदी")
        ) {

            selectLanguage(
                "hi"
            );

            return;

        }


        if (
            text.includes("marathi")
            ||
            text.includes("मराठी")
        ) {

            selectLanguage(
                "mr"
            );

            return;

        }


        const digit =
            text.match(
                /[1-4]/
            );


        if (digit) {

            pressKey(
                digit[0]
            );

            return;

        }


        respond(
            t("invalid")
        );


        return;

    }


    // --------------------------------------------------------
    // CROP SELECTION
    // --------------------------------------------------------

    if (
        state === "crop_status"
        ||
        state === "crop_raksha"
    ) {

        const numberWords = {

            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",

            "एक": "1",
            "दो": "2",
            "तीन": "3",
            "चार": "4",
            "पाँच": "5",

            "ఒకటి": "1",
            "రెండు": "2",
            "మూడు": "3",
            "నాలుగు": "4",
            "ఐదు": "5"

        };


        for (
            const word
            in numberWords
        ) {

            if (
                text.includes(word)
            ) {

                pressKey(
                    numberWords[word]
                );

                return;

            }

        }


        const digit =
            text.match(
                /[1-9]/
            );


        if (digit) {

            pressKey(
                digit[0]
            );

            return;

        }


        // Crop-name recognition

        for (
            let i = 0;
            i < CROPS.length;
            i++
        ) {

            const cropName =
                CROPS[i]
                    .crop_name
                    .toLowerCase();


            if (
                text.includes(
                    cropName
                )
            ) {

                if (
                    state === "crop_status"
                ) {

                    showStatus(
                        CROPS[i]
                    );

                } else {

                    showRaksha(
                        CROPS[i]
                    );

                }


                return;

            }

        }


        respond(
            t("invalid")
        );


        return;

    }


    // --------------------------------------------------------
    // MAIN MENU VOICE COMMANDS
    // --------------------------------------------------------

    if (
        state === "menu"
    ) {

        if (
            text.includes("diagnosis")
            ||
            text.includes("diagnose")
            ||
            text.includes("disease")
            ||
            text.includes("रोग")
            ||
            text.includes("వ్యాధి")
        ) {

            pressKey("1");

            return;

        }


        if (
            text.includes("status")
            ||
            text.includes("health")
            ||
            text.includes("स्थिति")
            ||
            text.includes("स्थिती")
            ||
            text.includes("స్థితి")
        ) {

            pressKey("2");

            return;

        }


        if (
            text.includes("raksha")
            ||
            text.includes("रक्षा")
            ||
            text.includes("రక్ష")
        ) {

            pressKey("3");

            return;

        }


        if (
            text.includes("help")
            ||
            text.includes("मदद")
            ||
            text.includes("सहायता")
            ||
            text.includes("సహాయం")
        ) {

            pressKey("4");

            return;

        }


        if (
            text.includes("repeat")
            ||
            text.includes("again")
        ) {

            pressKey("9");

            return;

        }


        if (
            text.includes("end")
            ||
            text.includes("exit")
            ||
            text.includes("stop")
            ||
            text.includes("goodbye")
        ) {

            pressKey("0");

            return;

        }


        const digit =
            text.match(
                /[0-4]/
            );


        if (digit) {

            pressKey(
                digit[0]
            );

            return;

        }


        respond(
            t("invalid")
        );

    }

}


// ============================================================
// MICROPHONE
// ============================================================

function toggleListening() {

    if (!recognition) {

        const available =
            setupRecognition();


        if (!available) {

            setStatus(
                "Speech recognition unavailable"
            );


            respond(
                "Voice input is not supported "
                + "by this browser. "
                + "Please use the keypad."
            );


            return;

        }

    }


    if (listening) {

        recognition.stop();

        return;

    }


    const localeList =
        LANGUAGE_LOCALES[
            language || "en"
        ];


    recognition.lang =
        localeList
            ? localeList[0]
            : "en-IN";


    try {

        recognition.start();

    } catch (error) {

        setStatus(
            "Microphone busy"
        );

    }

}


// ============================================================
// INITIALIZE
// ============================================================

window.onload =
    function() {

        loadVoices();

        setupRecognition();


        setTimeout(
            function() {

                loadVoices();

                startCall();

            },
            700
        );

    };

</script>

</body>

</html>
"""


# ============================================================
# RENDERER
# ============================================================

def render_anjaneya_voice():
    global crops_data, raksha_history, monitoring_history
    global crops, crop_records, translations_json, crops_json, page_html

    crops_data = load_json(CROPS_FILE, [])
    raksha_history = load_json(RAKSHA_FILE, [])
    monitoring_history = load_json(MONITORING_FILE, [])
    crops = normalize_crops(crops_data)

    crop_records = []
    for crop in crops:
        crop_id = crop["id"]
        raksha_records = [r for r in raksha_history if str(r.get("crop_id", "")) == crop_id]
        monitoring_records = [r for r in monitoring_history if str(r.get("crop_id", "")) == crop_id or (not r.get("crop_id") and str(r.get("crop", "")).strip().lower() == str(crop["crop_name"]).strip().lower())]
        latest_raksha = sorted(raksha_records, key=lambda x: str(x.get("date", "")))[-1] if raksha_records else None
        latest_monitoring = sorted(monitoring_records, key=lambda x: str(x.get("date") or x.get("timestamp") or ""))[-1] if monitoring_records else None
        crop_records.append({"id":crop_id,"crop_name":crop["crop_name"],"farmer_name":crop["farmer_name"],"field_label":crop["field_label"],"sowing_date":crop["sowing_date"],"raksha_count":len(raksha_records),"monitoring_count":len(monitoring_records),"latest_raksha":latest_raksha,"latest_monitoring":latest_monitoring})

    translations_json = json.dumps(translations, ensure_ascii=False)
    crops_json = json.dumps(crop_records, ensure_ascii=False)

    # ============================================================
    # INJECT PYTHON DATA
    # ============================================================

    html = page_html.replace(
        "__LANGUAGES__",
        translations_json
    )

    html = html.replace(
        "__CROPS__",
        crops_json
    )


    # ============================================================
    # STREAMLIT TITLE
    # ============================================================

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:8px 0 4px 0;
        ">

            <h2 style="margin-bottom:0;">
                🔱 Anjaneya — AI Voice Crop Guardian
            </h2>

            <p style="
                color:#888;
                margin-top:4px;
            ">
                Multilingual Offline AI Voice Assistant
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ============================================================
    # INFORMATION
    # ============================================================

    with st.expander(
        "ℹ️ IVR Demo — How it works",
        expanded=False
    ):

        st.write(
            """
            **Crop Doctor IVR is a local voice assistant demonstration.**

            The farmer can:

            - 🎙️ Speak to the assistant
            - 🔢 Use the keypad
            - 🇬🇧 English
            - 🇮🇳 Telugu
            - 🇮🇳 Hindi
            - 🇮🇳 Marathi
            - 🩺 Crop Diagnosis
            - 🌱 Crop Status
            - 🛡️ Crop Raksha AI
            - ❓ Help
            - 🔁 Repeat
            - ☎️ End Call

            The application uses the browser's available speech voices.
            No phone network or external telephony service is required.
            """
        )


    # ============================================================
    # DATA METRICS
    # ============================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Registered Crops",
            len(crop_records)
        )


    with col2:

        st.metric(
            "Raksha Records",
            len(raksha_history)
        )


    with col3:

        st.metric(
            "Monitoring Records",
            len(monitoring_history)
        )


    # ============================================================
    # IVR
    # ============================================================

    components.html(
        html,
        height=850,
        scrolling=False
    )
