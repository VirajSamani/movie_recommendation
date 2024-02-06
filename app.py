import streamlit as st
import pickle
import pandas as pd

similarity = pickle.load(open('similarity.pkl','rb'))
movies_dict = pickle.load(open('movie.pkl','rb'))

movies_list = pd.DataFrame(movies_dict)

def recommend(selected_movie_name):
    movie_index = movies_list[movies_list['title'] == selected_movie_name].index[0]
    distances = similarity[movie_index]
    result = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    result_recommended = []

    for i in result:
        movie_id = i[0]
        result_recommended.append(movies_list.iloc[movie_id]['title'])
    
    return result_recommended

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie', movies_list['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)