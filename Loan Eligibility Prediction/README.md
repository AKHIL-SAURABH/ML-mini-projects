
---

# 🏦 Loan Eligibility Prediction using Machine Learning

This project builds a **Machine Learning classification model** that predicts whether a loan application will be approved or rejected based on applicant details such as income, marital status, gender, loan amount, and other financial attributes.

The goal is to simulate how financial institutions evaluate loan applications using data-driven decision making.

---

## 📌 Project Objective

To develop a predictive model that can:

✔ Analyze applicant financial and demographic information
✔ Identify patterns affecting loan approval
✔ Handle imbalanced datasets
✔ Predict loan eligibility using supervised learning

---

## 📊 Dataset Information

The dataset contains applicant-related attributes such as:

* Gender
* Marital Status
* Applicant Income
* Loan Amount
* Other financial and personal features
* Loan Status (Target Variable)

The target variable indicates whether the loan is:

* Approved
* Not Approved

---

## ⚙️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Imbalanced-learn

---

## 🔬 Project Workflow

### 1️⃣ Data Loading

* Dataset imported using Pandas
* Shape, info, and statistical summary explored

---

### 2️⃣ Exploratory Data Analysis (EDA)

Performed visual analysis to understand patterns:

* Loan approval distribution (pie chart)
* Relationship between categorical features and loan status
* Income and loan amount distributions
* Outlier detection using boxplots
* Group-based statistical analysis

Key observations:

* Dataset was imbalanced
* Loan amount varies by gender and marital status
* Outliers present in income and loan amount

---

### 3️⃣ Data Cleaning & Preprocessing

* Removed extreme outliers
* Label encoded categorical variables
* Split data into training and validation sets
* Balanced dataset using **Random OverSampling**
* Feature normalization using **StandardScaler**

---

### 4️⃣ Model Development

Model used:

👉 Support Vector Classifier (SVC) with RBF kernel

The model was trained on normalized and balanced data.

---

### 5️⃣ Model Evaluation

Evaluation metrics used:

* ROC AUC Score
* Confusion Matrix
* Classification Report

Visualization:

* Heatmap of confusion matrix

---

## 📈 Model Performance

The model achieved moderate predictive performance.
Due to limited features and dataset size, accuracy is not optimal.

Future improvements can significantly enhance performance.

---

## 🚀 How to Run the Project

### Step 1 — Clone the repository

```bash
git clone https://github.com/yourusername/loan-eligibility-prediction.git
cd loan-eligibility-prediction
```

### Step 2 — Install dependencies

```bash
pip install numpy pandas matplotlib seaborn scikit-learn imbalanced-learn
```

### Step 3 — Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```
Loan_Eligibility_Prediction.ipynb
```

---

## 📉 Limitations

* Small dataset
* Limited features
* Basic feature engineering
* Single model used
* No hyperparameter tuning

---

## 🔮 Future Improvements

✔ Use larger real-world dataset
✔ Apply advanced models (Random Forest, XGBoost, Neural Networks)
✔ Hyperparameter optimization
✔ Feature engineering
✔ Model deployment (Flask / FastAPI)
✔ Web interface for predictions

---

## 🎯 Learning Outcomes

This project demonstrates:

* End-to-end ML workflow
* Handling imbalanced data
* Data preprocessing techniques
* Model training and evaluation
* Visualization for analysis

---

