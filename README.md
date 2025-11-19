
🎬 Movie Recommender System (2019–2024 Movies)
Content-Based Recommendation using TF-IDF + kNN + Flask
This project is a movie recommendation system built using:
Python


Pandas


TF-IDF vectorization


k-Nearest Neighbors


Flask Web Framework


It recommends the most similar movies based on textual metadata such as:
 genres, directors, writers, actors, runtime, ratings, and vote counts.

📌 1. Project Overview
This system analyses movie descriptions and finds similarities using TF-IDF and cosine distance.
 A simple Flask web interface allows users to type a movie title and receive recommendations.
This repository contains:
The complete dataset used (test2020UPDATED.csv)


All preprocessing code


The machine learning model


The Flask interface


Documentation for setup and usage



📌 2. Repository Structure
movie-recommender/
├── code.ipynb                # Data collection, cleaning, TF-IDF,KNNmodel
├── test2020UPDATED.csv    # Final cleaned dataset
├── app.py                     # Flask application
├─index.html             # User interface
├── requirements.txt           # Dependencies
├── README.md




📌 3. Data Collection
The dataset is built directly from official IMDb sources:
title.basics.tsv.gz
title.crew.tsv.gz
title.akas.tsv.gz
title.ratings.tsv.gz
name.basics.tsv.gz
title.principals.tsv.gz

The script downloads and extracts these files, keeping only movies from 2019 to 2024.
Each dataset contributes:
File
Information
title.basics
Title, year, runtime, genres
title.crew
Directors, writers
title.ratings
Ratings, votes
title.principals
Actors/actresses
name.basics
Maps IDs → human names

A final cleaned dataset is saved as:
test2020UPDATED.csv


📌 4. Feature Engineering (Content Column)
The model uses a content-based approach.
 All important metadata is concatenated into a single text field:
df['content'] = df['Movie'] + ' ' + df['runtimeMinutes'] + ' ' + df['genres'] + ' ' + df['directors'] + ' ' + df['writers'] + ' ' + df['averageRating'] + ' ' + df['numVotes'] + df['actors']

This text is vectorized using TF-IDF.

📌 5. Model: TF-IDF + kNN (Cosine Distance)
TF-IDF
Transforms textual metadata into numerical vectors.
 Important words (director names, genres, actor names…) get more weight.
k-Nearest Neighbors
We use:
NearestNeighbors(metric="cosine", algorithm="brute")

Cosine similarity measures how close two movies are based on their TF-IDF vectors.
Recommendation Function
def recommend_movie(title, n_recommendations=5):
    if title not in df['Movie'].values:
        return ["Movie not found"]

    idx = df.index[df['Movie'] == title][0]

    distances, indices = model_knn.kneighbors(
        tfidf_matrix[idx],
        n_neighbors=n_recommendations + 1
    )

    return df.iloc[indices[0][1:]]['Movie'].tolist()


📌 6. Flask Web Application
🔹 Route /
Handles both GET and POST:
@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    query = ""

    if request.method == "POST":
        query = request.form.get("movie")
        recommendations = recommend_movie(query, 5)

    return render_template("index.html", recommendations=recommendations, query=query)

🔹 index.html
Simple form:
<form method="POST">
    <input type="text" name="movie" placeholder="Enter movie title" value="{{ query }}">
    <input type="submit" value="Recommend">
</form>

Recommendations are displayed in a list.

📌 7. Results (Example)
Input:
Oppenheimer (2023)

Output:
Tenet (2020)
Forest City: A Documentary Film (2019)
Return to the Island (2022)
Drinking the Red Soda (2023)
Heartbreak Falls Part 1 (2023)


📌 8. Installation & Usage
1 — Install dependencies
pip install -r requirements.txt

2 — Run Flask app
python app.py

3 — Open browser
http://127.0.0.1:5000


📌 9. Authors
BENELMOUDDEN HASSAN 
LAMRANI AHMED
