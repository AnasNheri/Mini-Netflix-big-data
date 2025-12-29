import pandas as pd
import os

# Load ratings
ratings = pd.read_csv("output/clean/ratings.csv")

# Top movies
top_movies = ratings.groupby("movieId").agg(
    avg_rating=("rating", "mean"),
    total_ratings=("rating", "count")
).reset_index().sort_values("avg_rating", ascending=False)

# Distribution ratings
distribution = ratings.groupby("rating").size().reset_index(name="count").sort_values("rating")

os.makedirs("output/analytics", exist_ok=True)
top_movies.to_csv("output/analytics/top_movies.csv", index=False)
distribution.to_csv("output/analytics/distribution.csv", index=False)

print("✔ SQL analytics done")
