import numpy as np
import cv2
from src.preprocessing.document_loader import load_document
from src.preprocessing.image_preprocessing import preprocess_image
from src.ocr.ocr_engine import extract_text
from src.nlp.field_extractor import extract_fields


def process_document(file_path):
    """
    Process an uploaded document through the complete AI pipeline.

    Parameters:
        file_path (str): Path to the uploaded PDF, JPG, or PNG file.

    Returns:
        dict: Extracted text and structured fields.
    """

    images = load_document(file_path)

    all_text = []


    for image in images:

        image = np.array(image)
        processed_image = preprocess_image(image)

        text = extract_text(processed_image)

        if text:
            all_text.append(text)

    combined_text = "\n".join(all_text)

    fields = extract_fields(combined_text)

    return {
        "text": combined_text,
        "fields": fields,
    }