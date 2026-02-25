# ✋ Hand Gesture–Based Media Controller

## 📌 Overview

This project is a real-time hand gesture recognition system built using Python, OpenCV, and MediaPipe.  
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
2. MediaPipe detects 21 hand landmarks.
3. Finger positions are determined by comparing landmark coordinates.
4. Based on detected gesture, corresponding keyboard actions are triggered using `pyautogui`.
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
- Webcam

---

## 📦 Installation

### 1️⃣ Install Python (Recommended: Python 3.10 or 3.11)

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How To Run

Navigate to project folder:

```
cd hand-gesture-media-controller
```

Run the script:

```
python gesture_controller.py
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

## 🔮 Future Improvements

- Add gesture smoothing for better accuracy
- Add gesture customization options
- Add GUI for gesture configuration
- Multi-hand support
- Cross-platform brightness control
- ML-based gesture classification

---

## 🎯 Learning Outcome

This project provided hands-on experience in:

- Real-time computer vision systems
- MediaPipe hand tracking
- Gesture recognition logic
- System automation using Python
- Handling real-time user input safely
