import pandas as pd
import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index

    if len(movie_index) == 0:  # Handle the case where the movie is not found
        return ["Movie not found!"]

    movie_index = movie_index[0]  # Get the first matching index
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for j in movie_list:
        movie_id = j[0]
        # fetch poster from API
        recommended_movies.append(movies.iloc[j[0]].title)
    return recommended_movies

movies_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values,
)
st.write("You selected:", selected_movie_name)

if st.button("Recommend"):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)