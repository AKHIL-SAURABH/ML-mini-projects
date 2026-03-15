
---

# 🚗 Predict Fuel Efficiency Using TensorFlow

This project builds a **deep learning regression model using TensorFlow/Keras** to predict the **fuel efficiency (Miles Per Gallon - MPG)** of automobiles based on various engine and vehicle characteristics.

Fuel efficiency prediction is an important task in **automotive engineering and environmental sustainability**, as it helps understand how vehicle design parameters influence fuel consumption.

The model is trained on the **Auto MPG dataset**, which contains car specifications from vehicles manufactured between **1970 and 1982**.

---

# 📊 Project Overview

The objective of this project is to develop a **machine learning model that can accurately predict fuel efficiency** using vehicle attributes such as:

* Cylinders
* Horsepower
* Weight
* Acceleration
* Model Year
* Origin

The notebook walks through the **complete machine learning pipeline**, including:

1. Data loading
2. Data cleaning
3. Exploratory Data Analysis (EDA)
4. Feature preprocessing
5. Model building using TensorFlow
6. Model training
7. Model evaluation

---

# 📂 Dataset

The dataset used in this project is the **Auto MPG dataset**, which contains information about cars produced between **1970–1982**.

### Dataset Characteristics

* Total records: **398**
* After cleaning: **392**
* Features: Multiple vehicle specifications
* Target variable: **MPG (Miles Per Gallon)**

### Features Used

| Feature      | Description                       |
| ------------ | --------------------------------- |
| mpg          | Fuel efficiency (target variable) |
| cylinders    | Number of cylinders in the engine |
| displacement | Engine displacement               |
| horsepower   | Engine horsepower                 |
| weight       | Vehicle weight                    |
| acceleration | Acceleration performance          |
| model year   | Year of manufacture               |
| origin       | Country of origin                 |

---

# 🔍 Exploratory Data Analysis (EDA)

Several exploratory analyses were performed to understand the dataset and relationships between variables.

### Key Observations

* The **horsepower column contained invalid values ('?')**, which were removed during data cleaning.
* After cleaning, **6 rows were removed**.
* Categorical analysis showed differences in MPG based on:

  * **Number of cylinders**
  * **Country of origin**

### Example Insights

* Vehicles with **fewer cylinders tend to have higher MPG**.
* Cars from **origin category 3 (foreign cars)** showed the **highest average fuel efficiency**.

---

# 🧹 Data Cleaning

The following preprocessing steps were performed:

1. Handling invalid values in the **horsepower** column.
2. Converting horsepower from **object → numeric datatype**.
3. Removing rows with invalid values.
4. Correlation analysis to identify **multicollinearity**.
5. Removing the **displacement feature** due to high correlation with other variables.

Final dataset size:

```
392 rows
```

---

# ⚙️ Data Preprocessing

The dataset was split into **training and validation sets**.

| Dataset    | Rows |
| ---------- | ---- |
| Training   | 313  |
| Validation | 79   |

A **TensorFlow data pipeline** was created using batching and prefetching to improve training performance.

---

# 🧠 Model Architecture

The model is built using **TensorFlow Keras Sequential API**.

### Neural Network Structure

```
Input Layer
   ↓
Dense Layer (256 units)
   ↓
Batch Normalization
   ↓
Dropout Layer
   ↓
Dense Layer (256 units)
   ↓
Batch Normalization
   ↓
Output Layer (Regression)
```

### Training Configuration

| Parameter     | Value                                 |
| ------------- | ------------------------------------- |
| Optimizer     | Adam                                  |
| Loss Function | MAE (Mean Absolute Error)             |
| Metric        | MAPE (Mean Absolute Percentage Error) |
| Epochs        | 50                                    |

Batch normalization improves training stability, while **dropout reduces overfitting**.

---

# 📈 Model Training

The model was trained for **50 epochs** using the training dataset.

During training, the following metrics were monitored:

* Training Loss
* Validation Loss
* Mean Absolute Percentage Error (MAPE)

Plots were generated to visualize:

* Training vs Validation Loss
* Training vs Validation Error

These plots help evaluate whether the model is **underfitting, overfitting, or learning effectively**.

---

# 📊 Model Evaluation

After training, the performance of the model was analyzed using:

* Loss curves
* Validation metrics

The results indicate that the neural network is capable of **learning meaningful relationships between vehicle features and fuel efficiency**.

---

# 🛠 Technologies Used

* **Python**
* **TensorFlow / Keras**
* **NumPy**
* **Pandas**
* **Matplotlib**
* **Seaborn**

---

# 📁 Project Structure

```
Predict-Fuel-Efficiency/
│
├── Predict_Fuel_Efficiency.ipynb
├── README.md
```

---

# 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/fuel-efficiency-prediction.git
```

### 2️⃣ Install Dependencies

```bash
pip install tensorflow pandas numpy matplotlib seaborn
```

### 3️⃣ Run the Notebook

```bash
jupyter notebook Predict_Fuel_Efficiency.ipynb
```

---

# 🎯 Key Learning Outcomes

This project demonstrates:

* Data cleaning and preprocessing
* Exploratory data analysis
* Handling categorical and numerical variables
* Building regression models with TensorFlow
* Training neural networks for tabular datasets
* Model evaluation and visualization

---

# 📌 Future Improvements

Possible improvements for this project include:

* Hyperparameter tuning
* Feature engineering
* Using advanced architectures
* Comparing results with classical ML models such as:

  * Linear Regression
  * Random Forest
  * Gradient Boosting

---

