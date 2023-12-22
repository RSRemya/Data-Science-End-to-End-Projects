import streamlit as st
import pickle
import pandas as pd




movies_dict = pickle.load(open('movies_df.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommnder System')

option = st.selectbox('Select you Movie : ', movies['title'].values)

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)





