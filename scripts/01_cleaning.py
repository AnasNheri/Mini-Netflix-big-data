"""01_cleaning.py
Data cleaning for raw MovieLens-style ratings with timestamp conversion.
"""

import pandas as pd
import os
from datetime import datetime, timezone

# Load raw ratings
ratings = pd.read_csv(
    "data/u.data",
    sep="\t",
    names=["userId", "movieId", "rating", "timestamp"]
)

# Keep only valid rating values (1-5) and drop exact duplicate records
clean = ratings[(ratings["rating"] >= 1) & (ratings["rating"] <= 5)].drop_duplicates()

# Function to safely convert timestamp to YYYY-MM-DD (timezone-aware, future-proof)
def convert_timestamp(ts):
    try:
        if pd.isna(ts):
            return None
        # If timestamp is very large, it may be in milliseconds → convert to seconds
        if ts > 4102444800:  # after year 2100
            ts = ts / 1000
        date = datetime.fromtimestamp(ts, tz=timezone.utc)
        # Filter out unrealistic dates
        if date.year < 1970 or date.year > 2100:
            return None
        return date.strftime("%Y-%m-%d")
    except:
        return None

# Apply conversion
clean["date"] = clean["timestamp"].apply(convert_timestamp)

# Ensure output directory exists and write cleaned file
os.makedirs("output/clean", exist_ok=True)
clean.to_csv("output/clean/ratings.csv", index=False)

print(f"✔ Cleaning done | Rows: {len(clean)}")
