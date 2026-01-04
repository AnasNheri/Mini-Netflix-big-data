"""split_for_streaming.py
Split the cleaned ratings CSV into small chunk files for streaming tests.

This utility slices `output/clean/ratings.csv` into smaller CSV files in
`stream/ratings_backup` which can then be used by the streaming simulator.
"""

import pandas as pd
import os

INPUT = "output/clean/ratings.csv"
OUTPUT = "stream/ratings_backup"
CHUNK_SIZE = 50  # taille réaliste pour streaming

os.makedirs(OUTPUT, exist_ok=True)

# Read the full cleaned file and write consecutive chunk files
df = pd.read_csv(INPUT)

for i in range(0, len(df), CHUNK_SIZE):
    chunk = df.iloc[i:i+CHUNK_SIZE]
    filename = f"ratings_{i//CHUNK_SIZE:04d}.csv"
    chunk.to_csv(os.path.join(OUTPUT, filename), index=False)
    print(f"✔ Created {filename}")
print("✔ Splitting for streaming done")