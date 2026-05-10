from fastapi import APIRouter
from sqlalchemy import text

from api.database import engine

router = APIRouter(prefix="/kpi")

# --------------------------------
# TOTAL ORDERS
# --------------------------------

@router.get("/total-orders")
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

# --------------------------------
# AVERAGE DELIVERY TIME
# --------------------------------

@router.get("/average-delivery-time")
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

# --------------------------------
# DELAYED ORDERS
# --------------------------------

@router.get("/delayed-orders")
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