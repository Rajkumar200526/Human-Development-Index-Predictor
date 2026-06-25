import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("dataset/hdi.csv", encoding="latin1")

# Remove empty column
df.drop(columns=["Unnamed: 6"], inplace=True)

# Rename columns
df.rename(columns={
    " (HDI) ": "HDI"
}, inplace=True)

# Remove commas from GNI
df["GNI"] = df["GNI"].astype(str).str.replace(",", "", regex=False)

# Convert numeric columns
df["HDI"] = pd.to_numeric(df["HDI"], errors="coerce")
df["LifeExpectancy"] = pd.to_numeric(df["LifeExpectancy"], errors="coerce")
df["ExpectedSchooling"] = pd.to_numeric(df["ExpectedSchooling"], errors="coerce")
df["MeanSchooling"] = pd.to_numeric(df["MeanSchooling"], errors="coerce")
df["GNI"] = pd.to_numeric(df["GNI"], errors="coerce")

# Remove rows without country
df.dropna(subset=["Country"], inplace=True)

# Fill missing numeric values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Display information
print(df.info())

print("\nFirst 5 Rows")
print(df.head())

# Save cleaned dataset
df.to_csv("dataset/clean_hdi.csv", index=False)

print("\nClean dataset saved successfully.")