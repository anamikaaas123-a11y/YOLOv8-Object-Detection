from detect import detect_image

results = detect_image("../test_images/car.jpg")
results[0].show()
results[0].save()