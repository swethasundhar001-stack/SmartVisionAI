def run_detection(model, image, confidence=0.25):
    """
    Run YOLO object detection on an image.
    """
    results = model.predict(
        image,
        conf=confidence,
        imgsz=320
    )

    return results[0]