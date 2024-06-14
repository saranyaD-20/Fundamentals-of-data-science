import matplotlib.pyplot as plt
import pandas as pd

# Example DataFrame creation (replace with your actual data loading)
sales_data = pd.DataFrame({
    'date': pd.date_range(start='2024-01-01', periods=30),
    'sales': [100, 120, 130, 110, 150, 140, 160, 170, 180, 200, 
              220, 230, 250, 240, 260, 270, 280, 300, 320, 330, 
              350, 340, 360, 370, 380, 400, 420, 430, 450, 440]
})

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Line plot
axs[0].plot(sales_data['date'], sales_data['sales'], color='blue')
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Sales')
axs[0].set_title('Monthly Sales Over Time')
axs[0].tick_params(axis='x', rotation=45)
axs[0].grid(True)

# Scatter plot
axs[1].scatter(sales_data['date'], sales_data['sales'], color='green', alpha=0.5)
axs[1].set_xlabel('Date')
axs[1].set_ylabel('Sales')
axs[1].set_title('Monthly Sales Scatter Plot')
axs[1].tick_params(axis='x', rotation=45)
axs[1].grid(True)

# Bar plot
monthly_sales = sales_data.groupby(sales_data['date'].dt.strftime('%B'))['sales'].sum()
monthly_sales.plot(kind='bar', ax=axs[2], color='red')
axs[2].set_xlabel('Month')
axs[2].set_ylabel('Sales')
axs[2].set_title('Monthly Sales Bar Plot')
axs[2].tick_params(axis='x', rotation=45)
axs[2].grid(axis='y')

plt.tight_layout()
plt.show()
