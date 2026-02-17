
---

# 📊 Customer Churn Analysis & 

## 📌 Project Overview

Customer churn occurs when customers stop using a company’s services. Predicting churn is crucial for businesses to retain customers and reduce revenue loss.

In this project, we analyze the **Telco Customer Churn dataset** and build machine learning models to predict whether a customer is likely to churn based on their demographic details, service usage, and account information.

This project covers the **complete data science pipeline** — from data understanding and preprocessing to model training and evaluation.

---

## 🧠 Objectives

* Understand customer behavior patterns leading to churn
* Perform exploratory data analysis (EDA)
* Preprocess and clean real-world customer data
* Build machine learning models to predict churn
* Evaluate and compare model performance

---

## 📂 Dataset Information

* Dataset: **Telco Customer Churn**
* Each row represents a customer
* Target variable: **Churn** (Yes / No)
* Features include:

  * Customer demographics
  * Service subscriptions
  * Contract details
  * Payment methods
  * Monthly and total charges

---

## 🛠️ Technologies & Libraries Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🔍 Project Workflow

### 1️⃣ Data Loading

* Imported required libraries
* Loaded the dataset into a Pandas DataFrame
* Inspected dataset shape, columns, and data types

---

### 2️⃣ Exploratory Data Analysis (EDA)

* Checked for missing and inconsistent values
* Analyzed churn distribution
* Explored relationships between churn and:

  * Contract type
  * Payment method
  * Internet services
  * Monthly charges
* Visualized insights using plots and charts

---

### 3️⃣ Data Preprocessing

* Handled missing and invalid values
* Converted categorical features using encoding techniques
* Scaled numerical features where required
* Split data into **training and testing sets**

---

### 4️⃣ Model Building

The following machine learning models were trained to predict customer churn:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

---

### 5️⃣ Model Evaluation

Models were evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report

Model performance was compared to identify the most effective churn prediction approach.

---

## 📈 Results & Insights

* Customers with **month-to-month contracts** show higher churn rates
* Higher **monthly charges** increase churn probability
* Long-term contracts significantly reduce churn
* Ensemble models (Random Forest) performed better than basic models

---

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/customer-churn-analysis.git
```

2. Navigate to the project directory:

```bash
cd customer-churn-analysis
```

3. Open the notebook:

```bash
jupyter notebook Customer_Churn_Analysis.ipynb
```

4. Run all cells sequentially

---

## 📌 Future Improvements

* Hyperparameter tuning for better accuracy
* Try advanced models like XGBoost or LightGBM
* Deploy the model using Streamlit or Flask
* Perform feature importance analysis

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.
Feel free to fork the repository and submit a pull request.

---

## 📬 Contact

**Akhil Saurabh**
If you have questions or suggestions, feel free to connect on LinkedIn or GitHub.

---

