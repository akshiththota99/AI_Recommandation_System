# AI Recommendation System

## 📌 Project Overview
This project is a simple AI-based Recommendation System that suggests items based on user interests using Content-Based Filtering.

The system takes user preferences as input, compares them with available items using TF-IDF Vectorization and Cosine Similarity, and recommends the most relevant items.

---

## 🚀 Features

- Takes user interests as input
- Uses TF-IDF for text feature extraction
- Uses Cosine Similarity for matching
- Displays top recommended items
- Simple and beginner-friendly implementation

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn

---

## 📂 Project Structure

AI_Recommendation-System/

├── app.py

├── items.csv

├── requirements.txt

├── README.md

└── .gitignore

---

## 📊 Dataset

The dataset contains items and their associated tags.

Example:

| Item | Tags |
|--------|--------|
| Python Course | python, programming, ai |
| Machine Learning | python, ai, machine learning |
| Web Development | html, css, javascript |

---

## ▶️ How to Run

### 1. Clone Repository

```bash
git clone <repository-url>
```

### 2. Move to Project Folder

```bash
cd AI_Recommendation-System
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Application

```bash
python app.py
```

---

## 💡 Example

Input:

```text
python ai
```

Output:

```text
Recommended Items:

Machine Learning
Data Science
Python Course
```

---

## 🧠 Concepts Used

- Recommendation Systems
- Content-Based Filtering
- TF-IDF Vectorization
- Cosine Similarity
- Text Processing

---

## 🎯 Learning Outcomes

After completing this project, you will understand:

- How recommendation systems work
- Feature extraction using TF-IDF
- Similarity matching techniques
- Building AI applications with Python

---

## 👨‍💻 Author

Akshith Kumar Thota

Industrial Training Program – DecodeLabs
