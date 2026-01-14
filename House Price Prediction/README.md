
---

# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

House price prediction is a common and important problem in the real estate domain.
In this mini project, we build and compare multiple **machine learning regression models** to predict house prices based on various housing features.

The notebook walks through the **complete ML pipeline**, including:

* Data loading
* Data preprocessing
* Exploratory Data Analysis (EDA)
* Model training
* Model evaluation and comparison

---

## 📊 Dataset Description

The dataset used in this project contains **13 features** related to house properties, including numerical and categorical attributes.

Key characteristics:

* Mix of **numerical** and **categorical** variables
* Target variable: **House Price**
* Dataset is suitable for regression-based prediction models

---

## 🛠️ Technologies & Libraries Used

* **Python**
* **Pandas** – data handling and preprocessing
* **NumPy** – numerical operations
* **Matplotlib** – static data visualization
* **Seaborn** – correlation analysis and EDA
* **Scikit-learn** – model building and evaluation

---

## 🔄 Project Workflow

### 1️⃣ Importing Libraries & Dataset

* Required libraries are imported
* Dataset is loaded into a Pandas DataFrame
* Dataset shape and structure are examined

---

### 2️⃣ Data Preprocessing

* Features are categorized based on data types
* Numerical and categorical variables are identified
* Missing values and data consistency are checked
* Data is prepared for model training

---

### 3️⃣ Exploratory Data Analysis (EDA)

EDA is performed to understand:

* Feature distributions
* Relationships between variables
* Categorical feature impact on house prices

📌 Visualizations include:

* Bar plots for categorical features
* Correlation heatmaps
* Distribution plots

📷 **EDA plots are saved as PNG images and included in the notebook output.**

---

### 4️⃣ Machine Learning Models Implemented

The following regression models are trained and evaluated:

* **Support Vector Machine (SVM) Regressor**
* **Random Forest Regressor**
* **Linear Regression**

Each model is trained using the same dataset to ensure fair comparison.

---

### 5️⃣ Model Evaluation

Models are evaluated using **Mean Absolute Error (MAE)**:

[
MAE = \frac{1}{n} \sum |y_{true} - y_{pred}|
]

📌 Lower MAE indicates better prediction accuracy.

---

## 📈 Results & Observations

* Among all tested models, **Support Vector Machine (SVM)** achieved the **lowest Mean Absolute Error**
* **SVM outperformed Random Forest and Linear Regression** in this dataset
* Linear Regression showed comparatively higher error
* Ensemble methods show promise for further accuracy improvements

---

## ▶️ How to Run the Project Locally

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd House-Price-Prediction
```

3. Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

4. Run the notebook:

```bash
jupyter notebook House_Price_Prediction.ipynb
```

---

## 📌 Project Type

* **Mini Machine Learning Project**
* Focused on **regression, EDA, and model comparison**
* Suitable for ML beginners and portfolio projects

---

## 🚀 Future Improvements

* Hyperparameter tuning
* Feature engineering
* Advanced ensemble models
* Cross-validation
* Deployment using Flask or FastAPI

---

## ✨ Conclusion

This project demonstrates a **complete end-to-end machine learning workflow** for house price prediction, with strong emphasis on **data understanding, visualization, and model evaluation**.
It serves as a solid foundation for more advanced regression-based ML projects.

---

