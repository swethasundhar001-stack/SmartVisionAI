import re


def extract_fields(text):
    """
    Extract important fields from OCR text.
    """

    fields = {
        "name": "",
        "date": "",
        "amount": "",
        "email": "",
        "phone": "",
        "address": "",
    }

    # -----------------------------
    # Extract name
    # -----------------------------

    name_match = re.search(
        r"(?:Name|Customer Name|Full Name)\s*[:\-]?\s*(.+?)(?=\n|Email|Ema|Phone|Date|Amount|Address|$)",
        text,
        re.IGNORECASE
    )

    if name_match:
        fields["name"] = name_match.group(1).strip()

    # -----------------------------
    # Extract email
    # -----------------------------

    email_match = re.search(
        r"[\w.-]+@[\w.-]+\.\w+",
        text,
        re.IGNORECASE
    )

    if email_match:
        fields["email"] = email_match.group().strip()

    # -----------------------------
    # Extract phone number
    # -----------------------------

    phone_match = re.search(
        r"(?:\+91[\s-]?)?[6-9]\d{9}",
        text
    )

    if phone_match:
        fields["phone"] = phone_match.group().strip()

    # -----------------------------
    # Extract date
    # -----------------------------

    date_match = re.search(
        r"\b(?:"
        r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}"
        r"|"
        r"\d{4}[/-]\d{1,2}[/-]\d{1,2}"
        r"|"
        r"\d{1,2}\.\d{1,2}\.\d{2,4}"
        r")\b",
        text
    )

    if date_match:
        fields["date"] = date_match.group().strip()

    # Date fallback for labelled dates
    if not fields["date"]:

        date_label_match = re.search(
            r"(?:Date|Date of Birth|DOB)\s*[:\-]?\s*"
            r"([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})",
            text,
            re.IGNORECASE
        )

        if date_label_match:
            fields["date"] = date_label_match.group(1).strip()

    # -----------------------------
    # Extract amount
    # -----------------------------

    amount_match = re.search(
        r"(?:₹|Rs\.?|INR|Ps\.?)\s*[\d,]+(?:\.\d{1,2})?",
        text,
        re.IGNORECASE
    )

    if amount_match:
        fields["amount"] = amount_match.group().strip()

        fields["amount"] = re.sub(
            r"^Ps\.?",
            "Rs",
            fields["amount"],
            flags=re.IGNORECASE
        )

    # Amount fallback
    if not fields["amount"]:

        amount_label_match = re.search(
            r"Amount\s*[:\-]?\s*"
            r"(?:₹|Rs\.?|INR|Ps\.?)?\s*"
            r"([\d,]+(?:\.\d{1,2})?)",
            text,
            re.IGNORECASE
        )

        if amount_label_match:
            fields["amount"] = "Rs " + amount_label_match.group(1)

    # -----------------------------
    # Extract address
    # -----------------------------

    address_match = re.search(
        r"Address\s*[:\-]?\s*(.+?)(?="
        r"\n\s*(?:Name|Email|Phone|Date|Amount)\s*[:\-]?"
        r"|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if address_match:
        fields["address"] = " ".join(
            address_match.group(1).split()
        ).strip()

    return fields