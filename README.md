# 📊 TELCO Customer Churn Analytics

<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)

</p>

---

# 📌 Project Overview

The **TELCO Customer Churn Analytics** project is an end-to-end Data Analytics project developed using **Excel, Python, PostgreSQL, SQL, and Power BI**.

The project analyzes telecom customer data to understand customer churn behavior, identify high-risk customer segments, and generate actionable business insights for improving customer retention.

The complete analytics workflow includes:

**Data Cleaning → Python EDA → Visualization → PostgreSQL SQL Analysis → Power BI Dashboard → Business Insights**

> **Note:** Machine Learning is not included in the current version of this project.

---

# 🎯 Business Objectives

The project focuses on answering important business questions such as:

- What percentage of customers are churning?
- Which contract types have the highest churn?
- Which internet services are associated with higher churn?
- Which payment methods have higher churn rates?
- How does customer tenure relate to churn?
- Which customer segments represent the highest retention risk?
- Which customer characteristics are associated with lower or higher churn?
- What strategies can help improve customer retention?

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Excel | Data Cleaning & Validation |
| Python | Exploratory Data Analysis |
| Pandas | Data Manipulation & Analysis |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| PostgreSQL | Database Management |
| SQL | Business Analysis |
| Power BI | Interactive Dashboard |
| DAX | KPI Calculations |
| GitHub | Version Control & Portfolio |

---

# 📂 Project Structure

