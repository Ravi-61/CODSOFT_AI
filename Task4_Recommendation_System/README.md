# Movie Recommendation System

## Overview

This project is a simple Movie Recommendation System developed using Python and Machine Learning techniques. It recommends movies based on their genres using Content-Based Filtering and Cosine Similarity.

## Features

- Recommends similar movies based on user input
- Uses Content-Based Filtering
- Calculates similarity using Cosine Similarity
- Handles invalid movie names gracefully
- Beginner-friendly AI/ML project

## Technologies Used

- Python
- Pandas
- Scikit-Learn
- CountVectorizer
- Cosine Similarity

## Project Structure

Task4_Recommendation_System/

├── recommendation_system.py

├── movies.csv

├── README.md

└── screenshots/

## Dataset

The dataset contains movie titles and genres.

Example:

title,genre

Avengers,Action

Iron Man,Action

Captain America,Action

Doctor Strange,Action

Titanic,Romance

Notebook,Romance

Frozen,Animation

Toy Story,Animation

## How It Works

1. Load movie data from CSV.
2. Convert genres into numerical features using CountVectorizer.
3. Compute similarity scores using Cosine Similarity.
4. Recommend movies with similar genres.

## Installation

Install required libraries:

pip install pandas

pip install scikit-learn

## Run the Project

python recommendation_system.py

## Example Output

Enter a movie name: Avengers

Recommendations for Avengers:

Iron Man

Captain America

Doctor Strange

## AI Concepts Used

- Recommendation Systems
- Content-Based Filtering
- Feature Extraction
- Cosine Similarity
- Machine Learning Basics

