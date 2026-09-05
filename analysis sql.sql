-- E-Commerce Sales Analytics
-- SQL Analysis Queries

-- 1. Overall KPIs
SELECT
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Quantity) AS Total_Quantity,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Revenue) / COUNT(DISTINCT Order_ID), 2) AS Average_Order_Value,
    ROUND(SUM(Profit) * 100.0 / SUM(Revenue), 2) AS Profit_Margin_Percent
FROM sales_data;


-- 2. Monthly Revenue and Profit
SELECT
    SUBSTRING(Order_Date, 1, 7) AS Month,
    ROUND(SUM(Revenue), 2) AS Revenue,
    ROUND(SUM(Profit), 2) AS Profit
FROM sales_data
GROUP BY SUBSTRING(Order_Date, 1, 7)
ORDER BY Month;


-- 3. Category Performance
SELECT
    Category,
    ROUND(SUM(Revenue), 2) AS Revenue,
    ROUND(SUM(Profit), 2) AS Profit,
    SUM(Quantity) AS Units_Sold
FROM sales_data
GROUP BY Category
ORDER BY Revenue DESC;


-- 4. Regional Performance
SELECT
    Region,
    ROUND(SUM(Revenue), 2) AS Revenue,
    ROUND(SUM(Profit), 2) AS Profit,
    COUNT(DISTINCT Order_ID) AS Orders
FROM sales_data
GROUP BY Region
ORDER BY Revenue DESC;


-- 5. Top 10 Products by Revenue
SELECT
    Product,
    ROUND(SUM(Revenue), 2) AS Revenue,
    ROUND(SUM(Profit), 2) AS Profit
FROM sales_data
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 10;


-- 6. Customer Segment Analysis
SELECT
    Customer_Segment,
    ROUND(SUM(Revenue), 2) AS Revenue,
    ROUND(SUM(Profit), 2) AS Profit,
    COUNT(DISTINCT Customer_ID) AS Customers
FROM sales_data
GROUP BY Customer_Segment
ORDER BY Revenue DESC;


-- 7. Payment Method Analysis
SELECT
    Payment_Method,
    COUNT(*) AS Orders,
    ROUND(SUM(Revenue), 2) AS Revenue
FROM sales_data
GROUP BY Payment_Method
ORDER BY Orders DESC;


-- 8. High-Value Customers
SELECT
    Customer_ID,
    ROUND(SUM(Revenue), 2) AS Customer_Revenue,
    ROUND(SUM(Profit), 2) AS Customer_Profit,
    COUNT(DISTINCT Order_ID) AS Orders
FROM sales_data
GROUP BY Customer_ID
ORDER BY Customer_Revenue DESC
LIMIT 10;
