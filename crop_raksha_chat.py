import streamlit as st
from datetime import datetime


# =====================================================
# CROP RAKSHA AI COMPANION
# =====================================================

def get_crop_raksha_message(crop, records):
    """
    Generate the opening Crop Raksha message
    based on the crop and its monitoring history.
    """

    crop_name = crop.get(
        "crop_name",
        "your crop"
    )

    farmer_name = crop.get(
        "farmer_name",
        "Farmer"
    )

    crop_age = crop.get(
        "crop_age",
        None
    )

    if not records:
        return f"""
👋 **Namaste, {farmer_name}! I'm Crop Raksha.** 🌱

I'm your daily AI companion for **{crop_name}**.

I don't just look at your crop once and forget it.

I'll help you:

📸 Record your crop every day  
🧠 Remember previous observations  
🔍 Compare changes over time  
🤖 Track AI disease predictions  
⚠️ Alert you when something needs attention  
🩺 Guide you toward Crop Diagnosis when necessary

Today will become the starting point of your
**Crop Raksha journey**.

📸 When you're ready, upload today's crop photograph.
"""

    latest = records[-1]

    day = latest.get(
        "day",
        len(records)
    )

    disease = latest.get(
        "disease",
        "Unknown"
    )

    confidence = latest.get(
        "confidence",
        0
    )

    status = latest.get(
        "status",
        "unknown"
    )

    message = f"""
👋 **Welcome back, {farmer_name}!** 🌱

I'm still keeping track of your **{crop_name}**.

🧠 **What I remember:**

📅 Latest observation: **Day {day}**
🦠 AI result: **{disease}**
🎯 Confidence: **{confidence:.1f}%**
📊 Total observations: **{len(records)}**
"""

    if status == "normal":

        message += """
🟢 Your latest visual comparison showed no
significant change.

Let's continue the daily monitoring routine.
"""

    elif status == "minor_change":

        message += """
🟠 A minor visual change was noticed in the
latest observation.

We'll keep watching it rather than assuming
that it is a disease.
"""

    elif status == "significant_change":

        message += """
🔴 A significant visual change was noticed.

This deserves closer attention. If the AI also
detects a possible disease, use Crop Diagnosis
for a deeper assessment.
"""

    else:

        message += """
🌱 We'll continue building your crop's health timeline.
"""

    message += """

📸 When today's monitoring is due, upload the
new photograph and I'll help you compare it
with what we already know.
"""

    return message


# =====================================================
# CHANGE MESSAGE
# =====================================================

def get_change_message(change_level, difference):
    """
    Convert image comparison results into a
    farmer-friendly Crop Raksha response.
    """

    if change_level == "baseline":
        return """
🌱 **Baseline created**

This is our first observation.

I've saved this image as the starting point
for your Crop Raksha timeline.

From the next observation onward, I'll compare
new images with this baseline.
"""

    if change_level == "normal":
        difference_text = (
            f"{difference:.2f}%"
            if difference is not None
            else "a low"
        )

        return f"""
🟢 **Crop looks visually consistent**

The visual difference from the previous
observation is approximately **{difference_text}**.

I haven't detected a significant visual change.

That doesn't mean we stop monitoring.

🌱 Keep following your daily Crop Raksha routine.
"""

    if change_level == "minor_change":
        difference_text = (
            f"{difference:.2f}%"
            if difference is not None
            else "a small"
        )

        return f"""
🟠 **Small visual change noticed**

The visual difference from the previous
observation is approximately **{difference_text}**.

This does **not automatically mean disease**.

It simply means we should pay a little more
attention to the crop.

📸 Continue tomorrow's observation so we can
see whether this change continues.
"""

    if change_level == "significant_change":
        difference_text = (
            f"{difference:.2f}%"
            if difference is not None
            else "a significant"
        )

        return f"""
🔴 **Significant visual change noticed**

The visual difference from the previous
observation is approximately **{difference_text}**.

This does **not automatically mean that
a disease has been detected**.

However, the change is large enough that
we should investigate further.

🩺 **Recommended action:**

Open **Crop Diagnosis** and upload the latest
image for a dedicated AI assessment.
"""

    return """
⚠️ I couldn't complete the visual comparison.

The observation has still been saved.

We'll continue monitoring the crop during
the next check.
"""


