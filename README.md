# Movie Recommender System
# ------------------------

A content-based movie recommendation system built with Python and Streamlit. The application recommends movies based on their genres, keywords, cast, crew, and plot overview, and uses the TMDb API to display additional movie information such as posters, ratings, release years, genres, and overviews.

## Project Overview
## ----------------

The goal of this project is to build an end-to-end movie recommendation system while practicing data preprocessing, natural language processing, similarity-based recommendation, API integration, and Streamlit application development.

The system uses a **content-based filtering** approach. When a user selects a movie, the system analyzes the movie's content and finds other movies with similar characteristics.

## Features
## --------

* Content-based movie recommendations
* Searchable movie selection
* Top 5 similar movie recommendations
* Cosine similarity scores
* Movie posters fetched from TMDb
* TMDb ratings
* Release year
* Movie genres
* Movie overview
* Cached API requests for improved performance
* API timeout and error handling
* API key stored securely using Streamlit secrets
* Pre-computed recommendation model stored using Git LFS

## How It Works
## ------------

The recommendation system follows several steps.

### 1. Data Preparation

The project uses the TMDb 5000 Movies and Credits datasets.

Relevant movie information includes:

* Genres
* Keywords
* Overview
* Cast
* Crew
* Movie ID
* Movie title

The movie and credits datasets are merged using the movie ID.

### 2. Creating Movie Tags

Information from different columns is combined into a single text representation called `tags`.

For example, a movie's tags can contain information such as:

```text
Action Adventure ChristopherNolan ChristianBale Batman
```

This allows the different characteristics of a movie to be represented together.

### 3. Text Processing

The project uses **Porter stemming** to reduce words to their root forms.

For example:

```text
playing → play
played → play
```

This helps similar words be treated more consistently during text processing.

### 4. Vectorization

The movie tags are converted into numerical vectors using `CountVectorizer`.

The vectorizer is configured with a maximum of 5,000 features and English stop-word removal.

The resulting matrix contains:

```text
4803 movies × 5000 features
```

### 5. Cosine Similarity

Cosine similarity is then calculated between every pair of movies.

This produces a:

```text
4803 × 4803
```

similarity matrix.

For a selected movie, the system compares its similarity scores with all other movies and returns the five movies with the highest scores.

> Note: The displayed similarity percentage represents the cosine similarity score multiplied by 100. It is **not a probability** that the user will like the recommended movie.

## Recommendation Pipeline
## -----------------------

```text
Movie Dataset
     ↓
Data Cleaning & Merging
     ↓
Feature Extraction
     ↓
Create Movie Tags
     ↓
Text Processing & Stemming
     ↓
CountVectorizer
     ↓
Movie Vectors
     ↓
Cosine Similarity
     ↓
Similarity Matrix
     ↓
Top 5 Recommendations
     ↓
TMDb API
     ↓
Posters + Ratings + Movie Details
     ↓
Streamlit Interface
```

## Tech Stack
## ----------

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### Machine Learning / NLP

* Scikit-learn
* NLTK
* CountVectorizer
* Cosine Similarity

### Web Application

* Streamlit

### API

* TMDb API
* Requests

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub
* Git LFS

## Project Structure
## -----------------

```text
Movie_Recommender/
│
├── .streamlit/
│   └── secrets.toml
│
├── data/
│   └── raw/
│       ├── tmdb_5000_credits.csv
│       └── tmdb_5000_movies.csv
│
├── models/
│   ├── movies.pkl
│   └── similarity.pkl
│
├── notebooks/
│   └── Movie_Recommender.ipynb
│
├── src/
│   └── recommender.py
│
├── app.py
├── .gitignore
├── README.md
└── requirements.txt
```

### File Descriptions

**`app.py`**

Contains the Streamlit user interface and controls the application flow.

**`src/recommender.py`**

Contains the recommendation logic, model loading, and TMDb API functionality.

**`models/movies.pkl`**

Stores the processed movie dataset used by the application.

**`models/similarity.pkl`**

Stores the pre-computed cosine similarity matrix.

**`notebooks/Movie_Recommender.ipynb`**

Contains the data exploration, preprocessing, feature engineering, vectorization, and similarity calculations used to build the recommendation system.

**`data/raw/`**

Contains the original TMDb datasets used for the project.

## Installation
## ------------

### 1. Clone the repository

```bash
git clone https://github.com/areebkhurram/MovieRecommender.git
cd MovieRecommender
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the TMDb API key

Create the following file:

```text
.streamlit/secrets.toml
```

Add your TMDb API key:

```toml
TMDB_API_KEY = "your_api_key_here"
```

Do not commit this file to GitHub. It is already included in `.gitignore`.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Example
## -------

For example, selecting:

```text
The Dark Knight Rises
```

can produce recommendations such as:

| Movie           | Similarity |
| --------------- | ---------: |
| The Dark Knight |      42.3% |
| Batman Returns  |      32.5% |
| Batman Forever  |      31.8% |
| Batman Begins   |      31.8% |
| Batman          |      30.2% |

The similarity values are calculated using cosine similarity between the movie feature vectors.

## Dataset
## -------

This project uses the **TMDb 5000 Movies and Credits datasets**.

The datasets contain information about thousands of movies, including movie titles, genres, keywords, cast, crew, and plot overviews.

The original datasets are used for educational and project purposes.

## API Key Security
## ----------------

The TMDb API key is stored locally using Streamlit's secrets mechanism:

```text
.streamlit/secrets.toml
```

The secrets file is excluded from Git using `.gitignore`.

The application also handles API failures and request timeouts so that the recommendation system can still display basic recommendation information if additional TMDb details cannot be retrieved.

## Model Files
## -----------

The pre-computed model files are included in the repository:

```text
models/movies.pkl
models/similarity.pkl
```

Because `similarity.pkl` is larger than GitHub's standard 100 MB file limit, the model files are managed using **Git LFS (Git Large File Storage)**.

This allows the complete recommendation model to remain part of the project repository without exceeding GitHub's normal file-size limit.

##  Future Improvements
##  -------------------

Possible future improvements include:

* Improve recommendation quality using TF-IDF or alternative text representations
* Add user ratings and personalized recommendations
* Add filtering by genre, rating, or release year
* Improve the movie search experience
* Add trailers and additional movie information
* Deploy the application publicly
* Experiment with hybrid recommendation techniques
* Evaluate recommendation quality using suitable recommendation metrics

##  What I Learned
##  --------------

Through this project, I practiced:

* Data cleaning and preprocessing
* Working with Pandas
* Feature engineering
* Natural language processing
* Text vectorization
* Cosine similarity
* Content-based recommendation systems
* Working with APIs
* API error handling
* Streamlit application development
* Caching
* Environment and secret management
* Git and GitHub
* Git LFS
* Organizing a Python project into separate modules

##  Author

**Areeb Khurram**

Bachelor's Student in Artificial Intelligence
Johannes Kepler University Linz

---

If you found this project useful, feel free to explore the repository and experiment with the recommendation system.
