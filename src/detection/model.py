from ultralytics import YOLO


def load_model(model_path):
    """
    Load the trained YOLO model.
    """
    return YOLO(model_path)