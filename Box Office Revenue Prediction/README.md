
---

# 🎬 Box Office Revenue Prediction Using Machine Learning

This project focuses on predicting **movie box office revenue** using machine learning techniques. By analyzing various movie-related features and applying appropriate preprocessing, feature encoding, and regression modeling, the project aims to estimate expected revenue for movies before release.

The notebook demonstrates a **complete ML pipeline**, starting from data loading and preprocessing to model training and evaluation.

---

## 📂 Project Structure

```
📁 Box-Office-Revenue-Prediction
│
├── Box_Office_Revenue_Prediction.ipynb
├── boxoffice.csv
└── README.md
```

---

## 🎯 Project Objective

The primary goals of this project are:

* Understand and preprocess real-world movie dataset
* Encode categorical and text-based features effectively
* Train a regression model to predict box office revenue
* Evaluate model performance using appropriate metrics
* Analyze overfitting and generalization behavior

---

## 🛠️ Technologies & Libraries Used

### Core Libraries

* **Python**
* **NumPy**
* **Pandas**

### Visualization

* **Matplotlib**
* **Seaborn**

### Machine Learning

* **Scikit-learn**
* **XGBoost**

---

## 📊 Dataset Description

* Dataset is loaded from `boxoffice.csv`
* Encoding used: `latin-1`
* Contains both **numerical** and **categorical/text-based** features related to movies
* Target variable: **Box Office Revenue**

---

## ⚙️ Workflow & Methodology

### 1️⃣ Data Loading

* Dataset loaded using Pandas
* Initial inspection using `.head()` and `.shape()`

---

### 2️⃣ Data Preprocessing

#### Handling Categorical Data

* **Label Encoding** is applied to categorical features

#### Handling Text Data

* **CountVectorizer** is used to convert text-based features into numerical format

#### Feature Scaling

* **StandardScaler** is applied to normalize feature values
* Scaling is done **after train-validation split** to prevent data leakage

---

### 3️⃣ Train–Validation Split

* Dataset split into:

  * **Training set**
  * **Validation set**
* Ensures proper evaluation of model generalization

---

### 4️⃣ Model Training

* **XGBRegressor** is used as the regression model
* Model is trained using normalized training data
* Chosen for its ability to handle non-linear relationships and complex feature interactions

---

### 5️⃣ Model Evaluation

#### Metric Used

* **Mean Absolute Error (MAE)**

#### Evaluation Results

* Training MAE ≈ **0.21**
* Validation MAE ≈ **0.63**

#### Interpretation:

* Low training error indicates strong learning
* Higher validation error suggests **mild overfitting**
* Model performs well but could benefit from:

  * Feature selection
  * Regularization
  * Hyperparameter tuning

---

## 📈 Key Observations

* End-to-end ML pipeline implemented correctly
* Proper separation of training and validation data
* Feature scaling and encoding handled appropriately
* Model evaluation highlights real-world generalization challenges
* Notebook is well-structured and beginner-friendly

---

## 🚀 How to Run the Project

1. Clone the repository
2. Ensure required libraries are installed:

   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn xgboost
   ```
3. Place `boxoffice.csv` in the same directory
4. Open and run `Box_Office_Revenue_Prediction.ipynb`

---

## 🔮 Future Improvements

* Hyperparameter tuning for XGBoost
* Feature importance analysis
* Trying additional regression models
* Cross-validation for more robust evaluation
* Revenue prediction category-wise (budget tiers)

---
