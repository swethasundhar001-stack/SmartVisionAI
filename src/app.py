import streamlit as st
from PIL import Image
import tempfile
import cv2
import os

from src.detection.model import load_model
from src.detection.inference import run_detection
from src.preprocessing.video import read_video
from src.rules.violation_rules import check_violations
from src.alerts.alert_manager import send_alert
from src.database.logger import log_violation


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="SmartVision AI",
    page_icon="🚨",
    layout="wide"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🚨 SmartVision AI")
st.subheader("Real-Time Safety Monitoring System")

st.write(
    "Detect safety equipment and safety violations "
    "from images and video files."
)


# --------------------------------------------------
# Load Model
# --------------------------------------------------

model = load_model("models/smartvision_best.pt")


# --------------------------------------------------
# Input Selection
# --------------------------------------------------

input_type = st.radio(
    "Select Input Type",
    ["Image", "Video"],
    horizontal=True
)


# ==================================================
# IMAGE DETECTION
# ==================================================

if input_type == "Image":

    uploaded_file = st.file_uploader(
        "Upload a safety image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.subheader("📷 Uploaded Image")
        st.image(
            image,
            use_container_width=True
        )

        if st.button("🔍 Detect Safety Objects"):

            result = run_detection(
                model,
                image,
                confidence=0.25
            )

            detected_classes = [
                result.names[int(class_id)]
                for class_id in result.boxes.cls
            ]

            st.subheader("🤖 AI Detection")

            annotated_image = result.plot()

            st.image(
                annotated_image,
                caption="AI Detection Result",
                use_container_width=True
            )

            st.subheader("🔍 Detected Objects")
            st.write(detected_classes)

            violations = check_violations(
                detected_classes
            )

            total_persons = detected_classes.count(
                "person"
            )

            violation_count = len(violations)

            safe_persons = max(
                total_persons - violation_count,
                0
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "👷 Total Persons",
                total_persons
            )

            col2.metric(
                "✅ Safe Persons",
                safe_persons
            )

            col3.metric(
                "🚨 Violations",
                violation_count
            )

            st.subheader("🚨 Safety Status")

            if violations:

                for violation in violations:

                    st.error(violation)

                    send_alert(violation)

                    log_violation(violation)

            else:

                st.success(
                    "✅ No safety violations detected"
                )


# ==================================================
# VIDEO DETECTION
# ==================================================

else:

    uploaded_video = st.file_uploader(
        "Upload a safety video",
        type=["mp4", "avi", "mov"]
    )

    if uploaded_video is not None:

        st.video(uploaded_video)

        if st.button("🎥 Process Video"):

            # Save uploaded video temporarily
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".mp4"
            ) as temp_video:

                temp_video.write(
                    uploaded_video.read()
                )

                video_path = temp_video.name

            cap = cv2.VideoCapture(video_path)

            if not cap.isOpened():

                st.error(
                    "❌ Unable to open video."
                )

            else:

                cap.release()

                st.subheader("🤖 AI Video Detection")

                frame_placeholder = st.empty()

                total_frames = 0
                total_violations = 0

                progress = st.progress(0)

                frames = list(
                    read_video(video_path)
                )

                total_frame_count = len(frames)

                for index, frame in enumerate(frames):

                    result = model.predict(
                        frame,
                        conf=0.25,
                        imgsz=320,
                        verbose=False
                    )[0]

                    detected_classes = [
                        result.names[int(class_id)]
                        for class_id in result.boxes.cls
                    ]

                    violations = check_violations(
                        detected_classes
                    )

                    if violations:

                        for violation in violations:

                            total_violations += 1

                            send_alert(violation)

                            log_violation(violation)

                    annotated_frame = result.plot()

                    annotated_frame = cv2.cvtColor(
                        annotated_frame,
                        cv2.COLOR_BGR2RGB
                    )

                    frame_placeholder.image(
                        annotated_frame,
                        caption=f"Frame {index + 1}",
                        use_container_width=True
                    )

                    total_frames += 1

                    if total_frame_count > 0:

                        progress.progress(
                            (index + 1) / total_frame_count
                        )

                st.success(
                    "✅ Video processing completed!"
                )

                col1, col2 = st.columns(2)

                col1.metric(
                    "🎞️ Frames Processed",
                    total_frames
                )

                col2.metric(
                    "🚨 Total Violations Detected",
                    total_violations
                )

            # Remove temporary video
            if os.path.exists(video_path):

                os.remove(video_path)