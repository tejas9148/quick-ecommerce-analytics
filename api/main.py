from fastapi import FastAPI
from sqlalchemy import text

from api.database import engine

app = FastAPI()

# --------------------------------
# HOME ROUTE
# --------------------------------

@app.get("/")
def home():
    return {
        "message": "Quick Commerce Analytics API Running"
    }

# --------------------------------
# KPI API
# --------------------------------

@app.get("/kpi/average-delivery-time")
def average_delivery_time():

    query = text("""
        SELECT AVG("Time_taken (min)")
        AS avg_delivery_time
        FROM fact_orders;
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        avg_time = result.scalar()

    return {
        "average_delivery_time": round(avg_time, 2)
    }
@app.get("/kpi/delayed-orders")
def delayed_orders():

    query = text("""
        SELECT COUNT(*)
        FROM fact_orders
        WHERE delay_flag = TRUE;
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        delayed_count = result.scalar()

    return {
        "delayed_orders": delayed_count
    }