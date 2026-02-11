---

# 🍽️ Waiter’s Tip Prediction using Machine Learning

## 📌 Project Overview

This mini project focuses on predicting the **tip amount given to a waiter** based on various factors such as total bill, customer characteristics, and dining context.
The problem is approached as a **regression task**, where multiple machine learning models are trained and evaluated to determine the best-performing approach.

The project demonstrates the **complete machine learning workflow**, from data exploration to model evaluation.

---

## 📂 Dataset Description

The dataset used in this project contains information about restaurant bills and tips, including:

* **Total Bill** – Total amount of the bill
* **Tip** – Tip given to the waiter (target variable)
* **Sex** – Gender of the customer
* **Smoker** – Whether the customer is a smoker
* **Day** – Day of the week
* **Time** – Lunch or Dinner
* **Size** – Number of people at the table

---

## ⚙️ Technologies & Libraries Used

* **Python**
* **NumPy**
* **Pandas**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **XGBoost**

---

## 🔍 Exploratory Data Analysis (EDA)

The notebook performs detailed EDA to understand:

* Distribution of tips and total bills
* Relationship between tip and categorical variables (sex, smoker, day, time)
* Correlation between numerical features

Various **visualizations** are created using **Matplotlib and Seaborn** to identify trends and patterns affecting tipping behavior.

---

## 🛠️ Data Preprocessing

Key preprocessing steps include:

* Encoding categorical variables using **Label Encoding**
* Feature scaling using **StandardScaler**
* Splitting the dataset into **training and testing sets**

---

## 🤖 Machine Learning Models Used

The following regression models are trained and compared:

1. **Linear Regression**
2. **Random Forest Regressor**
3. **AdaBoost Regressor**
4. **XGBoost Regressor**

Each model is trained on the same dataset to ensure fair comparison.

---

## 📊 Model Evaluation

* **Evaluation Metric Used:**

  * Mean Absolute Error (**MAE**)

* Performance is evaluated on:

  * Training data
  * Validation/Test data

The notebook prints MAE values for each model, allowing direct comparison of prediction accuracy.

---

## 🏆 Results & Conclusion

* Ensemble-based models (such as **Random Forest** and **XGBoost**) outperform simple linear models.
* Feature relationships like **total bill size** and **group size** have a strong impact on tip prediction.
* The project successfully demonstrates how machine learning can be applied to real-world regression problems.

---

## 🚀 How to Run the Project

1. Clone the repository:

   ```bash
   git clone <your-repo-link>
   ```
2. Navigate to the project directory:

   ```bash
   cd waiter-tip-prediction
   ```
3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Open the notebook:

   ```bash
   jupyter notebook Waiter_Tip_Prediction.ipynb
   ```

---

## 📌 Key Learnings

* Hands-on experience with regression models
* Understanding feature impact through EDA
* Comparing multiple ML models using proper evaluation metrics
* End-to-end ML workflow implementation

---

## 📎 Future Improvements

* Hyperparameter tuning for ensemble models
* Feature engineering (tip percentage, bill categories)
* Deployment using Streamlit or Flask

---

