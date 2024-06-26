import numpy as np

# Assuming response_times is your NumPy array containing response time data
response_times = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

# Calculate the percentiles
percentiles = np.percentile(response_times, [25, 50, 75])

# Printing the results
print("25th percentile (Q1):", percentiles[0])
print("50th percentile (Q2 or median):", percentiles[1])
print("75th percentile (Q3):", percentiles[2])
