CAMPUSIQ — SALES ANALYTICS DASHBOARD
===================================

1. ABOUT THE PROJECT
--------------------
CampusIQ is a web-based Sales Analytics Dashboard developed to make sales data easier to understand and analyze.

The main idea behind this project is simple: businesses generate a lot of sales data, but raw data alone does not always provide useful insights. CampusIQ transforms that data into meaningful information through an interactive dashboard.

Users can explore sales performance, monitor revenue and profit, identify top-selling products, compare regions, and understand monthly sales trends — all from one place.

This project was developed as a practical portfolio project to demonstrate Python programming, data analysis, backend development, and frontend integration skills.

2. MAIN FEATURES
----------------
• Total Revenue: Displays the total revenue generated from sales.
• Net Profit: Calculates profit after deducting product costs.
• Orders Processed: Shows the number of unique orders.
• Units Sold: Displays the total quantity of products sold.
• Monthly Trends: Visualizes monthly revenue and profit.
• Category Analysis: Compares revenue across product categories.
• Regional Performance: Shows sales performance in different regions.
• Top Products: Identifies products generating the highest revenue.
• Interactive Filters: Filter data by date, category, and region.
• CSV Export: Download filtered sales records for further analysis.
• Responsive Design: Dashboard layout adapts to different screen sizes.

3. TECHNOLOGIES USED
--------------------
Python — Main programming language.
Flask — Backend framework for handling routes and API requests.
Pandas — Data cleaning, filtering, grouping, and analysis.
NumPy — Numerical calculations and data processing.
HTML5 — Dashboard structure.
CSS3 — Styling and responsive layout.
JavaScript — Frontend functionality and API integration.
Chart.js — Interactive charts and data visualization.
CSV — Storage format for sample sales data.
Pytest — Automated testing of analytics functions.

4. PROJECT STRUCTURE
--------------------
campusiq-sales-analytics/
|
|-- app.py
|-- analytics.py
|-- requirements.txt
|-- README.md
|
|-- data/
|   |-- sales.csv
|
|-- templates/
|   |-- index.html
|
|-- static/
|   |-- css/
|   |   |-- style.css
|   |
|   |-- js/
|       |-- dashboard.js
|
|-- tests/
    |-- test_analytics.py

5. HOW THE PROJECT WORKS
------------------------
The project follows a simple frontend-backend architecture.

Step 1: Sales records are stored in the CSV dataset.
Step 2: Pandas reads the dataset and prepares the data for analysis.
Step 3: NumPy is used for numerical calculations.
Step 4: Flask processes requests and provides the analyzed information through API endpoints.
Step 5: JavaScript receives the API response and updates the dashboard.
Step 6: Chart.js displays the information through interactive visualizations.

When a user changes a filter, the dashboard requests updated results from the backend.

6. INSTALLATION AND SETUP
-------------------------
Follow these steps to run CampusIQ on your computer.

Requirements:
• Python 3.10 or later
• pip
• A code editor such as Visual Studio Code
• A modern web browser

Step 1: Extract the ZIP file.

Step 2: Open the extracted project folder in Visual Studio Code.

Step 3: Open the terminal in the project directory.

Step 4: Create a virtual environment:

    python -m venv venv

Step 5: Activate the virtual environment.

For Windows:

    venv\Scripts\activate

For macOS/Linux:

    source venv/bin/activate

Step 6: Install the required packages:

    pip install -r requirements.txt

Step 7: Start the Flask application:

    python app.py

Step 8: Open your browser and visit:

    http://127.0.0.1:5000

The CampusIQ dashboard should now be running locally.

7. DATASET INFORMATION
----------------------
The project includes a sample dataset named sales.csv.

It contains 360 synthetic sales records created for demonstration and testing purposes.

Dataset columns:

• order_id — Unique order identification.
• order_date — Date of the order.
• product — Name of the purchased product.
• category — Product category.
• region — Sales region.
• quantity — Number of units sold.
• unit_price — Selling price per unit.
• unit_cost — Cost price per unit.

The application calculates additional values:

Revenue = Quantity × Unit Price

Cost = Quantity × Unit Cost

Profit = Revenue − Cost

Note: The included dataset is fictional sample data. It does not contain actual customer or business records.

8. API ENDPOINTS
----------------
CampusIQ provides the following Flask API endpoints:

GET /
Loads the main dashboard.

GET /api/dashboard
Returns dashboard summaries, chart data, and available filter options.

GET /api/dashboard?category=Electronics
Returns dashboard data for a selected category.

GET /api/dashboard?region=North
Returns dashboard data for a selected region.

GET /api/export
Downloads sales records as a CSV file.

GET /health
Checks whether the Flask application is running.

Available dashboard filters:
• start
• end
• category
• region

9. RUNNING TESTS
----------------
Automated tests are included to check important analytics functions.

Run the following command in your terminal:

    pytest -q

The tests cover:
• Sales summary calculations.
• Region-based filtering.
• Date-based filtering.
• Monthly chart data generation.

10. WHAT I LEARNED
------------------
While developing this project, I practiced several important software development concepts:

• Building a web application using Flask.
• Working with real-world-style tabular data using Pandas.
• Performing numerical calculations with NumPy.
• Creating and connecting REST API endpoints.
• Connecting frontend JavaScript with a Python backend.
• Displaying data using interactive charts.
• Applying filters to datasets.
• Organizing a project using a clean folder structure.
• Writing automated tests.
• Preparing a project for GitHub and portfolio presentation.

11. FUTURE IMPROVEMENTS
-----------------------
There are several features that could make CampusIQ even more powerful in the future:

• User authentication and login system.
• Database integration using SQLite or PostgreSQL.
• Uploading custom CSV and Excel files.
• Downloading reports in PDF format.
• Advanced sales forecasting.
• Machine learning-based sales predictions.
• More detailed business insights.
• Admin dashboard and user management.

12. PROJECT PURPOSE
-------------------
CampusIQ was created as a learning and portfolio project to demonstrate how Python and data analysis libraries can be used to solve practical business problems.

It brings together data processing, backend development, frontend design, and data visualization in one application.

The project reflects my interest in Python development, data analytics, and building practical software solutions.

13. DEVELOPER
-------------
Developed by: [Your Name]

Degree: BS Software Engineering

University: Virtual University of Pakistan

Skills demonstrated:
Python | Flask | Pandas | NumPy | HTML | CSS | JavaScript | Data Analysis | REST APIs

GitHub: [Add Your GitHub Repository Link]

LinkedIn: [Add Your LinkedIn Profile Link]

14. LICENSE
-----------
This project is available for educational and portfolio purposes. You may customize it and build upon it according to your requirements.

Thank you for exploring CampusIQ!

I hope this project gives you a clear idea of how raw sales data can be transformed into meaningful business insights.

===================================
CAMPUSIQ — TURNING DATA INTO INSIGHTS
===================================
