
---

# 🔍 Object Counting Using Python & OpenCV

## 📌 Overview

This mini project demonstrates how to **count the number of objects in an image** using **Python and OpenCV**.
The approach is based on **image preprocessing, edge detection, morphological operations, and contour detection** to accurately identify and count objects present in an image.

The project is beginner-friendly and serves as a strong introduction to **computer vision fundamentals** using OpenCV.

---

## 🧠 Key Concepts Used

* Image Reading & Color Space Conversion
* Grayscale Processing
* Gaussian Blurring
* Edge Detection (Canny)
* Morphological Operations (Dilation)
* Contour Detection
* Object Counting

---

## 🛠️ Tech Stack & Libraries

* **Python**
* **OpenCV (cv2)** – Image processing & computer vision
* **NumPy** – Numerical operations
* **Matplotlib** – Visualization

---

## 📂 Project Structure

```
├── objects.ipynb        # Jupyter Notebook with complete implementation
└── README.md            # Project documentation
```

---

## ⚙️ Step-by-Step Implementation

### **Step 1: Import Required Libraries**

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
```

---

### **Step 2: Read & Convert Image to Grayscale**

* Image is read using `cv2.imread()`
* Converted from **BGR → Grayscale** for better processing

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

---

### **Step 3: Noise Reduction using Gaussian Blur**

Gaussian blur smooths the image and reduces noise before edge detection.

```python
blur = cv2.GaussianBlur(gray, (5, 5), 0)
```

---

### **Step 4: Edge Detection using Canny Algorithm**

Detects object boundaries efficiently.

```python
canny = cv2.Canny(blur, 30, 150, 3)
```

---

### **Step 5: Morphological Dilation**

* Thickens and connects broken edges
* Helps in accurate contour detection

```python
dilated = cv2.dilate(canny, (1, 1), iterations=0)
```

---

### **Step 6: Contour Detection & Visualization**

* Contours are extracted from the processed image
* Drawn over the original image for visualization

```python
(cnt, hierarchy) = cv2.findContours(
    dilated.copy(),
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
```

---

### **Step 7: Object Counting**

The total number of detected contours represents the number of objects.

```python
print("Objects in the image:", len(cnt))
```

---

## 📊 Output

* Displays intermediate image transformations
* Final image with detected contours
* Prints the **total object count**

---

## 🚀 Applications

* Coin counting systems
* Industrial object inspection
* Inventory analysis
* Basic computer vision pipelines
* Academic & learning projects

---

## 🔮 Future Improvements

* Filter small/noise contours using area threshold
* Apply adaptive thresholding
* Improve accuracy for overlapping objects
* Convert to real-time webcam-based object counter

---

## 📎 Conclusion

This project provides a **practical foundation in computer vision**, showing how classical image processing techniques can be combined to solve real-world problems like object counting.

It’s an excellent starting point for more advanced topics such as **object detection, tracking, and deep learning-based vision models**.

---
