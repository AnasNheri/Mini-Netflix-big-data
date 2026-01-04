"""02_sql_analytics.py
Generate simple analytics CSVs from cleaned ratings.

Produces `top_movies.csv` (average rating and count per movie) and
`distribution.csv` (number of ratings per rating value).
"""

import pandas as pd
import os

# Read cleaned ratings produced by `01_cleaning.py`
ratings = pd.read_csv("output/clean/ratings.csv")

# Compute per-movie metrics: mean rating and total number of ratings
top_movies = ratings.groupby("movieId").agg(
    avg_rating=("rating", "mean"),
    total_ratings=("rating", "count")
).reset_index().sort_values("avg_rating", ascending=False)

# Compute distribution of rating values (1..5)
distribution = ratings.groupby("rating").size().reset_index(name="count").sort_values("rating")

# Ensure output directory and write analytics CSVs
os.makedirs("output/analytics", exist_ok=True)
top_movies.to_csv("output/analytics/top_movies.csv", index=False)
distribution.to_csv("output/analytics/distribution.csv", index=False)

print("✔ SQL analytics done")
