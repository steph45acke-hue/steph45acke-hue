import mysql.connector
import pandas as pd

# 1. Connect to your MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="stephen0111301468", 
    database="sales_inventory_forecasting_db"
)

# 2. Query the data
query = """
    SELECT 
        s.sale_date,
        p.product_name,
        p.category,
        s.quantity_sold,
        s.total_revenue
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
"""

df = pd.read_sql(query, db)
db.close()

# 3. Prepare data for forecasting
# Convert sale_date to actual datetime objects and sort chronologically
df['sale_date'] = pd.to_datetime(df['sale_date'])
daily_sales = df.groupby('sale_date')['total_revenue'].sum().reset_index()
daily_sales = daily_sales.sort_values('sale_date')

# 4. Simple Moving Average Forecasting (Smoothing out trends to predict next steps)
# We calculate a 7-day rolling average to see the baseline trend
daily_sales['forecast_trend'] = daily_sales['total_revenue'].rolling(window=7).mean()

print("\n--- Sales Forecasting & Trend Analysis ---")
print(daily_sales.tail(10))