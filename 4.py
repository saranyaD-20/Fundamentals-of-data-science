import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [5, 7, 12, 18, 22, 25, 27, 26, 22, 18, 12, 7],
    'Rainfall': [30, 25, 40, 50, 70, 80, 60, 50, 40, 30, 20, 25]
}
df = pd.DataFrame(data)
plt.figure(figsize=(10, 6))

plt.plot(df['Month'], df['Temperature'], label='Temperature (°C)', marker='o', color='red')
plt.ylabel('Temperature (°C)')

ax2 = plt.twinx()
plt.plot(df['Month'], df['Rainfall'], label='Rainfall (mm)', marker='s', color='blue', alpha=0.7, linestyle='--')
plt.ylabel('Rainfall (mm)', color='blue')

plt.xlabel('Month')
plt.title('Monthly Temperature and Rainfall Trends')
plt.xticks(rotation=45, ha='right') 
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df['Temperature'], df['Rainfall'], c='green', alpha=0.7)
plt.xlabel('Temperature (°C)')
plt.ylabel('Rainfall (mm)')
plt.title('Temperature vs. Rainfall (Scatter Plot)')
plt.grid(True)
plt.show()
