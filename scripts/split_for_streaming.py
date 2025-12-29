import pandas as pd
import os

INPUT = "output/clean/ratings.csv"
OUTPUT = "stream/ratings_backup"
CHUNK_SIZE = 50  # taille réaliste pour streaming

os.makedirs(OUTPUT, exist_ok=True)

df = pd.read_csv(INPUT)

for i in range(0, len(df), CHUNK_SIZE):
    chunk = df.iloc[i:i+CHUNK_SIZE]
    filename = f"ratings_{i//CHUNK_SIZE:04d}.csv"
    chunk.to_csv(os.path.join(OUTPUT, filename), index=False)
    print(f"✔ Created {filename}")
print("✔ Splitting for streaming done")