# =====================================================
# DISEASE MESSAGE
# =====================================================

def get_disease_message(disease, confidence):
    """
    Explain an AI disease result in simple,
    farmer-friendly language.
    """

    if not disease:
        return ""

    disease_lower = disease.lower().strip()

    # -------------------------------------------------
    # HEALTHY
    # -------------------------------------------------

    if disease_lower == "healthy":
        return f"""
🌱 **Crop Doctor AI result: Healthy**

The AI currently classifies this image as
**Healthy** with approximately
**{confidence:.2f}% confidence**.

That's a positive result. 👍

However, one healthy observation doesn't mean
we stop monitoring.

Crop Raksha will continue checking your crop
over time for visual changes.
"""

    # -------------------------------------------------
    # LOW CONFIDENCE
    # -------------------------------------------------

    if confidence < 60:
        return f"""
⚠️ **Possible AI result: {disease}**

The model predicted **{disease}**, but its
confidence is only **{confidence:.2f}%**.

Because the confidence is relatively low,
we should treat this as a signal rather than
a definite diagnosis.

📸 Try a clearer photograph with good lighting
and use the **Crop Diagnosis** section for
further investigation.
"""

    # -------------------------------------------------
    # HIGHER CONFIDENCE
    # -------------------------------------------------

    return f"""
🦠 **AI result: {disease}**

The model detected **{disease}** with approximately
**{confidence:.2f}% confidence**.

This is an AI prediction, so it should be treated
as an indication that the crop deserves attention,
not as a guaranteed agricultural diagnosis.

🩺 If you're concerned, use the **Crop Diagnosis**
section for a dedicated assessment.
"""


# =====================================================
# HELPER FUNCTIONS
# =====================================================

def _get_latest(records):
    if not records:
        return None

    return sorted(
        records,
        key=lambda x: x.get("day", 0)
    )[-1]


def _get_previous(records):
    if len(records) < 2:
        return None

    ordered = sorted(
        records,
        key=lambda x: x.get("day", 0)
    )

    return ordered[-2]


def _format_record(record):
    if not record:
        return "No observation available."

    disease = record.get(
        "disease",
        "Unknown"
    )

    confidence = record.get(
        "confidence",
        0
    )

    day = record.get(
        "day",
        "?"
    )

    status = record.get(
        "status",
        "unknown"
    )

    return (
        f"📅 Day {day}\n"
        f"🦠 AI result: **{disease}**\n"
        f"🎯 Confidence: **{confidence:.1f}%**\n"
        f"📊 Visual status: **{status}**"
    )


# =====================================================
# CHATBOT RESPONSE
# =====================================================

