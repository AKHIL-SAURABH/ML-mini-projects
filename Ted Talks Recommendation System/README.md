
---

# 🎤 TED Talks Recommendation System

## 📌 Project Overview

The **TED Talks Recommendation System** is a content-based recommendation engine that suggests similar TED Talks based on user input.

The system analyzes textual features such as:

* Talk titles
* Descriptions
* Speaker names
* Tags / topics

Using Natural Language Processing (NLP) techniques and similarity measures, the model recommends talks that are contextually similar.

This project demonstrates practical implementation of:

* Text preprocessing
* Feature extraction using TF-IDF
* Cosine similarity
* Recommendation logic

---

## 🎯 Objective

The goal of this project is to:

* Build a content-based recommendation system.
* Apply NLP techniques to real-world text data.
* Compute similarity between talks using vector space modeling.
* Provide relevant TED Talk recommendations based on user-selected input.

---

## 📂 Dataset

The dataset contains information about TED Talks including:

* Title
* Speaker
* Description
* Tags
* Views
* Ratings (if available)

The textual columns are combined and processed to create meaningful feature representations.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation
* **NumPy** – Numerical operations
* **Scikit-learn**

  * TF-IDF Vectorizer
  * Cosine Similarity
* **NLTK / Text Preprocessing**
* **Jupyter Notebook**

---

## ⚙️ Project Workflow

### 1️⃣ Data Loading

* Import dataset using Pandas.
* Inspect structure and clean missing values.

### 2️⃣ Data Preprocessing

* Combine important text features.
* Convert text to lowercase.
* Remove special characters and unnecessary spaces.
* (Optional) Remove stopwords.

### 3️⃣ Feature Extraction

* Apply **TF-IDF Vectorization** to convert text into numerical vectors.
* Each talk becomes a high-dimensional vector representation.

### 4️⃣ Similarity Calculation

* Use **Cosine Similarity** to measure similarity between talks.
* Similarity scores range between 0 and 1.

### 5️⃣ Recommendation Function

* Input: TED Talk title
* Process:

  * Find index of selected talk
  * Retrieve similarity scores
  * Sort scores in descending order
* Output:

  * Top N most similar TED Talks

---

## 🧠 How the Recommendation Works

The system follows a **Content-Based Filtering Approach**:

* Talks with similar descriptions and topics have similar TF-IDF vectors.
* Cosine similarity measures the angle between vectors.
* Smaller angle → Higher similarity → Better recommendation.

Mathematically:

[
\text{Cosine Similarity} = \frac{A \cdot B}{||A|| \ ||B||}
]

Where:

* A and B are TF-IDF vectors of two talks.

---

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/Ted-Talks-Recommendation-System.git
```

2. Navigate to the project folder:

```bash
cd Ted-Talks-Recommendation-System
```

3. Install required libraries:

```bash
pip install -r requirements.txt
```

4. Open Jupyter Notebook:

```bash
jupyter notebook
```

5. Run all cells in:

```
Ted_Talks_Recommendation_System.ipynb
```

---

## 📊 Example Usage

```python
recommend("The power of vulnerability")
```

**Output:**

* List of 5–10 similar TED Talks based on content similarity.

---

## 📈 Key Learnings

Through this project, I learned:

* How to preprocess real-world textual data
* How TF-IDF captures word importance
* How cosine similarity works in vector space
* How to build a scalable recommendation logic
* How content-based filtering differs from collaborative filtering

---

## 🔍 Possible Improvements

* Add collaborative filtering
* Deploy as a web app (Flask / FastAPI)
* Use Word2Vec / BERT embeddings for better semantic understanding
* Add user-based personalization
* Create an interactive frontend UI

---

## 📌 Future Scope

* Integrate with TED API (if available)
* Build hybrid recommendation system
* Add rating-based weighted recommendations
* Deploy on cloud platforms like Render or AWS

---

