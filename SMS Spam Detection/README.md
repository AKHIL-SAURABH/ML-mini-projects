
---

# 📩 SMS Spam Detection using Deep Learning (TensorFlow)

## 📌 Project Overview

This mini project focuses on **automatically detecting spam SMS messages** using **deep learning models built with TensorFlow and Keras**.
The notebook explores multiple neural-network approaches for text classification and compares their performance using standard evaluation metrics.

---

## 🎯 Objective

To classify SMS messages into:

* **Spam**
* **Ham (Not Spam)**

using deep learning–based Natural Language Processing (NLP) techniques.

---

## 📂 Dataset

* **File used:** `spam.csv`
* **Encoding:** `latin-1`
* **Description:** A labeled SMS dataset containing spam and non-spam messages.

### Label Encoding

* `spam` → `1`
* `ham` → `0`

---

## 🧹 Data Preprocessing

The following preprocessing steps are performed:

* Removal of unnecessary columns
* Renaming columns for clarity
* Label encoding
* Train-test split
* Text length analysis (average & maximum word counts)

---

## 🧠 Models Implemented

The notebook builds and evaluates **three different deep learning models**:

### 1️⃣ Dense Neural Network with Text Vectorization

* `TextVectorization` layer
* Embedding layer
* Fully connected dense layers
* Binary classification output

---

### 2️⃣ Bidirectional LSTM Model

* `TextVectorization`
* Embedding layer
* **Bidirectional LSTM layers**
* Dropout for regularization
* Dense classification layers

---

### 3️⃣ Transfer Learning using Universal Sentence Encoder (USE)

* Pre-trained **Universal Sentence Encoder (TensorFlow Hub)**
* Frozen embeddings
* Dense neural network on top
* Faster training and semantic understanding

---

## ⚙️ Model Training

* **Optimizer:** Adam
* **Loss Function:** Binary Crossentropy
* **Metrics:** Accuracy
* **Epochs:** 5

A reusable `compile_and_fit()` function is used for consistent training across models.

---

## 📊 Evaluation Metrics

Each model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score

Results are stored in a DataFrame and visualized using:

* **Bar chart**
* **Line graph**

---

## 📈 Results Comparison

A performance table is generated comparing:

* Dense Embedding Model
* Bi-LSTM Model
* Transfer Learning (USE) Model

This makes it easy to observe how advanced NLP techniques improve classification performance.

---

## 🛠️ Tech Stack

* **Python**
* **TensorFlow / Keras**
* **TensorFlow Hub**
* **Scikit-learn**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**

---

## ▶️ How to Run the Project Locally

1. Clone the repository

```bash
git clone <your-repo-link>
```

2. Install required libraries

```bash
pip install tensorflow tensorflow-hub pandas numpy matplotlib seaborn scikit-learn
```

3. Ensure `spam.csv` is present in the project directory

4. Open and run the notebook

```bash
jupyter notebook SMS_Spam_Detection.ipynb
```

---

## 📌 Key Learnings

* Text preprocessing for deep learning
* Sequence modeling with LSTMs
* Transfer learning for NLP tasks
* Performance comparison across multiple architectures

---

## 📎 Project Type

**Mini Project – Machine Learning / Deep Learning**

---

