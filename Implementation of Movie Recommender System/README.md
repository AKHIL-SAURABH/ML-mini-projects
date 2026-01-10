
---

# 🎬 Movie Recommender System (Python)

## 📌 Overview

This project implements a **Movie Recommender System** using **Collaborative Filtering** in Python.
The system analyzes user–movie rating patterns and recommends movies based on **similar user preferences** using correlation analysis.

The notebook walks through the complete pipeline—from data loading and preprocessing to exploratory data analysis and recommendation generation.

---

## 🧠 Recommendation Approach

This project uses **Item-Based Collaborative Filtering**, where:

* Movies are recommended based on **similarity between movie ratings**
* Pearson correlation is used to find movies with similar rating patterns
* Popularity and rating counts are considered to improve recommendation quality

---

## 📂 Dataset Used

Two CSV files are used in this project:

1. **User Ratings Dataset**

   * Contains user IDs, movie IDs, ratings, and timestamps
   * Each row represents a user’s rating for a specific movie

2. **Movie Titles Dataset**

   * Maps movie IDs to movie titles
   * Helps display movie names instead of numeric IDs

---

## ⚙️ Project Workflow

### 1️⃣ Importing Libraries

The following Python libraries are used:

* `pandas` – data manipulation
* `matplotlib` & `seaborn` – data visualization

---

### 2️⃣ Loading Movie Titles

* Movie ID–Title mapping is loaded
* Enables readable movie names in analysis and recommendations

---

### 3️⃣ Merging Datasets

* User ratings and movie titles are merged
* Final dataset contains:

  * User ID
  * Movie title
  * Rating

---

### 4️⃣ Exploratory Data Analysis (EDA)

The notebook performs detailed analysis including:

* Average rating per movie
* Number of ratings per movie
* Distribution of ratings
* Relationship between rating count and average rating

📊 **Visualizations include:**

* Histograms of ratings
* Joint plots between rating count and average rating

---

### 5️⃣ Creating the User–Movie Matrix

* A pivot table is created with:

  * Rows → Users
  * Columns → Movies
  * Values → Ratings
* This matrix forms the foundation for similarity calculations

---

### 6️⃣ Building the Recommendation System

* A target movie is selected
* Correlation is computed between the target movie and all other movies
* Movies with:

  * High correlation
  * Sufficient number of ratings
    are recommended

---

## 🔍 Example Recommendation Logic

* Select a movie liked by the user
* Find movies with similar rating patterns
* Filter results based on rating count
* Display top correlated movies as recommendations

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Matplotlib**
* **Seaborn**
* **Jupyter Notebook**

---

## 📁 Project Structure

```
Movie_Recommender_System.ipynb
Movie_Id_Titles.csv
```

---

## 🚀 How to Run the Project

1. Clone the repository
2. Ensure required CSV files are in the same directory
3. Open the notebook:

   ```bash
   jupyter notebook Movie_Recommender_System.ipynb
   ```
4. Run cells sequentially

---

## 📌 Key Learnings

* Understanding collaborative filtering concepts
* Building item-based recommendation systems
* Using correlation for similarity detection
* Performing meaningful EDA for recommender systems

---

## 🔮 Future Improvements

* Implement user-based collaborative filtering
* Add cosine similarity
* Integrate content-based filtering
* Deploy as a web application

---

## ✨ Conclusion

This project demonstrates a **fundamental and practical implementation of a movie recommender system** using real-world rating data and collaborative filtering techniques. It serves as a strong foundation for more advanced recommendation engines.

---
