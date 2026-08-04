import os
import cv2
from ultralytics import YOLO

# Load model once
model = YOLO("Models/yolov8n.pt")


def process_video(video_path):
    """
    Detect objects in a video and save the annotated video.
    """

    os.makedirs("../outputs/videos", exist_ok=True)

    output_path = "../outputs/videos/result.mp4"

    cap = cv2.VideoCapture(video_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame)

        annotated_frame = results[0].plot()

        out.write(annotated_frame)

    cap.release()
    out.release()

    return output_path