import pandas as pd

file_path = "dataset/preReviewsCSV.csv"

label_counts = {}

chunk_size = 200000  # 2 lakh rows per chunk

for chunk in pd.read_csv(file_path, usecols=["label"], chunksize=chunk_size):
    counts = chunk["label"].value_counts()

    for label, count in counts.items():
        label_counts[label] = label_counts.get(label, 0) + count

print("\nFull Dataset Label Distribution:\n")
print(label_counts)
