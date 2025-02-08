
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Load the trained YOLOv8 model
model_path = "/Users/Learning Stuffs/360DigiTMg/Solar Project/Streamlit/best.pt"  # Replace with your trained model path
model = YOLO(model_path)

st.set_page_config(
    page_title="Solar Panel Defect Detection",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("Solar Panel Defect Detection")
st.write("This application uses YOLOv8 to detect defects in solar panels. Upload an image to get started!")

# Sidebar options
st.sidebar.header("Settings")
confidence_threshold = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.5)
iou_threshold = st.sidebar.slider("IoU Threshold", 0.0, 1.0, 0.45)

# File uploader
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the uploaded file to an image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Perform detection
    results = model.predict(np.array(image), conf=confidence_threshold, iou=iou_threshold)

    # Annotate results on the image
    annotated_image = results[0].plot()
    st.image(annotated_image, caption="Detected Image", use_column_width=True)

    # Display detection details
    st.subheader("Detection Results")
    detected_classes = {}
    for result in results[0].boxes.data.tolist():
        class_id = int(result[5])
        class_name = model.names[class_id]
        score = result[4]

        # Keep a count of detected classes
        if class_name in detected_classes:
            detected_classes[class_name] += 1
        else:
            detected_classes[class_name] = 1

        st.write(f"- {class_name}: {score:.2f}")

    # Display detected class summary
    st.subheader("Detected Classes Summary")
    if detected_classes:
        for class_name, count in detected_classes.items():
            st.write(f"{class_name}: {count} instances detected")
    else:
        st.write("No defects detected.")

st.sidebar.info("Model trained on the following classes: [Bird-drop, Defective, Dusty, Electrical-Damage, Non-Defective, Physical-Damage]")
st.sidebar.write("Adjust the confidence and IoU thresholds using the sliders above to fine-tune detection results.")