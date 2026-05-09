import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# -----------------------------
# PROJECT ROOT
# -----------------------------

project_root = Path(__file__).resolve().parents[1]

# -----------------------------
# READ CLEANED DATA
# -----------------------------

df = pd.read_csv(
    project_root /
    "data" /
    "processed" /
    "clean_orders.csv"
)

print("Dataset Loaded:")
print(df.shape)

# -----------------------------
# DATABASE CONNECTION
# -----------------------------


DATABASE_URL = (
    "postgresql://postgres:Tejas%40555@localhost:5432/quick_commerce_db"
)

engine = create_engine(DATABASE_URL)

# -----------------------------
# TEST CONNECTION
# -----------------------------

try:
    with engine.connect() as conn:
        print("Database Connected Successfully!")

except Exception as e:
    print("Connection Failed")
    print(e)

    # -----------------------------
# LOAD DATA INTO POSTGRESQL
# -----------------------------

df.to_sql(
    "fact_orders",
    engine,
    if_exists="replace",
    index=False
)

print("\nData loaded into PostgreSQL successfully!")