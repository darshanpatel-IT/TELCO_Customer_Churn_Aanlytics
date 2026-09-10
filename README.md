TELCO Customer Churn Analytics

An end-to-end Customer Churn Analytics project built to understand why telecom customers leave, identify high-risk customer segments, and present actionable business insights using Excel, Python, PostgreSQL, and Power BI.

Current scope: Data cleaning, exploratory data analysis, SQL business analysis, and an interactive Power BI dashboard.
Machine learning is not included in the current version.

📌 Business Problem

Customer churn is a major challenge for subscription-based telecom businesses.

This project aims to answer:

How many customers are churning?

Which customer characteristics are associated with higher churn?

Which services, contracts, and payment methods show higher churn?

Which customer segments represent the greatest retention risk?

What actions could help improve customer retention?

📂 Dataset

Dataset: Telco Customer Churn

Records: 7,043 customers
Features: 21 columns

Main Variables

Category

Variables

Customer profile

gender, SeniorCitizen, Partner, Dependents

Services

PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies

Contract & billing

Contract, PaperlessBilling, PaymentMethod

Financial

MonthlyCharges, TotalCharges

Customer lifecycle

tenure

Target

Churn

🧹 Data Cleaning

The dataset was reviewed and cleaned before analysis.

Data-quality checks

Verified 7,043 records and 21 columns

Checked for duplicate rows → 0 duplicates

Checked for duplicate customer IDs → 0 duplicates

Checked for missing values

Investigated blank TotalCharges values

Found 11 blank TotalCharges records

All 11 records had tenure = 0

Converted TotalCharges to numeric

Replaced the 11 verified blank TotalCharges values with 0

Checked categorical values for unexpected categories

Validated numerical ranges such as tenure and MonthlyCharges

🐍 Python EDA

Tools

Python

Pandas

Matplotlib

Seaborn

Analysis Performed

Overall churn distribution

Gender vs churn

Senior citizen status vs churn

Partner and dependents vs churn

Phone and multiple-line services

Internet service

Online security and backup

Device protection

Technical support

Streaming services

Contract type

Paperless billing

Payment method

Tenure analysis

Monthly charge analysis

Total charge analysis

Tenure vs total charges

Correlation analysis

Contract + tenure segmentation

Contract + monthly-charge segmentation

Internet-service + contract segmentation

Payment-method + contract segmentation

📊 Key EDA Findings

Overall Churn

Total customers: 7,043

Churned customers: 1,869

Overall churn rate: 26.54%

Contract

Contract

Churn Rate

Month-to-month

42.71%

One year

11.27%

Two year

2.83%

Internet Service

Internet Service

Churn Rate

Fiber optic

41.89%

DSL

18.96%

No internet service

7.40%

Payment Method

Payment Method

Churn Rate

Electronic check

45.29%

Mailed check

19.11%

Bank transfer (automatic)

16.71%

Credit card (automatic)

15.24%

Tenure

Customers in the first 0–12 months had a 47.44% churn rate, while customers with 61–72 months of tenure had a 6.61% churn rate.

Support Services

Customers without these services showed substantially higher churn:

No OnlineSecurity: 41.77%

No TechSupport: 41.64%

No OnlineBackup: 39.93%

No DeviceProtection: 39.13%

🔥 High-Risk Customer Segments

Multivariate analysis was used to go beyond individual features.

Fiber optic + Month-to-month

Customers: 2,128

Churn rate: 54.61%

Electronic check + Month-to-month

Customers: 1,850

Churn rate: 53.73%

Fiber optic + Month-to-month + Electronic check

Customers: 1,307

Churned customers: 789

Churn rate: 60.37%

These findings describe associations observed in the dataset. They should not be interpreted as proof that a particular contract, service, or payment method causes churn.

🗄️ PostgreSQL Analysis

The cleaned dataset was imported into PostgreSQL for business-focused SQL analysis.

The SQL work included:

Customer and churn KPIs

Average tenure and charges

Contribution of contract types to total churn

Payment-method contribution to total churn

High-risk tenure segments

High-risk contract segments

Multi-dimensional customer segmentation

GROUP BY

FILTER

HAVING

CTEs

Window functions such as RANK(), DENSE_RANK(), and ROW_NUMBER()

The project includes 25 business-oriented SQL questions, progressing from core KPIs to advanced customer segmentation.

📈 Power BI Dashboard

A one-page interactive TELCO Customer Churn Analytics dashboard was created.

Dashboard Components

TELCO branding and custom header

KPI cards

Total Customers

Churned Customers

Churn Rate

Average Monthly Charges

Average Tenure

Churn Rate by Contract Type

Churn Rate by Internet Service

Churn Rate by Payment Method

Churn Rate by Tenure

High-Risk Customer Segments matrix

Conditional formatting for churn risk

Interactive slicers

Gender

Senior Citizen

Contract

Internet Service

Payment Method

Tech Support

Key Insights section

Dashboard KPIs

KPI

Value

Total Customers

7,043

Churned Customers

1,869

Churn Rate

26.54%

Average Monthly Charges

$64.76

Average Tenure

32.37 months

💡 Business Recommendations

Improve first-year customer retention
Customers in their first 12 months show the highest churn. Strengthening onboarding and early engagement should be a priority.

Encourage longer-term contracts
Month-to-month customers have much higher churn than one- and two-year contract customers.

Prioritize high-risk segments
Give special attention to customers combining high-risk characteristics such as fiber optic service, month-to-month contracts, and electronic-check payment.

Investigate support and protection services
Customers without TechSupport, OnlineSecurity, OnlineBackup, or DeviceProtection show higher churn and may be useful targets for retention experiments.

Investigate electronic-check customers
Electronic-check users have the highest churn rate among payment methods. The business should investigate the underlying customer or payment experience rather than assuming the payment method itself causes churn.

🛠️ Technology Stack

Tool

Purpose

Excel

Data cleaning and validation

Python

Data analysis and EDA

Pandas

Data manipulation

Matplotlib

Visualization

Seaborn

Statistical visualization

PostgreSQL

SQL business analysis

Power BI

Interactive dashboard

GitHub

Version control and portfolio

📁 Suggested Project Structure

Customer-Churn-Analytics/
│
├── data/
│   └── Telco-Customer-Churn-Clean.csv
│
├── python/
│   └── Customers-churn-EDA.py
│
├── sql/
│   └── customer_churn_analysis.sql
│
├── powerbi/
│   └── Customer-Churn.pbix
│
├── images/
│   └── Customer-Churn-Dashboard.png
│
└── README.md

🎯 Project Outcome

This project demonstrates an end-to-end Data Analyst workflow:

Raw Dataset
     ↓
Excel Data Cleaning
     ↓
Python EDA
     ↓
Matplotlib / Seaborn Visualization
     ↓
PostgreSQL Business Analysis
     ↓
Power BI Interactive Dashboard
     ↓
Business Insights & Recommendations

The project focuses on turning customer data into actionable retention insights, rather than only producing charts or SQL queries.

👤 Author

Darshan Patel

GitHub: https://github.com/darshanpatel-IT
LinkedIn: https://www.linkedin.com/in/darshan-patel-a75124288
