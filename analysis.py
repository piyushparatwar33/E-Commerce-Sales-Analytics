1. Install Libraries
!pip install pandas numpy matplotlib seaborn
2. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
3. Load Dataset

Apni CSV file ka naam sales_data.csv rakho.

df = pd.read_csv("sales_data.csv")

print(df.head())
print("Dataset Shape:", df.shape)
print(df.info())
print(df.isnull().sum())

Expected columns:

OrderID
OrderDate
CustomerID
Product
Category
Region
Quantity
UnitPrice

Agar tumhari CSV mein columns ke naam alag hain, to code ko unke according modify karna hoga.

4. Data Cleaning
# Remove duplicate rows
df = df.drop_duplicates()

# Convert date column
df["OrderDate"] = pd.to_datetime(
    df["OrderDate"], errors="coerce"
)

# Convert numeric columns
df["Quantity"] = pd.to_numeric(
    df["Quantity"], errors="coerce"
)

df["UnitPrice"] = pd.to_numeric(
    df["UnitPrice"], errors="coerce"
)

# Remove rows with missing essential values
df = df.dropna(
    subset=["OrderDate", "Quantity", "UnitPrice"]
)

# Remove invalid sales records
df = df[
    (df["Quantity"] > 0) &
    (df["UnitPrice"] >= 0)
].copy()

print("Cleaned Dataset Shape:", df.shape)
5. Calculate Revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

total_revenue = df["Revenue"].sum()
total_orders = df["OrderID"].nunique()
total_customers = df["CustomerID"].nunique()
total_products = df["Product"].nunique()

print("Total Revenue:", round(total_revenue, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Total Products:", total_products)
6. Category-Wise Sales Analysis
category_sales = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(category_sales)

category_sales.plot(
    kind="bar",
    figsize=(10, 5),
    title="Category-Wise Revenue"
)

plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
7. Region-Wise Sales Analysis
region_sales = (
    df.groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(region_sales)

region_sales.plot(
    kind="bar",
    figsize=(8, 5),
    title="Region-Wise Revenue"
)

plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
8. Monthly Sales Trend
df["YearMonth"] = df["OrderDate"].dt.to_period("M")

monthly_sales = (
    df.groupby("YearMonth")["Revenue"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

monthly_sales.plot(
    figsize=(12, 5),
    marker="o",
    title="Monthly Revenue Trend"
)

plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
9. Top 10 Products
top_products = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

top_products.sort_values().plot(
    kind="barh",
    figsize=(10, 6),
    title="Top 10 Products by Revenue"
)

plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.show()
10. Export Cleaned Dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("Cleaned dataset exported successfully!")
