# 🎬 Movie Recommendation System using Machine Learning

## 📌 Overview

This project is a simple yet effective **Movie Recommendation System** that suggests movies based on similarity. It uses machine learning techniques to recommend movies that are similar in genre to the selected movie.

The system is built using Machine Learning and provides recommendations through an interactive web interface.

---

## 🚀 Features

* Recommends movies based on selected input
* Uses content-based filtering
* Simple and interactive UI built with Streamlit
* Fast and lightweight implementation
* Beginner-friendly project

---

## 🧠 How It Works

1. Movie dataset is loaded
2. Genres are converted into numerical vectors using TF-IDF
3. Similarity between movies is calculated using cosine similarity
4. Based on similarity, top 5 recommended movies are displayed

---

## 📂 Project Structure

```id="n9yq3m"
movie-recommendation-system/
│── main.py              # Builds similarity model
│── app.py               # Streamlit web app
│── movies.csv           # Dataset
│── similarity.pkl       # Saved similarity matrix
│── movies.pkl           # Saved dataset
│── requirements.txt     # Dependencies
│── README.md            # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash id="q0h9sj"
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

---

### 2️⃣ Install Dependencies

```bash id="fpyqgm"
pip install -r requirements.txt
```

---

### 3️⃣ Run Model Script

```bash id="8h0z9u"
python main.py
```

---

### 4️⃣ Run Web App

```bash id="4d6k1y"
streamlit run app.py
```

---

## 🌐 Usage

* Select a movie from the dropdown
* Click **Recommend**
* View suggested similar movies

---

## 📊 Example

**Input:** Inception
**Output:** Interstellar, The Matrix, Avengers, etc.

---

## ⚠️ Limitations

* Uses a small dataset
* Recommendations are based only on genre
* No user personalization

---

## 🚀 Future Improvements

* Add larger dataset
* Include ratings and user preferences
* Use collaborative filtering
* Add movie posters (UI enhancement)
* Deploy application online

---

## 📌 Conclusion

This project demonstrates how a basic recommendation system can be built using machine learning techniques. It highlights the concept of similarity-based recommendations and provides a foundation for more advanced systems.

---

## 👨‍💻 Author

**Khushi Chauhan**</br>
**26BCE11046**

---

## ⭐ Support

If you like this project, give it a star ⭐
