"""06_streaming_ratings.py
Simulate a lightweight streaming ingestion loop.

This script watches `stream/ratings` for CSV files, concatenates newly
arrived files into `output/streaming/new_ratings.csv`, and writes a few
simple metrics to `output/streaming/metrics`.
"""

import pandas as pd
import time
import os
from glob import glob

STREAM_DIR = "stream/ratings"
OUTPUT_DIR = "output/streaming"
METRICS_DIR = f"{OUTPUT_DIR}/metrics"

os.makedirs(METRICS_DIR, exist_ok=True)

# Keep track of processed filenames to avoid re-processing
processed_files = set()

print("▶ Streaming simulation started...")

while True:
    # Find all CSV files in the stream directory
    files = glob(f"{STREAM_DIR}/*.csv")

    new_files = [f for f in files if f not in processed_files]

    if new_files:
        dfs = []
        for f in new_files:
            # Read the new chunk and mark as processed
            df = pd.read_csv(f)
            dfs.append(df)
            processed_files.add(f)

        # Concatenate all new chunks and write a combined file
        data = pd.concat(dfs, ignore_index=True)
        data.to_csv(f"{OUTPUT_DIR}/new_ratings.csv", index=False)

        # Simple metrics: count, average rating and number of active users
        pd.DataFrame({"ratings_count": [len(data)]}).to_csv(f"{METRICS_DIR}/ratings_count.csv", index=False)
        pd.DataFrame({"avg_rating": [data["rating"].mean()]}).to_csv(f"{METRICS_DIR}/avg_rating.csv", index=False)
        pd.DataFrame({"active_users": [data["userId"].nunique()]}).to_csv(f"{METRICS_DIR}/users_active.csv", index=False)

        print(f"✔ Processed {len(data)} new ratings")

    # Wait between polling cycles (adjust for production)
    time.sleep(5)
