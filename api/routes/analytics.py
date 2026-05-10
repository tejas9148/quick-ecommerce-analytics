from fastapi import APIRouter
from sqlalchemy import text

from api.database import engine

router = APIRouter(prefix="/analytics")

# --------------------------------
# CITY PERFORMANCE
# --------------------------------

@router.get("/city-performance")
def city_performance():

    query = text("""
        SELECT
            "City",

            ROUND(
                AVG("Time_taken (min)")::numeric,
                2
            ) AS avg_delivery_time

        FROM fact_orders

        GROUP BY "City"

        ORDER BY avg_delivery_time DESC;
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        data = []

        for row in result:

            data.append({
                "city": row[0],
                "average_delivery_time": float(row[1])
            })

    return data

# --------------------------------
# PEAK HOURS
# --------------------------------

@router.get("/peak-hours")
def peak_hours():

    query = text("""
        SELECT
            order_hour,
            COUNT(*) AS total_orders

        FROM fact_orders

        GROUP BY order_hour

        ORDER BY total_orders DESC;
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        data = []

        for row in result:

            data.append({
                "hour": int(row[0]),
                "total_orders": row[1]
            })

    return data