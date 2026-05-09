import pandas as pd

df = pd.read_csv("data/raw/orders.csv")

print(df.head())
print("\nFIRST 5 ROWS")
print(df.head())

# Dataset shape
print("\nDATASET SHAPE")
print(df.shape)

# Column names
print("\nCOLUMN NAMES")
print(df.columns)

# Data types
print("\nDATA TYPES")
print(df.dtypes)

# Null values
print("\nNULL VALUES")
print(df.isnull().sum())