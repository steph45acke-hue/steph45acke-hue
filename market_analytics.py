import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(page_title="Market Analytics Hub", layout="wide")

st.title("📈 Stock Trading Platform Dashboard")
st.markdown("Database-backed financial analytics hub.")

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="stephen0111301468",
        database="stock_trading_db"
    )

tab1, tab2, tab3 = st.tabs(["💼 Net Worth Summary", "📊 Market Watchlist", "📜 Transaction History"])

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
        df = pd.read_sql(query1, conn)
        conn.close()
        st.dataframe(df, width='stretch')
    except Exception as e:
        st.error(f"Error: {e}")

with tab2:
    st.subheader("Live Stock Market Tickers")
    try:
        conn = get_db_connection()
        # Removed 'sector' column to match your database schema
        df = pd.read_sql("SELECT ticker, company_name, current_price FROM stocks;", conn)
        conn.close()
        st.dataframe(df, width='stretch')
    except Exception as e:
        st.error(f"Error: {e}")

with tab3:
    st.subheader("Platform Transaction Audit Log")
    try:
        conn = get_db_connection()
        # Adjusted columns to match standard transaction fields
        query3 = """
            SELECT 
                t.transaction_id, u.username, s.ticker, t.transaction_type, 
                t.shares, t.price_per_share, t.total_amount
            FROM transactions t
            JOIN users u ON t.user_id = u.user_id
            JOIN stocks s ON t.stock_id = s.stock_id;
        """
        df = pd.read_sql(query3, conn)
        conn.close()
        st.dataframe(df, width='stretch')
    except Exception as e:
        st.error(f"Error: {e}")