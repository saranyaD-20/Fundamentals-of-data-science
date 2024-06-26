import pandas as pd
# Creating a sample dataset  
data = {
    'OrderID': [1, 2, 3, 4, 5],
    'CustomerID': [101, 102, 101, 103, 104],
    'ProductID': [1001, 1002, 1003, 1001, 1002],
    'Quantity': [2, 1, 4, 2, 3],
    'TotalPrice': [50.0, 20.0, 80.0, 50.0, 60.0]
}
# Creating a DataFrame
df = pd.DataFrame(data)
# Displaying the DataFrame
print("Sample Dataset:\n", df)
# Performing analysis
# 1. Total revenue generated
total_revenue = df['TotalPrice'].sum()
print("\nTotal Revenue: $", total_revenue)
# 2. Number of unique customers
unique_customers = df['CustomerID'].nunique()
print("\nNumber of Unique Customers:", unique_customers)
# 3. Total quantity of products sold
total_quantity_sold = df['Quantity'].sum()
print("\nTotal Quantity Sold:", total_quantity_sold)
# 4. Average order value
average_order_value = df['TotalPrice'].mean()
print("\nAverage Order Value: $", average_order_value)
# 5. Orders per customer
orders_per_customer = df['CustomerID'].value_counts()
print("\nOrders per Customer:\n", orders_per_customer)
# 6. Total revenue per customer
revenue_per_customer = df.groupby('CustomerID')['TotalPrice'].sum()
print("\nTotal Revenue per Customer:\n", revenue_per_customer)
# 7. Total quantity sold per product
quantity_per_product = df.groupby('ProductID')['Quantity'].sum()
print("\nTotal Quantity Sold per Product:\n", quantity_per_product)
