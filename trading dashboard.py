import streamlit as st
import mysql.connector
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Stock Trading Dashboard", layout="wide")

st.title("📈 Stock Trading Platform Dashboard")
st.markdown("Welcome to your database-backed financial analytics hub.")

# Database Connection Function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          
        password="stephen0111301468",  
        database="stock_trading_db"
    )

# Create Sidebar Navigation Tabs
tab1, tab2, tab3 = st.tabs(["💼 Net Worth Summary", "📊 Market Watchlist", "📜 Transaction History"])

# --- TAB 1: NET WORTH SUMMARY ---
with tab1:
    st.subheader("Executive Net Worth Summary")
    try:
        conn = get_db_connection()
        query1 = """
            SELECT 
                u.username,
                u.cash_balance,
                COALESCE(eq.equity_value, 0) AS equity_portfolio_value,
                (u.cash_balance + COALESCE(eq.equity_value, 0)) AS total_net_worth
            FROM users u
            LEFT JOIN (
                SELECT 
                    p.user_id,
                    SUM(p.shares_owned * s.current_price) AS equity_value
                FROM portfolio p
                JOIN stocks s ON p.stock_id = s.stock_id
                GROUP BY p.user_id
            ) eq ON u.user_id = eq.user_id;
        """
        df_net_worth = pd.read_sql(query1, conn)
        conn.close()
        st.dataframe(df_net_worth, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading net worth data: {e}")

# --- TAB 2: MARKET WATCHLIST ---
with tab2:
    st.subheader("Live Stock Market Tickers")
    try:
        conn = get_db_connection()
        query2 = "SELECT ticker, company_name, current_price, sector FROM stocks;"
        df_stocks = pd.read_sql(query2, conn)
        conn.close()
        st.dataframe(df_stocks, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading stocks data: {e}")

# --- TAB 3: TRANSACTION HISTORY ---
with tab3:
    st.subheader("Platform Transaction Audit Log")
    try:
        conn = get_db_connection()
        query3 = """
            SELECT 
                t.transaction_id,
                u.username,
                s.ticker,
                t.transaction_type,
                t.shares,
                t.price_per_share,
                t.total_amount,
                t.transaction_date
            FROM transactions t
            JOIN users u ON t.user_id = u.user_id
            JOIN stocks s ON t.stock_id = s.stock_id
            ORDER BY t.transaction_date DESC;
        """
        df_transactions = pd.read_sql(query3, conn)
        conn.close()
        st.dataframe(df_transactions, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading transaction history: {e}")