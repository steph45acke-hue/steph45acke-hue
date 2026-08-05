import streamlit as st
import mysql.connector
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Sales & Inventory Dashboard", page_icon="📈", layout="wide")

st.title("📊 Sales & Inventory Forecasting Dashboard")
st.write("Welcome to your live operational analytics platform powered by MySQL, Pandas, and Streamlit.")

# 2. Connect to Database and Load Data
@st.cache_resource
def load_data():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="stephen0111301468",
        database="sales_inventory_forecasting_db"
    )
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
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    return df

df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Filter Options")
selected_category = st.sidebar.selectbox("Select Product Category", options=["All"] + list(df['category'].unique()))

if selected_category != "All":
    filtered_df = df[df['category'] == selected_category]
else:
    filtered_df = df

# 4. Key Metrics Display (KPIs)
total_rev = filtered_df['total_revenue'].sum()
total_items = filtered_df['quantity_sold'].sum()

col1, col2 = st.columns(2)
col1.metric("Total Revenue", f"${total_rev:,.2f}")
col2.metric("Total Items Sold", f"{total_items:,}")

st.markdown("---")

# 5. Visualizations & Forecasting Trend
st.subheader("📈 Daily Revenue & 7-Day Forecast Trend")

# Group by date and compute daily revenue
daily_trend = filtered_df.groupby('sale_date')['total_revenue'].sum().reset_index()
daily_trend = daily_trend.sort_values('sale_date')

# Calculate the rolling forecast trend
daily_trend['forecast_trend'] = daily_trend['total_revenue'].rolling(window=7).mean()

# Set index to sale_date for clean multi-line charting in Streamlit
chart_data = daily_trend.set_index('sale_date')[['total_revenue', 'forecast_trend']]

st.line_chart(chart_data)

st.subheader("📋 Raw Data Preview")
st.dataframe(filtered_df.head(10))