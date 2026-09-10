# ============================================================
# SECTION 1: IMPORT REQUIRED LIBRARIES
# Pandas -> data loading and data analysis
# Matplotlib -> create and customize plots
# Seaborn -> statistical and categorical visualizations
# ============================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# SECTION 2: LOAD CLEANED DATASET
# Read the cleaned Telco Customer Churn CSV into a DataFrame.
# ============================================================
df = pd.read_csv("Telco-Customer-Churn-Clean.csv")

# View the first 5 rows to confirm the dataset loaded correctly.
print(df.head())

# Inspect row count, column names, non-null values, and data types.
print(df.info())

# Check for missing values in every column.
print(df.isnull().sum())

# Check whether the dataset contains duplicate rows.
print(df.duplicated().sum())


# ============================================================
# SECTION 3: OVERALL CHURN DISTRIBUTION
# Count how many customers stayed and how many customers churned.
# ============================================================
print(df["Churn"].value_counts())

# Calculate the percentage distribution of Churn = Yes/No.
print(df["Churn"].value_counts(normalize=True) * 100)

# Create a count plot to visually compare retained vs churned customers.
sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.show()

# ============================================================
# SECTION 4: GENDER VS CHURN
# Cross-tabulation shows customer counts by gender and churn status.
# ============================================================
print(pd.crosstab(df["gender"], df["Churn"]))
print(pd.crosstab(df["gender"], df["Churn"], normalize="index") * 100)

churn_by_gender = pd.crosstab(
    df["gender"],
    df["Churn"],
    normalize="index"
) * 100  # Calculate churn percentage within each group.  # Convert each row to a percentage of that category.

print(churn_by_gender)

churn_by_gender["Yes"].plot(kind="bar")

plt.title("Churn Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()

# ============================================================
# SECTION 5: SENIOR CITIZEN VS CHURN
# Calculate churn percentage separately for senior and non-senior customers.
# ============================================================
print(pd.crosstab(df["SeniorCitizen"], df["Churn"], normalize="index") * 100)

senior_churn = pd.crosstab(
    df["SeniorCitizen"],
    df["Churn"],
    normalize="index"
) * 100

print(senior_churn)
senior_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Senior Citizen Status")
plt.xlabel("Senior Citizen (0 = No, 1 = Yes)")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()

# ============================================================
# SECTION 6: PARTNER STATUS VS CHURN
# Compare churn percentages for customers with and without a partner.
# ============================================================
print(pd.crosstab(df["Partner"], df["Churn"],normalize="index")*100)

partner_churn = pd.crosstab(
    df["Partner"],
    df["Churn"],
    normalize="index"
) * 100

print(partner_churn)

partner_churn["Yes"].rename(
    index={"No": "No Partner", "Yes": "Has Partner"}
).plot(kind="bar")

plt.title("Churn Rate by Partner Status")
plt.xlabel("Partner Status")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()

# ============================================================
# SECTION 7: DEPENDENTS VS CHURN
# Compare customers with and without dependents.
# ============================================================
print(pd.crosstab(df["Dependents"], df["Churn"]))

dependents_churn = pd.crosstab(
    df["Dependents"],
    df["Churn"],
    normalize="index"
) * 100

print(dependents_churn)

dependents_churn["Yes"].rename(
    index={"No": "No Dependents", "Yes": "Has Dependents"}
).plot(kind="bar")

plt.title("Churn Rate by Dependents")
plt.xlabel("Dependents Status")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()

# ============================================================
# SECTION 8: PHONE SERVICE VS CHURN
# Examine whether having phone service is associated with churn.
# ============================================================
print(pd.crosstab(df["PhoneService"], df["Churn"]))

phone_churn = pd.crosstab(
    df["PhoneService"],
    df["Churn"],
    normalize="index"
) * 100

print(phone_churn)

phone_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Phone Service")
plt.xlabel("Phone Service")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()

# ============================================================
# SECTION 9: MULTIPLE LINES VS CHURN
# Compare churn across phone-line service categories.
# ============================================================
print(pd.crosstab(df["MultipleLines"], df["Churn"]))

multiple_lines_churn = pd.crosstab(
    df["MultipleLines"],
    df["Churn"],
    normalize="index"
) * 100

print(multiple_lines_churn)

multiple_lines_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Multiple Lines")
plt.xlabel("Multiple Lines")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()

# ============================================================
# SECTION 10: INTERNET SERVICE VS CHURN
# Compare churn rates for DSL, Fiber optic, and No internet service.
# ============================================================
print(pd.crosstab(df["InternetService"], df["Churn"]))

internet_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"],
    normalize="index"
) * 100

