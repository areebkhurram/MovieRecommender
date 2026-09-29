import requests
import streamlit as st
import pickle
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"


with open(MODEL_DIR / "movies.pkl", "rb") as file:
    movies = pickle.load(file)

with open(MODEL_DIR / "similarity.pkl", "rb") as file:
    similarity = pickle.load(file)

movie_titles = movies['title'].values

def recommend(movie):
    index = movies[movies['title'] == movie]
    if index.empty:
        return []
    else:
        index = index.index[0]
        
    #similar_movies = similarity[index]
    #movie_list = list(enumerate(similarity[index]))

    movie_list = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)[1:6]
    recommendations = [(movies.iloc[idx]["title"],
                        movies.iloc[idx]["id"], 
                        round(float(score)*100,1)) 
                       for idx,score in movie_list]
    return recommendations

@st.cache_data
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    params = {
        "api_key": st.secrets["TMDB_API_KEY"]
    }

    response = requests.get(url, params=params,timeout=10)
    
    if response.status_code != 200:
        raise requests.exceptions.RequestException(
            f"TMDb API returned status code {response.status_code}"
        )

    data = response.json()

    poster_path = data.get("poster_path")

    if poster_path:
        poster_url =  f"https://image.tmdb.org/t/p/w500{poster_path}"
    else:
        poster_url = None

    return{ 
        "title": data.get("title"),
        "poster": poster_url,
        "rating": data.get("vote_average"),
        "release_date": data.get("release_date"),
        "genres": [genre["name"] for genre in data.get("genres", [])],
        "overview": data.get("overview")
    }




