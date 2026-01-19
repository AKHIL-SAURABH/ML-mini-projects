
---

# 🔥 Calories Burnt Prediction using Machine Learning

## 📌 Project Overview

This project focuses on predicting the **number of calories burnt during a workout** using machine learning techniques.
The prediction is based on **biological and workout-related attributes**, helping estimate energy expenditure more accurately.

The notebook demonstrates the **complete end-to-end ML workflow**, including data analysis, preprocessing, model training, evaluation, and comparison of multiple regression models.

---

## 🎯 Objective

To build and evaluate machine learning models that can **accurately predict calories burnt** during physical activity using given input features.

---

## 🧠 Machine Learning Approach

This is a **supervised regression problem**, where:

* **Input** → Biological and activity-related features
* **Output** → Calories burnt

Multiple regression models are trained and compared to identify the **best-performing model**.

---

## 📂 Dataset

* The dataset is loaded from `calories.csv`
* Contains numerical features related to physical and workout attributes
* Target variable: **Calories Burnt**

---

## 🔍 Exploratory Data Analysis (EDA)

EDA is performed to:

* Understand feature distributions
* Identify correlations between variables
* Detect patterns and trends in the data

### Techniques used:

* Histograms
* Heatmaps
* Pair plots
* Feature correlation analysis

📊 **Matplotlib** and **Seaborn** are used for data visualization.

---

## 🧹 Data Preprocessing

The following preprocessing steps are applied:

* Feature–target separation
* Train–validation split
* Feature scaling using **StandardScaler**
* Data normalization to ensure stable and faster training

---

## 🤖 Models Trained

The following regression models are implemented and compared:

* **Linear Regression**
* **Lasso Regression**
* **Ridge Regression**
* **Random Forest Regressor**
* **XGBoost Regressor**

Each model is trained on the same dataset to ensure fair comparison.

---

## 📏 Evaluation Metric

Model performance is evaluated using:

* **Mean Absolute Error (MAE)**

  * Calculated for both training and validation data

This helps measure how close predictions are to actual calorie values.

---

## 🏆 Results & Model Selection

After comparing all models:

* **Random Forest Regressor** achieved the **best performance**
* It showed the **lowest validation MAE**
* Provided more stable and accurate predictions compared to linear and boosting models

✅ **Final Selected Model:** Random Forest Regressor

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries Used:**

  * NumPy
  * Pandas
  * Matplotlib
  * Seaborn
  * Scikit-learn
  * XGBoost

---

## 🚀 How to Run the Project

1. Clone this repository

   ```bash
   git clone <your-repo-link>
   ```
2. Install required dependencies

   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn xgboost
   ```
3. Run the Jupyter Notebook

   ```bash
   jupyter notebook Calories_Burnt_Prediction.ipynb
   ```

---

## 📌 Key Learnings

* End-to-end ML regression pipeline
* Importance of data normalization
* Model comparison using validation error
* Random Forest’s effectiveness on structured data

---

## 🔮 Future Improvements

* Hyperparameter tuning for Random Forest and XGBoost
* Cross-validation for more robust evaluation
* Deployment using Streamlit or Flask
* Real-time calorie prediction system

---

