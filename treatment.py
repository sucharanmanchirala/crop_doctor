# =====================================================
# CROP DOCTOR — TREATMENT RECOMMENDATION SYSTEM
# =====================================================

import json
import os

TREATMENTS_FILE = "disease_treatments.json"
_treatments_cache = None


def load_treatments():
    """
    Load treatment data from disease_treatments.json.
    Results are cached for performance.
    """
    global _treatments_cache

    if _treatments_cache is not None:
        return _treatments_cache

    if not os.path.exists(TREATMENTS_FILE):
        _treatments_cache = {}
        return _treatments_cache

    try:
        with open(TREATMENTS_FILE, "r", encoding="utf-8") as f:
            _treatments_cache = json.load(f)
        return _treatments_cache
    except Exception:
        _treatments_cache = {}
        return _treatments_cache


def get_treatment(class_id):
    """
    Perform an EXACT lookup for the given class ID.

    Args:
        class_id: The model's predicted class ID
                  (e.g. "tomato_early_blight", "banana_healthy")

    Returns:
        A dictionary with treatment data if found:
            {
                "fertilizer": "...",
                "fertilizer_quantity": "...",
                "pesticide": "...",
                "pesticide_quantity": "...",
                "description": "..."
            }
        OR None if the class_id is not found.
    """
    treatments = load_treatments()
    return treatments.get(class_id)
