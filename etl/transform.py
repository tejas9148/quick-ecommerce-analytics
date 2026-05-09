import pandas as pd
from pathlib import Path

# Read dataset
project_root = Path(__file__).resolve().parents[1]
df = pd.read_csv(project_root / "data" / "raw" / "orders.csv")

print("Original Shape:")
print(df.shape)

# -----------------------------
# REMOVE DUPLICATES
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# HANDLE NULL VALUES
# -----------------------------

# Fill numerical columns
df["Delivery_person_Age"] = df["Delivery_person_Age"].fillna(
    df["Delivery_person_Age"].median()
)

df["Delivery_person_Ratings"] = df["Delivery_person_Ratings"].fillna(
    df["Delivery_person_Ratings"].median()
)

df["multiple_deliveries"] = df["multiple_deliveries"].fillna(
    df["multiple_deliveries"].median()
)

# Fill categorical columns
df["Weather_conditions"] = df["Weather_conditions"].fillna("Unknown")

df["Road_traffic_density"] = df["Road_traffic_density"].fillna("Unknown")

df["Festival"] = df["Festival"].fillna("No")

df["City"] = df["City"].fillna("Unknown")

# Remove rows where order time is missing
df.dropna(subset=["Time_Orderd"], inplace=True)

# -----------------------------
# CONVERT DATE COLUMNS
# -----------------------------

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    dayfirst=True
)

# -----------------------------
# CREATE KPI COLUMNS
# -----------------------------

# Order hour
order_time = pd.to_datetime(
    df["Time_Orderd"],
    format="%H:%M",
    errors="coerce"
)
order_time = order_time.fillna(
    pd.to_datetime(
        pd.to_numeric(df["Time_Orderd"], errors="coerce"),
        unit="D",
        errors="coerce"
    )
)
df["order_hour"] = order_time.dt.hour

# Peak hour flag
df["peak_hour"] = df["order_hour"].between(18, 22)

# Delay flag
df["delay_flag"] = df["Time_taken (min)"] > 30

# Delivery speed category
df["delivery_speed"] = df["Time_taken (min)"].apply(
    lambda x:
    "Fast" if x <= 20
    else "Medium" if x <= 40
    else "Slow"
)

# -----------------------------
# FINAL DATASET INFO
# -----------------------------

print("\nCleaned Shape:")
print(df.shape)

print("\nNull Values After Cleaning:")
print(df.isnull().sum())

print("\nSample Data:")
print(df.head())

# -----------------------------
# SAVE CLEANED DATA
# -----------------------------

df.to_csv(
    project_root / "data" / "processed" / "clean_orders.csv",
    index=False
)

print("\nProcessed dataset saved successfully!")