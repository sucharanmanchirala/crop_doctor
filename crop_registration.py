import json
import os
import uuid
from datetime import datetime, date

CROPS_FILE = "crops.json"


def load_crops():
    """Return the list of all registered crop profiles."""

    if not os.path.exists(CROPS_FILE):
        return []

    try:
        with open(CROPS_FILE, "r") as f:
            return json.load(f)

    except Exception:
        return []


def save_crops(crops):
    with open(CROPS_FILE, "w") as f:
        json.dump(crops, f, indent=4)


def add_crop(
    farmer_name,
    crop_name,
    sowing_date,
    field_label="",
    monitoring_time="18:00"
):
    """
    Register a new crop profile.

    monitoring_time:
    Daily time chosen by the farmer for Crop Raksha monitoring.
    """

    crops = load_crops()

    new_crop = {
        "id": uuid.uuid4().hex[:8],

        "farmer_name": farmer_name.strip(),

        "crop_name": crop_name,

        "field_label": field_label.strip(),

        "sowing_date": sowing_date.strftime("%Y-%m-%d"),

        "monitoring_time": monitoring_time,

        "registered_on": datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        ),

        "status": "active"
    }

    crops.append(new_crop)

    save_crops(crops)

    return new_crop["id"]


def get_crop(crop_id):

    for crop in load_crops():

        if crop["id"] == crop_id:
            return crop

    return None


def delete_crop(crop_id):

    crops = load_crops()

    crops = [
        crop
        for crop in crops
        if crop["id"] != crop_id
    ]

    save_crops(crops)


def days_since_sowing(sowing_date_str):

    sowing = datetime.strptime(
        sowing_date_str,
        "%Y-%m-%d"
    ).date()

    return (date.today() - sowing).days


def display_name(crop):

    if crop.get("field_label"):

        return (
            f"{crop['crop_name']} — "
            f"{crop['field_label']}"
        )

    return crop["crop_name"]