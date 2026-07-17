import requests
import os
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib


def create_embedding(text_list):
    all_embeddings = []

    batch_size = 32

    for i in range(0, len(text_list), batch_size):

        batch = text_list[i:i + batch_size]

        r = requests.post(
            "http://localhost:11434/api/embed",
            json={
                "model": "bge-m3:latest",
                "input": batch
            }
        )

        r.raise_for_status()

        all_embeddings.extend(r.json()["embeddings"])

    return all_embeddings


jsons = os.listdir("jsons")

my_dicts = []
chunk_id = 0

for json_file in jsons:

    with open(f"jsons/{json_file}", "r", encoding="utf-8") as f:
        content = json.load(f)

    print(f"\nCreating Embeddings for {json_file}")

    texts = [c["text"] for c in content["chunks"]]

    print("\n========== DEBUG ==========")
    print("texts type:", type(texts))
    print("texts length:", len(texts))
    print("first text type:", type(texts[0]))
    print("first text:")
    print(texts[0])
    print("===========================\n")

    embeddings = create_embedding(texts)

    for i, chunk in enumerate(content["chunks"]):

        chunk["chunk_id"] = chunk_id
        chunk["embedding"] = embeddings[i]

        chunk_id += 1

        my_dicts.append(chunk)

    

df = pd.DataFrame.from_records(my_dicts)

# print(df)

# Save this data frame
joblib.dump(df, 'embeddings.joblib')

print("\nFinished Successfully.")


