import numpy as np

# Assuming sales_data is your NumPy array containing sales data
sales_data = np.array([
    [50, 60, 70],  # Sales data for product 1: price1, price2, price3
    [45, 55, 65],  # Sales data for product 2: price1, price2, price3
    [55, 65, 75]   # Sales data for product 3: price1, price2, price3
])

# Calculate the average price of all products
average_price = np.mean(sales_data)

# Printing the result
print("Average price of all products sold in the past month:", average_price)
