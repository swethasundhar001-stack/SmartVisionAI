# 🚨 SmartVision AI

## Real-Time Safety Monitoring System

SmartVision AI is a Deep Learning and Computer Vision based safety monitoring system that detects safety equipment and safety violations from images and video files.

The system uses a YOLO-based object detection model to identify people and safety-related objects and provides safety status and violation alerts through a Streamlit web application.

---

## 🎯 Project Objective

The main objective of this project is to automate workplace safety monitoring using Artificial Intelligence.

The system can analyze images and video frames and detect safety-related objects such as:

- 👷 Person
- ⛑️ Helmet
- 🦺 Safety Vest
- 👢 Boots
- 🕶️ Safety Glasses
- ⚠️ No Vest and other safety-related classes

---

## 🧠 Technologies Used

- Python
- Deep Learning
- Computer Vision
- YOLO
- Ultralytics
- OpenCV
- Streamlit
- NumPy
- Pandas
- Pillow
- Git & GitHub

---

## 🏗️ Project Architecture

```text
Input Image / Video
        ↓
OpenCV Preprocessing
        ↓
YOLO Object Detection Model
        ↓
Detected Objects
        ↓
Safety Violation Rules
        ↓
Alert & Violation Logging
        ↓
Streamlit Dashboard
