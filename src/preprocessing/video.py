import cv2


def read_video(video_path):
    """
    Read a video file frame by frame.
    """
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError("Unable to open video")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        yield frame

    cap.release()