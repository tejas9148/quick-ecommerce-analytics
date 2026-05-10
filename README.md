# Quick Commerce Delivery Analytics Platform

## Project Overview

The Quick Commerce Delivery Analytics Platform is an end-to-end Data Engineering and Analytics project built to analyze delivery operations for quick commerce companies such as Blinkit, Swiggy Instamart, Zepto, and Zomato.

This project simulates a real-world analytics architecture where raw delivery data is transformed into business insights through:

* ETL Pipelines
* PostgreSQL Data Warehouse
* FastAPI Analytics APIs
* Power BI Dashboards

The platform helps analyze:

* Delivery efficiency
* Delayed orders
* Peak order hours
* Traffic impact
* Weather impact
* City-wise delivery performance
* Vehicle performance

---

# Project Architecture

```text
Raw CSV Dataset
        ↓
Python ETL Pipeline
        ↓
PostgreSQL Data Warehouse
        ↓
FastAPI Analytics APIs
        ↓
Power BI Dashboard
```

---

# Tech Stack

| Category              | Tools Used    |
| --------------------- | ------------- |
| Programming Language  | Python        |
| Data Processing       | Pandas, NumPy |
| Database              | PostgreSQL    |
| ORM / DB Connection   | SQLAlchemy    |
| API Framework         | FastAPI       |
| API Server            | Uvicorn       |
| Environment Variables | python-dotenv |
| Dashboarding          | Power BI      |
| Version Control       | Git & GitHub  |

---

# Features

## ETL Pipeline

* Reads raw delivery dataset
* Cleans missing values
* Removes duplicates
* Converts date columns
* Creates KPI columns
* Stores transformed data in PostgreSQL

---

## PostgreSQL Data Warehouse

The warehouse stores transformed delivery analytics data inside:

```text
fact_orders
```

The warehouse supports:

* SQL analytics
* Dashboard integration
* API-based analytics serving
* Operational reporting

---

## FastAPI Backend

The backend exposes analytics through REST APIs.

### KPI APIs

| Endpoint                        | Purpose                    |
| ------------------------------- | -------------------------- |
| `/kpi/total-orders`             | Total number of orders     |
| `/kpi/average-delivery-time`    | Average delivery time      |
| `/kpi/delayed-orders`           | Total delayed deliveries   |
| `/kpi/fast-delivery-percentage` | Fast delivery success rate |

---

### Analytics APIs

| Endpoint                      | Purpose                      |
| ----------------------------- | ---------------------------- |
| `/analytics/city-performance` | City-wise delivery analysis  |
| `/analytics/peak-hours`       | Peak ordering hours          |
| `/analytics/weather-impact`   | Weather impact on deliveries |

---

### Operational APIs

| Endpoint                          | Purpose                      |
| --------------------------------- | ---------------------------- |
| `/operations/top-delay-cities`    | Cities with highest delays   |
| `/operations/vehicle-performance` | Vehicle delivery performance |
| `/operations/traffic-impact`      | Traffic density impact       |

---

# Power BI Dashboard

The Power BI dashboard provides:

## KPI Cards

* Total Orders
* Average Delivery Time
* Delayed Orders
* Fast Delivery Percentage

---

## Analytics Visualizations

* City delivery performance
* Peak hour analysis
* Traffic impact analysis
* Weather impact analysis
* Vehicle performance analysis
* Daily order trends

---

# Dataset Information

The dataset contains delivery order information including:

* Delivery person details
* Order timestamps
* Delivery locations
* Weather conditions
* Traffic density
* Vehicle type
* Delivery time
* City information

### Dataset Size

* Rows: ~45,000+
* Columns: 20+

---

# ETL Workflow

## Step 1 — Extract

Read raw CSV dataset using Pandas.

## Step 2 — Transform

Data cleaning operations:

* Remove duplicates
* Handle missing values
* Convert dates and times
* Create derived KPI columns

### Engineered Columns

| Column           | Description                            |
| ---------------- | -------------------------------------- |
| `order_hour`     | Hour of order                          |
| `peak_hour`      | Peak order flag                        |
| `delay_flag`     | Delayed delivery indicator             |
| `delivery_speed` | Fast / Medium / Slow delivery category |

## Step 3 — Load

Load transformed data into PostgreSQL warehouse.

---

# API Architecture

The backend uses modular FastAPI architecture.

```text
api/
├── main.py
├── database.py
└── routes/
    ├── analytics.py
    ├── kpi.py
    └── operations.py
```

---

# Project Folder Structure

```text
quick-commerce-analytics/
│
├── api/
│   ├── main.py
│   ├── database.py
│   └── routes/
│       ├── analytics.py
│       ├── kpi.py
│       └── operations.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dashboard/
│   └── quick_commerce_dashboard.pbix
│
├── etl/
│   ├── transform.py
│   └── load.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# How to Run the Project

## 1. Clone Repository

```bash
git clone <your-github-repo-link>
cd quick-commerce-analytics
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create `.env` file:

```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=quick_commerce_db
```

---

## 5. Run ETL Pipeline

### Transform Data

```bash
python etl/transform.py
```

### Load Data into PostgreSQL

```bash
python etl/load.py
```

---

## 6. Run FastAPI Server

```bash
uvicorn api.main:app --reload
```

---

## 7. Open API Documentation

```text
http://127.0.0.1:8000/docs
```

---

# Sample API Responses

## Average Delivery Time API

```json
{
  "average_delivery_time": 26.29
}
```

---

## Total Orders API

```json
{
  "total_orders": 43853
}
```

---

# Key Business Insights

The platform helps answer important business questions:

* Which cities have the highest delays?
* What are the busiest ordering hours?
* How does traffic affect delivery times?
* Which vehicles perform best?
* How does weather impact operations?
* What percentage of deliveries are fast?

---

# Real-World Relevance

This project simulates real analytics systems used by:

* Blinkit
* Swiggy Instamart
* Zepto
* Zomato
* Uber Eats

The architecture reflects real-world:

* ETL systems
* Data warehouses
* Backend analytics services
* Business intelligence platforms

---

# Future Improvements

Future versions of the project can include:

* Apache Airflow scheduling
* Docker containerization
* Cloud deployment
* Snowflake warehouse integration
* AWS S3 data lake
* Real-time streaming with Kafka
* Machine learning delivery prediction
* Authentication & authorization

---

# Skills Demonstrated

This project demonstrates:

* Data Engineering
* ETL Development
* SQL Analytics
* PostgreSQL Warehousing
* FastAPI Backend Development
* Business Intelligence Dashboarding
* API Development
* Data Cleaning & Transformation
* Analytics Engineering

---

# Conclusion

The Quick Commerce Delivery Analytics Platform is a complete end-to-end analytics project that combines:

* Data Engineering
* Backend Analytics APIs
* Data Warehousing
* Business Intelligence

The project showcases how raw operational delivery data can be transformed into actionable business insights using modern analytics engineering practices.

---

# Author

Tejas

Computer Science & Engineering Student
