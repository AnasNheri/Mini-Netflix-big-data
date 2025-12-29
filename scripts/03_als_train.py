import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os

# Load ratings
ratings = pd.read_csv("output/clean/ratings.csv")

# Split data
train, test = train_test_split(ratings, test_size=0.2, random_state=42)

# Simple collaborative filtering: compute user-item averages
user_means = train.groupby("userId")["rating"].mean()
movie_means = train.groupby("movieId")["rating"].mean()
global_mean = train["rating"].mean()

# Make predictions
predictions = []
for _, row in test.iterrows():
    user_id = row["userId"]
    movie_id = row["movieId"]
    
    user_avg = user_means.get(user_id, global_mean)
    movie_avg = movie_means.get(movie_id, global_mean)
    pred = (user_avg + movie_avg) / 2
    predictions.append(pred)

test_copy = test.copy()
test_copy["prediction"] = predictions

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(test_copy["rating"], test_copy["prediction"]))
print("✔ RMSE =", rmse)

# Save recommendations (top 10 movies per user)
recommendations = []
for user_id in ratings["userId"].unique():
    movie_scores = {}
    for _, row in ratings[ratings["userId"] == user_id].iterrows():
        movie_id = row["movieId"]
        rating = row["rating"]
        if movie_id not in movie_scores:
            movie_scores[movie_id] = []
        movie_scores[movie_id].append(rating)
    
    # Average scores and get top 10
    avg_scores = {m: np.mean(s) for m, s in movie_scores.items()}
    top_movies = sorted(avg_scores.items(), key=lambda x: x[1], reverse=True)[:10]
    
    for movie_id, score in top_movies:
        recommendations.append({"userId": user_id, "movieId": movie_id, "score": score})

recs_df = pd.DataFrame(recommendations)
os.makedirs("output/als", exist_ok=True)
recs_df.to_csv("output/als/recommendations.csv", index=False)
