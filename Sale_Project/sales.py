import pandas as pd
shahab = pd.read_csv('large_sales_dataset.csv')
print(shahab.head())



##Explore your dataset:====
## Before cleaning data, we should understand how much data we have and whether it contains missing or duplicate values.

import pandas as pd
shahab=pd.read_csv('large_sales_dataset.csv')
# Display the first five Row
print("Display the First Five rows.")
print(shahab.head())

# Check the Number of Row and Column
print("\nDataSet Shape.")
print(shahab.shape)

# Check the Column name.
print("\n Column Name.")
print(shahab.columns)

# Checking messing value.
print("\nMessing Value.")
print(shahab.isnull().sum())

# Check Duplicate rows
print("\nDuplicate Rows")
print(shahab.duplicated().sum())


## Remove duplicate rows:==
import pandas as pd
shahab=pd.read_csv('large_sales_dataset.csv')

# Count duplicates before removing them
print("Duplicate Before Cleaning:")
print(shahab.duplicated().sum())

# Remove Duplicate values
shahab.drop_duplicates(inplace=True)

# Count Duplicate After removing them.
print("Duplicate After Removing.")
print(shahab.duplicated().sum())

# Display the Number of row remaining.
print("Dataset Shape after the Cleaning.")
print(shahab.shape)


import pandas as pd
shahab=pd.read_csv("large_sales_dataset.csv")
#  Missing value in each column
print(shahab.isnull().sum())

# isnull() check karta hai ke koi value missing hai ya nahi.
# any(axis=1) check karta hai ke har row mein kam az kam ek missing value hai ya nahi.
# sum() un rows ko count karta hai
print("Total row with Missing value.")
print(shahab.isnull().any(axis=1).sum())



# dropna() ka matlab hai un rows ko remove karna jin mein missing values (NaN) hoti hain.
import pandas as pd
shahab = pd.read_csv('large_sales_dataset.csv')
print("before Messing value.")
print(shahab.isnull().sum())



# Remove row containing Missing Value.
shahab.dropna(inplace=True)

print("\nAfter Removing Missing Vale.")
print(shahab.isnull().sum())

print("Remaining Row and Column")
print(shahab.shape)

print("Last 5 rows:")
print(shahab.tail())

print("Total rows")
print(len(shahab))

shahab.drop_duplicates(inplace=True)

print("Remaining rows:", len(shahab))
print("Remaining columns:", len(shahab.columns))
print("Dataset shape:", shahab.shape)


import pandas as pd
shahab=pd.read_csv('large_sales_dataset.csv')
print(shahab.dtypes)

import pandas as pd
shahab = pd.read_csv('large_sales_dataset.csv')
# Convert Date column in to Datatime formate
shahab["Date"] = pd.to_datetime(shahab["Date"])

#check the Data type
print("Data type After the conversion")
print(shahab.dtypes)

# Display First five Rows
print(" Display First five Rows")
print(shahab.head())


# Save the updated Dataset;
shahab.to_csv('sales_data_converted.csv',index=False)

print("\nUpdated Dataset Successfully.")

import pandas as pd
shahab = pd.read_csv('large_sales_dataset.csv')
# Convert Date column into datetime format
shahab['Date'] = pd.to_datetime(shahab['Date'], errors='coerce')
 
# Check the data type
print("Date Column Data Type:")
print(shahab['Date'].dtype)

# Check for invalid or missing data
print("\nMissing Data")
print(shahab["Date"].isnull().sum())

# Display the first Five rows
print(" First five row.")
print(shahab.head())


## Explore sale data
print("sale dataset summarry")
print(shahab.describe())

print("\nTotal Sales")
print(shahab['Sales'].sum())

print("Total Profit")
print(shahab['Profit'].sum())

print("Total Quantity Sold")
print(shahab['Quantity'].sum())

# product wise sale Analysis
print("Total Sales by Product")
product_sales = shahab.groupby('Product')['Sales'].sum()
print(product_sales.sort_values(ascending=False))

print("\nTotal Profit By Product")
product_sales=shahab.groupby('Product')['Profit'].sum()
print(product_sales.sort_values(ascending=False))


# Region_Wise Sale Analysis
print("Total sales by Region")
region_sale = shahab.groupby('Region')['Sales'].sum()
print(region_sale.sort_values(ascending=False))

print("Total Profit By Region")
region_profit = shahab.groupby('Region')['Profit'].sum()
print(region_profit.sort_values(ascending=False))



# Month-wise Sales Analysis

shahab['Date'] = pd.to_datetime(shahab['Date'], errors='coerce')

# Extract month from Date
shahab['Month'] = shahab['Date'].dt.to_period('M')

# Calculate monthly Sales, Profit and Quantity
monthly_sales = shahab.groupby('Month').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Quantity': 'sum'
})

print("Month-wise Sales, Profit and Quantity:")
print(monthly_sales)


## Step 3 — Sales Data ko Chart mein Visualize karna
## Abhi tak humne numbers ki form mein Sales aur Profit dekha hai. Ab hum Bar Chart banayenge, jisse pata chalega ke kaun se products ki Sales zyada hain.



