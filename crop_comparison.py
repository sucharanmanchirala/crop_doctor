import numpy as np
from PIL import Image, ImageFilter


IMAGE_SIZE = (224, 224)


# =====================================================
# IMAGE DIFFERENCE
# =====================================================

def calculate_image_difference(previous_image, current_image):
    """
    Compare the previous monitoring image with today's image.

    Returns a percentage representing overall visual difference.
    Higher value = greater visual change.
    """

    try:
        previous_image = (
            previous_image
            .convert("RGB")
            .resize(IMAGE_SIZE)
        )

        current_image = (
            current_image
            .convert("RGB")
            .resize(IMAGE_SIZE)
        )

        previous_array = np.array(
            previous_image
        ).astype(np.float32)

        current_array = np.array(
            current_image
        ).astype(np.float32)

        difference = np.mean(
            np.abs(
                previous_array - current_array
            )
        )

        difference_percentage = (
            difference / 255
        ) * 100

        return round(
            float(difference_percentage),
            2
        )

    except Exception:
        return None


# =====================================================
# CHANGE CLASSIFICATION
# =====================================================

def classify_change(difference_percentage):
    """
    Convert visual difference into a
    Crop Raksha warning level.
    """

    if difference_percentage is None:
        return "unknown"

    if difference_percentage < 10:
        return "normal"

    elif difference_percentage < 20:
        return "minor_change"

    else:
        return "significant_change"


# =====================================================
# VISUAL DIFFERENCE HEATMAP
# =====================================================

def generate_difference_heatmap(
    previous_image,
    current_image
):
    """
    Generate a visual heatmap showing WHERE
    the crop image has changed.

    Darker areas = smaller difference
    Brighter areas = larger difference

    Returns:
        PIL Image containing the heatmap.
    """

    try:

        # ---------------------------------------------
        # RESIZE BOTH IMAGES
        # ---------------------------------------------

        previous_image = (
            previous_image
            .convert("RGB")
            .resize(IMAGE_SIZE)
        )

        current_image = (
            current_image
            .convert("RGB")
            .resize(IMAGE_SIZE)
        )

        # ---------------------------------------------
        # CONVERT TO NUMPY ARRAYS
        # ---------------------------------------------

        previous_array = np.array(
            previous_image
        ).astype(np.float32)

        current_array = np.array(
            current_image
        ).astype(np.float32)

        # ---------------------------------------------
        # PIXEL DIFFERENCE
        # ---------------------------------------------

        pixel_difference = np.abs(
            previous_array - current_array
        )

        # Convert RGB difference into
        # one grayscale difference value.
        difference_map = np.mean(
            pixel_difference,
            axis=2
        )

        # ---------------------------------------------
        # NORMALIZE
        # ---------------------------------------------

        maximum = difference_map.max()

        if maximum > 0:

            normalized = (
                difference_map / maximum
            ) * 255

        else:

            normalized = np.zeros_like(
                difference_map
            )

        normalized = normalized.astype(
            np.uint8
        )

        # ---------------------------------------------
        # CREATE GRAYSCALE HEATMAP
        # ---------------------------------------------

        heatmap_gray = Image.fromarray(
            normalized,
            mode="L"
        )

        # Slight smoothing makes the heatmap
        # easier to visually understand.
        heatmap_gray = heatmap_gray.filter(
            ImageFilter.GaussianBlur(
                radius=1.2
            )
        )

        # ---------------------------------------------
        # CREATE COLORED HEATMAP
        # ---------------------------------------------
        #
        # We create a simple blue -> green -> yellow ->
        # red gradient without requiring matplotlib.
        #

        gray_array = np.array(
            heatmap_gray
        ).astype(np.float32) / 255.0

        red = np.clip(
            gray_array * 2,
            0,
            1
        )

        green = np.clip(
            2 - np.abs(
                gray_array * 4 - 2
            ),
            0,
            1
        )

        blue = np.clip(
            1 - gray_array * 2,
            0,
            1
        )

        heatmap_array = np.stack(
            [
                red,
                green,
                blue
            ],
            axis=2
        )

        heatmap_array = (
            heatmap_array * 255
        ).astype(
            np.uint8
        )

        heatmap = Image.fromarray(
            heatmap_array,
            mode="RGB"
        )

        return heatmap

    except Exception:
        return None