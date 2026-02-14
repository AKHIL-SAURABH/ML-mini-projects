
---

# 📊 Loan Approval Prediction using Machine Learning

This project focuses on predicting whether a loan application will be approved or rejected based on applicant details using Machine Learning classification models.

Financial institutions receive thousands of loan applications and evaluating them manually is time-consuming. This project demonstrates how machine learning can help automate loan approval decisions by learning patterns from historical data.

---

## 🎯 Objective

To build a machine learning model that predicts **loan approval status** using applicant financial and demographic information.

---

## 📁 Dataset

The dataset contains multiple applicant-related features used to determine loan eligibility.

### Key Features Include:

* Gender
* Marital Status
* Education
* Applicant Income
* Coapplicant Income
* Loan Amount
* Loan Term
* Credit History
* Property Area
* Loan Status (Target Variable)

---

## 🛠 Technologies Used

* Python
* Pandas → Data handling
* NumPy → Numerical operations
* Matplotlib & Seaborn → Data visualization
* Scikit-learn → Machine learning models

---

## 🔍 Project Workflow

### 1️⃣ Data Loading

* Dataset imported using Pandas.
* Initial inspection performed using `.head()`.

---

### 2️⃣ Data Preprocessing

* Removed irrelevant column: `Loan_ID`
* Identified categorical features.
* Applied **Label Encoding** to convert categorical values into numeric format.
* Filled missing values using mean imputation.

---

### 3️⃣ Exploratory Data Analysis (EDA)

* Bar plots used to visualize categorical distributions.
* Correlation heatmap used to analyze relationships between features.
* Observed:

  * Credit history strongly influences loan approval.
  * Loan amount and applicant income show correlation patterns.

---

### 4️⃣ Feature Engineering & Splitting

* Features and target separated.
* Dataset split into training and testing sets (60% train, 40% test).

---

### 5️⃣ Model Training

The following classification models were trained:

* K-Nearest Neighbors (KNN)
* Random Forest Classifier
* Support Vector Classifier (SVC)
* Logistic Regression

---

### 6️⃣ Model Evaluation

Performance measured using **Accuracy Score**.

| Model               | Accuracy  |
| ------------------- | --------- |
| Random Forest       | ~82%      |
| KNN                 | Evaluated |
| SVC                 | Evaluated |
| Logistic Regression | Evaluated |

✅ **Random Forest performed best** on the test dataset.

---

## 📈 Results & Insights

* Credit history is the most influential feature.
* Random Forest achieved the highest prediction accuracy.
* Ensemble methods significantly improve classification performance.
* Further improvements possible using:

  * Hyperparameter tuning
  * Boosting methods
  * Cross-validation
  * Feature scaling

---

## 🚀 How to Run the Project

```bash
# Clone repository
git clone <repo-link>

# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

# Run notebook
jupyter notebook Loan_Approval_Prediction.ipynb
```

---

## 📌 Future Improvements

* Hyperparameter optimization
* Model deployment using Flask or FastAPI
* Web interface for loan prediction
* Feature importance visualization
* Handling class imbalance

---

## 🎓 Learning Outcomes

Through this project, you will learn:

✔ Data preprocessing techniques
✔ Label encoding for categorical data
✔ Correlation analysis using heatmaps
✔ Training multiple classification models
✔ Model comparison and evaluation

---

## 📜 Conclusion

Machine learning can significantly simplify the loan approval process by analyzing applicant data and predicting approval probability. The Random Forest classifier showed the best performance in this study, demonstrating the effectiveness of ensemble learning for financial decision systems.
