"""03_als_train.py
Lightweight training / evaluation of a simple recommender.

This script demonstrates a baseline approach using user/movie averages
to predict ratings and compute an RMSE on a holdout set. It also
builds simple per-user top-N recommendations based on historical averages.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os

# Load cleaned ratings from disk
ratings = pd.read_csv("output/clean/ratings.csv")

# Train/test split for evaluation (80/20)
train, test = train_test_split(ratings, test_size=0.2, random_state=42)

# Baseline model: per-user and per-movie mean ratings, plus a global mean
user_means = train.groupby("userId")["rating"].mean()
movie_means = train.groupby("movieId")["rating"].mean()
global_mean = train["rating"].mean()

# Predict on test set by averaging available user and movie means
predictions = []
for _, row in test.iterrows():
    user_id = row["userId"]
    movie_id = row["movieId"]

    # Fallback to global mean if user or movie unseen in training
    user_avg = user_means.get(user_id, global_mean)
    movie_avg = movie_means.get(movie_id, global_mean)
    pred = (user_avg + movie_avg) / 2
    predictions.append(pred)

test_copy = test.copy()
test_copy["prediction"] = predictions

# Compute RMSE between true ratings and predictions
rmse = np.sqrt(mean_squared_error(test_copy["rating"], test_copy["prediction"]))
print("✔ RMSE =", rmse)

# Build simple recommendations: for each user, rank movies by historical average
# (this uses the full dataset and is a simple illustrative baseline)
recommendations = []
for user_id in ratings["userId"].unique():
    movie_scores = {}
    for _, row in ratings[ratings["userId"] == user_id].iterrows():
        movie_id = row["movieId"]
        rating = row["rating"]
        movie_scores.setdefault(movie_id, []).append(rating)

    # Compute average score per movie and take top 10
    avg_scores = {m: np.mean(s) for m, s in movie_scores.items()}
    top_movies = sorted(avg_scores.items(), key=lambda x: x[1], reverse=True)[:10]

    for movie_id, score in top_movies:
        recommendations.append({"userId": user_id, "movieId": movie_id, "score": score})

recs_df = pd.DataFrame(recommendations)
os.makedirs("output/als", exist_ok=True)
recs_df.to_csv("output/als/recommendations.csv", index=False)
