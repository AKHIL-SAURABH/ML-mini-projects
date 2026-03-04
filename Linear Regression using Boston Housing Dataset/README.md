
---

# Boston Housing Price Prediction using Linear Regression

## Project Overview

This project demonstrates how **Linear Regression**, one of the most fundamental machine learning algorithms, can be used to **predict housing prices** using the **Boston Housing Dataset**.

The goal of the project is to build a regression model that learns the relationship between multiple housing features (such as crime rate, number of rooms, property tax rate, etc.) and the **median house price**.

Using the **Scikit-learn** library, we train a **Multiple Linear Regression model**, evaluate its performance using error metrics, and visualize the predicted vs actual values.

This project is a **beginner-friendly introduction to supervised machine learning and regression analysis**.

---

# Dataset Information

The **Boston Housing Dataset** contains information about housing in Boston suburbs.

The dataset was originally collected by the **U.S. Census Service** and maintained by **Carnegie Mellon University**.

### Target Variable

The model predicts:

**Price** – Median value of owner-occupied homes (in $1000s)

### Features in the Dataset

| Feature | Description                                          |
| ------- | ---------------------------------------------------- |
| CRIM    | Per capita crime rate by town                        |
| ZN      | Proportion of residential land zoned for large lots  |
| INDUS   | Proportion of non-retail business acres              |
| CHAS    | Charles River dummy variable                         |
| NOX     | Nitric oxide concentration                           |
| RM      | Average number of rooms per dwelling                 |
| AGE     | Proportion of owner-occupied units built before 1940 |
| DIS     | Distance to employment centers                       |
| RAD     | Index of accessibility to highways                   |
| TAX     | Property tax rate                                    |
| PTRATIO | Pupil-teacher ratio                                  |
| B       | Proportion of Black population                       |
| LSTAT   | % lower status population                            |

These features help determine the **price of houses in Boston**.

---

# Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Jupyter Notebook

---

# Machine Learning Workflow

The project follows a standard **machine learning pipeline**.

### 1. Importing Libraries

Essential libraries are imported for data manipulation, visualization, and machine learning.

```
numpy
pandas
matplotlib
sklearn
```

---

### 2. Loading the Dataset

The dataset is loaded using:

```
fetch_openml()
```

This provides both:

* Feature matrix
* Target variable

---

### 3. Data Preparation

The dataset is converted from **NumPy arrays to a Pandas DataFrame** for easier handling.

Steps performed:

* Assign column names
* Add target column **Price**
* Inspect dataset using

```
data.head()
data.describe()
data.info()
```

This helps understand:

* Data distribution
* Data types
* Missing values

---

### 4. Splitting Dataset

The dataset is divided into:

* **Training Set**
* **Testing Set**

Typical split:

```
80% Training
20% Testing
```

Training data is used to train the model, while testing data evaluates performance.

---

### 5. Model Training

A **Multiple Linear Regression model** is trained using:

```
from sklearn.linear_model import LinearRegression
```

The model learns the relationship between:

```
Input Features → Housing Price
```

---

### 6. Model Prediction

After training, the model predicts housing prices for the **test dataset**.

```
y_pred = model.predict(X_test)
```

These predictions are compared with actual values.

---

### 7. Visualization

A **scatter plot** is used to compare:

* Actual prices
* Predicted prices

```
Actual Price vs Predicted Price
```

If the model performs well, the points should lie close to a **diagonal line**.

---

### 8. Model Evaluation

Model performance is evaluated using regression metrics.

### Mean Squared Error (MSE)

[
MSE = \frac{1}{n}\sum (y_{true} - y_{pred})^2
]

Measures the average squared difference between predicted and actual values.

---

### Mean Absolute Error (MAE)

[
MAE = \frac{1}{n}\sum |y_{true} - y_{pred}|
]

Measures the average absolute difference.

---

### Accuracy of Model

The model achieved approximately:

**66.55% prediction accuracy**

This indicates that **Linear Regression alone may not fully capture complex housing price relationships**.

---

# Results

Key findings:

* Linear Regression can model basic relationships in housing data.
* However, the prediction accuracy is moderate.
* Housing prices depend on **complex nonlinear relationships** which simple linear regression may fail to capture.

---

# Possible Improvements

The model can be improved using more advanced techniques such as:

* Polynomial Regression
* Random Forest Regression
* Gradient Boosting
* XGBoost
* Feature Engineering
* Data Normalization
* Hyperparameter tuning

These approaches can significantly improve prediction performance.

---

# Project Structure

```
Boston-Housing-Linear-Regression
│
├── Boston_Housing_Linear_Regression.ipynb
├── README.md
```

---

# Learning Outcomes

Through this project, you will learn:

* Fundamentals of **Supervised Machine Learning**
* How **Linear Regression works**
* Data preprocessing with **Pandas**
* Training models using **Scikit-learn**
* Evaluating regression models
* Visualizing predictions

---

# Conclusion

This project demonstrates a basic implementation of **Multiple Linear Regression for housing price prediction**. While the model provides reasonable results, more sophisticated machine learning techniques are required to achieve higher accuracy in real-world scenarios.

---