def chatbot_response(
        user_message,
        crop,
        records
):
    """
    Expanded local rule-based Crop Raksha companion.

    No external API is required.
    """

    message = (
        user_message
        .lower()
        .strip()
    )

    crop_name = crop.get(
        "crop_name",
        "your crop"
    )

    farmer_name = crop.get(
        "farmer_name",
        "Farmer"
    )

    latest = _get_latest(
        records
    )

    previous = _get_previous(
        records
    )

    # =================================================
    # GREETINGS
    # =================================================

    if any(
            word in message
            for word in [
                "hello",
                "hi",
                "hey",
                "namaste",
                "good morning",
                "good evening",
                "good afternoon"
            ]
    ):
        return f"""
👋 **Namaste, {farmer_name}!** 🌱

I'm here with you and your
**{crop_name}** crop.

I currently remember **{len(records)} observation(s)**.

You can ask me:

🌱 **"How is my crop?"**  
🧠 **"What do you remember?"**  
📅 **"What happened yesterday?"**  
📊 **"Show me my latest result."**  
🔄 **"Has my crop changed?"**  
📸 **"Why do I need a photo?"**  
🎯 **"How confident is the AI?"**  
🌿 **"How old is my crop?"**  
🩺 **"What should I do if there is a disease?"**
"""

    # =================================================
    # THANK YOU
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "thank you",
                "thanks",
                "thank u",
                "thx"
            ]
    ):
        return """
😊 You're welcome!

I'll keep helping you monitor the crop.

🌱 One observation at a time,
we'll build a useful health timeline.
"""

    # =================================================
    # HELP
    # =================================================

    if (
            "help" in message
            or "what can you do" in message
            or "commands" in message
            or "questions" in message
    ):
        return """
🤖 **Here's what I can help you with:**

🌱 **Crop status**
> "How is my crop?"

🧠 **Memory**
> "What do you remember?"

📅 **Previous observation**
> "What happened yesterday?"

🔄 **Change detection**
> "Has my crop changed?"

📊 **Latest result**
> "What was the AI result?"

🎯 **Confidence**
> "How confident is the AI?"

📸 **Daily monitoring**
> "What should I do today?"

🌿 **Crop age**
> "How old is my crop?"

🩺 **Disease guidance**
> "What should I do if there is a disease?"

Just ask naturally — I'll do my best to understand.
"""

    # =================================================
    # CURRENT CROP STATUS
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "how is my crop",
                "how's my crop",
                "crop status",
                "crop condition",
                "crop health",
                "is my crop okay",
                "is my crop ok",
                "is my plant okay",
                "is my plant ok",
                "how is the crop",
                "how does my crop look"
            ]
    ):

        if not latest:
            return f"""
🌱 **{crop_name} status**

We don't have an observation yet.

This is the beginning of your Crop Raksha
journey.

📸 Upload your first crop photograph so
I can start building the health timeline.
"""

        disease = latest.get(
            "disease",
            "Unknown"
        )

        confidence = latest.get(
            "confidence",
            0
        )

        status = latest.get(
            "status",
            "unknown"
        )

        if disease.lower() == "healthy":

            health_message = (
                "🟢 The latest AI result is **Healthy**."
            )

        else:

            health_message = (
                f"🦠 The latest AI result is "
                f"**{disease}**."
            )

        return f"""
🌱 **Current Crop Raksha Status**

Crop: **{crop_name}**

📅 Latest observation: **Day {latest.get('day', '?')}**
{health_message}
🎯 AI confidence: **{confidence:.1f}%**
🔍 Visual status: **{status}**
📊 Observations remembered: **{len(records)}**

{self_status_advice(status, disease, confidence)}
"""

    # =================================================
    # LATEST RESULT
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "latest result",
                "last result",
                "latest diagnosis",
                "last diagnosis",
                "what did the ai say",
                "what was the ai result",
                "ai result",
                "what did you find"
            ]
    ):

        if not latest:
            return """
🧠 I don't have an AI result yet.

Upload your first crop photograph and
I'll start recording observations.
"""

        return f"""
🤖 **Latest AI Result**

{_format_record(latest)}

🧠 This result belongs to your most recent
Crop Raksha observation.
"""

    # =================================================
    # PREVIOUS / YESTERDAY
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "yesterday",
                "previous",
                "before",
                "last observation",
                "previous observation",
                "what happened yesterday",
                "what happened before"
            ]
    ):

        if not records:
            return """
📅 There isn't a previous observation yet.

Today's first observation will become
our baseline.
"""

        if len(records) == 1:
            return f"""
📅 **Your Previous Observation**

You currently have only one observation:

{_format_record(latest)}

That means we don't have a second day
to compare against yet.

Tomorrow's observation will give us our
first real day-to-day comparison. 🌱
"""

        return f"""
📅 **Previous Observation**

{_format_record(previous)}

Today's latest observation is:

{_format_record(latest)}

🧠 Crop Raksha uses these observations
to understand how your crop is changing
over time.
"""

    # =================================================
    # HISTORY / MEMORY
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "what do you remember",
                "what do you know",
                "remember",
                "memory",
                "history",
                "monitoring history",
                "show history",
                "tell me everything"
            ]
    ):

        if not records:
            return """
🧠 **Crop Raksha Memory**

I don't have any observations stored yet.

Once you upload your first photograph,
I'll begin remembering your crop's
monitoring history.
"""

        first = sorted(
            records,
            key=lambda x: x.get("day", 0)
        )[0]

        latest = _get_latest(records)

        return f"""
🧠 **What I remember about your crop**

🌱 Crop: **{crop_name}**

📊 Total observations: **{len(records)}**

📅 First observation: **Day {first.get('day', '?')}**
📅 Latest observation: **Day {latest.get('day', '?')}**

🦠 Latest AI result:
**{latest.get('disease', 'Unknown')}**

🎯 Latest confidence:
**{latest.get('confidence', 0):.1f}%**

🔍 Latest visual status:
**{latest.get('status', 'unknown')}**

I'm building this timeline so we can look
at your crop as a changing system rather
than as one isolated photograph.
"""

    # =================================================
    # OBSERVATION COUNT
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "how many observations",
                "how many records",
                "how many days have we monitored",
                "how many days monitored",
                "how many checks",
                "number of observations",
                "observations count"
            ]
    ):
        return f"""
📊 **Crop Raksha Monitoring**

I've currently recorded
**{len(records)} observation(s)**

for your **{crop_name}** crop.

Each observation gives us another point
in the crop's health timeline. 🌱
"""

    # =================================================
    # CHANGE DETECTION
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "has my crop changed",
                "did my crop change",
                "any change",
                "what changed",
                "change from yesterday",
                "visual change",
                "did you notice anything",
                "is there a change",
                "compare",
                "comparison"
            ]
    ):

        if not latest:
            return """
🔍 We don't have enough observations to
detect a change yet.

Upload your first photograph.

After the next observation, I'll be able
to compare the images.
"""

        status = latest.get(
            "status",
            "unknown"
        )

        if status == "baseline":
            return """
🌱 This is our baseline observation.

We need another photograph before Crop Raksha
can compare changes over time.
"""

        if status == "normal":
            return """
🟢 **No significant visual change was detected
in the latest comparison.**

The crop looks visually consistent with
the previous observation.

We'll continue checking it daily. 🌱
"""

        if status == "minor_change":
            return """
🟠 **A minor visual change was detected.**

That does not automatically mean disease.

We'll keep monitoring the crop to see whether
the change continues or disappears.
"""

        if status == "significant_change":
            return """
🔴 **A significant visual change was detected.**

This doesn't automatically mean disease,
but it deserves closer attention.

🩺 Consider using Crop Diagnosis with the
latest photograph for a dedicated AI check.
"""

        return """
🔍 I have an observation saved, but the
visual comparison result isn't available.
"""

    # =================================================
    # TODAY
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "what should i do today",
                "what should we do today",
                "today's task",
                "todays task",
                "what do i do today",
                "what now",
                "what next",
                "next step",
                "daily task"
            ]
    ):

        if not records:
            return """
📸 **Today's Crop Raksha task**

Take a clear photograph of your crop.

Try to make sure:

☀️ There is enough light  
📷 The plant is clearly visible  
🔍 The important leaf/area is not blurry  
📐 Try to use a similar angle each day

Then upload it as today's observation.
"""

        return """
📸 **Today's Crop Raksha task**

Take a clear photograph of your crop.

For better day-to-day comparison, try to
capture a similar area from a similar
distance and angle.

Then upload today's photograph.

I'll analyze it and compare it with the
previous observation. 🌱
"""

    # =================================================
    # PHOTO / IMAGE QUESTIONS
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "why photo",
                "why photograph",
                "why picture",
                "why image",
                "why upload",
                "why do i need a photo",
                "why do i need to upload",
                "photo important",
                "photograph important"
            ]
    ):
        return """
📸 **Why do we need daily photographs?**

A single photograph tells us what the AI
sees at one moment.

But Crop Raksha is designed to answer a
different question:

**"What changed over time?"**

By recording:

Day 1 → Day 2 → Day 3 → Day 4 → ...

we can compare observations and look for
visual changes.

That's why consistent photographs are useful. 🌱
"""

    # =================================================
    # PHOTO QUALITY
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "blurry",
                "bad photo",
                "poor photo",
                "clear photo",
                "better photo",
                "how to take photo",
                "how should i take",
                "photograph"
            ]
    ):
        return """
📸 **For a better Crop Raksha photograph:**

☀️ Use good natural lighting.

🔍 Keep the important part of the plant
clearly visible.

📷 Avoid excessive blur.

📐 Try to photograph a similar area each day.

↔️ Keep a similar distance when possible.

These things make both AI analysis and
day-to-day comparison more useful.
"""

    # =================================================
    # CONFIDENCE
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "confidence",
                "how sure",
                "how certain",
                "is the ai sure",
                "can i trust the ai"
            ]
    ):

        if not latest:
            return """
🎯 We don't have an AI confidence value yet.

Upload your first crop photograph and
I'll show you the model's confidence.
"""

        disease = latest.get(
            "disease",
            "Unknown"
        )

        confidence = latest.get(
            "confidence",
            0
        )

        if confidence < 60:

            level = (
                "relatively low, so the result "
                "should be treated cautiously"
            )

        elif confidence < 80:

            level = (
                "moderate, so the result should "
                "still be interpreted carefully"
            )

        else:

            level = (
                "high according to the model"
            )

        return f"""
🎯 **Latest AI confidence**

Result: **{disease}**

Confidence: **{confidence:.1f}%**

The model's confidence is **{level}**.

Remember that confidence is not the same
thing as guaranteed correctness.

If the image is unclear or the result seems
unexpected, take another clear photograph
and use Crop Diagnosis for further checking.
"""

    # =================================================
    # HEALTHY
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "healthy",
                "good condition",
                "looks good",
                "is it healthy"
            ]
    ):

        if not latest:
            return """
🌱 We haven't analyzed your crop yet.

Upload a photograph and I'll check the
AI result.
"""

        disease = latest.get(
            "disease",
            "Unknown"
        )

        confidence = latest.get(
            "confidence",
            0
        )

        if disease.lower() == "healthy":
            return f"""
🟢 **The latest AI result is Healthy.**

Confidence: **{confidence:.1f}%**

That's encouraging. 🌱

Still, Crop Raksha will continue monitoring
because crop health can change over time.
"""

        return f"""
🦠 The latest AI result is **{disease}**
with **{confidence:.1f}% confidence**.

So the latest observation is not currently
classified as Healthy.

For a deeper assessment, use the
**Crop Diagnosis** section.
"""

    # =================================================
    # DISEASE / PROBLEM
    # =================================================

    if any(
            word in message
            for word in [
                "disease",
                "problem",
                "issue",
                "infection",
                "sick",
                "bad",
                "yellow",
                "spots",
                "spot",
                "wilting",
                "wilt",
                "dry",
                "damage"
            ]
    ):

        if not latest:
            return """
🌱 I understand you're concerned.

We don't have an observation yet, so
let's start with a clear photograph.

📸 Upload the crop image and I'll help
you investigate what the AI sees.
"""

        disease = latest.get(
            "disease",
            "Unknown"
        )

        confidence = latest.get(
            "confidence",
            0
        )

        status = latest.get(
            "status",
            "unknown"
        )

        return f"""
🩺 **Let's investigate carefully.**

Your latest observation says:

🦠 AI result: **{disease}**
🎯 Confidence: **{confidence:.1f}%**
🔍 Visual status: **{status}**

An AI prediction is not automatically a
confirmed diagnosis.

If the crop looks unusual, use the
**Crop Diagnosis** section with a clear
photograph for a more focused assessment.

🌱 Crop Raksha will also continue tracking
what happens in later observations.
"""

    # =================================================
    # WHAT TO DO WITH DISEASE
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "what should i do if",
                "what do i do if",
                "what should i do about",
                "how do i treat",
                "how can i treat",
                "treatment",
                "management"
            ]
    ):
        return """
🩺 **First, confirm what you're seeing.**

Crop Raksha can detect changes and provide
an AI prediction, but treatment depends on
the actual crop problem.

The safest next step is:

1️⃣ Check the latest AI result.
2️⃣ Look at the crop symptoms carefully.
3️⃣ Use **Crop Diagnosis** with a clear image.
4️⃣ Check the disease's management and
   prevention information in the app.
5️⃣ Continue monitoring the crop.

Don't assume that every visual change is
caused by disease. 🌱
"""

    # =================================================
    # CROP AGE
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "crop age",
                "how old",
                "how many days old",
                "age of my crop",
                "when did i sow",
                "sowing date"
            ]
    ):

        sowing_date = crop.get(
            "sowing_date"
        )

        if sowing_date:

            try:

                if isinstance(
                        sowing_date,
                        str
                ):

                    sowing_date_obj = (
                        datetime.strptime(
                            sowing_date,
                            "%Y-%m-%d"
                        ).date()
                    )

                else:

                    sowing_date_obj = (
                        sowing_date
                    )

                today = datetime.now().date()

                age = (
                        today - sowing_date_obj
                ).days

                return f"""
🌿 **Crop Age**

Crop: **{crop_name}**

📅 Sowing date: **{sowing_date_obj}**
🌱 Current age: approximately **{age} days**

Crop Raksha can use this timeline together
with your daily observations.
"""

            except Exception:
                pass

        return f"""
🌿 Your registered crop is **{crop_name}**.

I don't have enough information here to
calculate the crop age.
"""

    # =================================================
    # MONITORING / DAILY CHECK
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "monitoring",
                "monitor",
                "daily check",
                "daily monitoring",
                "how does crop raksha work",
                "what is crop raksha"
            ]
    ):
        return """
🛡️ **How Crop Raksha works**

Crop Raksha is designed around repeated
observations:

📸 You photograph the crop.

🤖 AI analyzes the image.

🧠 The observation is saved.

🔍 The new image is compared with the
previous observation.

📊 The result becomes part of your timeline.

🔄 Tomorrow, we repeat the process.

The goal is to understand **change over time**
rather than relying on one photograph.
"""

    # =================================================
    # TIMELINE
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "timeline",
                "days",
                "day 1",
                "day 2",
                "day 3",
                "progress",
                "progression"
            ]
    ):

        if not records:
            return """
📅 Your Crop Raksha timeline hasn't started yet.

Upload the first photograph to create
Day 1. 🌱
"""

        ordered = sorted(
            records,
            key=lambda x: x.get("day", 0)
        )

        first = ordered[0]
        latest = ordered[-1]

        return f"""
📅 **Crop Raksha Timeline**

🌱 First observation:
**Day {first.get('day', '?')}**
{first.get('date', '')}

📊 Total observations:
**{len(records)}**

🌱 Latest observation:
**Day {latest.get('day', '?')}**
{latest.get('date', '')}

🦠 Latest AI result:
**{latest.get('disease', 'Unknown')}**

We're gradually building a picture of
how your crop changes over time.
"""

    # =================================================
    # START / FIRST OBSERVATION
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "start",
                "first observation",
                "begin",
                "baseline"
            ]
    ):

        if records:
            return f"""
🌱 Your Crop Raksha journey has already started.

You currently have **{len(records)} observation(s)**.

Your first observation is saved as the
starting point of the monitoring timeline.
"""

        return """
🌱 **Let's start Crop Raksha!**

Your first photograph will become the
baseline observation.

📸 Upload a clear crop photograph and
we'll begin your monitoring timeline.
"""

    # =================================================
    # CHANGE + DISEASE COMBINATION
    # =================================================

    if (
            "change" in message
            and (
            "disease" in message
            or "problem" in message
            or "bad" in message
    )
    ):

        if not latest:
            return """
We don't have enough observations yet.

Let's record the first photograph before
trying to understand changes.
"""

        status = latest.get(
            "status",
            "unknown"
        )

        disease = latest.get(
            "disease",
            "Unknown"
        )

        confidence = latest.get(
            "confidence",
            0
        )

        return f"""
🔍 **Change + AI assessment**

Visual status:
**{status}**

AI result:
**{disease}**

AI confidence:
**{confidence:.1f}%**

Remember:

**Visual change ≠ automatic disease.**

Crop Raksha uses visual comparison to notice
changes, while the AI model separately predicts
a disease/healthy class.

We should consider both signals together
rather than treating either one as perfect.
"""

    # =================================================
    # THANKS / GOOD
    # =================================================

    if any(
            phrase in message
            for phrase in [
                "good",
                "fine",
                "okay",
                "ok",
                "great"
            ]
    ):
        return f"""
👍 That's good to hear, {farmer_name}!

Even when the crop looks fine, the daily
photograph is useful.

Consistent observations help Crop Raksha
understand what is normal for your
**{crop_name}**. 🌱
"""

    # =================================================
    # DEFAULT RESPONSE
    # =================================================

    return f"""
🤖 I'm listening, {farmer_name}. 🌱

You're talking about your **{crop_name}**.

I can currently help you with:

🌱 Crop health  
🧠 Monitoring memory  
📅 Previous observations  
🔄 Visual changes  
🦠 AI disease results  
🎯 AI confidence  
📸 Daily photographs  
🌿 Crop age  
🩺 What to do next

Try asking:

**"How is my crop?"**

or

**"What changed?"**

or

**"What do you remember?"**
"""


