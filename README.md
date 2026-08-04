# YOLOv8 Object Detection System

## Overview

This project is an object detection system built using **YOLOv8**.

It detects objects from images and videos using deep learning and provides bounding box visualization with confidence scores.

The system supports:
- Image object detection
- Video object detection
- Uploading input files
- Saving detection outputs

---

## Features

- Real-time object detection
- YOLOv8 based inference
- Image and video processing
- Bounding box visualization
- Confidence score prediction
- Organized ML project structure

---

## Technologies Used

- Python
- YOLOv8
- Ultralytics
- PyTorch
- OpenCV
- NumPy

---

## Project Structure

```text
YOLO_Object_Detection/

├── configs/            
│   └── Model configuration files
│
├── models/             
│   └── YOLO model weights
│
├── data/               
│   ├── test_images/
│   └── test_videos/
│
├── uploads/            
│   └── Input uploaded files
│
├── outputs/            
│   └── Detection results
│
├── utils/              
│   └── Helper functions
│
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project directory

```bash
cd <repository-name>
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the detection application:

```bash
python app.py
```

Provide an image or video input to generate object detection results.

---

## Output

Detection results are saved in:

```text
outputs/
```

The output contains processed images and videos with detected objects, bounding boxes, and confidence scores.

---

## Model

This project uses **YOLOv8 from Ultralytics** for object detection.

The model performs:

- Object localization
- Object classification
- Confidence score prediction

---

## Future Improvements

- Real-time webcam detection
- Custom dataset training
- Model optimization
- API deployment
- Cloud integration

---

## Author

**Anamika S**  
B.Tech Artificial Intelligence and Machine Learning
