import numpy as np
from scipy import stats

# Assuming purchase_amounts is your NumPy array containing purchase amount data
purchase_amounts = np.array([20, 30, 40, 50, 50, 60, 70, 70, 70, 80])

# Calculate the mean (average) purchase amount
mean_purchase_amount = np.mean(purchase_amounts)

# Identify the mode of the purchase amounts
mode_purchase_amount = stats.mode(purchase_amounts)

# Printing the results
print("Mean (average) purchase amount:", mean_purchase_amount)
print("Mode of purchase amounts:", mode_purchase_amount.mode.item())
