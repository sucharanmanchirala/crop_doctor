"""
demo.py — SIH Demo Features for Crop Doctor

High-impact features designed to impress SIH judges:
1. SIH Demo Mode with guided walkthrough
2. One-click sample images with AI diagnosis
3. Onboarding / first-time guide
4. AI explanation helpers
5. Diagnosis export
6. Voice feedback
"""

import streamlit as st
import json
import os
import csv
import io
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import random

from language import t, translate_crop_name

# =====================================================
# PATHS
# =====================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEMO_IMAGES_DIR = os.path.join(BASE_DIR, "demo_images")
DEMO_DIAGNOSIS_DIR = os.path.join(BASE_DIR, "demo_images", "diagnosis")
HISTORY_FILE = os.path.join(BASE_DIR, "monitoring_history.json")
RAKSHA_FILE = os.path.join(BASE_DIR, "crop_raksha_history.json")
CROPS_FILE = os.path.join(BASE_DIR, "crops.json")

os.makedirs(DEMO_IMAGES_DIR, exist_ok=True)

# Map crop names to diagnosis directory names
CROP_TO_DIAGNOSIS_DIR = {
    "banana": "banana",
    "corn": "corn",
    "cotton": "cotton",
    "grape": "grape",
    "mango": "mango",
    "paddy": "paddy",
    "potato": "potato",
    "soybean": "soya been",  # directory name
    "tomato": "tomato",
    "wheat": "wheat",
}


# =====================================================
# SAMPLE IMAGES (generated programmatically)
# We create distinctive synthetic leaf images so judges
# can click-to-diagnose without uploading files.
# =====================================================

