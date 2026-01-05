
---

# 💳 Credit Card Fraud Detection

## 📌 Project Overview

This mini project focuses on detecting **fraudulent credit card transactions** using **Machine Learning**.
The goal is to build a model that can identify suspicious transactions from highly **imbalanced financial data**, helping reduce fraud-related risks.

---

## 🧠 Problem Statement

Credit card fraud datasets are extremely imbalanced, where fraudulent transactions form a very small percentage of the total data.
A naive model may achieve high accuracy but fail to detect fraud effectively. This project addresses this challenge using proper evaluation metrics.

---

## 📂 Dataset Description

* Dataset contains **284,807 transactions**
* **31 features** in total:

  * `Time`, `Amount`
  * `V1` to `V28` (anonymized features from PCA)
  * `Class` (Target: `0 = Legit`, `1 = Fraud`)
* Fraudulent transactions represent **~0.02%** of the data (highly imbalanced)

---

## ⚙️ Project Workflow

1. Import required libraries
2. Load and explore the dataset
3. Analyze class imbalance
4. Compare transaction amounts for fraud vs normal cases
5. Visualize feature correlations using a heatmap
6. Prepare data (feature-target split & train-test split)
7. Train a **Random Forest Classifier**
8. Evaluate model performance using multiple metrics
9. Visualize results with a confusion matrix

---

## 🤖 Machine Learning Model Used

* **Random Forest Classifier**

Chosen because it:

* Handles non-linear relationships well
* Performs effectively on structured/tabular data
* Is robust to noise and feature interactions

---

## 📊 Model Evaluation Metrics

Due to class imbalance, accuracy alone is not sufficient. The following metrics are used:

* **Accuracy**
* **Precision**
* **Recall**
* **F1-Score**
* **Matthews Correlation Coefficient (MCC)**
* **Confusion Matrix (visualized)**

> Special focus is given to **Precision, Recall, and F1-Score**, as they provide more meaningful insights for fraud detection problems.

---

## 🛠️ Tech Stack

* **Python**
* **NumPy**
* **Pandas**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**

---

## 📌 Key Insights

* The dataset is **highly imbalanced**, which strongly affects accuracy
* Fraudulent transactions tend to have **higher average transaction amounts**
* Proper evaluation metrics are crucial for real-world fraud detection systems

---

## 🚀 How to Run the Project

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn
   ```
3. Place `creditcard.csv` in the project directory
4. Run the Jupyter Notebook

---

## 📎 Note

* The dataset file (`creditcard.csv`) is not included due to size and licensing constraints.
* This project is built for **learning and demonstration purposes**.

---