print(internet_churn)

internet_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()

# ============================================================
# SECTION 11: ONLINE SECURITY VS CHURN
# Compare churn among customers with/without OnlineSecurity.
# ============================================================
print(pd.crosstab(df["OnlineSecurity"], df["Churn"]))

security_churn = pd.crosstab(
    df["OnlineSecurity"],
    df["Churn"],
    normalize="index"
) * 100

print(security_churn)

security_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Online Security")
plt.xlabel("Online Security")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()

# ============================================================
# SECTION 12: ONLINE BACKUP VS CHURN
# Compare churn among customers with/without OnlineBackup.
# ============================================================
print(pd.crosstab(df["OnlineBackup"], df["Churn"]))

backup_churn = pd.crosstab(
    df["OnlineBackup"],
    df["Churn"],
    normalize="index"
) * 100

print(backup_churn)

backup_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Online Backup")
plt.xlabel("Online Backup")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()

# ============================================================
# SECTION 13: DEVICE PROTECTION VS CHURN
# Compare churn among customers with/without DeviceProtection.
# ============================================================
print(pd.crosstab(df["DeviceProtection"], df["Churn"]))

device_churn = pd.crosstab(
    df["DeviceProtection"],
    df["Churn"],
    normalize="index"
) * 100

print(device_churn)

device_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Device Protection")
plt.xlabel("Device Protection")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()

# ============================================================
# SECTION 14: TECH SUPPORT VS CHURN
# Compare churn among customers with/without TechSupport.
# ============================================================
print(pd.crosstab(df["TechSupport"], df["Churn"]))

techsupport_churn = pd.crosstab(
    df["TechSupport"],
    df["Churn"],
    normalize="index"
) * 100

print(techsupport_churn)

techsupport_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Tech Support")
plt.xlabel("Tech Support")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()

# ============================================================
# SECTION 15: STREAMING TV VS CHURN
# Compare churn across StreamingTV service categories.
# ============================================================
print(pd.crosstab(df["StreamingTV"], df["Churn"]))

streamingtv_churn = pd.crosstab(
    df["StreamingTV"],
    df["Churn"],
    normalize="index"
) * 100

print(streamingtv_churn)

streamingtv_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Streaming TV")
plt.xlabel("Streaming TV")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()


# ============================================================
# SECTION 16: STREAMING MOVIES VS CHURN
# Compare churn across StreamingMovies service categories.
# ============================================================
print(pd.crosstab(df["StreamingMovies"], df["Churn"]))

streamingmovies_churn = pd.crosstab(
    df["StreamingMovies"],
    df["Churn"],
    normalize="index"
) * 100

print(streamingmovies_churn)

# ============================================================
# SECTION 17: CONTRACT TYPE VS CHURN
# Compare churn rates for month-to-month, one-year, and two-year contracts.
# ============================================================
print(pd.crosstab(df["Contract"], df["Churn"]))

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100

print(contract_churn)

contract_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()

# ============================================================
# SECTION 18: PAPERLESS BILLING VS CHURN
# Compare churn rates for paperless and non-paperless billing customers.
# ============================================================
# paperlessbilling 

print(pd.crosstab(df["PaperlessBilling"], df["Churn"]))

paperless_churn = pd.crosstab(
    df["PaperlessBilling"],
    df["Churn"],
    normalize="index"
    ) *100
print(paperless_churn)

paperless_churn["Yes"].plot(kind = "bar")

plt.title("churn rate by paperlessbilling type")
plt.xlabel("paperlessbilling type")
plt.ylabel("churn rate(%)")
plt.xticks(rotation=0)

plt.show()


