import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")

vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])

similarity = cosine_similarity(genre_matrix)

def recommend(movie_name):

    movie_name = movie_name.lower()

    movie_titles = movies["title"].str.lower()

    if movie_name not in movie_titles.values:
        print("\nMovie not found!")
        print("\nAvailable Movies:")

        for movie in movies["title"]:
            print("-", movie)

        return

    idx = movie_titles[movie_titles == movie_name].index[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommendations for {movies.iloc[idx]['title']}:\n")

    for movie in scores[1:4]:
        print(movies.iloc[movie[0]]["title"])

movie = input("Enter a movie name: ")
recommend(movie)