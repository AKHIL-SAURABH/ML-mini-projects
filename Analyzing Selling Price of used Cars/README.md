
---

# 🚗 Analyzing Selling Price of Used Cars using Python

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on a used car dataset to understand the key factors that influence the **selling price of cars**.

The analysis helps buyers and sellers make informed pricing decisions by identifying relationships between vehicle characteristics and price.

The project walks through the complete data analysis pipeline including:

* Data loading
* Data cleaning
* Feature engineering
* Data normalization
* Visualization
* Statistical testing

A real-world scenario is considered where a car owner wants to determine the best selling price for their vehicle.

---

## 🎯 Problem Statement

Our friend **Otis** wants to sell his car but is unsure about the correct price.
The objective is to analyze market data and identify the major factors that influence car prices so he can set a competitive and profitable selling price.

---

## 📊 Dataset Description

The dataset contains various attributes of used cars such as:

* Make (brand)
* Fuel type
* Body style
* Engine size
* Horsepower
* Drive wheels
* Dimensions (length, width, height)
* Fuel consumption
* Price

These features are analyzed to understand their impact on the selling price.

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy

---

## 🧪 Project Workflow

### 1️⃣ Import Libraries

Essential data analysis and visualization libraries are imported.

### 2️⃣ Load Dataset

The dataset is loaded into a Pandas DataFrame for processing.

### 3️⃣ Assign Column Headers

Column names are assigned to improve readability and usability.

### 4️⃣ Handle Missing Values

Missing values are detected and handled to ensure data reliability.

### 5️⃣ Feature Engineering

* Converted fuel efficiency from **MPG to L/100km**
* Converted price column to numeric
* Removed invalid entries

### 6️⃣ Data Normalization

Numerical features such as:

* Length
* Width
* Height

are normalized to enable fair comparison.

### 7️⃣ Price Binning

Cars are categorized into price groups:

* Low
* Medium
* High

### 8️⃣ Convert Categorical to Numerical

Categorical variables are transformed using **one-hot encoding**.

### 9️⃣ Data Visualization

Multiple visualizations are used to explore relationships:

* Price distribution (boxplot)
* Price vs drive wheels
* Engine size vs price (scatter plot)

### 🔟 Grouping Analysis

Mean prices are analyzed based on:

* Drive wheels
* Body style

### 1️⃣1️⃣ Pivot Table & Heatmap

A pivot table and heatmap are created to visualize price variation across categories.

### 1️⃣2️⃣ Statistical Testing (ANOVA)

ANOVA test is performed to check whether price differences between car brands are statistically significant.

---

## 📈 Key Insights

* Engine size strongly influences price.
* Drive wheel configuration impacts average price.
* Car brand significantly affects pricing (verified using ANOVA).
* Data normalization improves comparison across features.
* Visualization helps detect patterns and trends clearly.

---

## 📦 Installation

Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn scipy
```

---

## ▶️ How to Run

1. Place the dataset file (`output.csv`) in the project directory.
2. Open the Jupyter Notebook.
3. Run cells sequentially to reproduce the analysis.

---

## 📁 Project Structure

```
Analyzing_Selling_Price_Cars.ipynb
output.csv
README.md
```

---

## 🎓 Learning Outcomes

By completing this project, you will understand:

* Real-world data preprocessing
* Feature engineering
* Data normalization techniques
* Exploratory Data Analysis
* Visualization for insights
* Statistical hypothesis testing (ANOVA)

---

## 🚀 Future Improvements

* Build a machine learning model for price prediction
* Add regression analysis
* Perform feature importance ranking
* Deploy a web app for price estimation

---

