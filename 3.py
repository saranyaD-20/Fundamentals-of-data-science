import pandas as pd
import matplotlib.pyplot as plt
data = {
    'OrderID': [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007],
    'ProductCategory': ['Electronics', 'Electronics', 'Clothing', 'Homeware', 'Electronics', 'Books', 'Clothing', 'Homeware'],
    'Sales': [500, 200, 300, 150, 700, 100, 400, 250]
}

df = pd.DataFrame(data)

categories = df['ProductCategory'].unique()
for category in categories:
    category_data = df[df['ProductCategory'] == category]
    plt.plot(category_data['OrderID'], category_data['Sales'], label=category)
plt.xlabel('Order ID')
plt.ylabel('Sales')
plt.title('Sales Trend by Product Category (Line Plot)')
plt.legend()
plt.grid(True)
plt.show()
colors = plt.cm.tab10(range(len(categories)))
category_sales = df.groupby('ProductCategory')['Sales'].sum()
plt.bar(category_sales.index, category_sales.values)
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.title('Total Sales per Product Category (Bar Plot)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.show()
