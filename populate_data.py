import mysql.connector
from datetime import datetime, timedelta
import random

# 1. Connect to your local MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",        
    password="stephen0111301468",       
    database="sales_inventory_forecasting_db"
)

cursor = db.cursor()

print("Connected to database successfully!")

# 2. Insert Sample Products
products_data = [
    ("Wireless Mouse", "Electronics", 15.00, 29.99),
    ("Mechanical Keyboard", "Electronics", 45.00, 89.99),
    ("Gaming Headset", "Electronics", 30.00, 59.99),
    ("USB-C Hub", "Accessories", 10.00, 24.99),
    ("Laptop Stand", "Accessories", 12.00, 29.99)
]

# Insert products and keep track of their IDs
product_ids = []
for prod in products_data:
    cursor.execute("""
        INSERT INTO products (product_name, category, unit_cost, unit_price) 
        VALUES (%s, %s, %s, %s)
    """, prod)
    db.commit()
    product_ids.append(cursor.lastrowid)

print("Products inserted successfully!")

# 3. Generate 6 Months of Historical Sales Data
# We simulate daily sales for each product from 6 months ago up to today
start_date = datetime.now() - timedelta(days=180)

for product_id in product_ids:
    # Fetch unit price for this product
    cursor.execute("SELECT unit_price FROM products WHERE product_id = %s", (product_id,))
    price = cursor.fetchone()[0]
    
    current_date = start_date
    while current_date <= datetime.now():
        # Simulate realistic daily sales quantity (e.g., between 0 and 10 items sold per day)
        # Adding a bit of random fluctuation to mimic real-world trends
        quantity_sold = random.randint(0, 8)
        
        if quantity_sold > 0:
            total_revenue = quantity_sold * price
            sale_date_str = current_date.strftime('%Y-%m-%d')
            
            cursor.execute("""
                INSERT INTO sales (product_id, sale_date, quantity_sold, total_revenue)
                VALUES (%s, %s, %s, %s)
            """, (product_id, sale_date_str, quantity_sold, total_revenue))
            
        current_date += timedelta(days=1)

db.commit()
print("Historical sales data generated and inserted successfully!")

# 4. Initialize Inventory Levels
for product_id in product_ids:
    cursor.execute("""
        INSERT INTO inventory (product_id, stock_on_hand, reorder_threshold, last_restock_date)
        VALUES (%s, %s, %s, %s)
    """, (product_id, 50, 10, datetime.now().strftime('%Y-%m-%d')))

db.commit()
print("Inventory levels initialized successfully!")

# Close connection
cursor.close()
db.close()