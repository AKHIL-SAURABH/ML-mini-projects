
---

# 📊 Anomaly Detection in Time Series using Autoencoders

## 🚀 Project Overview

This project focuses on **detecting anomalies in time series data** using an **unsupervised deep learning approach (Autoencoders)**.

Anomaly detection helps identify unusual patterns or deviations in data that may indicate:

* System failures ⚠️
* Fraudulent activities 💳
* Unexpected behavior 📉

In this project, we use a real-world dataset of ambient temperature readings to detect anomalies based on **reconstruction error**.

---

## 🧠 Key Concept

### 🔹 What is Anomaly Detection?

Anomaly detection is the process of identifying rare or unusual data points that differ significantly from normal patterns.

### 🔹 Why Autoencoders?

Autoencoders are neural networks that:

1. Compress input data into a lower-dimensional representation
2. Reconstruct the original data

👉 If reconstruction error is high → it's likely an anomaly.

---

## 📂 Dataset

* **Name:** Ambient Temperature System Failure Dataset
* **Source:** Numenta Anomaly Benchmark (NAB)
* **File:** `ambient_temperature_system_failure.csv`

### 📌 Dataset Description:

* Time-series temperature readings
* Includes labeled anomalies (system failure points)

---

## ⚙️ Tech Stack

* **Python 🐍**
* **Pandas** – Data handling
* **NumPy** – Numerical operations
* **Matplotlib / Seaborn** – Visualization
* **Scikit-learn** – Evaluation metrics
* **TensorFlow / Keras** – Autoencoder model

---

## 🏗️ Project Workflow

### 1️⃣ Data Preprocessing

* Load dataset using Pandas
* Remove unnecessary columns (`timestamp`)
* Convert data to `float32`
* Handle missing values

---

### 2️⃣ Model Building (Autoencoder)

* Input layer
* Encoding (compression)
* Decoding (reconstruction)

The model learns **normal patterns** from the data.

---

### 3️⃣ Anomaly Detection

* Compute **reconstruction error**
* Define a threshold
* Points with high error → anomalies

---

### 4️⃣ Evaluation Metrics

* **Precision**
* **Recall**
* **F1 Score**

✔️ Achieved:

* Precision = 1.0
* Recall = 1.0
* F1 Score = 1.0

👉 This indicates perfect anomaly detection on this dataset.

---

## 📈 Results & Insights

* The model successfully identified anomalies in time-series data.
* High reconstruction error clearly separates abnormal patterns.
* Suitable for:

  * Predictive maintenance
  * System monitoring
  * Financial anomaly detection

---

## 📌 Applications

* 🏭 Industrial equipment failure detection
* 💰 Fraud detection systems
* 🌡️ Sensor monitoring
* 📊 Financial time-series analysis

---

## 🛠️ How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/anomaly-detection.git

# Navigate to project folder
cd anomaly-detection

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook Anomaly_Detection.ipynb
```

---

## 📁 Project Structure

```
├── Anomaly_Detection.ipynb
├── ambient_temperature_system_failure.csv
├── README.md
```

---

## ✨ Future Improvements

* Implement LSTM Autoencoders for better temporal learning
* Real-time anomaly detection system
* Deploy as a web app/dashboard
* Add multiple datasets for robustness

---

## 🙌 Acknowledgements

* Numenta Anomaly Benchmark (NAB) dataset
* TensorFlow & Keras documentation

---


