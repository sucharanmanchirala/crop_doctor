"""
crop_comparison_view.py — Before/After Crop Comparison Viewer

Lets users select any two observations of the same crop and view them
side-by-side with an optional heatmap overlay.
"""

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
from crop_comparison import (
    calculate_image_difference,
    generate_difference_heatmap,
    classify_change,
)
from language import t


def render_comparison_viewer(records, selected_crop_id):
    """
    Render the before/after comparison viewer.

    Args:
        records: List of Crop Raksha observation records (with image_path)
        selected_crop_id: Current crop ID
    """

    if not records or len(records) < 1:
        st.info(t("raksha_compare_no_observations"))
        return

    # Only records with valid image paths
    valid_records = [
        r for r in records
        if r.get("image_path") and os.path.exists(r["image_path"])
    ]

    if not valid_records:
        st.warning(t("raksha_compare_no_images"))
        return

    # Sort by day
    valid_records = sorted(valid_records, key=lambda x: x.get("day", 0))

    st.markdown(t("raksha_compare_explanation"))

    # Build dropdown options
    options = {
        t("raksha_compare_day_option", day=r.get('day', '?'), date=r.get('date', ''), disease=r.get('disease', 'Unknown')): i
        for i, r in enumerate(valid_records)
    }

    # Default: first and last
    default_left = 0
    default_right = len(valid_records) - 1

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"##### {t('before_label')}")
        left_label = st.selectbox(
            t("select_earlier_observation"),
            list(options.keys()),
            index=default_left,
            key=f"compare_left_{selected_crop_id}"
        )
        left_idx = options[left_label]
        left_record = valid_records[left_idx]

    with col2:
        st.markdown(f"##### {t('after_label')}")
        right_label = st.selectbox(
            t("select_later_observation"),
            list(options.keys()),
            index=default_right,
            key=f"compare_right_{selected_crop_id}"
        )
        right_idx = options[right_label]
        right_record = valid_records[right_idx]

    if left_idx == right_idx:
        st.warning(t("raksha_compare_select_different"))
        return

    # Load images
    try:
        left_img = Image.open(left_record["image_path"]).convert("RGB")
        right_img = Image.open(right_record["image_path"]).convert("RGB")
    except Exception as e:
        st.error(t("raksha_compare_load_error", error=e))
        return

    # Side-by-side
    col1, col2 = st.columns(2)

    with col1:
        st.image(
            left_img,
            caption=t("raksha_observation_caption", day=left_record.get('day', '?'), disease=left_record.get('disease', 'Unknown')),
            use_container_width=True
        )
        if left_record.get("confidence"):
            st.caption(t("ai_confidence_label", ) + f" {left_record.get('confidence'):.1f}%")

    with col2:
        st.image(
            right_img,
            caption=t("raksha_observation_caption", day=right_record.get('day', '?'), disease=right_record.get('disease', 'Unknown')),
            use_container_width=True
        )
        if right_record.get("confidence"):
            st.caption(t("ai_confidence_label") + f" {right_record.get('confidence'):.1f}%")

    # Visual difference analysis
    st.divider()
    st.subheader(t("visual_difference_analysis"))

    difference = calculate_image_difference(left_img, right_img)
    if difference is None:
        st.error(t("could_not_compute"))
        return

    change_level = classify_change(difference)

    # Difference metric
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(t("visual_difference_label"), f"{difference:.2f}%")
    with m2:
        if change_level == "normal":
            st.metric(t("status"), t("normal"))
        elif change_level == "minor_change":
            st.metric(t("status"), t("minor_change"))
        elif change_level == "significant_change":
            st.metric(t("status"), t("significant_change"))
        else:
            st.metric(t("status"), change_level)
    with m3:
        days_diff = abs(
            int(right_record.get("day", 0)) - int(left_record.get("day", 0))
        )
        st.metric(t("days_apart"), days_diff)

    # Heatmap toggle
    show_heatmap = st.checkbox(t("show_heatmap"), value=True)

    if show_heatmap:
        heatmap = generate_difference_heatmap(left_img, right_img)
        if heatmap is not None:
            st.image(
                heatmap,
                caption=t("raksha_compare_heatmap_caption"),
                use_container_width=True
            )

    # AI comparison
    st.divider()
    st.subheader(t("ai_comparison"))

    left_disease = left_record.get("disease", "Unknown")
    right_disease = right_record.get("disease", "Unknown")
    left_conf = left_record.get("confidence", 0)
    right_conf = right_record.get("confidence", 0)

    if left_disease.lower() == right_disease.lower():
        st.info(t("ai_verdict_consistent", disease=left_disease))
    else:
        st.warning(
            t("ai_verdict_changed", day1=left_record.get('day', '?'), disease1=left_disease, conf1=f"{left_conf:.1f}", day2=right_record.get('day', '?'), disease2=right_disease, conf2=f"{right_conf:.1f}")
        )
