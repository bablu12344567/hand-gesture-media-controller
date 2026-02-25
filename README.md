# ✋ Hand Gesture–Based Media Controller

## 📌 Overview

This project is a real-time hand gesture recognition system built using **Python, OpenCV, and MediaPipe**.  
It uses a webcam to detect hand landmarks and maps specific finger gestures to media control actions such as play/pause, volume control, skipping, and brightness adjustment.

The goal of this project was to explore computer vision and human-computer interaction by building a practical, real-time gesture-controlled media system.

---

## 🚀 Features

- Real-time hand tracking using MediaPipe
- Finger counting using hand landmark detection
- Control media playback (play/pause, next, previous)
- Adjust system volume
- Adjust screen brightness (Windows)
- CLI-based execution
- Action delay control to prevent repeated triggers

---

## 🧠 How It Works

1. Webcam captures live video using OpenCV.
2. MediaPipe detects hand landmarks.
3. The system calculates finger positions using landmark coordinates.
4. Based on the number of fingers detected, specific keyboard actions are triggered using `pyautogui`.
5. Brightness control is handled using `screen_brightness_control` (Windows only).

---

## 🎮 Gesture Mapping

| Gesture | Action |
|----------|--------|
| 👍 Thumb Only | Increase Brightness |
| 🤙 Pinky Only | Decrease Brightness |
| ☝️ 1 Finger | Skip Forward |
| ✌️ 2 Fingers | Skip Backward |
| 🤟 3 Fingers | Volume Up |
| 🖖 4 Fingers | Volume Down |
| ✋ 5 Fingers | Play / Pause |

---

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- Screen Brightness Control (Windows)
- Webcam (for real-time capture)

---

## 📂 Installation & Setup

### 1️⃣ Install Python (Recommended: Python 3.10 or 3.11)

### 2️⃣ Install Required Packages

```bash
pip install opencv-python mediapipe pyautogui screen-brightness-control
```

---

## ▶️ How To Run

Navigate to project folder:

```bash
cd "C:\Users\reddy\Desktop\hand gesture"
```

Run the script:

```bash
python "hand gesture media player controller.py"
```

Press **ESC** to exit the application.

---

## 🧩 Core Concepts Used

- Computer Vision
- Hand Landmark Detection
- Real-time Video Processing
- Coordinate-based Finger Counting
- OS-level Automation
- Event Throttling (to prevent repeated actions)

---

## 📷 Example Workflow

1. Show hand to webcam.
2. System detects number of raised fingers.
3. Corresponding media action is triggered instantly.

---

## 🔮 Future Improvements

- Add gesture smoothing for better accuracy
- Add gesture customization options
- Add GUI for gesture configuration
- Multi-hand support
- Cross-platform brightness control
- Add machine learning-based gesture classification

---

## 🎯 Learning Outcome

Through this project, I gained hands-on experience with:

- Real-time computer vision systems
- MediaPipe hand tracking model
- Gesture recognition logic
- System automation using Python
- Handling real-time user input with controlled event triggering

This project helped bridge the gap between theoretical computer vision concepts and practical implementation.