# =====================================================
# STATUS ADVICE
# =====================================================

def self_status_advice(
        status,
        disease,
        confidence
):
    """
    Return a short explanation of the current
    Crop Raksha status.
    """

    if disease.lower() == "healthy":

        if status == "significant_change":
            return """
⚠️ The AI currently says **Healthy**, but
the image comparison noticed a significant
visual change.

That means we should continue watching the
crop rather than assuming everything is perfect.
"""

        if status == "minor_change":
            return """
🟠 The AI currently says **Healthy**, and only
a minor visual change was detected.

Continue daily monitoring.
"""

        return """
🟢 The AI currently says **Healthy**, and
there is no major visual warning.
"""

    if confidence < 60:
        return """
⚠️ The AI detected a possible issue, but its
confidence is relatively low.

A clearer image and further observation
would be useful.
"""

    if status == "significant_change":
        return """
🔴 Both the AI result and visual comparison
deserve attention.

Use Crop Diagnosis for a closer assessment.
"""

    if status == "minor_change":
        return """
🟠 The AI detected a possible issue and a
minor visual change was also noticed.

Continue monitoring and consider a dedicated
diagnosis.
"""

    return """
🟠 The AI detected a possible issue.

Consider using Crop Diagnosis for a more
focused assessment.
"""


