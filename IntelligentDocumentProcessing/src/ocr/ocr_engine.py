import os
import pytesseract


if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )


def extract_text(image):
    try:
        text = pytesseract.image_to_string(
            image,
            config="--psm 3"
        )
        return text.strip()
    except Exception as error:
        print(f"OCR Error: {error}")
        return ""