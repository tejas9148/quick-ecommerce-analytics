import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# --------------------------------
# LOAD ENV VARIABLES
# --------------------------------

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# --------------------------------
# ENCODE PASSWORD
# --------------------------------

encoded_password = quote_plus(DB_PASSWORD)

# --------------------------------
# DATABASE URL
# --------------------------------

DATABASE_URL = (
    f"postgresql://{DB_USER}:{encoded_password}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# --------------------------------
# CREATE ENGINE
# --------------------------------

engine = create_engine(DATABASE_URL)