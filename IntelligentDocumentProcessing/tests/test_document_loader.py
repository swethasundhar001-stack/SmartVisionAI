from PIL import Image
import pytest

from src.preprocessing.document_loader import load_document


def test_load_image(tmp_path):
    image_path = tmp_path / "test.png"

    image = Image.new("RGB", (100, 100), "white")
    image.save(image_path)

    result = load_document(str(image_path))

    assert len(result) == 1
    assert isinstance(result[0], Image.Image)


def test_unsupported_file(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("test")

    with pytest.raises(ValueError):
        load_document(str(file_path))