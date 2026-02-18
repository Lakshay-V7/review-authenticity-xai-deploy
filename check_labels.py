import pandas as pd

file_path = "dataset/preReviewsCSV.csv"

# Load only small part
df = pd.read_csv(file_path, usecols=["label"], nrows=20000)

print("Unique Labels in Dataset:")
print(df["label"].value_counts())