SAMPLE_IMAGES = [
    {
        "id": "sample_tomato_healthy",
        "crop": "Tomato",
        "class": "tomato_healthy",
        "disease": "Healthy",
        "label": "🍅 Tomato — Healthy",
        "description": "A healthy tomato leaf with vibrant green color.",
        "color": (60, 140, 50),
        "spots": [],
    },
    {
        "id": "sample_tomato_late_blight",
        "crop": "Tomato",
        "class": "tomato_late_blight",
        "disease": "Late Blight",
        "label": "🍅 Tomato — Late Blight",
        "description": "Tomato leaf showing Late Blight symptoms: dark irregular lesions.",
        "color": (60, 140, 50),
        "spots": [(80, 60, 100, 80), (140, 100, 170, 120), (50, 120, 90, 150)],
    },
    {
        "id": "sample_tomato_early_blight",
        "crop": "Tomato",
        "class": "tomato_early_blight",
        "disease": "Early Blight",
        "label": "🍅 Tomato — Early Blight",
        "description": "Tomato leaf with Early Blight concentric ring patterns.",
        "color": (60, 140, 50),
        "spots": [(60, 50, 120, 100), (130, 80, 180, 140)],
    },
    {
        "id": "sample_paddy_healthy",
        "crop": "Paddy",
        "class": "paddy_healthy",
        "disease": "Healthy",
        "label": "🌾 Paddy — Healthy",
        "description": "A healthy paddy/rice leaf with bright green color.",
        "color": (70, 150, 45),
        "spots": [],
    },
    {
        "id": "sample_paddy_bacterial_blight",
        "crop": "Paddy",
        "class": "paddy_bacterial_leaf_blight",
        "disease": "Bacterial Leaf Blight",
        "label": "🌾 Paddy — Bacterial Leaf Blight",
        "description": "Paddy leaf with Bacterial Leaf Blight: water-soaked lesions near margins.",
        "color": (140, 160, 40),
        "spots": [(20, 40, 200, 60), (20, 80, 200, 100)],
    },
    {
        "id": "sample_paddy_brown_spot",
        "crop": "Paddy",
        "class": "paddy_brown_spot",
        "disease": "Brown Spot",
        "label": "🌾 Paddy — Brown Spot",
        "description": "Paddy leaf showing Brown Spot: circular brown lesions.",
        "color": (100, 140, 40),
        "spots": [(40, 30, 80, 70), (120, 50, 170, 90), (60, 110, 110, 150)],
    },
    {
        "id": "sample_cotton_healthy",
        "crop": "Cotton",
        "class": "cotton_healthy",
        "disease": "Healthy",
        "label": "🌿 Cotton — Healthy",
        "description": "A healthy cotton leaf with normal green color.",
        "color": (55, 120, 45),
        "spots": [],
    },
    {
        "id": "sample_cotton_leaf_curl",
        "crop": "Cotton",
        "class": "cotton_cotton_leaf_curl",
        "disease": "Cotton Leaf Curl",
        "label": "🌿 Cotton — Leaf Curl Disease",
        "description": "Cotton leaf showing Leaf Curl Disease: upward curling and thickening.",
        "color": (100, 130, 50),
        "spots": [],
    },
    {
        "id": "sample_potato_healthy",
        "crop": "Potato",
        "class": "potato_healthy",
        "disease": "Healthy",
        "label": "🥔 Potato — Healthy",
        "description": "A healthy potato leaf with good green color.",
        "color": (65, 130, 48),
        "spots": [],
    },
    {
        "id": "sample_potato_late_blight",
        "crop": "Potato",
        "class": "potato_late_blight",
        "disease": "Late Blight",
        "label": "🥔 Potato — Late Blight",
        "description": "Potato leaf showing Late Blight: dark irregular lesions that spread rapidly.",
        "color": (80, 130, 50),
        "spots": [(50, 40, 150, 100), (100, 90, 200, 160), (30, 130, 120, 190)],
    },
    {
        "id": "sample_wheat_healthy",
        "crop": "Wheat",
        "class": "wheat_healthy",
        "disease": "Healthy",
        "label": "🌾 Wheat — Healthy",
        "description": "A healthy wheat leaf with bright green color.",
        "color": (72, 145, 48),
        "spots": [],
    },
    {
        "id": "sample_wheat_yellowrust",
        "crop": "Wheat",
        "class": "wheat_yellowrust",
        "disease": "Yellow Rust",
        "label": "🌾 Wheat — Yellow Rust",
        "description": "Wheat leaf showing Yellow Rust: yellow-orange pustules in stripe patterns.",
        "color": (120, 150, 40),
        "spots": [(20, 20, 200, 50), (20, 70, 200, 100), (20, 120, 200, 150)],
    },
    {
        "id": "sample_banana_healthy",
        "crop": "Banana",
        "class": "banana_healthy",
        "disease": "Healthy",
        "label": "🍌 Banana — Healthy",
        "description": "A healthy banana leaf with large green leaf surface.",
        "color": (50, 130, 45),
        "spots": [],
    },
    {
        "id": "sample_banana_sigatoka",
        "crop": "Banana",
        "class": "banana_sigatoka",
        "disease": "Sigatoka Leaf Spot",
        "label": "🍌 Banana — Sigatoka Leaf Spot",
        "description": "Banana leaf with Sigatoka Leaf Spot: streaks and dark spots.",
        "color": (90, 130, 50),
        "spots": [(30, 30, 120, 80), (100, 60, 190, 120), (40, 100, 150, 160)],
    },
    {
        "id": "sample_grape_healthy",
        "crop": "Grape",
        "class": "grape_healthy",
        "disease": "Healthy",
        "label": "🍇 Grape — Healthy",
        "description": "A healthy grape leaf with normal green color.",
        "color": (58, 125, 42),
        "spots": [],
    },
    {
        "id": "sample_grape_black_rot",
        "crop": "Grape",
        "class": "grape_black_rot",
        "disease": "Black Rot",
        "label": "🍇 Grape — Black Rot",
        "description": "Grape leaf with Black Rot: brown/reddish spots with dark margins.",
        "color": (100, 125, 45),
        "spots": [(50, 50, 110, 100), (120, 70, 180, 130), (60, 110, 130, 160)],
    },
    {
        "id": "sample_corn_healthy",
        "crop": "Corn",
        "class": "corn_healthy",
        "disease": "Healthy",
        "label": "🌽 Corn — Healthy",
        "description": "A healthy corn/maze leaf with bright green color.",
        "color": (68, 138, 46),
        "spots": [],
    },
    {
        "id": "sample_corn_common_rust",
        "crop": "Corn",
        "class": "corn_common_rust",
        "disease": "Common Rust",
        "label": "🌽 Corn — Common Rust",
        "description": "Corn leaf showing Common Rust: rust-colored pustules on both sides.",
        "color": (100, 135, 45),
        "spots": [(40, 20, 100, 70), (120, 30, 190, 90), (50, 90, 140, 150)],
    },
    {
        "id": "sample_soybean_healthy",
        "crop": "Soybean",
        "class": "soybean_healthy",
        "disease": "Healthy",
        "label": "🫘 Soybean — Healthy",
        "description": "A healthy soybean leaf with normal green color.",
        "color": (62, 128, 44),
        "spots": [],
    },
    {
        "id": "sample_soybean_caterpillar",
        "crop": "Soybean",
        "class": "soybean_caterpillar",
        "disease": "Caterpillar Damage",
        "label": "🫘 Soybean — Caterpillar Damage",
        "description": "Soybean leaf showing caterpillar feeding damage: irregular holes.",
        "color": (60, 125, 42),
        "spots": [],
    },
    {
        "id": "sample_mango_healthy",
        "crop": "Mango",
        "class": "mango_healthy",
        "disease": "Healthy",
        "label": "🥭 Mango — Healthy",
        "description": "A healthy mango leaf with dark green color.",
        "color": (48, 118, 40),
        "spots": [],
    },
    {
        "id": "sample_mango_anthracnose",
        "crop": "Mango",
        "class": "mango_anthracnose",
        "disease": "Anthracnose",
        "label": "🥭 Mango — Anthracnose",
        "description": "Mango leaf with Anthracnose: dark sunken spots on leaves and shoots.",
        "color": (85, 118, 42),
        "spots": [(40, 40, 110, 90), (110, 60, 190, 120), (50, 110, 130, 160)],
    },
]


