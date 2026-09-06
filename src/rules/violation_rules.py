def check_violations(detected_classes):
    """
    Check detected objects and identify safety violations.
    """

    violations = []

    # Explicit violation classes
    if "no_helmet" in detected_classes:
        violations.append("No Helmet Detected")

    if "no_vest" in detected_classes:
        violations.append("No Safety Vest Detected")

    # Fallback checks
    if "person" in detected_classes and "helmet" not in detected_classes:
        violations.append("No Helmet Detected")

    if "person" in detected_classes and "safety_vest" not in detected_classes:
        violations.append("No Safety Vest Detected")

    return list(set(violations))