# ============================================================
# SECTION 19: PAYMENT METHOD VS CHURN
# Compare churn rates across all payment methods.
# ============================================================
# PaymentMethod

print(pd.crosstab(df["PaymentMethod"], df["Churn"]))

PaymentMethod_churn  = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"],
    normalize="index"
)*100
print(PaymentMethod_churn)

PaymentMethod_churn["Yes"].plot(kind="bar")

plt.title("churn rate by payment method type ")
plt.xlabel("payment method type")
plt.ylabel("churn rate(%)")
plt.xticks(rotation=12)

plt.show()


# ============================================================
# SECTION 20: TENURE VS CHURN
# Calculate average tenure for retained and churned customers.
# ============================================================
print(df.groupby("Churn")["tenure"].mean())

# Box plot compares the distribution and spread of tenure by churn status.
sns.boxplot(x="Churn", y="tenure", data=df)

plt.title("tenure distribution by churn")
plt.xlabel("churn")
plt.ylabel("tenure(month)")
plt.show()


# ============================================================
# SECTION 21: MONTHLY CHARGES VS CHURN
# Compare average monthly charges and their distribution by churn status.
# ============================================================
# monthly charge

print(df.groupby("Churn")["MonthlyCharges"].mean()) 

sns.boxplot(x="Churn", y="MonthlyCharges", data=df)

plt.title("Monthly Charges Distribution by Churn")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")

plt.show()

# Divide MonthlyCharges into business-friendly ranges for segment analysis.
bins = [0, 30, 50, 70, 90, 110, 130]
labels = ["0-30", "31-50", "51-70", "71-90", "91-110", "111-130"]

# Create a categorical column containing the monthly-charge ranges.
df["MonthlyChargesGroup"] = pd.cut(
    df["MonthlyCharges"],
    bins=bins,
    labels=labels,
    include_lowest=True  # Include the minimum value in the first interval.
)

monthly_churn = pd.crosstab(
    df["MonthlyChargesGroup"],
    df["Churn"],
    normalize="index"
) * 100

print(monthly_churn)

monthly_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Monthly Charges Group")
plt.xlabel("Monthly Charges")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.show()


# ============================================================
# SECTION 22: TOTAL CHARGES VS CHURN
# Compare accumulated customer charges across churn groups.
# ============================================================
# total charges

print(df.groupby("Churn")["TotalCharges"].mean())

sns.boxplot(x="Churn", y="TotalCharges", data=df)

plt.title("Total Charges Distribution by Churn")
plt.xlabel("Churn")
plt.ylabel("Total Charges")

plt.show()


# ============================================================
# SECTION 23: TENURE VS TOTAL CHARGES
# Use a scatter plot to examine the relationship between tenure
# and accumulated charges, colored by churn status.
# ============================================================
# tenure VS total charges

sns.scatterplot(
    x="tenure",
    y="TotalCharges",
    hue="Churn",
    data=df
)

plt.title("Tenure vs Total Charges by Churn")
plt.xlabel("Tenure (Months)")
plt.ylabel("Total Charges")

plt.show()

# ============================================================
# SECTION 24: CONVERT CHURN TO NUMERIC FOR CORRELATION
# Map No -> 0 and Yes -> 1 so Churn can be included in a correlation matrix.
# ============================================================
df["Churn_numeric"] = df["Churn"].map({
    "No": 0,   # Retained customer
    "Yes": 1   # Churned customer
})

# Calculate Pearson correlation among the selected numeric variables.
corr = df[
    ["SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges", "Churn_numeric"]
].corr()

print(corr)

plt.figure(figsize=(8, 6))

# Visualize the correlation matrix as a heatmap.
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.show()

bins = [0, 12, 24, 36, 48, 60, 72]
labels = ["0-12", "13-24", "25-36", "37-48", "49-60", "61-72"]

# ============================================================
# SECTION 25: TENURE GROUP SEGMENTATION
# Create ordered tenure ranges for deeper customer-segment analysis.
# ============================================================
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

print(df[["tenure", "TenureGroup"]].head())

# Calculate churn percentage for every Contract + TenureGroup combination.
contract_tenure_churn = pd.crosstab(
    [df["Contract"], df["TenureGroup"]],
    df["Churn"],
    normalize="index"
) * 100

