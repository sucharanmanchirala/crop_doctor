import json
import os
from datetime import datetime

RAKSHA_FILE = "crop_raksha_history.json"


# =====================================================
# LOAD / SAVE HISTORY
# =====================================================

def load_raksha_history():
    """Load all Crop Raksha monitoring records."""

    if not os.path.exists(RAKSHA_FILE):
        return []

    try:
        with open(RAKSHA_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []


def save_raksha_history(history):
    """Save Crop Raksha monitoring records."""

    with open(RAKSHA_FILE, "w") as f:
        json.dump(history, f, indent=4)


# =====================================================
# CROP RECORDS
# =====================================================

def get_crop_records(crop_id):
    """Return all monitoring records belonging to one crop."""

    history = load_raksha_history()

    records = [
        record
        for record in history
        if record.get("crop_id") == crop_id
    ]

    return records


# =====================================================
# MONITORING DAY
# =====================================================

def get_next_day(crop_id):
    """Return the next monitoring day for a crop."""
    records = get_crop_records(crop_id)
    if not records:
        return 1

    # Prefer the stored day number. This keeps the sequence stable even
    # when multiple observations are made on the same calendar day.
    day_numbers = []
    for record in records:
        try:
            day_numbers.append(int(record.get("day", 0)))
        except (TypeError, ValueError):
            pass

    if day_numbers:
        return max(day_numbers) + 1

    # Backward compatibility for legacy records without a day field.
    try:
        records = sorted(records, key=lambda x: x.get("date", ""))
        first_date = datetime.strptime(
            records[0]["date"], "%Y-%m-%d %H:%M"
        ).date()
        return (datetime.now().date() - first_date).days + 1
    except (KeyError, TypeError, ValueError):
        return len(records) + 1

def get_latest_record(crop_id):
    """Return the latest monitoring record for a crop."""

    records = get_crop_records(crop_id)

    if not records:
        return None

    records = sorted(
        records,
        key=lambda x: x["date"]
    )

    return records[-1]


# =====================================================
# PREVIOUS RECORD
# =====================================================

def get_previous_record(crop_id):
    """
    Return the observation immediately before
    the latest observation.
    """

    records = get_crop_records(crop_id)

    if len(records) < 2:
        return None

    records = sorted(
        records,
        key=lambda x: x["date"]
    )

    return records[-2]


# =====================================================
# ADD MONITORING RECORD
# =====================================================

def add_monitoring_record(
    crop_id,
    image_path,
    status="pending",
    observation="",
    disease="Unknown",
    confidence=0
):
    """
    Save one Crop Raksha daily observation.

    Each observation remembers:

    - Crop
    - Day
    - Date/time
    - Image
    - Visual change status
    - Observation message
    - AI disease result
    - AI confidence
    """

    history = load_raksha_history()

    day = get_next_day(crop_id)

    record = {
        "id": f"{crop_id}_{day}",

        "crop_id": crop_id,

        "day": day,

        "date": datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        ),

        "image_path": image_path,

        "status": status,

        "observation": observation,

        "disease": disease,

        "confidence": round(
            float(confidence),
            2
        )
    }

    history.append(record)

    save_raksha_history(history)

    return record


# =====================================================
# UPDATE MONITORING RECORD
# =====================================================

def update_monitoring_record(
    record_id,
    status=None,
    observation=None,
    disease=None,
    confidence=None
):
    """Update an existing Crop Raksha observation."""

    history = load_raksha_history()

    for record in history:

        if record.get("id") == record_id:

            if status is not None:
                record["status"] = status

            if observation is not None:
                record["observation"] = observation

            if disease is not None:
                record["disease"] = disease

            if confidence is not None:
                record["confidence"] = round(
                    float(confidence),
                    2
                )

            break

    save_raksha_history(history)


# =====================================================
# DELETE CROP HISTORY
# =====================================================

def delete_crop_history(crop_id):
    """Delete all Crop Raksha records for one crop."""

    history = load_raksha_history()

    history = [
        record
        for record in history
        if record.get("crop_id") != crop_id
    ]

    save_raksha_history(history)


# =====================================================
# CHECK TODAY'S RECORD
# =====================================================

def get_today_record(crop_id):
    """
    Return today's monitoring record if it exists.
    Otherwise return None.
    """

    records = get_crop_records(crop_id)

    today = datetime.now().strftime("%Y-%m-%d")

    for record in records:

        if record.get("date", "").startswith(today):
            return record

    return None


# =====================================================
# GET RECORD BY DAY
# =====================================================

def get_record_by_day(crop_id, day):
    """Return a specific Crop Raksha day record."""

    records = get_crop_records(crop_id)

    for record in records:

        if record.get("day") == day:
            return record

    return None