import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Load the dataset
file_path = 'coursera-course-detail-data.csv'
df = pd.read_csv(file_path)

# Combine 'Name' and 'Tags' columns into a single string for each course
df['combined_features'] = df['Name'].astype(str) + ' ' + df['Tags'].astype(str)

def train_kmeans_model(n_clusters=10):
    # Create a TF-IDF vectorizer with stopword removal
    vectorizer = TfidfVectorizer(stop_words='english')

    # Fit and transform the combined features (Name + Tags) of courses
    tfidf_matrix = vectorizer.fit_transform(df['combined_features'])

    # Train K-Means clustering model
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(tfidf_matrix)

    return kmeans, vectorizer, tfidf_matrix

kmeans_model, tfidf_vectorizer, tfidf_matrix = train_kmeans_model(n_clusters=10)

def recommend_courses_kmeans(keywords, kmeans, vectorizer, top_n=5):
    query_vec = vectorizer.transform([keywords])

    cluster_similarities = cosine_similarity(query_vec, kmeans.cluster_centers_).flatten()
    best_cluster = cluster_similarities.argmax()

    cluster_courses = df[df['Cluster'] == best_cluster]

    course_similarities = cosine_similarity(query_vec, vectorizer.transform(cluster_courses['combined_features'])).flatten()
    cluster_courses = cluster_courses.copy()
    cluster_courses['Similarity'] = course_similarities

    # recommendations = cluster_courses[['Name', 'Tags', 'Rating', 'Difficulty', 'Similarity']].sort_values(by='Similarity', ascending=False).head(top_n)
    recommendations = cluster_courses[['Name', 'Rating', 'Difficulty', 'Similarity']].sort_values(by='Similarity', ascending=False).head(top_n)
    return recommendations

def run_recommendation_sys(keywords1):
    recommend_courses_kmeans(keywords1, kmeans_model, tfidf_vectorizer, 5)

# Streamlit GUI
st.title("Course Recommendation System")

keywords = st.text_input("Enter keywords for course recommendation:", "Cybersecurity")

if st.button("Recommend Courses"):
    recommended_courses = recommend_courses_kmeans(keywords, kmeans_model, tfidf_vectorizer)
    recommended_courses = recommended_courses.drop('Similarity', axis = 1)
    st.write(f"Top recommended courses for '{keywords}':")
    
    # Display the recommendations in a table format
    st.dataframe(recommended_courses)