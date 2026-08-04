import os
from detect import detect_image

def process_image(image_path):

    results, detected_objects = detect_image(image_path)

    os.makedirs("../outputs/images", exist_ok=True)

    output_path = "../outputs/images/result.jpg"

    results[0].save(filename=output_path)

    return output_path, detected_objects