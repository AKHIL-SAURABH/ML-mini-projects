
---

# 👤 Real-Time Face Counting Using MediaPipe (Webcam)

## 📌 Project Overview

This project implements **real-time face detection and counting** using a webcam feed.
It uses **MediaPipe Tasks Vision API** with a **BlazeFace model** to detect human faces in live video frames and display the total number of detected faces on screen.

The application processes each video frame in real time, draws bounding boxes around detected faces, and continuously updates the face count.

---

## 🎯 What This Project Does

✔ Captures live video from the system webcam
✔ Detects human faces in each frame
✔ Draws bounding boxes around detected faces
✔ Counts the number of faces per frame
✔ Displays the face count in real time
✔ Runs entirely on the local machine (no internet required after setup)

---

## ❌ What This Project Does NOT Do

* No face recognition or identity matching
* No face landmark detection
* No emotion, age, or gender analysis
* No image or video file input (webcam only)
* No data storage or logging

---

## 🛠️ Technologies Used

* **Python**
* **OpenCV** – for webcam access and image processing
* **MediaPipe Tasks Vision API** – for face detection
* **BlazeFace (Short-Range) Model** – lightweight face detection model

---

## 🧠 How It Works (High-Level)

1. The webcam captures live video frames.
2. Each frame is converted from BGR to RGB format.
3. The frame is passed to MediaPipe’s Face Detector along with a timestamp.
4. The BlazeFace model detects faces in the frame.
5. Bounding boxes are drawn around detected faces.
6. The total face count is displayed on the video feed.
7. The process repeats until the user exits the application.

---

## 📁 Project Structure

```
Count number of Faces/
│
├── faces.py
├── models/
│   └── blaze_face_short_range.tflite
├── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create a Virtual Environment

```powershell
python -m venv face_env
face_env\Scripts\Activate
```

---

### 2️⃣ Install Required Libraries

```powershell
pip install numpy==1.26.4
pip install opencv-python
pip install mediapipe==0.10.32
pip install protobuf==3.20.3
```

---

### 3️⃣ Download Face Detection Model

Download the BlazeFace short-range model from:

```
https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite
```

Place it in:

```
models/blaze_face_short_range.tflite
```

---

## ▶️ How to Run

```powershell
python faces.py
```

* Press **`q`** to exit the application.

---

## 📊 Output

* A live webcam window opens.
* Green rectangles appear around detected faces.
* The number of detected faces is shown in real time.

---

## 🚀 Future Improvements (Optional)

* Add FPS (frames-per-second) display
* Extend to video file input
* Integrate face tracking for improved performance
* Upgrade to a deep learning–based detector like YOLOv8

---

## 👨‍💻 Author

**Akhil Saurabh**
Computer Science Undergraduate
Focus Areas: Data Science, Machine Learning, Applied AI

---

## 📝 License

This project is intended for educational and learning purposes.

---



