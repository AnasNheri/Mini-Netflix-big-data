import pandas as pd
import time
import os

rmse_value = 1.05  # valeur simulée ou récupérée
timestamp = int(time.time())

rmse_df = pd.DataFrame(
    {"rmse": [rmse_value], "timestamp": [timestamp]}
)

os.makedirs("output/metrics", exist_ok=True)

# Append to existing file if it exists
metrics_file = "output/metrics/rmse.csv"
if os.path.exists(metrics_file):
    existing_df = pd.read_csv(metrics_file)
    rmse_df = pd.concat([existing_df, rmse_df], ignore_index=True)

rmse_df.to_csv(metrics_file, index=False)

print("✔ RMSE tracked")
