from fastapi import APIRouter
from sqlalchemy import text

from api.database import engine

router = APIRouter(prefix="/operations")

# --------------------------------
# TOP DELAY CITIES
# --------------------------------

@router.get("/top-delay-cities")
def top_delay_cities():

    query = text("""
        SELECT
            "City",
            COUNT(*) AS delayed_orders

        FROM fact_orders

        WHERE delay_flag = TRUE

        GROUP BY "City"

        ORDER BY delayed_orders DESC;
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        data = []

        for row in result:

            data.append({
                "city": row[0],
                "delayed_orders": row[1]
            })

    return data

# --------------------------------
# VEHICLE PERFORMANCE
# --------------------------------

@router.get("/vehicle-performance")
def vehicle_performance():

    query = text("""
        SELECT
            "Type_of_vehicle",

            ROUND(
                AVG("Time_taken (min)")::numeric,
                2
            ) AS avg_delivery_time

        FROM fact_orders

        GROUP BY "Type_of_vehicle"

        ORDER BY avg_delivery_time;
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        data = []

        for row in result:

            data.append({
                "vehicle_type": row[0],
                "average_delivery_time": float(row[1])
            })

    return data