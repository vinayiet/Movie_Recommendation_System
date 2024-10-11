import streamlit as st 
import pickle
import pandas as pd

# Load the movie data
movie_dict = pickle.load(open('movies.pkl', 'rb'))  # Assuming you have a separate movie_dict.pkl
movies = pd.DataFrame(movie_dict)

# Load the similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title) 
    return recommended_movies 

st.title("Movie Recommender System")

# Create a selectbox with movie titles
selected_movie = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    recommendation = recommend(selected_movie)
    for i in recommendation:
        st.write(i)
