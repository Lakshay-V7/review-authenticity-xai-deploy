import pandas as pd

file_path = "dataset/preReviewsCSV.csv"

print("Loading only first 5 rows...")

df = pd.read_csv(file_path, nrows=5)

print("\n Dataset Columns:\n")
print(df.columns)

print("\n Sample Rows:\n")
print(df.head())
