import os
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy import sparse

# Fast user similarity using sparse matrix + NearestNeighbors (cosine)
ratings = pd.read_csv("output/clean/ratings.csv")

# Map ids to indices
user_ids = ratings["userId"].unique()
movie_ids = ratings["movieId"].unique()
user_to_idx = {u: i for i, u in enumerate(user_ids)}
movie_to_idx = {m: i for i, m in enumerate(movie_ids)}

n_users = len(user_ids)
n_items = len(movie_ids)

# Build sparse user x item matrix
rows = ratings["userId"].map(user_to_idx)
cols = ratings["movieId"].map(movie_to_idx)
data = ratings["rating"]

user_item = sparse.csr_matrix((data, (rows, cols)), shape=(n_users, n_items))

# Use NearestNeighbors with cosine distance (1 - cosine_similarity)
# We'll compute top_k neighbors for each user (excluding self)
top_k = 10
nn = NearestNeighbors(n_neighbors=top_k + 1, metric="cosine", algorithm="brute", n_jobs=-1)
nn.fit(user_item)

distances, indices = nn.kneighbors(user_item, return_distance=True)

results = []
for ui in range(n_users):
    u_id = user_ids[ui]
    for dist, idx in zip(distances[ui], indices[ui]):
        if idx == ui:
            continue
        sim = 1.0 - dist
        if sim <= 0:
            continue
        results.append({"user1": int(u_id), "user2": int(user_ids[idx]), "cosine_similarity": float(sim)})

sim_df = pd.DataFrame(results)

# Optional: filter by threshold and keep top_k per user
threshold = 0.8
sim_df = sim_df[sim_df["cosine_similarity"] >= threshold]

os.makedirs("output/similarity", exist_ok=True)
sim_df.to_csv("output/similarity/users.csv", index=False)

print(f"✔ User similarity computed | pairs: {len(sim_df)}")
