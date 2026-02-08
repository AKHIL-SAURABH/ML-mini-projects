---

# 🍷 Wine Quality Prediction using Machine Learning

## 📌 Project Overview

Wine Quality Prediction is a **machine learning classification project** that aims to predict the **quality of wine** based on its **physicochemical properties** such as acidity, alcohol content, pH level, sulphates, and more.

The project demonstrates a **complete ML workflow** — from data analysis and preprocessing to training multiple models and evaluating their performance.

---

## 🎯 Problem Statement

Wine quality assessment is traditionally done by human experts, which can be **time-consuming and subjective**.
This project leverages **machine learning algorithms** to automatically predict wine quality, helping wineries and distributors **maintain consistent quality standards**.

---

## 🧠 Machine Learning Approach

* Supervised Learning (Classification)
* Binary classification of wine quality:

  * **Good Quality**
  * **Bad Quality**

---

## 📂 Dataset Information

* **Source**: Wine Quality Dataset
* **File Used**: `winequalityN.csv`
* **Target Column**: `quality`
* **Features** include:

  * Fixed acidity
  * Volatile acidity
  * Citric acid
  * Residual sugar
  * Chlorides
  * Free sulfur dioxide
  * Total sulfur dioxide
  * Density
  * pH
  * Sulphates
  * Alcohol

---

## 🔍 Exploratory Data Analysis (EDA)

* Dataset structure and data types inspection
* Statistical summary using `describe()`
* Handling missing values
* Visualization of:

  * Feature distributions
  * Correlation heatmap
  * Feature importance insights

---

## ⚙️ Data Preprocessing

* Handling missing values
* Label encoding of wine quality
* Feature scaling using **StandardScaler**
* Train-test split for model evaluation

---

## 🤖 Machine Learning Models Used

The following models were trained and evaluated:

* Logistic Regression
* Support Vector Classifier (SVC)
* Random Forest Classifier
* XGBoost Classifier

Each model was compared based on **accuracy and classification performance**.

---

## 📊 Model Evaluation

* Accuracy Score
* Confusion Matrix
* Classification Report
* Comparison of model performances

📌 **Best performing model** was selected based on accuracy and generalization ability.

---

## 🛠️ Tech Stack & Tools

### 🧪 Machine Learning & Data Science

* Python
* NumPy
* Pandas
* Scikit-learn
* XGBoost

### 📊 Data Visualization

* Matplotlib
* Seaborn

### 🧰 Development Tools

* Jupyter Notebook

---

## 🚀 How to Run This Project Locally

```bash
# Clone the repository
git clone https://github.com/your-username/wine-quality-prediction.git

# Navigate to the project directory
cd wine-quality-prediction

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook Wine_Quality_Prediction.ipynb
```

⚠️ **Note**: The trained model file is not uploaded.
You can retrain the model by running the notebook cells sequentially.

---

## 📈 Results & Insights

* Certain chemical properties like **alcohol content and sulphates** play a major role in determining wine quality.
* Ensemble models performed better than linear models.
* Feature scaling significantly improved model performance.

---

## 🏷️ Project Type

✅ **Machine Learning Mini Project**
✅ **Classification Problem**
✅ **Beginner–Intermediate Level**

---

## 📌 Future Improvements

* Hyperparameter tuning
* Multiclass classification
* Model deployment using Flask / FastAPI
* Web interface for user input

---

## ⭐ Key Takeaways

* Hands-on experience with real-world dataset
* End-to-end ML pipeline implementation
* Model comparison and evaluation
* Strong foundation in data preprocessing and feature analysis

---

Just tell me 👍
