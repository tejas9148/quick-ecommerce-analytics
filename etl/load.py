import os
import pandas as pd

from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine

# -----------------------------
# LOAD ENV VARIABLES
# -----------------------------

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

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
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
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
    raise

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