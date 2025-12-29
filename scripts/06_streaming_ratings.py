import pandas as pd
import time
import os
from glob import glob

STREAM_DIR = "stream/ratings"
OUTPUT_DIR = "output/streaming"
METRICS_DIR = f"{OUTPUT_DIR}/metrics"

os.makedirs(METRICS_DIR, exist_ok=True)

processed_files = set()

print("▶ Streaming simulation started...")

while True:
    files = glob(f"{STREAM_DIR}/*.csv")

    new_files = [f for f in files if f not in processed_files]

    if new_files:
        dfs = []
        for f in new_files:
            df = pd.read_csv(f)
            dfs.append(df)
            processed_files.add(f)

        data = pd.concat(dfs, ignore_index=True)

        # Save all new ratings
        data.to_csv(f"{OUTPUT_DIR}/new_ratings.csv", index=False)

        # METRICS
        pd.DataFrame({
            "ratings_count": [len(data)]
        }).to_csv(f"{METRICS_DIR}/ratings_count.csv", index=False)

        pd.DataFrame({
            "avg_rating": [data["rating"].mean()]
        }).to_csv(f"{METRICS_DIR}/avg_rating.csv", index=False)

        pd.DataFrame({
            "active_users": [data["userId"].nunique()]
        }).to_csv(f"{METRICS_DIR}/users_active.csv", index=False)

        print(f"✔ Processed {len(data)} new ratings")

    time.sleep(5)
