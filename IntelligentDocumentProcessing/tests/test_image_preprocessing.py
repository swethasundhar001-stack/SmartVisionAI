import cv2
import numpy as np
import pytest

from src.preprocessing.image_preprocessing import preprocess_image


def test_preprocess_image():
    image = np.zeros((100, 100, 3), dtype=np.uint8)

    result = preprocess_image(image)

    assert result is not None
    assert len(result.shape) == 2
    assert result.shape == (150, 150)


def test_invalid_image():
    with pytest.raises(ValueError):
        preprocess_image(None)