import pandas as pd

# Example DataFrame creation (replace with your actual data loading)
sales_data = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'customer_age': [25, 30, 35, 40, 45],  # Assuming this is the column representing customer age
    'purchase_date': pd.date_range(start='2024-05-01', periods=5)  # Assuming purchases were made in May 2024
})

# Filtering data for the past month
current_month_sales = sales_data[sales_data['purchase_date'].dt.month == pd.Timestamp.now().month]

# Frequency distribution of customer ages
age_frequency_distribution = current_month_sales['customer_age'].value_counts().sort_index()

print("Frequency distribution of customer ages in the past month:")
print(age_frequency_distribution)
