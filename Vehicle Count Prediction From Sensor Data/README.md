
---

# 🚗 Vehicle Count Prediction From Sensor Data

## 📌 Project Overview

This mini project focuses on predicting the **number of vehicles at road junctions** using historical sensor data. Sensors installed at traffic junctions collect vehicle count data at different timestamps.
Using this data, a **machine learning regression model** is trained to predict vehicle counts for a given time.

The project demonstrates a **complete ML workflow** — from data preprocessing to model training and prediction.

---

## 🎯 Objective

* Analyze vehicle count data collected from traffic sensors
* Apply a **regression-based machine learning approach**
* Predict the number of vehicles at a given timestamp

---

## 📂 Dataset Description

The dataset contains the following key attributes:

* **Datetime** – Timestamp indicating when the sensor data was collected
* **Vehicles** – Number of vehicles recorded at that timestamp

Since the target variable (**Vehicles**) is numerical, this problem is treated as a **regression task**.

---

## ⚙️ Methodology

### 1️⃣ Data Preprocessing

* Converted the `Datetime` column into a proper datetime format
* Extracted useful time-based features such as:

  * Hour
  * Day
  * Month
* Prepared feature variables (`X`) and target variable (`y`)

---

### 2️⃣ Train-Test Split

* Split the dataset into training and testing sets
* Ensured the model is evaluated on unseen data

---

### 3️⃣ Model Selection

* Used **Random Forest Regressor**
* Reason:

  * Handles non-linear patterns effectively
  * Reduces overfitting by averaging multiple decision trees
  * Performs well on tabular data

---

### 4️⃣ Model Training

* Trained the `RandomForestRegressor` using extracted time features
* Learned the relationship between time-based patterns and vehicle count

---

### 5️⃣ Prediction

* Provided a sample datetime input
* The trained model predicted the **approximate number of vehicles** for that timestamp
* Example output:

  * **Predicted Vehicle Count ≈ 9.61 vehicles**

---

## 🧠 Machine Learning Algorithm Used

* **Random Forest Regressor**

  * Ensemble learning technique
  * Improves accuracy by combining multiple decision trees
  * Robust to noise and overfitting

---

## 🛠️ Technologies & Libraries

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook

---

## 📊 Results & Observations

* The model successfully learned temporal patterns in traffic data
* Predictions are reasonable for given timestamps
* Demonstrates how **sensor data + ML** can help in traffic analysis and planning

---

## 📌 Key Learnings

* Feature extraction from datetime data is crucial
* Random Forest performs well for regression on structured datasets
* End-to-end ML pipeline implementation using real-world inspired data

---

## 🚀 Future Improvements

* Use larger and more diverse traffic datasets
* Add visualization for traffic trends
* Experiment with other regression models (XGBoost, Gradient Boosting)
* Evaluate performance using metrics like RMSE and R² score

---

## 📁 Project Type

**Mini Machine Learning Project**

---

