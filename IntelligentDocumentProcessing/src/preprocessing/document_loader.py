from pathlib import Path

from pdf2image import convert_from_path


def load_document(file_path):
    """
    Load PDF, JPG, or PNG document.

    Parameters:
        file_path (str): Path to the uploaded document.

    Returns:
        list: List of PIL images.
    """

    file_extension = Path(file_path).suffix.lower()

    if file_extension == ".pdf":
        images = convert_from_path(file_path)
        return images

    if file_extension in [".jpg", ".jpeg", ".png"]:
        from PIL import Image

        image = Image.open(file_path)
        return [image]

    raise ValueError(
        "Unsupported file format. Please upload PDF, JPG, or PNG."
    )