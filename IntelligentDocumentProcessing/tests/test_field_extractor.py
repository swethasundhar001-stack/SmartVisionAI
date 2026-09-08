from src.nlp.field_extractor import extract_fields


def test_extract_fields():
    text = """
    Name: Priya Kumar
    Email: priya@gmail.com
    Phone: 9876543210
    Date: 01/09/2026
    Amount: Rs 12500
    Address: Chennai, Tamil Nadu
    """

    result = extract_fields(text)

    assert result["name"] == "Priya Kumar"
    assert result["email"] == "priya@gmail.com"
    assert result["phone"] == "9876543210"
    assert result["date"] == "01/09/2026"
    assert result["amount"] == "Rs 12500"
    assert result["address"] == "Chennai, Tamil Nadu"