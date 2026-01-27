
---

# 🚗 Real-Time Car License Plate Detection & Recognition (Video-Based)

## 📌 Overview

This project implements a **real-time car license plate detection and recognition system** using **Computer Vision and Deep Learning**.
Given a **video input**, the system automatically:

* Detects vehicle license plates from each frame
* Extracts and segments individual characters
* Recognizes the license number using a **pre-trained OCR deep learning model**
* Displays the detected plate and prints the recognized number in real time

The project is designed to simulate a **surveillance-based Intelligent Transportation System (ITS)** or **automated security camera system**.

---

## 🎯 Key Features

* ✅ Real-time license plate detection from video
* ✅ Robust contour-based plate localization
* ✅ Adaptive image preprocessing for varying lighting conditions
* ✅ Character segmentation using connected component analysis
* ✅ Deep learning–based OCR for character recognition
* ✅ Modular, clean, and scalable code structure

---

## 🧠 Workflow of the Project

The complete pipeline follows the steps below:

### 🔹 Step 1: Video Frame Capture

* The video is read frame-by-frame using OpenCV.
* Each frame is processed independently for plate detection.

### 🔹 Step 2: Image Preprocessing

For each frame:

* Gaussian Blur → reduces noise
* Grayscale conversion
* Sobel operator → extracts **vertical edges**
* Otsu’s Thresholding → binarization
* Morphological Closing → reveals rectangular plate regions

### 🔹 Step 3: License Plate Detection

* Contours are extracted from the processed image
* Each contour is validated using:

  * Area constraints
  * Aspect ratio checks
  * Orientation constraints
* Valid plate candidates are extracted from the frame

### 🔹 Step 4: Plate Cleaning & Validation

* Adaptive thresholding is applied
* The largest valid contour inside the plate region is selected
* Ensures clean and accurate plate extraction

### 🔹 Step 5: Character Segmentation

* Plate image converted to HSV color space
* Value channel extracted
* Adaptive thresholding applied
* Connected component analysis used to isolate characters
* Convex hulls drawn to refine character regions
* Characters are sorted left-to-right

### 🔹 Step 6: OCR (Optical Character Recognition)

* Each character image is resized and normalized
* Converted into a tensor
* Passed through a **pre-trained TensorFlow OCR model**
* Predicted characters are concatenated to form the license number

### 🔹 Step 7: Output Display

* Original video displayed
* Detected license plate displayed
* Recognized license number printed in the console in real time

---

## 🖼️ Sample Output

### 📥 Input

* Video containing vehicles with visible license plates

### 📤 Output

* Real-time video playback
* Detected license plate displayed in a separate window
* Recognized license number printed in terminal, for example:

```
29A33185
```

> Press **`Q`** to exit the video stream safely.

---
## 📸 Visual Results (Screenshots)

The following screenshots demonstrate the **actual working output** of the system during real-time execution.

### 🎥 Video Frame (Input)
This screenshot shows a frame captured from the input video where the vehicle is detected.

![Video Frame Input](screenshots/video_frame.png)

### 🚘 Detected License Plate (Output)
This screenshot shows the **extracted license plate region** detected by the system and displayed in real time.

![Detected License Plate](screenshots/detected_plate.png)

> 📌 **Note:**  
> The recognized license number corresponding to the detected plate is printed in the terminal during execution.  
> Since GitHub does not support real-time video playback, screenshots are provided to showcase the actual output.

---

## 🗂️ Project Structure

```
license_plate_recognition/
│
├── main.py                 # Main driver code (run this file)
├── plate_finder.py         # License plate detection logic
├── ocr.py                  # OCR model loading and prediction
├── utils.py                # Character segmentation utilities
│
├── model/
│   ├── binary_128_0.50_ver3.pb
│   └── binary_128_0.50_labels_ver2.txt
│
├── test.MOV                # Input video file
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

* **Python**
* **OpenCV**
* **NumPy**
* **Scikit-image**
* **TensorFlow**
* **Imutils**

---

## ⚙️ Installation & Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv license
license\Scripts\activate   # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

```bash
python main.py
```

### Controls:

* Click on the video window
* Press **Q** → Exit the program

---

## 📌 Important Notes

* GitHub **cannot render real-time video output**
* To see full functionality:

  * Clone the repository
  * Run the project locally
* OCR model is pre-trained and may not recognize **all alphabets perfectly**

---

## 🚀 Possible Improvements

* Restrict detection to a fixed Region of Interest (ROI)
* Replace contour-based detection with YOLO or SSD
* Train a custom OCR model for higher accuracy
* Add FPS counter and performance metrics
* Extend support for multiple countries’ plate formats

---

## 🏁 Conclusion

This project demonstrates a **complete real-time computer vision pipeline**, combining:

* Classical image processing
* Geometric validation
* Deep learning–based OCR

It serves as a strong **mini-project / portfolio project** for:

* Computer Vision
* Machine Learning
* Intelligent Surveillance Systems

---

## ⚠️ Note

I have provide you a jupyter notebook **"license_plate_recognition.ipynb"** the project also for understanding the whole working of the project.