# =====================================================
# CHAT UI
# =====================================================

def render_crop_raksha_chat(
        crop,
        records
):
    """
    Display the interactive Crop Raksha
    conversational companion.
    """

    # -------------------------------------------------
    # SESSION STATE
    # -------------------------------------------------

    if (
            "raksha_messages"
            not in st.session_state
    ):
        st.session_state.raksha_messages = []

    # -------------------------------------------------
    # RESET WHEN CROP CHANGES
    # -------------------------------------------------

    current_crop_id = crop.get(
        "id"
    )

    if (
            "raksha_crop_id"
            not in st.session_state
            or
            st.session_state.raksha_crop_id
            != current_crop_id
    ):
        st.session_state.raksha_messages = []

        st.session_state.raksha_crop_id = (
            current_crop_id
        )

    # -------------------------------------------------
    # FIRST MESSAGE
    # -------------------------------------------------

    if not st.session_state.raksha_messages:
        opening_message = (
            get_crop_raksha_message(
                crop,
                records
            )
        )

        st.session_state.raksha_messages.append(
            {
                "role": "assistant",
                "content": opening_message
            }
        )

    # -------------------------------------------------
    # DISPLAY CHAT
    # -------------------------------------------------

    for message in (
            st.session_state.raksha_messages
    ):
        with st.chat_message(
                message["role"]
        ):
            st.markdown(
                message["content"]
            )

    # -------------------------------------------------
    # CHAT INPUT
    # -------------------------------------------------

    user_message = st.chat_input(
        "💬 Talk to Crop Raksha..."
    )

    if user_message:
        # ---------------------------------------------
        # SAVE USER MESSAGE
        # ---------------------------------------------

        st.session_state.raksha_messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        # ---------------------------------------------
        # GENERATE RESPONSE
        # ---------------------------------------------

        response = chatbot_response(
            user_message,
            crop,
            records
        )

        # ---------------------------------------------
        # SAVE AI RESPONSE
        # ---------------------------------------------

        st.session_state.raksha_messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        st.rerun()