""""
import matplotlib.pyplot as plt — charts banane ke liye library import karta hai.
groupby('Product') — har product ki sales ko group karta hai.
sum() — har product ki total sales nikalta hai.
sort_values(ascending=False) — sab se zyada sales wala product pehle dikhata hai.
plot(kind='bar') — bar chart banata hai.
plt.show() — chart screen par display karta hai.
"""
import matplotlib.pyplot as plt
# Calculate total sale by product
product_sales = shahab.groupby('Product')['Sales'].sum()

# Sort Sale From Highest to Lowest
product_sales = product_sales.sort_values(ascending=False)

# Create Bar Chart
product_sales.plot(kind="bar",figsize=(10,5))

# Add chart tital and label
plt.title("Total Sales By Product.")
plt.xlabel('Product')
plt.ylabel('Total Sales')

# Display the Chart
plt.tight_layout()
plt.show()


## Region-wise Sales Chart
# Pichle step mein humne Product-wise Sales ka chart banaya tha. Ab hum dekhenge ke kis Region mein sab se zyada Sales hui hain
"""
groupby('Region') — data ko Region ke hisaab se group karta hai.
['Sales'].sum() — har Region ki total Sales calculate karta hai.
sort_values(ascending=False) — zyada Sales wale Region ko pehle rakhta hai.
plot(kind='bar') — bar chart banata hai.
plt.show() — chart display karta hai.
"""
import matplotlib.pyplot as plt
# Calculate Total Sales Region
region_sale = shahab.groupby('Region')['Sales'].sum()
# Sort from Highest to Lowest
region_sale = region_sale.sort_values(ascending=False)
# Create Bar chart
region_sale.plot(kind='bar',figsize=(8,5))
# Add Tital and labels
plt.title('Total Sales By Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
# Display the chart
plt.tight_layout()
plt.show()



"""
idxmax() — Batata hai ke sab se bari value kis month mein hai.
max() — Sab se bari value batata hai.
monthly_sales['Sales'] — Sirf Sales column select karta hai.
monthly_sales['Profit'] — Sirf Profit column select karta hai.
"""
# Find the month with highest sales
best_sales_month = monthly_sales['Sales'].idxmax()
highest_sales = monthly_sales['Sales'].max()

# Find the month with highest profit
best_profit_month = monthly_sales['Profit'].idxmax()
highest_profit = monthly_sales['Profit'].max()

print("Month with Highest Sales:", best_sales_month)
print("Highest Sales:", highest_sales)

print("Month with Highest Profit:", best_profit_month)
print("Highest Profit:", highest_profit)



"""
monthly_sales['Sales'] — Month-wise Sales select karta hai.
kind='bar' — Bar chart banata hai.
figsize=(10, 5) — Chart ki width aur height set karta hai.
plt.title() — Chart ka title set karta hai.
plt.show() — Chart display karta hai.
"""
import matplotlib.pyplot as plt

# Calculate Total Sales by Month
monthly_sales['Sales'].plot(kind='bar',figsize=(10, 5))

# Add Title and Labels
plt.title('Total Sales By Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')

# Display the Chart
plt.tight_layout()
plt.show()



"""
- groupby('Region') — Data ko Region ke hisaab se divide karta hai.
- [['Sales', 'Profit']] — Dono columns select karta hai.
- .sum() — Har Region ki total Sales aur Profit calculate karta hai.
- plot(kind='bar') — Dono ko ek chart mein side-by-side bars ki shakal mein dikhata hai.
"""
import matplotlib.pyplot as plt

# Calculate Sales and Profit by Region
region_data = shahab.groupby('Region')[['Sales', 'Profit']].sum()

# Create Bar Chart
region_data.plot(kind='bar', figsize=(9, 5))

# Add Title and Labels
plt.title('Sales vs Profit by Region')
plt.xlabel('Region')
plt.ylabel('Total Amount')

# Display Chart
plt.tight_layout()
plt.show()

#Product-wise Sales aur Profit Analysis
# Is step mein hum pata lagayenge ke kaun sa Product sab se zyada Sales aur Profit generate kar raha hai.
"""  groupby('Product') — Data ko Product ke hisaab se group karta hai.
[['Sales', 'Profit']] — Sales aur Profit ke columns select karta hai.
sum() — Har Product ki total Sales aur Profit nikalta hai.
sort_values(by='Sales', ascending=False) — Products ko highest Sales se lowest Sales tak arrange karta hai.
plot(kind='bar') — Dono values ka comparison chart banata hai.
"""

import matplotlib.pyplot as plt

# Calculate Sales and Profit by Product
product_data = shahab.groupby('Product')[['Sales', 'Profit']].sum()

# Sort Products by Sales (Highest to Lowest)
product_data = product_data.sort_values(by='Sales',ascending=False)
# Create Bar Chart
product_data.plot(kind='bar', figsize=(10, 6))

# Add Title and Labels
plt.title('Product-wise Sales vs Profit')
plt.xlabel('Product')
plt.ylabel('Total Amount')

# Display Chart
plt.tight_layout()
plt.show()



# Top 5 Products by Sales
#Ab hum apne dataset mein se woh Top 5 Products nikalenge jinki total Sales sab se zyada hain.
"""- groupby('Product')['Sales'].sum() — Har Product ki total Sales nikalta hai.
- sort_values(ascending=False) — Sales ko highest se lowest tak arrange karta hai.
- .head(5) — Sirf pehli 5 rows, yani Top 5 Products, select karta hai.
- plot(kind='bar') — Top 5 Products ka chart banata hai.
"""

# Calculate Total Sales by Product
product_sales = shahab.groupby('Product')['Sales'].sum()
# Sort and Select Top 5 Products
top_5_products = product_sales.sort_values(ascending=False).head(5)

# Display Results
print("Top 5 Products by Sales:")
print(top_5_products)

# Create Bar Chart
top_5_products.plot(kind='bar', figsize=(8, 5))

import matplotlib.pyplot as plt
plt.title('Top 5 Products by Sales')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()



# Best aur Worst Performing Region
# Is step mein hum pata lagayenge ke kis Region ki Sales sab se zyada aur kis Region ki Sales sab se kam hain.
""" groupby('Region')['Sales'].sum() — Har Region ki total Sales nikalta hai.
idxmax() — Us Region ka naam batata hai jiski Sales sab se zyada hain.
idxmin() — Us Region ka naam batata hai jiski Sales sab se kam hain.
max() — Sab se bari Sales value deta hai.
min() — Sab se chhoti Sales value deta hai.
"""

# Calculate Total Sales by Region
region_sales = shahab.groupby('Region')['Sales'].sum()

# Find Best Performing Region
best_region = region_sales.idxmax()
highest_sales = region_sales.max()

# Find Worst Performing Region
worst_region = region_sales.idxmin()
lowest_sales = region_sales.min()

# Display Results
print("Best Performing Region:", best_region)
print("Highest Sales:", highest_sales)

print("Worst Performing Region:", worst_region)
print("Lowest Sales:", lowest_sales)




# Region-wise Profit Analysis
# Pichle step mein hum ne har Region ki Sales compare ki thin. Ab hum check karenge ke kis Region se sab se zyada aur sab se kam Profit hua.
""" groupby('Region')['Profit'].sum() — Har Region ka total Profit calculate karta hai.
idxmax() — Sab se zyada Profit wale Region ka naam deta hai.
idxmin() — Sab se kam Profit wale Region ka naam deta hai.
max() aur min() — Profit ki highest aur lowest values dete hain.
"""

# Calculate Total Profit by Region
region_profit = shahab.groupby('Region')['Profit'].sum()

# Find Best Region by Profit
best_profit_region = region_profit.idxmax()
highest_profit = region_profit.max()

# Find Lowest Profit Region
worst_profit_region = region_profit.idxmin()
lowest_profit = region_profit.min()

# Display Results
print("Region with Highest Profit:", best_profit_region)
print("Highest Profit:", highest_profit)

print("Region with Lowest Profit:", worst_profit_region)
print("Lowest Profit:", lowest_profit)



# Cleaned Dataset ko CSV File mein Save Karna
# Ab tak hum ne data cleaning aur Sales Analysis ki hai. Ab hum apne cleaned dataset ko ek nayi CSV file mein save karenge, taake original file bhi safe rahe.
"""shahab.to_csv() — DataFrame ko CSV file mein save karta hai.
'cleaned_sales_dataset.csv' — Nayi file ka naam hai.
index=False — Extra index column ko CSV mein save hone se rokta hai.
print() — Success ka message show karta hai.
"""

# Save the cleaned dataset into a new CSV file
shahab.to_csv('cleaned_sales_dataset.csv', index=False)
print("Cleaned dataset saved successfully!")


# Final Business Insights Report
# Company mein Data Analyst sirf code nahi likhta. Woh data se useful information bhi nikalta hai aur business ko samjhata hai ke results ka kya matlab hai.
"""  sum() — Total Sales, Profit aur Quantity nikalta hai.
idxmax() — Sab se zyada Sales wale Region ya Product ka naam deta hai.
max() — Uski highest Sales value deta hai.
print() — Final report screen par dikhata hai
"""


# Final Sales Analysis Report

# Total Sales
total_sales = shahab['Sales'].sum()

# Total Profit
total_profit = shahab['Profit'].sum()

# Total Quantity Sold
total_quantity = shahab['Quantity'].sum()

# Best Region by Sales
region_sales = shahab.groupby('Region')['Sales'].sum()
best_region = region_sales.idxmax()
best_region_sales = region_sales.max()

# Best Product by Sales
product_sales = shahab.groupby('Product')['Sales'].sum()
best_product = product_sales.idxmax()
best_product_sales = product_sales.max()

# Display Final Report
print("===== FINAL SALES ANALYSIS REPORT =====")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Quantity Sold:", total_quantity)
print("Best Region:", best_region)
print("Best Region Sales:", best_region_sales)
print("Best Product:", best_product)
print("Best Product Sales:", best_product_sales)
