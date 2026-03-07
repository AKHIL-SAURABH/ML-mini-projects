
---

# 📦 Inventory Demand Forecasting using Machine Learning

## 📌 Project Overview

Efficient inventory management is critical for vendors and retailers. Maintaining the right stock levels helps prevent:

* **Stock shortages** that lead to lost sales
* **Overstocking** that increases storage and operational costs

This project applies **Machine Learning techniques to forecast product demand** across multiple stores. Using historical sales data, the system predicts future demand so businesses can make smarter inventory decisions.

The project demonstrates how **data preprocessing, feature engineering, visualization, and regression models** can be combined to build a demand forecasting system.

---

# 🎯 Objectives

The main objectives of this project are:

* Analyze historical sales data from multiple stores
* Perform **feature engineering on date-based variables**
* Understand sales patterns using **data visualization**
* Train **Machine Learning regression models** to predict demand
* Compare different models using **error metrics**

---

# 📊 Dataset Description

The dataset contains historical sales records.

| Feature | Description              |
| ------- | ------------------------ |
| date    | Date of the sales record |
| store   | Store ID                 |
| item    | Item/Product ID          |
| sales   | Number of items sold     |

### Dataset Characteristics

* **10 stores**
* **50 different products**
* **Daily sales data**
* **5 years of records**

---

# 🛠️ Technologies Used

* **Python**
* **Pandas** – data manipulation
* **NumPy** – numerical operations
* **Matplotlib** – visualization
* **Seaborn** – statistical plots
* **Scikit-Learn** – machine learning models
* **XGBoost** – advanced regression model
* **Datetime / Holidays libraries** – date feature engineering

---

# ⚙️ Project Workflow

## 1️⃣ Import Libraries

The project begins by importing required Python libraries for:

* Data manipulation
* Visualization
* Machine learning
* Feature engineering

Libraries used include:

```
numpy
pandas
matplotlib
seaborn
sklearn
xgboost
datetime
holidays
```

---

# 2️⃣ Data Loading and Exploration

The dataset is loaded using **Pandas**.

Basic exploration steps include:

* Viewing dataset samples
* Checking dataset size
* Inspecting data types
* Descriptive statistics

```
df = pd.read_csv("train.csv")
```

Key analysis performed:

* Dataset shape
* Column types
* Summary statistics
* Null value check

---

# 3️⃣ Feature Engineering

The **date column is decomposed** to extract useful time-based features.

### Extracted Features

| Feature  | Description                          |
| -------- | ------------------------------------ |
| year     | Year of the sales record             |
| month    | Month of the sale                    |
| day      | Day of the month                     |
| weekday  | Day of the week                      |
| weekend  | Indicates weekend sales              |
| holidays | Whether the day is an Indian holiday |

Example:

```
df["year"]
df["month"]
df["weekday"]
```

### Cyclical Encoding for Month

Seasonal patterns are captured using **sin and cosine transformation**:

```
sin(month)
cos(month)
```

This helps the model understand **seasonality**.

---

# 4️⃣ Data Visualization

Several visualizations are used to understand patterns in sales.

### Sales vs Features

Bar plots analyze how sales change with:

* Store
* Month
* Weekday
* Weekend
* Holidays

### Distribution Analysis

The distribution of sales is examined using:

* **Histogram**
* **Boxplot**

This helps detect **outliers** and skewed distributions.

---

# 5️⃣ Moving Average Analysis

A **30-day Simple Moving Average (SMA)** is calculated to identify trends in sales.

```
rolling(window = 30)
```

This helps visualize:

* demand fluctuations
* seasonal trends
* long-term demand patterns

---

# 6️⃣ Correlation Analysis

A **correlation heatmap** is used to examine relationships between variables.

This helps identify:

* strongly related features
* redundant features
* useful predictors

---

# 7️⃣ Data Cleaning

Outliers are removed to improve model performance.

Example:

```
df = df[df["sales"] < 140]
```

---

# 8️⃣ Train-Test Split

The dataset is divided into:

* **Training Set**
* **Validation Set**

```
train_test_split(test_size = 0.05)
```

---

# 9️⃣ Feature Scaling

Features are normalized using **StandardScaler**.

This improves:

* model stability
* convergence speed
* prediction accuracy

```
scaler = StandardScaler()
```

---

# 🤖 Machine Learning Models Used

Multiple regression models are trained and compared.

### 1️⃣ Linear Regression

A baseline model that assumes a **linear relationship** between features and sales.

### 2️⃣ Lasso Regression

Adds **L1 regularization** to reduce overfitting and perform feature selection.

### 3️⃣ Ridge Regression

Uses **L2 regularization** to stabilize predictions.

### 4️⃣ XGBoost Regressor

A powerful **gradient boosting algorithm** widely used in real-world forecasting problems.

---

# 📏 Model Evaluation

Models are evaluated using:

### Mean Absolute Error (MAE)

[
MAE = \frac{1}{n}\sum |Actual - Predicted|
]

Lower MAE indicates **better model performance**.

Evaluation is done on:

* Training data
* Validation data

---

# 📈 Example Output

Each model prints:

```
Model Name
Training Error
Validation Error
```

This allows easy comparison of model performance.

---

# 🧠 Key Insights

* Sales show **seasonal patterns across months**
* Weekends and holidays can affect demand
* Feature engineering significantly improves prediction performance
* Tree-based models like **XGBoost often outperform simple linear models**

---

# 🚀 Applications

This system can be used for:

* Retail inventory planning
* Supply chain management
* Demand forecasting
* Warehouse optimization
* Sales trend analysis

---

# 📂 Project Structure

```
Inventory-Demand-Forecasting
│
├── Inventory_Demand_Forecasting.ipynb
├── train.csv
└── README.md
```

---

# 🔮 Future Improvements

Possible enhancements include:

* Using **Deep Learning (LSTM)** for time series forecasting
* Implementing **ARIMA or Prophet models**
* Adding **product-level demand forecasting**
* Deploying the model as a **web application**
* Real-time inventory recommendation system

---

