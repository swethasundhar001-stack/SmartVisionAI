from src.ocr.ocr_engine import extract_text


def test_extract_text(monkeypatch):

    def mock_ocr(image, config):
        return "Name: Priya Kumar\nEmail: priya@gmail.com"

    monkeypatch.setattr(
        "src.ocr.ocr_engine.pytesseract.image_to_string",
        mock_ocr
    )

    result = extract_text("dummy_image")

    assert result == "Name: Priya Kumar\nEmail: priya@gmail.com"