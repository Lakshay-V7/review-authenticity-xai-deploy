import pandas as pd

file_path = "dataset/preReviewsCSV.csv"

print("Loading dataset in chunks...")

fake_reviews = []
genuine_reviews = []

chunk_size = 200000

for chunk in pd.read_csv(file_path, usecols=["reviewContent", "label"], chunksize=chunk_size):

    # Separate classes
    fake_chunk = chunk[chunk["label"] == 0]
    genuine_chunk = chunk[chunk["label"] == 1]

    fake_reviews.append(fake_chunk)
    genuine_reviews.append(genuine_chunk)

    # Stop when enough collected
    if sum(len(x) for x in fake_reviews) >= 20000 and sum(len(x) for x in genuine_reviews) >= 8000:
        break

# Combine collected
fake_df = pd.concat(fake_reviews).head(20000)
genuine_df = pd.concat(genuine_reviews).head(8000)

# Balance dataset (Upsample Genuine)
genuine_df = genuine_df.sample(20000, replace=True, random_state=42)

final_df = pd.concat([fake_df, genuine_df]).sample(frac=1).reset_index(drop=True)

# Rename columns for training
final_df = final_df.rename(columns={
    "reviewContent": "text",
    "label": "target"
})

final_df.to_csv("dataset/yelp_balanced.csv", index=False)

print(" Balanced dataset saved: dataset/yelp_balanced.csv")
print(final_df["target"].value_counts())