def _draw_leaf_base(draw, size, color, leaf_id):
    """Draw a realistic-looking leaf shape."""
    w, h = size
    # Leaf outline (ellipse rotated slightly)
    cx, cy = w // 2, h // 2

    # Main leaf body
    draw.ellipse([cx - 85, cy - 110, cx + 85, cy + 110],
                 fill=color, outline=(20, 80, 20))

    # Central vein
    draw.line([cx, cy - 100, cx, cy + 100], fill=(30, 90, 30), width=3)

    # Side veins
    for i in range(-4, 5):
        y = cy + i * 22
        if abs(i) < 4:
            draw.line([cx, y, cx - 60, y - 15], fill=(35, 95, 35), width=1)
            draw.line([cx, y, cx + 60, y - 15], fill=(35, 95, 35), width=1)


def _add_spots(draw, spots, size, disease):
    """Add disease spots to the leaf image."""
    w, h = size
    cx, cy = w // 2, h // 2

    if disease == "cotton_cotton_leaf_curl":
        # Curling effect - use wavy edges
        draw.ellipse([cx - 75, cy - 100, cx + 75, cy + 100],
                     fill=(100, 130, 50), outline=(20, 80, 20))
        return

    for (x1, y1, x2, y2) in spots:
        if disease in ["paddy_bacterial_leaf_blight"]:
            # Yellow/white water-soaked streaks along margin
            draw.rectangle([x1, y1, x2, y2],
                          fill=(200, 200, 100), outline=(160, 160, 60))
        elif disease in ["corn_common_rust", "wheat_yellowrust"]:
            # Rust pustules - orange/yellow raised spots
            draw.ellipse([x1, y1, x2, y2],
                        fill=(210, 140, 20), outline=(180, 100, 0))
        elif disease in ["soybean_caterpillar"]:
            # Irregular holes
            draw.ellipse([x1, y1, x2, y2],
                        fill=(200, 240, 200), outline=(50, 50, 20))
        else:
            # Brown/dark necrotic spots
            draw.ellipse([x1, y1, x2, y2],
                        fill=(100, 45, 15), outline=(60, 20, 5))