print(contract_tenure_churn)

print(contract_tenure_churn["Yes"])


plt.figure(figsize=(10, 6))

for contract in contract_tenure_churn.index.get_level_values(0).unique():
    data = contract_tenure_churn.loc[contract, "Yes"]
    plt.plot(
        data.index,
        data.values,
        marker="o",
        label=contract
    )

plt.title("Churn Rate by Contract Type and Tenure Group")
plt.xlabel("Tenure Group")
plt.ylabel("Churn Rate (%)")
plt.legend(title="Contract")
plt.grid(True)

plt.show()

# ============================================================
# SECTION 26: CONTRACT + MONTHLY CHARGES + CHURN
# Identify high-risk combinations of contract type and monthly charges.
# ============================================================
# Contract + MonthlyCharges + Churn

bins = [0, 30, 50, 70, 90, 110, 130]
labels = ["0-30", "31-50", "51-70", "71-90", "91-110", "111-130"]

df["MonthlyChargesGroup"] = pd.cut(
    df["MonthlyCharges"],
    bins=bins,
    labels=labels,
    include_lowest=True
)
# Calculate churn percentage for each Contract + MonthlyChargesGroup combination.
contract_charge_churn = pd.crosstab(
    [df["Contract"], df["MonthlyChargesGroup"]],
    df["Churn"],
    normalize="index"
) * 100

print(contract_charge_churn["Yes"])

contract_charge_churn["Yes"].unstack(level=0).plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Churn Rate by Monthly Charges and Contract Type")
plt.xlabel("Monthly Charges Group")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.legend(title="Contract")

plt.tight_layout()
plt.show()

# ============================================================
# SECTION 27: INTERNET SERVICE + CONTRACT
# Identify high-risk combinations of internet service and contract type.
# ============================================================
# InternetService + Contract

# Calculate churn percentage for each InternetService + Contract combination.
internet_contract_churn = pd.crosstab(
    [df["InternetService"], df["Contract"]],
    df["Churn"],
    normalize="index"
) * 100

print(internet_contract_churn["Yes"])

internet_contract_churn["Yes"].unstack(level=0).plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Churn Rate by Internet Service and Contract")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.legend(title="Internet Service")

plt.tight_layout()
plt.show()

segment_counts = pd.crosstab(
    df["InternetService"],
    df["Contract"]
)

print(segment_counts)

# ============================================================
# SECTION 28: PAYMENT METHOD + CONTRACT + CHURN
# Identify high-risk combinations of payment method and contract type.
# ============================================================
# PaymentMethod + Contract + Churn

# Calculate churn percentage for each PaymentMethod + Contract combination.
payment_contract_churn = pd.crosstab(
    [df["PaymentMethod"], df["Contract"]],
    df["Churn"],
    normalize="index"
) * 100

print(payment_contract_churn["Yes"])

payment_contract_count = pd.crosstab(
    df["PaymentMethod"],
    df["Contract"]
)

print(payment_contract_count)



# ============================================================
# SECTION 29: FINAL EDA SUMMARY
# Collect the strongest churn findings into one DataFrame for reporting.
# ============================================================
# FINAL EDA SUMMARY

# Create a summary table containing the key churn-risk findings.
final_churn_rates = pd.DataFrame({
    "Feature": [
        "Month-to-month Contract",
        "0-12 Month Tenure",
        "Fiber optic + Month-to-month",
        "Electronic check + Month-to-month",
        "No OnlineSecurity",
        "No TechSupport",
        "Senior Citizen",
        "Paperless Billing"
    ],
    "ChurnRate": [
        42.71,
        47.44,
        54.61,
        53.73,
        41.77,
        41.64,
        41.68,
        33.57
    ]
})

print(final_churn_rates)

plt.figure(figsize=(10, 6))

# Plot the final churn-risk summary for quick comparison.
sns.barplot(
    data=final_churn_rates,
    x="ChurnRate",
    y="Feature"
)

plt.title("Key Customer Churn Risk Segments")
plt.xlabel("Churn Rate (%)")
plt.ylabel("Feature / Segment")

plt.tight_layout()
plt.show()
