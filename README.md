# 📊 Sales & Inventory Forecasting System

An end-to-end data analytics and predictive web application designed to solve real-world retail inventory challenges using **Python, MySQL, Pandas, and Streamlit**.

---

## 🎯 The Core Business Problem
In the retail industry, inventory management is often driven by guesswork rather than empirical data. Without granular visibility into daily sales velocities and category-specific trends, store managers routinely run into two major financial pitfalls:
1. **Overstocking:** Storing slow-moving or perishable goods that tie up critical working capital and lead to dead inventory.
2. **Stockouts:** Running out of high-demand items during peak periods, resulting in direct revenue loss and frustrated customers.

## 💡 The Technical Solution & Real-World Questions Answered
To eliminate this guesswork, I built an interactive operational analytics platform that directly answers critical business questions for store managers and inventory planners:

* **"Which products or categories are driving our revenue growth?"** 
  * *Solution:* The app connects to a normalized **MySQL** database backend to pull real-time sales logs and aggregates them dynamically via **Pandas** to calculate total revenue and item quantities instantly.
* **"Are sales growing, stabilizing, or declining over time?"** 
  * *Solution:* Built-in rolling trends and forecasting models smooth out daily market volatility so stakeholders can see the true directional momentum of the business.
* **"What can we expect in customer demand over the next 7 days?"** 
  * *Solution:* Integrates a 7-day predictive forecasting model directly into the dashboard UI to guide proactive reordering schedules.

---

## 📈 Visual Showcase & System Walkthrough

### 1. Executive Dashboard & Daily Trend Analysis
*The main interface tracking high-level KPIs (Total Revenue, Total Items Sold) and daily revenue volatility.*

![Dashboard Main View](<Screenshot (74).png>)

### 2. Category Filtering & Raw Data Verification
*Allows users to drill down by product category (e.g., Electronics) while dynamically updating the underlying Pandas data frame preview.*

![Filtered Data View](<Screenshot (75).png>)

### 3. Predictive Forecasting Layer
*Visualizing historical performance alongside a 7-day forecast trend to support data-driven inventory planning.*

![Forecast Visualization](<Screenshot (76).jpg>)

*The corresponding raw data view displaying the predictive metrics side-by-side with actual revenue logs.*

![Forecast Data Table](<Screenshot (77).png>)

### 4. Backend Processing & Pipeline Execution
*Console output from VS Code illustrating the underlying execution of database queries, Pandas data manipulation, and model generation.*

![Python Terminal Output](<Screenshot (78).jpg>)

---

## 🛠️ Technical Stack
* **Frontend & Web UI:** Streamlit
* **Data Processing & Analytics:** Python, Pandas, NumPy
* **Database Management:** MySQL Server, MySQL Workbench
* **Version Control:** Git & GitHub

---

## 🚀 How to Run It Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Steph45.ac.ke-hue/SALES_AND_INVENTORY_FORECASTING_SYSTEM.git](https://github.com/Steph45.ac.ke-hue/SALES_AND_INVENTORY_FORECASTING_SYSTEM.git)
   cd SALES_AND_INVENTORY_FORECASTING_SYSTEM
Install required dependencies:

Bash
pip install streamlit mysql-connector-python pandas numpy
Configure Database:

Import the project database schema into your local MySQL server.

Update your database connection parameters inside app.py.

Launch the application:

Bash
streamlit run app.py