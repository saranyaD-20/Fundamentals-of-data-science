import numpy as np

# Assuming recovery_times is your NumPy array containing recovery time data
recovery_times = np.array([3, 5, 7, 9, 11, 13, 15, 17, 19, 21])

# Calculate the percentiles
percentiles = np.percentile(recovery_times, [10, 50, 90])

# Printing the results
print("10th percentile:", percentiles[0])
print("50th percentile (median):", percentiles[1])
print("90th percentile:", percentiles[2])