```text
TELCO-Customer-Churn-Analytics/
│
├── Excel/
│   └── Telco-Customer-Churn-Clean.xlsx
│
├── Python/
│   └── Customers-churn-EDA.py
│
├── SQL/
│   └── customer_churn_analysis.sql
│
├── Power BI/
│   ├── Customer-Churn.pbix
│   └── Customer-Churn.pdf
│
├── Images/
│   ├── Customer-Churn-Dashboard.png
│   └── Customer-Churn-Full-HD.png
│
└── README.md

GitHub: https://github.com/darshanpatel-IT
LinkedIn: https://www.linkedin.com/in/darshan-patel-a75124288

---

# 🧹 Data Cleaning

The dataset was cleaned and validated before performing analysis.

Data Cleaning Steps
Verified 7,043 customer records
Verified 21 columns
Checked duplicate rows → 0
Checked duplicate customer IDs → 0
Checked missing values
Investigated blank TotalCharges records
Found 11 blank TotalCharges values
Verified all 11 customers had tenure = 0
Replaced verified blank TotalCharges values with 0
Converted TotalCharges into a numeric field
Checked categorical columns for inconsistent values
Verified numerical fields such as tenure and MonthlyCharges

🐍 Python EDA

Python was used to perform exploratory data analysis and identify relationships between customer characteristics and churn.

EDA Analysis
Overall churn distribution
Gender vs Churn
Senior Citizen vs Churn
Partner vs Churn
Dependents vs Churn
Phone Service vs Churn
Multiple Lines vs Churn
Internet Service vs Churn
Online Security vs Churn
Online Backup vs Churn
Device Protection vs Churn
Tech Support vs Churn
Streaming TV vs Churn
Streaming Movies vs Churn
Contract vs Churn
Paperless Billing vs Churn
Payment Method vs Churn
Tenure Analysis
Monthly Charges Analysis
Total Charges Analysis
Tenure vs Total Charges
Correlation Analysis
Contract + Tenure Segmentation
Contract + Monthly Charges Segmentation
Internet Service + Contract Segmentation
Payment Method + Contract Segmentation

📊 Visualization

The Python analysis used Matplotlib and Seaborn to create visualizations including:

Count Plots
Bar Charts
Box Plots
Scatter Plots
Line Charts
Correlation Heatmaps

These visualizations were used to identify customer churn patterns and support business conclusions.

🗄️ PostgreSQL & SQL Analysis

The cleaned dataset was imported into PostgreSQL for business-oriented SQL analysis.

SQL Analysis Includes
Customer Churn KPIs
Average Tenure Analysis
Average Monthly Charge Analysis
Average Total Charge Analysis
Churn Contribution Analysis
Contract Analysis
Payment Method Analysis
Internet Service Analysis
Tenure Segmentation
High-Risk Customer Segmentation
Multi-dimensional Customer Analysis
CTEs
Aggregate Functions
FILTER
GROUP BY
HAVING
RANK()
DENSE_RANK()
ROW_NUMBER()
Window Functions

The project contains 25 business-focused SQL questions ranging from core KPIs to advanced customer segmentation.

📈 Power BI Dashboard

A professional one-page TELCO Customer Churn Analytics Dashboard was developed in Power BI.

Dashboard KPIs
Total Customers: 7,043
Churned Customers: 1,869
Churn Rate: 26.54%
Average Monthly Charges: $64.76
Average Tenure: 32.37 Months
Dashboard Visuals
Churn Rate by Contract Type
Churn Rate by Internet Service
Churn Rate by Payment Method
Churn Rate by Tenure
High-Risk Customer Segments Matrix
Conditional Formatting for Churn Risk
Interactive Filters
Key Insights Panel
Interactive Filters
Gender
Senior Citizen
Contract
Internet Service
Payment Method
Tech Support

---

# 🔥 Key Insights

Based on the analysis performed in Python, PostgreSQL, and Power BI, the following major business insights were identified:

📄 Contract Analysis
Month-to-month customers have the highest churn rate at 42.71%.
One-year contract customers have a churn rate of 11.27%.
Two-year contract customers have the lowest churn rate at 2.83%.
🌐 Internet Service Analysis
Fiber optic customers have the highest churn rate at 41.89%.
DSL customers have a churn rate of 18.96%.
Customers without internet service have the lowest churn rate at 7.40%.
💳 Payment Method Analysis
Electronic-check customers have the highest churn rate at 45.29%.
Mailed-check customers have a churn rate of 19.11%.
Bank-transfer customers have a churn rate of 16.71%.
Credit-card customers have the lowest churn rate at 15.24%.
⏳ Tenure Analysis
Customers with 0–12 months of tenure have a churn rate of 47.44%.
Customers with 61–72 months of tenure have a churn rate of only 6.61%.
Churn decreases substantially as customer tenure increases.
🛡 Service Analysis

Customers without additional services show substantially higher churn:

No OnlineSecurity → 41.77%
No TechSupport → 41.64%
No OnlineBackup → 39.93%
No DeviceProtection → 39.13%
🚨 High-Risk Customer Segments
🔴 Fiber Optic + Month-to-Month
Customer Count → 2,128
Churn Rate → 54.61%
🔴 Electronic Check + Month-to-Month
Customer Count → 1,850
Churn Rate → 53.73%
🔴 Fiber Optic + Month-to-Month + Electronic Check
Customer Count → 1,307
Churned Customers → 789
Churn Rate → 60.37%

This segment represents one of the strongest high-risk patterns identified in the analysis.

These results represent observed associations in the dataset and should not be interpreted as proof that a specific service, contract, or payment method causes churn.

---

# 💡 Business Recommendations

1. Improve First-Year Customer Retention
Strengthen customer onboarding.
Monitor customers during their first 12 months.
Introduce early engagement and retention programs.
2. Encourage Long-Term Contracts
Provide incentives for month-to-month customers to move toward one-year or two-year contracts.
Offer targeted discounts or value-added services.
3. Prioritize High-Risk Customer Segments
Monitor fiber-optic month-to-month customers closely.
Prioritize customers who combine multiple high-risk characteristics.
Develop targeted retention campaigns instead of treating all customers equally.
4. Investigate Payment Experience
Analyze why electronic-check customers show significantly higher churn.
Review payment convenience, customer experience, and billing processes.
Consider promoting automated payment options where appropriate.
5. Strengthen Customer Support
Investigate the high churn rate among customers without TechSupport and OnlineSecurity.
Consider targeted service bundles or retention offers.
Monitor whether support engagement improves customer retention.

---

# 📈 Expected Business Impact

Implementing these recommendations can help the business:

✅ Improve first-year customer retention
✅ Reduce customer churn
✅ Identify high-risk customers earlier
✅ Improve customer support strategies
✅ Optimize contract offerings
✅ Improve payment experience
✅ Strengthen customer loyalty
✅ Support data-driven retention decisions
✅ Improve customer lifetime value
⭐ Features
Interactive Power BI Dashboard
Dynamic KPI Cards
Customer Churn Analysis
High-Risk Customer Segmentation
Conditional Formatting
Interactive Slicers
Python EDA
Matplotlib Visualizations
Seaborn Visualizations
PostgreSQL Database
SQL Business Analysis
CTEs
Window Functions
DAX Measures
Business Insights
Data Cleaning & Validation

---

# 🚀 How to Run

1️⃣ Clone Repository
git clone https://github.com/darshanpatel-IT/TELCO-Customer-Churn-Analytics.git

2️⃣ Data Cleaning

Use the cleaned dataset available inside:

Excel/

3️⃣ Python EDA

Navigate to:

Python/

Run:

python Customers-churn-EDA.py

Install required packages:

pip install pandas matplotlib seaborn

4️⃣ PostgreSQL

Create a PostgreSQL database and import the cleaned dataset.

Then execute the SQL queries located inside:

SQL/

5️⃣ Power BI

Open:

Power BI/Customer-Churn.pbix

Refresh the data connection if required.

---

# 💼 Skills Demonstrated

Excel
Python
Pandas
Matplotlib
Seaborn
PostgreSQL
SQL
CTEs
Window Functions
Data Cleaning
Exploratory Data Analysis
Data Visualization
Data Segmentation
DAX
Power BI
Dashboard Design
Business Intelligence
Business Analysis
Customer Retention Analytics

---

# 📜 License

This project is developed for educational, internship, and portfolio purposes.

---

# 👨‍💻 Author

Darshan Patel

---

# Connect with me

GitHub: https://github.com/darshanpatel-IT
LinkedIn: https://www.linkedin.com/in/darshan-patel-a75124288

---


