from src.utils.pipeline import process_document


def process_file(file_path):
    """
    Process an uploaded document and return
    extracted text and structured fields.
    """
    return process_document(file_path)