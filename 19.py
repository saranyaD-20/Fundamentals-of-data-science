import matplotlib.pyplot as plt
import pandas as pd

# Sample data (replace with your actual data)
dates = pd.date_range(start='2024-01-01', end='2024-06-01', freq='MS')
sales = [1000, 1200, 1500, 1400, 1600, 1800]

# Create DataFrame
sales_df = pd.DataFrame({'Date': dates, 'Sales': sales})

# Plotting
plt.figure(figsize=(15, 5))

# Line plot
plt.subplot(1, 3, 1)
plt.plot(sales_df['Date'], sales_df['Sales'], marker='o', linestyle='-')
plt.title('Monthly Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)

# Scatter plot
plt.subplot(1, 3, 2)
plt.scatter(sales_df['Date'], sales_df['Sales'], color='blue')
plt.title('Monthly Sales Scatter Plot')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)

# Bar plot
plt.subplot(1, 3, 3)
plt.bar(sales_df['Date'], sales_df['Sales'], color='green')
plt.title('Monthly Sales Bar Plot')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(axis='y')

plt.tight_layout()
plt.show()
