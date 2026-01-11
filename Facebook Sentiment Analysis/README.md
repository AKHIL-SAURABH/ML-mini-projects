
---

# 📊 Facebook Sentiment Analysis using NLTK

## 📌 Project Overview

This mini project focuses on performing **sentiment analysis on text data** using **Natural Language Processing (NLP)** techniques with the **NLTK library**.
The goal is to analyze textual content and determine whether the overall sentiment expressed is **positive, negative, or neutral**.

Although the dataset used is a text file (`kindle.txt`), the techniques demonstrated in this project are **directly applicable to Facebook posts, comments, and other social media data**.

---

## 🎯 Objectives

* Understand basic NLP preprocessing steps
* Perform sentence and word tokenization
* Apply stemming and lemmatization
* Perform Part-of-Speech (POS) tagging
* Analyze sentiment using **VADER Sentiment Analyzer**
* Interpret overall sentiment polarity of the text

---

## 🛠️ Technologies & Libraries Used

* **Python**
* **NLTK (Natural Language Toolkit)**
* NumPy
* Regular Expressions

---

## 📂 Dataset

* **File Name:** `kindle.txt`
* **Format:** Plain text
* **Description:**
  Contains English text used for demonstrating NLP preprocessing and sentiment analysis.

> ⚠️ The dataset is not scraped from Facebook, but the same methodology can be applied to Facebook comments and posts.

---

## 🔄 Project Workflow

1. Load and read text data
2. Text preprocessing (cleaning & normalization)
3. Sentence tokenization
4. Word tokenization
5. Stemming using Porter Stemmer
6. Lemmatization using WordNet
7. POS tagging
8. Sentiment analysis using VADER
9. Overall sentiment interpretation

---

## 🧠 NLP Techniques Implemented

* **Sentence Tokenization**
* **Word Tokenization**
* **Stemming**
* **Lemmatization**
* **Part-of-Speech Tagging**
* **Lexicon-based Sentiment Analysis (VADER)**

---

## 📈 Sentiment Analysis Logic

* Each sentence is analyzed using **VADER**
* Sentiment scores obtained:

  * Positive
  * Negative
  * Neutral
  * Compound score
* The **average compound score** is calculated to determine overall sentiment

### Sentiment Interpretation

* `compound > 0.05` → Positive
* `compound < -0.05` → Negative
* Otherwise → Neutral

---

## ✅ Results

* The project successfully classifies the **overall sentiment** of the text
* Demonstrates how NLP techniques can be applied to social media sentiment analysis
* Provides a foundation for more advanced sentiment-based applications

---

## ⚠️ Issues Faced & Fixes

* Missing NLTK resources (`punkt_tab`, `averaged_perceptron_tagger_eng`)
* Fixed by explicitly downloading required NLTK datasets
* Proper variable management was implemented to avoid type-related errors

---

## 📌 Conclusion

This mini project demonstrates a complete **NLP-based sentiment analysis pipeline** using NLTK.
It serves as a strong introductory project for understanding **text preprocessing and sentiment analysis**, and can be easily extended to real-world social media datasets such as Facebook or Twitter data.

---

## 🚀 Future Enhancements

* Use real Facebook/Twitter API data
* Add sentiment visualization (graphs & charts)
* Compare VADER with machine learning models
* Build a web interface for live sentiment analysis

---

## 👨‍🎓 Author

**Akhil Saurabh**
Mini Project – Natural Language Processing

---
