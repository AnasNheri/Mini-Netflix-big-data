import pandas as pd
import os

# Load ratings
ratings = pd.read_csv("data/u.data", sep="\t", names=["userId", "movieId", "rating", "timestamp"])

# Cleaning
clean = ratings[(ratings["rating"] >= 1) & (ratings["rating"] <= 5)].drop_duplicates()

# Save clean data
os.makedirs("output/clean", exist_ok=True)
clean.to_csv("output/clean/ratings.csv", index=False)

print(f"✔ Cleaning done | Rows: {len(clean)}")
