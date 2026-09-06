from datetime import datetime
import csv
import os


LOG_FILE = "outputs/violation_logs.csv"


def log_violation(violation):
    """
    Save a safety violation with timestamp into a CSV log file.
    """

    os.makedirs("outputs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Timestamp", "Violation"])

        writer.writerow([timestamp, violation])

    print(f"[{timestamp}] VIOLATION: {violation}")