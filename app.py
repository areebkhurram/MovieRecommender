
import requests
import requests
import streamlit as st

from src.recommender import fetch_movie_details, movie_titles, recommend


# Page configuration
st.set_page_config(
    
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)


# Title
st.title("Movie Recommender")
st.write("Discover movies similar to your favorites!")

st.markdown("---")

# Movie selection
with st.container(border=True):

    st.markdown("### Find Similar Movies")
    movie = st.selectbox(
        "Search for a movie",
        movie_titles,
        index=None,
        placeholder="Select a movie to get recommendations"
    )


# Recommendation button
    if st.button("Find Similar Movies", use_container_width=True):

        if movie is None:
            st.warning("Please select a movie first.")
        else:

            recommendations = recommend(movie)
            if recommendations:
                st.subheader(f"**Because You Liked '{movie}'**") 
                st.subheader("Recommended Movies:")

                cols = st.columns(5)
                for col, (title, movie_id, score) in zip(cols, recommendations):

                    with col:
                        try:
                            movie_details = fetch_movie_details(movie_id)
                        except requests.exceptions.RequestException:
                            st.error(f"Failed to fetch details for {title}. Please try again later.")
                            movie_details = None

                        if movie_details:
                            if movie_details["poster"]:
                                st.image(movie_details["poster"], use_container_width=True)
                            else:
                                st.info("No poster available")

                            st.markdown(f"**{movie_details['title']}**")

                            if movie_details["rating"]:
                                st.caption(f" Rating: {movie_details['rating']:.1f}/10")

                            if movie_details["release_date"]:
                                year = movie_details["release_date"][:4]
                                st.caption(f"Release Year: {year}")

                            if movie_details["genres"]:
                                st.caption(" - ".join(movie_details["genres"]))

                            st.caption(f"**Similarity: {score}%**")
                            st.markdown("---")
                            if movie_details["overview"]:
                                with st.expander("About the Movie"):
                                    st.write(movie_details["overview"])
                        else:
                            st.markdown(f"**{title}**")
                            st.caption(f"**Similarity: {score}%**")
                            st.warning("Movie details unavailable")

            else:
                st.warning("No recommendations found.")

st.markdown("---")
with st.expander("About This App"):
    st.write("""
        This movie recommender uses a content-based filtering approach. Each movie is represented using information such as its genres, keywords, cast, crew, and overview. The text data is converted into numerical vectors using CountVectorizer, and cosine similarity is then used to find movies with similar content. When you select a movie, the system compares it with all other movies and returns the five most similar movies.
        """)