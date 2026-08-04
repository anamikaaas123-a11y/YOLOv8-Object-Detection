from ultralytics import YOLO

model = YOLO("Models/yolov8n.pt")

def detect_image(image_path):

    results = model(image_path)

    detected_objects = []

    for box in results[0].boxes:

        class_id = int(box.cls[0])

        detected_objects.append({
            "Class": model.names[class_id],
            "Confidence": round(float(box.conf[0]), 2)
        })

    return results, detected_objects