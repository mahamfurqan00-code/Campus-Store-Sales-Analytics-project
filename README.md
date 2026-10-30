# Campus-Store-Sales-Analytics-project
📌 Project Overview

This project analyzes sales data from three TFES campus stores for June 2026 using Python, NumPy, and pandas. The dataset contains intentionally messy data, including duplicate records, missing values, and inconsistent product names, to simulate real-world data cleaning and analysis.

The objective is to transform raw sales data into a clean, analysis-ready dataset and generate meaningful business insights such as top-selling products, branch performance, revenue analysis, outlier transactions, and inventory restocking requirements.

🎯 Learning Objectives
Load and inspect CSV datasets using pandas
Clean real-world messy datasets
Handle missing values and duplicate records
Perform feature engineering
Apply NumPy aggregations and broadcasting
Analyze sales using pandas groupby and pivot tables
Merge multiple datasets
Identify products requiring restocking
Export cleaned datasets
🛠 Technologies Used
Python 3
NumPy
pandas
Matplotlib
📂 Project Structure
Campus_Store_Sales_Analytics/
│
├── campus_store_sales.csv
├── store_inventory.csv
├── sales_analysis.ipynb
├── campus_store_sales_clean.csv
└── README.md
📈 Features Implemented
✅ Data Loading & Inspection
Loaded sales and inventory datasets
Displayed dataset information
Checked missing values
Identified duplicate records
Generated statistical summary
✅ Data Cleaning
Removed duplicate rows
Standardized product names
Filled missing unit prices using product-wise averages
Converted date column to datetime format
✅ Feature Engineering
Created Revenue column
Revenue = Units Sold × Unit Price
Calculated Net Revenue after applying branch-specific tax rates
📊 NumPy Analysis

Performed the following calculations using NumPy:

Total Revenue
Mean Revenue per Transaction
Standard Deviation
90th Percentile Revenue
Outlier Transaction Detection
Tax Broadcasting
📊 Business Analysis
Total Revenue by Product
Highest Revenue Product
Revenue by Category and Branch
Pivot Table Analysis
Most Frequently Sold Product
📦 Inventory Analysis

Merged sales data with inventory data to:

Compare Stock Quantity and Reorder Level
Identify products requiring restocking
📤 Output

The cleaned and merged dataset is exported as:

campus_store_sales_clean.csv
📉 Visualization

The project includes a line chart showing:

Daily Revenue Trend
Revenue Pattern Across June 2026
📚 Skills Demonstrated
Data Cleaning
Data Wrangling
Exploratory Data Analysis (EDA)
NumPy Arrays
Broadcasting
Boolean Indexing
pandas GroupBy
Pivot Tables
Data Merging
CSV Processing
Business Data Analysis
Data Visualization

## Interactive Flask Dashboard

This repository also includes the CampusIQ Flask dashboard as a self-contained project in [`campusiq-dashboard/`](./campusiq-dashboard/). See its [README](./campusiq-dashboard/README.md) for setup and run instructions.
