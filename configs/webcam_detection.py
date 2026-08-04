import cv2
from ultralytics import YOLO

# Load the model
model = YOLO("Models/yolov8n.pt")


def webcam_detection():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Run YOLO detection
        results = model(frame)

        # Draw detections
        annotated_frame = results[0].plot()

        # Display
        cv2.imshow("YOLOv8 Webcam Detection", annotated_frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    webcam_detection()
