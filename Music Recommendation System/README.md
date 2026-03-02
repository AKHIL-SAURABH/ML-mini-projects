
---

# 🎵 Music Recommendation System using Machine Learning

## 📌 Project Overview

This project builds a **content-based music recommendation system** using machine learning techniques.
It analyzes song metadata such as artist, genre, and other textual features to recommend songs that are similar to a given input song.

The system works similarly to how platforms like YouTube or Spotify suggest content — by identifying patterns and similarities in the data.

This implementation demonstrates the **complete pipeline of a recommendation system**, including:

* Data loading
* Exploratory data analysis (EDA)
* Feature engineering
* Text vectorization
* Similarity computation
* Recommendation generation
* Visualization of results

---

## 🚀 Objectives

* Understand how recommendation systems work
* Build a content-based recommender using ML concepts
* Apply TF-IDF vectorization to song metadata
* Use cosine similarity to find similar songs
* Generate and visualize recommendations

---

## 📂 Dataset

The dataset contains information about songs released over a long time period (around 100 years), including:

* Song metadata
* Artist name
* Genre and textual attributes
* Other descriptive features

These attributes are combined to represent each song for similarity comparison.

Dataset file used:

```
tcc_ceds_music.csv
```

---

## 🧠 Machine Learning Approach

This project uses a **Content-Based Filtering** technique.

### Workflow

1. **Data Loading**

   * Import dataset using Pandas

2. **Exploratory Data Analysis**

   * Understand song distribution
   * Identify top artists by number of songs
   * Visualize dataset patterns

3. **Feature Engineering**

   * Combine relevant song attributes into a single feature column

4. **Text Vectorization**

   * Convert text into numerical representation using:

     * TF-IDF (Term Frequency – Inverse Document Frequency)

5. **Similarity Computation**

   * Compute similarity between songs using:

     * Cosine Similarity

6. **Recommendation Generation**

   * For a given song:

     * Find similarity scores
     * Sort results
     * Return top N similar songs

7. **Visualization**

   * Display recommended songs using bar charts

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

  * TF-IDF Vectorizer
  * Cosine Similarity

---

## ⚙ How to Run the Project

### Step 1 — Install dependencies

```bash
pip install pandas numpy matplotlib scikit-learn
```

### Step 2 — Place dataset

Ensure the dataset file is in the project directory:

```
tcc_ceds_music.csv
```

### Step 3 — Run notebook

Open and run:

```
Music_Recommendation_System.ipynb
```

---

## 🎯 Example Usage

Input:

```
Song Name: "cry"
```

Output:

```
Top 10 songs similar to "cry"
```

The system computes similarity and recommends songs with the closest matching features.

---

## 📊 Results

* Successfully recommends similar songs based on metadata
* Visualizes recommendations clearly
* Demonstrates working ML pipeline for recommendation systems

---

## ⚠ Limitations

* Uses only content-based filtering
* No user personalization
* Limited feature set
* Not optimized for production-scale deployment

---

## 🔮 Future Improvements

* Hybrid recommendation (content + collaborative filtering)
* User preference modeling
* Deep learning embeddings
* Real-time recommendation API
* Web or mobile interface
* Audio feature extraction
* Model evaluation metrics

---

## 🎓 Learning Outcomes

Through this project, you will understand:

* How recommendation systems work
* Text feature extraction using TF-IDF
* Similarity measurement using cosine similarity
* End-to-end ML pipeline development

---

## 📜 Conclusion

This project demonstrates how machine learning can be used to recommend music based on song characteristics. While simple, it provides a strong foundation for building more advanced recommendation systems used in real-world applications.

---
