
---

# 📈 Stock Price Direction Prediction using Support Vector Machines (SVM)

## 📌 Project Overview

Predicting the **direction of stock prices** (whether the price will go **up or down**) is a fundamental problem in financial analytics.
This project implements a **machine learning–based classification approach** using **Support Vector Machines (SVM)** to predict stock price movement based on historical market data.

The goal is **not price prediction**, but **direction prediction**, which is more practical and realistic in real-world trading and analytics systems.

---

## 🎯 Problem Statement

Given historical stock market data, can we predict whether the **next day’s stock price will increase or decrease**?

This is formulated as a **binary classification problem**:

* **1 → Price goes up**
* **0 → Price goes down**

---

## 📊 Dataset

* Stock market historical data downloaded from **Yahoo Finance**
* Typical features include:

  * Open price
  * High price
  * Low price
  * Close price
  * Volume
* Date column is used as an index and removed from feature set during modeling.

---

## 🛠️ Tech Stack & Tools

* **Programming Language:** Python
* **Libraries Used:**

  * NumPy
  * Pandas
  * Matplotlib
  * Scikit-learn
* **Algorithm:** Support Vector Machine (SVM)
* **Environment:** Jupyter Notebook

---

## ⚙️ Project Workflow

### 1️⃣ Data Loading

* Historical stock data is read into a Pandas DataFrame.
* The date column is set as the index for time-series consistency.

---

### 2️⃣ Data Preprocessing

* Removal of unnecessary columns.
* Creation of a **target variable** indicating stock price direction.
* Feature selection based on historical price values.

---

### 3️⃣ Feature Engineering

* Explanatory variables (features) are separated from the target variable.
* Dataset is prepared for supervised learning.

---

### 4️⃣ Train–Test Split

* The dataset is split into:

  * **Training data**
  * **Testing data**
* Ensures proper evaluation of model performance.

---

### 5️⃣ Model Building

* A **Support Vector Machine (SVM)** classifier is used.
* SVM is chosen due to its effectiveness in:

  * Binary classification
  * High-dimensional data
  * Financial pattern recognition

---

### 6️⃣ Model Evaluation

* Predictions are made on the test dataset.
* Model performance is evaluated using:

  * Accuracy score
  * Classification results

---

## 📈 Results & Insights

* The SVM model successfully classifies stock price direction based on historical features.
* Demonstrates how **machine learning can support financial decision-making**.
* Highlights the importance of **direction-based prediction** over raw price forecasting.

---

## 🚀 Key Takeaways

* Stock market problems are better framed as **classification tasks** rather than exact price prediction.
* Support Vector Machines are effective for **directional market analysis**.
* Proper data preprocessing is critical in financial ML projects.

---

## 🔮 Future Improvements

* Add technical indicators (RSI, MACD, Moving Averages)
* Experiment with other models (Logistic Regression, Random Forest, XGBoost)
* Perform hyperparameter tuning
* Add cross-validation
* Integrate risk metrics and trading strategy evaluation

---

## 📂 Repository Structure

```
📦 Stock-Price-Direction-Prediction
 ┣ 📜 Stock_Price_Direction.ipynb
 ┣ 📜 README.md
```

---

