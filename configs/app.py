import os
import streamlit as st
from image_detection import process_image

st.set_page_config(
    page_title="YOLOv8 Object Detection",
    layout="wide"
)

st.title("🚀 YOLOv8 Object Detection")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Save uploaded image
    os.makedirs("../uploads", exist_ok=True)

    image_path = os.path.join("../uploads", uploaded_file.name)

    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Run detection
    output_path, detected_objects = process_image(image_path)

    st.success("Detection Completed!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Detected Image")
        st.image(output_path)

    with col2:
        st.subheader("Detected Objects")
        st.table(detected_objects)