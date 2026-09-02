import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array
from disease_info import DISEASE_INFO

# ==============================
# CROP DOCTOR - PREDICTION
# ==============================

MODEL_PATH = "models/best_crop_doctor.keras"
CLASS_PATH = "class_names.json"
IMAGE_SIZE = (224, 224)

# Load trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Load class names
with open(CLASS_PATH, "r") as f:
    class_data = json.load(f)

# Handle either a list or dictionary
if isinstance(class_data, list):
    class_names = class_data
else:
    class_names = list(class_data.values())

# Ask for image
image_path = input("Enter the path of the leaf image: ")

# Load image
image = load_img(image_path, target_size=IMAGE_SIZE)
image = img_to_array(image)

# Add batch dimension
image = np.expand_dims(image, axis=0)

# Predict
predictions = model.predict(image, verbose=0)

# Get best prediction
predicted_index = np.argmax(predictions[0])
confidence = float(predictions[0][predicted_index]) * 100

predicted_class = class_names[predicted_index]

# Display result


info = DISEASE_INFO.get(predicted_class)

print("\n========================================")
print("🌱 CROP DOCTOR RESULT")
print("========================================")

print(f"Prediction : {predicted_class}")
print(f"Confidence : {confidence:.2f}%")

if info:
    print(f"\nCrop       : {info['crop']}")
    print(f"Disease    : {info['disease']}")

    print("\nDescription:")
    print(info["description"])

    print("\nSymptoms:")
    for symptom in info["symptoms"]:
        print(f"  • {symptom}")

    print("\nManagement:")
    for item in info["management"]:
        print(f"  • {item}")

    print("\nPrevention:")
    for item in info["prevention"]:
        print(f"  • {item}")

else:
    print("\n⚠️ Information for this disease has not been added yet.")

print("========================================")