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
@app.get("/kpi/total-orders")
def total_orders():

    query = text("""
        SELECT COUNT(*)
        FROM fact_orders;
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        total = result.scalar()

    return {
        "total_orders": total
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

        delayed = result.scalar()

    return {
        "delayed_orders": delayed
    }
@app.get("/kpi/fast-delivery-percentage")
def fast_delivery_percentage():

    query = text("""
        SELECT
        ROUND(
            100.0 * SUM(
                CASE
                    WHEN delivery_speed = 'Fast'
                    THEN 1
                    ELSE 0
                END
            ) / COUNT(*),
            2
        )
        AS fast_percentage
        FROM fact_orders;
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        percentage = result.scalar()

    return {
        "fast_delivery_percentage": percentage
    }
@app.get("/analytics/city-performance")
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
@app.get("/analytics/peak-hours")
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
@app.get("/analytics/weather-impact")
def weather_impact():

    query = text("""
        SELECT
            "Weather_conditions",
            ROUND(
                AVG("Time_taken (min)")::numeric,
                2
            ) AS avg_delivery_time

        FROM fact_orders

        GROUP BY "Weather_conditions"

        ORDER BY avg_delivery_time DESC;
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        data = []

        for row in result:

            data.append({
                "weather": row[0],
                "average_delivery_time": float(row[1])
            })

    return data
@app.get("/operations/top-delay-cities")
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
@app.get("/operations/vehicle-performance")
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
@app.get("/operations/traffic-impact")
def traffic_impact():

    query = text("""
        SELECT
            "Road_traffic_density",

            ROUND(
                AVG("Time_taken (min)")::numeric,
                2
            ) AS avg_delivery_time

        FROM fact_orders

        GROUP BY "Road_traffic_density"

        ORDER BY avg_delivery_time DESC;
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        data = []

        for row in result:

            data.append({
                "traffic_density": row[0],
                "average_delivery_time": float(row[1])
            })

    return data