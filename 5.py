import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1000, 1200, 1500, 1800, 2100, 2300, 2000, 1800, 1600, 1400, 1100, 900]

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', linestyle='-', color='blue')
plt.xlabel('Month')  
plt.ylabel('Sales') 
plt.title('Monthly Sales Trend (Line Plot)') 
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.show()
