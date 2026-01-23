# Online Payment Fraud Detection using Machine Learning

## 📌 Project Overview

With the rapid growth of digital transactions, **online payment fraud** has become a critical challenge for financial institutions and users alike.
This project focuses on detecting fraudulent online payment transactions using **Machine Learning techniques in Python**.

The goal is to build a reliable classification model that can **distinguish between legitimate and fraudulent transactions** based on transaction patterns and features.

---

## 🚀 Problem Statement

Online transactions are vulnerable to fraud due to anonymity, high transaction volume, and evolving fraud patterns.
Manual detection is inefficient and error-prone, making **machine learning-based fraud detection systems essential**.

**Objective:**
To develop a machine learning model that accurately identifies fraudulent transactions from transaction data.

---

## 📊 Dataset Description

The dataset contains transaction-level information with the following key features:

* **type** – Type of transaction (e.g., CASH_OUT, TRANSFER)
* **amount** – Transaction amount
* **oldbalanceOrg** – Initial balance before transaction
* **newbalanceOrig** – New balance after transaction
* **oldbalanceDest** – Initial destination balance
* **newbalanceDest** – Destination balance after transaction
* **isFraud** – Target variable (1 = Fraud, 0 = Not Fraud)

---

## 🧠 Technologies & Tools Used

* **Python**
* **Pandas** – Data manipulation
* **NumPy** – Numerical operations
* **Matplotlib & Seaborn** – Data visualization
* **Scikit-learn** – Machine Learning models & evaluation

---

## 🔍 Project Workflow

1. **Data Loading & Exploration**

   * Imported dataset and explored its structure
   * Checked for missing values and data distribution

2. **Exploratory Data Analysis (EDA)**

   * Analyzed transaction types and fraud distribution
   * Visualized transaction amounts and balance patterns
   * Identified important features related to fraudulent behavior

3. **Data Preprocessing**

   * Label encoding of categorical variables
   * Feature selection
   * Splitting data into training and testing sets

4. **Model Building**

   * Implemented machine learning classification models
   * Trained the model on historical transaction data

5. **Model Evaluation**

   * Accuracy score
   * Confusion matrix
   * Classification report (Precision, Recall, F1-score)

---

## 📈 Results & Insights

* Fraudulent transactions are **highly imbalanced** compared to legitimate ones
* Certain transaction types (like transfers and cash-outs) show higher fraud probability
* The trained model successfully learns transaction patterns and identifies fraud with good accuracy

---

## ▶️ How to Run the Project

```bash
# Clone the repository
git clone https://github.com/your-username/online-payment-fraud-detection.git

# Navigate to the project directory
cd online-payment-fraud-detection

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook Online_Payment_Fraud_Detection.ipynb
```

---

## 📂 Project Structure

```
├── Online_Payment_Fraud_Detection.ipynb
├── README.md
├── requirements.txt

```

---

## 🔮 Future Improvements

* Handle class imbalance using **SMOTE or undersampling**
* Try advanced models like **Random Forest, XGBoost, or LightGBM**
* Hyperparameter tuning for better performance
* Deploy as a **real-time fraud detection API**
* Add explainability using **SHAP or LIME**

---

## 📌 Conclusion

This project demonstrates how **machine learning can be effectively applied to real-world financial fraud detection problems**.
It highlights data preprocessing, exploratory analysis, and model evaluation — making it a strong **beginner-to-intermediate ML portfolio project**.

---

⭐ *If you found this project useful, consider starring the repository!*
