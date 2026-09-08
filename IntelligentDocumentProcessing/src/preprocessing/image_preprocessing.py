import cv2
import numpy as np


def preprocess_image(image):
    """
    Preprocess an image before OCR.
    """

    # If a file path is provided, read the image
    if isinstance(image, str):
        image = cv2.imread(image)

    # Check image
    if image is None:
        raise ValueError("Unable to read the image.")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize for better OCR accuracy
    resized = cv2.resize(
        gray,
        None,
        fx=1.5,
        fy=1.5,
        interpolation=cv2.INTER_CUBIC
    )

    return resized