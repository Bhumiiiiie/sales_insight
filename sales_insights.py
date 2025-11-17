import pandas as pd

# Load data
df = pd.read_csv("sales_data.csv")

print(df.head())

# Clean data
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')

df.dropna(inplace=True)

# KPIs
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
top_product = df.groupby('Product Name')['Sales'].sum().idxmax()
top_customer = df.groupby('Customer Name')['Sales'].sum().idxmax()
top_region = df.groupby('Region')['Sales'].sum().idxmax()

# Print insights
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Top Product:", top_product)
print("Top Customer:", top_customer)
print("Top Region:", top_region)

