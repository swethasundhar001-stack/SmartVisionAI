import numpy as np

import src.utils.pipeline as pipeline


def test_process_document(monkeypatch):

    # Mock document loader
    def mock_load_document(file_path):
        return [np.zeros((100, 100, 3), dtype=np.uint8)]

    # Mock preprocessing
    def mock_preprocess_image(image):
        return image

    # Mock OCR
    def mock_extract_text(image):
        return "Name: Priya Kumar\nEmail: priya@gmail.com"

    # Mock field extraction
    def mock_extract_fields(text):
        return {
            "name": "Priya Kumar",
            "date": "",
            "amount": "",
            "email": "priya@gmail.com",
            "phone": "",
            "address": "",
        }

    monkeypatch.setattr(
        pipeline,
        "load_document",
        mock_load_document
    )

    monkeypatch.setattr(
        pipeline,
        "preprocess_image",
        mock_preprocess_image
    )

    monkeypatch.setattr(
        pipeline,
        "extract_text",
        mock_extract_text
    )

    monkeypatch.setattr(
        pipeline,
        "extract_fields",
        mock_extract_fields
    )

    result = pipeline.process_document("dummy.pdf")

    assert result is not None
    assert isinstance(result, dict)

    assert "text" in result
    assert "fields" in result

    assert result["text"] == "Name: Priya Kumar\nEmail: priya@gmail.com"

    assert result["fields"]["name"] == "Priya Kumar"
    assert result["fields"]["email"] == "priya@gmail.com"