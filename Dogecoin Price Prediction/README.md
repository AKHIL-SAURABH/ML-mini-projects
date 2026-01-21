
---

# 📈 Dogecoin Price Prediction using Machine Learning & Time Series Analysis

## 📌 Project Overview

This project focuses on **predicting the price of Dogecoin (DOGE-USD)** using **time series analysis techniques**. Cryptocurrencies are highly volatile, and forecasting their prices helps in understanding market trends and behavior.
In this project, historical Dogecoin price data is analyzed and a **SARIMAX (Seasonal ARIMA with exogenous variables)** model is implemented to predict future closing prices.

The notebook walks through **data preprocessing, correlation analysis, feature selection, time series modeling, and visualization of predictions**.

---

## 🎯 Objectives

* Analyze historical Dogecoin price data
* Understand relationships between price features
* Apply time series forecasting using **ARIMA / SARIMAX**
* Predict future closing prices
* Visualize actual vs predicted prices

---

## 🧠 Concepts & Techniques Used

* Time Series Analysis
* Correlation Analysis
* Feature Selection
* ARIMA / SARIMAX Model
* Data Visualization
* Train–Test Split for Time Series

---

## 🛠️ Tech Stack & Libraries

* **Python**
* **Pandas** – Data manipulation
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Scikit-learn** – ML utilities
* **Statsmodels** – ARIMA / SARIMAX modeling

---

## 📂 Dataset

* **File:** `DOGE-USD.csv`
* **Source:** Historical Dogecoin price data
* **Key Features:**

  * `Open`
  * `High`
  * `Low`
  * `Close`
  * `Volume`
  * `Date`

---

## 🔍 Project Workflow

### 1️⃣ Importing Libraries

All required Python libraries are imported for data handling, visualization, and modeling.

### 2️⃣ Loading the Dataset

The Dogecoin dataset is loaded using Pandas and initial exploration is performed.

### 3️⃣ Correlation Analysis

* Correlation between numerical features is analyzed
* Highly correlated features (`Open`, `High`, `Low`) are identified for modeling

### 4️⃣ Data Preprocessing

* Date column is converted to proper datetime format
* Date is set as index
* Dataset is checked for missing values

### 5️⃣ Feature Selection

* The **Close price** is selected as the target variable
* Relevant correlated features are chosen as exogenous variables

### 6️⃣ Train–Test Split

* Data is split into training and testing sets while maintaining time order

### 7️⃣ Model Development

* **SARIMAX model** is implemented with selected features
* Model parameters `(p, d, q)` are defined
* Model is trained on historical data

### 8️⃣ Prediction

* Future closing prices are predicted on test data
* Predictions are generated using the trained SARIMAX model

### 9️⃣ Visualization

* Actual closing prices are plotted
* Predicted prices are overlaid for comparison

---

## 📊 Results

* The SARIMAX model successfully captures price trends
* Predictions closely follow actual price movements
* Visualization clearly shows model performance over time

---

## 🚀 How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/your-username/dogecoin-price-prediction.git
```

2. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
```

3. Place `DOGE-USD.csv` in the project directory

4. Run the Jupyter Notebook

```bash
jupyter notebook Dogecoin_Price_Prediction.ipynb
```

---

## ⚠️ Disclaimer

This project is for **educational and learning purposes only**.
Cryptocurrency markets are highly volatile, and predictions should **not be considered financial advice**.

---

## ⭐ Acknowledgements

* Historical data from public cryptocurrency datasets
* Open-source Python libraries for data science and time series analysis

---

