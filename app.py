import joblib
import streamlit as st

# Load data
data = joblib.load('movies.pkl')
similarity = joblib.load('similarity.pkl')

# Set page configuration
st.set_page_config(
    page_title="Netflix Style Recommender", page_icon="🎬", layout="wide"
)

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #141414;
        color: white;
    }
    .movie-card {
        background-color: #1f1f1f;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 15px;
        min-height: 120px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Header
st.title("🎬 Netflix Style Recommender")
st.write("Find movies similar to your taste 🍿")


# Recommendation Logic
def recommend(movie):
  index = data[data['title'] == movie].index[0]
  distances = similarity[index]
  movies_list = sorted(
      list(enumerate(distances)), reverse=True, key=lambda x: x[1]
  )[1:11]

  recommendations = []
  for i in movies_list:
    recommendations.append(data.iloc[i[0]].title)
  return recommendations


# Movie Selection
movie_list = data['title'].values
selected_movie = st.selectbox("Choose a movie:", movie_list)

# Display Recommendations
if st.button("🍿 Recommend"):
  results = recommend(selected_movie)

  st.divider()
  st.subheader("Top Picks For You")

  cols = st.columns(5)

  for i, movie in enumerate(results):
    with cols[i % 5]:
      st.markdown(
          f"""
                <div class="movie-card">
                    🎬 <br><br>
                    <b>{movie}</b>
                </div>
            """,
          unsafe_allow_html=True,
      )