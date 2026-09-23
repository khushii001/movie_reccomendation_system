import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# 1. LOAD & CLEAN DATA
# ==========================================
data = pd.read_csv('movies.csv')

# Handle missing values in genre column
data['genre'] = data['genre'].fillna('')

# ==========================================
# 2. FEATURE EXTRACTION & SIMILARITY MATRIX
# ==========================================
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data['genre'])

# Compute cosine similarity between movies
similarity = cosine_similarity(tfidf_matrix)

# ==========================================
# 3. EXPORT ARTIFACTS
# ==========================================
joblib.dump(similarity, 'similarity.pkl')
joblib.dump(data, 'movies.pkl')

print("✅ Model prepared successfully!")