def generate_sample_image(sample_info, seed=None):
    """
    Generate a programmatically created leaf image.
    Uses a deterministic seed so the same sample always looks the same.
    """
    if seed is None:
        seed = hash(sample_info["id"]) % 1000000
    random.seed(seed)
    np.random.seed(seed)

    size = (224, 224)
    color = sample_info["color"]
    disease = sample_info["class"]
    spots = sample_info["spots"]

    # Base leaf color with slight texture variation
    base = Image.new("RGB", size)
    draw = ImageDraw.Draw(base)

    # Fill with leaf color
    base.paste(color, (0, 0, size[0], size[1]))

    # Add texture noise
    arr = np.array(base)
    noise = np.random.randint(-15, 15, arr.shape, dtype=np.int16)
    arr = np.clip(arr.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    base = Image.fromarray(arr)
    draw = ImageDraw.Draw(base)

    # Draw leaf shape
    _draw_leaf_base(draw, size, color, sample_info["id"])

    # Add disease spots
    if spots:
        _add_spots(draw, spots, size, disease)

    # Add slight blur for realism
    base = base.filter(ImageFilter.GaussianBlur(radius=0.5))

    return base


def ensure_sample_images():
    """Generate and cache all sample images."""
    for sample in SAMPLE_IMAGES:
        img_path = os.path.join(DEMO_IMAGES_DIR, f"{sample['id']}.jpg")
        if not os.path.exists(img_path):
            img = generate_sample_image(sample)
            img.save(img_path, "JPEG", quality=92)
        sample["image_path"] = img_path
    return SAMPLE_IMAGES


# =====================================================
# SIH DEMO MODE
# =====================================================

DEMO_STEPS = [
    {
        "page": "Dashboard",
        "title_key": "demo_step1_title",
        "desc_key": "demo_step1_desc",
        "highlight": "dashboard",
    },
    {
        "page": "Crop Registration",
        "title_key": "demo_step2_title",
        "desc_key": "demo_step2_desc",
        "highlight": "crop_registration",
    },
    {
        "page": "Diagnose",
        "title_key": "demo_step3_title",
        "desc_key": "demo_step3_desc",
        "highlight": "diagnose",
    },
    {
        "page": "Crop Raksha",
        "title_key": "demo_step4_title",
        "desc_key": "demo_step4_desc",
        "highlight": "crop_raksha",
    },
    {
        "page": "Anjaneya Voice",
        "title_key": "demo_step5_title",
        "desc_key": "demo_step5_desc",
        "highlight": "voice",
    },
    {
        "page": "Disease Library",
        "title_key": "demo_step6_title",
        "desc_key": "demo_step6_desc",
        "highlight": "disease_library",
    },
    {
        "page": "Monitoring",
        "title_key": "demo_step7_title",
        "desc_key": "demo_step7_desc",
        "highlight": "monitoring",
    },
]


def render_sih_demo_banner():
    """Render the SIH Demo Mode banner in the sidebar."""

    st.sidebar.markdown("---")

    # Demo mode indicator
    st.sidebar.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #1a3a2a, #2d5a3f);
        border: 2px solid #ffd700;
        border-radius: 12px;
        padding: 14px 16px;
        margin: 8px 0;
        text-align: center;
        box-shadow: 0 4px 15px rgba(255,215,0,0.15);
    ">
        <div style="font-size: 18px; margin-bottom: 4px;">{t('sih_demo_mode')}</div>
        <div style="font-size: 11px; color: #aaffcc; opacity: 0.85;">
            {t('sih_click_start_tour')}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Initialize session state
    if "demo_mode" not in st.session_state:
        st.session_state.demo_mode = False
    if "demo_step" not in st.session_state:
        st.session_state.demo_step = 0

    if not st.session_state.demo_mode:
        if st.sidebar.button(
            t("start_guided_tour"),
            use_container_width=True,
            type="primary"
        ):
            st.session_state.demo_mode = True
            st.session_state.demo_step = 0
            st.rerun()
    else:
        # Show current step info
        step = DEMO_STEPS[st.session_state.demo_step]
        step_title = t(step['title_key'])
        step_desc = t(step['desc_key'])

        st.sidebar.markdown(f"""
        <div style="
            background: #1e3a2e;
            border: 1px solid #2d5a3f;
            border-radius: 8px;
            padding: 10px 12px;
            margin: 4px 0;
        ">
            <div style="color: #ffd700; font-size: 11px; margin-bottom: 4px;">
                {t('sih_step_indicator', current=st.session_state.demo_step + 1, total=len(DEMO_STEPS))}
            </div>
            <div style="color: #80ffb0; font-size: 13px; font-weight: bold;">
                {step_title}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.sidebar.caption(step_desc)

        col1, col2 = st.sidebar.columns(2)
        with col1:
            if st.button(t("demo_prev"), use_container_width=True, key="demo_prev"):
                st.session_state.demo_step = max(0, st.session_state.demo_step - 1)
                st.rerun()
        with col2:
            if st.button(t("demo_next"), use_container_width=True, key="demo_next"):
                if st.session_state.demo_step < len(DEMO_STEPS) - 1:
                    st.session_state.demo_step += 1
                    st.rerun()
                else:
                    st.session_state.demo_mode = False
                    st.rerun()

        if st.button(t("demo_exit"), use_container_width=True, key="demo_exit"):
            st.session_state.demo_mode = False
            st.rerun()

        # Return current step info for main.py to use
        return step

    return None


def get_current_demo_step():
    """Return the current demo step info."""
    if st.session_state.get("demo_mode") and st.session_state.get("demo_step", 0) < len(DEMO_STEPS):
        return DEMO_STEPS[st.session_state.demo_step]
    return None


# =====================================================
# ONBOARDING GUIDE
# =====================================================

def render_onboarding():
    """Show first-time onboarding tips if user hasn't dismissed it."""

    if "onboarding_dismissed" not in st.session_state:
        st.session_state.onboarding_dismissed = False

    if st.session_state.onboarding_dismissed:
        return

    with st.sidebar.expander(t("getting_started"), expanded=False):
        st.markdown(f"""
        **{t('welcome_crop_doctor')}**

        {t('how_to_get_started')}

        **{t('step1_register_crop')}**
        {t('step1_register_desc')}

        **{t('step2_daily_monitoring')}**
        {t('step2_monitoring_desc')}

        **{t('step3_ai_diagnosis')}**
        {t('step3_diagnosis_desc')}

        **{t('step4_voice_assistant')}**
        {t('step4_voice_desc')}

        **{t('step5_sample_images')}**
        {t('step5_sample_desc')}

        ---
        {t('works_offline')}
        """)

        if st.button(t("got_it_hide")):
            st.session_state.onboarding_dismissed = True
            st.rerun()


# =====================================================
# SAMPLE IMAGES GALLERY (Real photographs)
# =====================================================

def get_real_sample_images():
    """Get list of real sample images from demo_images/diagnosis/ directories."""
    samples = []
    image_extensions = {'.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG'}

    for crop_name, dir_name in CROP_TO_DIAGNOSIS_DIR.items():
        crop_dir = os.path.join(DEMO_DIAGNOSIS_DIR, dir_name)
        if os.path.isdir(crop_dir):
            files = os.listdir(crop_dir)
            # Filter for image files
            image_files = [f for f in files if any(f.lower().endswith(ext) for ext in image_extensions)]
            for img_file in image_files:
                img_path = os.path.join(crop_dir, img_file)
                samples.append({
                    "id": f"real_{crop_name}_{img_file}",
                    "crop": crop_name.capitalize(),
                    "disease": "Unknown",  # Real images - disease not pre-determined
                    "image_path": img_path,
                    "filename": img_file,
                })
    return samples


def render_sample_images_gallery():
    """Render the one-click sample images gallery in Diagnose page using real photographs."""

    st.markdown("---")
    st.subheader(t("sample_gallery_heading"))

    st.markdown(t("sample_gallery_instructions"))

    # Get real images from diagnosis directories
    samples = get_real_sample_images()

    if not samples:
        st.info(t("no_sample_images_available"))
        return

    # Group by crop
    crops = {}
    for s in samples:
        crop = s["crop"]
        if crop not in crops:
            crops[crop] = []
        crops[crop].append(s)

    for crop_name in sorted(crops.keys()):
        crop_samples = crops[crop_name]
        translated_crop = translate_crop_name(crop_name)
        with st.expander(t("crop_samples_count", crop=translated_crop, count=len(crop_samples)), expanded=False):
            cols = st.columns(min(len(crop_samples), 3))
            for i, sample in enumerate(crop_samples):
                with cols[i % 3]:
                    try:
                        img = Image.open(sample["image_path"])
                        # Use filename as caption, truncate if too long
                        filename = sample.get("filename", "Sample")
                        caption = f"{translate_crop_name(sample.get('crop', ''))} — {filename[:30]}..."
                        st.image(img, caption=caption, width=200)

                        if st.button(
                            t("sample_diagnose"),
                            key=f"sample_{sample['id']}"
                        ):
                            st.session_state[f"auto_sample_{sample['id']}"] = True
                            st.session_state["auto_sample_data"] = sample
                            st.rerun()
                    except Exception as e:
                        st.warning(t("sample_load_error", id=sample["id"]))


# =====================================================
# AI EXPLANATION
# =====================================================

def render_ai_explanation(predicted_class, confidence, top_predictions, crop):
    """
    Render an interactive AI explanation after diagnosis.

    Args:
        predicted_class: The model's top prediction
        confidence: Confidence percentage
        top_predictions: List of (class_name, probability) tuples
        crop: Detected crop name
    """

    st.markdown("---")
    st.subheader(t("how_ai_reached_result"))

    # Confidence interpretation
    if confidence >= 80:
        conf_level = t("ai_high_confidence")
        conf_color = "#22c55e"
        conf_text = t("ai_high_confidence_desc", confidence=f"{confidence:.1f}%")
    elif confidence >= 60:
        conf_level = t("ai_medium_confidence")
        conf_color = "#eab308"
        conf_text = t("ai_medium_confidence_desc", confidence=f"{confidence:.1f}%")
    else:
        conf_level = t("ai_lower_confidence")
        conf_color = "#f97316"
        conf_text = t("ai_lower_confidence_desc", confidence=f"{confidence:.1f}%")

    # What the AI sees
    info_for_class = None
    for s in SAMPLE_IMAGES:
        if s["class"] == predicted_class:
            info_for_class = s
            break

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #f0fdf4, #dcfce7);
            border: 1px solid #22c55e;
            border-radius: 10px;
            padding: 14px;
            margin: 4px 0;
        ">
            <div style="color: {conf_color}; font-size: 16px; font-weight: bold; margin-bottom: 6px;">
                {conf_level}
            </div>
            <div style="color: #374151; font-size: 13px; line-height: 1.5;">
                {conf_text}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #eff6ff, #dbeafe);
            border: 1px solid #3b82f6;
            border-radius: 10px;
            padding: 14px;
            margin: 4px 0;
        ">
            <div style="color: #1d4ed8; font-size: 14px; font-weight: bold; margin-bottom: 6px;">
                {t('ai_looked_for')}
            </div>
            <div style="color: #374151; font-size: 13px; line-height: 1.5;">
                {t('ai_looked_for_desc')}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Top predictions bar chart
    st.markdown(f"#### {t('top_ai_predictions')}")

    if top_predictions and len(top_predictions) > 0:
        # Show top 5
        display_preds = top_predictions[:5]

        for class_name, prob in display_preds:
            is_top = class_name == predicted_class
            bar_color = "#22c55e" if is_top else "#94a3b8"
            bar_width = int(prob * 100)

            disease_label = class_name.replace("_", " ").title()
            if "healthy" in class_name.lower():
                disease_label = t("ai_healthy_label")

            marker = "▶ " if is_top else "  "

            st.markdown(f"""
            <div style="margin: 6px 0;">
                <div style="font-size: 12px; color: #374151; margin-bottom: 2px;">
                    {marker}<b>{disease_label}</b> — {prob*100:.1f}%
                </div>
                <div style="
                    background: #e5e7eb;
                    border-radius: 4px;
                    height: 10px;
                    width: 100%;
                    overflow: hidden;
                ">
                    <div style="
                        background: {bar_color};
                        width: {bar_width}%;
                        height: 100%;
                        border-radius: 4px;
                        transition: width 0.3s;
                    "></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # AI model info
    st.info(t("about_ai_confidence"))


# =====================================================
# GET TOP PREDICTIONS
# =====================================================

def get_top_predictions(model, image, class_names, top_n=5):
    """
    Run prediction and return top N predictions with probabilities.
    """
    try:
        from PIL import Image as PILImage
        import numpy as np

        img = image.resize((224, 224))
        img_array = np.array(img).astype(np.float32)

        if img_array.ndim != 3 or img_array.shape[2] != 3:
            return None

        img_array = np.expand_dims(img_array, axis=0)
        predictions = model.predict(img_array, verbose=0)

        probs = predictions[0]

        # Get indices sorted by probability
        indices = np.argsort(probs)[::-1][:top_n]

        return [
            (class_names[idx], float(probs[idx]))
            for idx in indices
        ]
    except Exception:
        return None


# =====================================================
# EXPORT DIAGNOSIS HISTORY
# =====================================================

def export_diagnosis_csv():
    """Generate and return CSV of all diagnosis history."""
    if not os.path.exists(HISTORY_FILE):
        return None

    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except Exception:
        return None

    if not history:
        return None

    output = io.StringIO()
    writer = csv.DictWriter(
        output,
        fieldnames=["Date", "Crop", "Disease", "Confidence", "Crop ID"]
    )
    writer.writeheader()

    for record in history:
        writer.writerow({
            "Date": record.get("date", ""),
            "Crop": record.get("crop", ""),
            "Disease": record.get("disease", ""),
            "Confidence": f"{record.get('confidence', 0):.2f}%",
            "Crop ID": record.get("crop_id", "General")
        })

    return output.getvalue()


def export_raksha_csv(crop_id=None):
    """Generate CSV of Crop Raksha observations."""
    if not os.path.exists(RAKSHA_FILE):
        return None

    try:
        with open(RAKSHA_FILE, "r") as f:
            history = json.load(f)
    except Exception:
        return None

    if crop_id:
        history = [r for r in history if r.get("crop_id") == crop_id]

    if not history:
        return None

    output = io.StringIO()
    writer = csv.DictWriter(
        output,
        fieldnames=["Day", "Date", "Status", "Disease", "Confidence", "Observation"]
    )
    writer.writeheader()

    for record in history:
        writer.writerow({
            "Day": record.get("day", ""),
            "Date": record.get("date", ""),
            "Status": record.get("status", ""),
            "Disease": record.get("disease", ""),
            "Confidence": f"{record.get('confidence', 0):.2f}%",
            "Observation": record.get("observation", "")
        })

    return output.getvalue()


# =====================================================
# VOICE FEEDBACK (browser TTS)
# =====================================================

def get_voice_feedback_html(disease, confidence, crop):
    """Return HTML/JS for browser text-to-speech of diagnosis result."""

    disease_lower = disease.lower().strip() if disease else ""

    if disease_lower == "healthy":
        message = t("voice_healthy_msg", crop=crop, confidence=confidence)
    else:
        message = t("voice_disease_msg", crop=crop, disease=disease, confidence=confidence)

    # Escape any double-quotes for safe embedding inside the JS string
    safe_message = message.replace('"', '\\"')

    return f"""
    <script>
    function speakDiagnosis() {{
        if ('speechSynthesis' in window) {{
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance("{safe_message}");
            utterance.rate = 0.88;
            utterance.pitch = 1.0;
            utterance.volume = 1.0;
            window.speechSynthesis.speak(utterance);
        }}
    }}
    // Auto-speak after page load
    window.addEventListener('load', function() {{
        setTimeout(speakDiagnosis, 500);
    }});
    </script>
    <button onclick="speakDiagnosis()" style="
        background: linear-gradient(135deg, #22c55e, #16a34a);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 14px;
        cursor: pointer;
        margin: 8px 0;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 2px 8px rgba(34,197,94,0.3);
    ">
        {t('voice_listen_btn')}
    </button>
    """


# =====================================================
# CROP RAKSHA INTELLIGENT INSIGHTS
# =====================================================

def get_raksha_insights(records, crop_name, farmer_name):
    """
    Generate natural-language insights from Crop Raksha observations.
    """
    if not records:
        return None

    # Sort by day
    ordered = sorted(records, key=lambda x: x.get("day", 0))

    # Count statuses
    statuses = [r.get("status", "unknown") for r in ordered]
    diseases = [r.get("disease", "") for r in ordered]

    healthy_count = sum(1 for d in diseases if d.lower() == "healthy")
    total = len(ordered)

    # Analyze trend
    if total == 1:
        trend = "just_started"
        trend_text = t(
            "raksha_just_started",
            farmer=farmer_name,
            crop=translate_crop_name(crop_name)
        )
    else:
        # Check if there are worsening signs
        has_issue = any(
            d.lower() != "healthy"
            for d in diseases[-2:]
        )
        has_significant = "significant_change" in statuses[-2:]

        if has_significant or (has_issue and ordered[-1].get("confidence", 0) >= 60):
            trend = "alert"
            trend_text = t(
                "raksha_alert",
                crop=translate_crop_name(crop_name)
            )
        elif "minor_change" in statuses[-1:]:
            trend = "watch"
            trend_text = t(
                "raksha_watch",
                farmer=farmer_name,
                crop=translate_crop_name(crop_name),
                total=total
            )
        else:
            trend = "stable"
            trend_text = t(
                "raksha_stable",
                farmer=farmer_name,
                crop=translate_crop_name(crop_name),
                total=total,
                healthy=healthy_count
            )

    # Days since last check
    if ordered:
        latest_date = ordered[-1].get("date", "")
        if latest_date:
            try:
                from datetime import datetime as dt
                last_dt = dt.strptime(latest_date, "%Y-%m-%d %H:%M")
                days_ago = (dt.now() - last_dt).days
                if days_ago == 0:
                    time_text = t("raksha_today")
                elif days_ago == 1:
                    time_text = t("raksha_yesterday")
                else:
                    time_text = t("raksha_days_ago", n=days_ago)
                time_text = t(
                    "raksha_last_observation",
                    time=time_text,
                    date=latest_date
                )
            except Exception:
                time_text = t(
                    "raksha_last_observation_date",
                    date=latest_date
                )
        else:
            time_text = t("raksha_no_date")
    else:
        time_text = t("raksha_no_observations")

    return {
        "trend": trend,
        "trend_text": trend_text,
        "time_text": time_text,
        "healthy_count": healthy_count,
        "total_observations": total,
        "latest_disease": diseases[-1] if diseases else None,
        "latest_confidence": ordered[-1].get("confidence", 0) if ordered else 0,
    }
