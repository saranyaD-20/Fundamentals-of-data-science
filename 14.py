import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Creating a DataFrame with the provided data
data = {
    'age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    'fat_percentage': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}

df = pd.DataFrame(data)

# Calculating mean, median, and standard deviation
mean_age = df['age'].mean()
median_age = df['age'].median()
std_dev_age = df['age'].std()

mean_fat_percentage = df['fat_percentage'].mean()
median_fat_percentage = df['fat_percentage'].median()
std_dev_fat_percentage = df['fat_percentage'].std()

print("Age:")
print("Mean:", mean_age)
print("Median:", median_age)
print("Standard Deviation:", std_dev_age)

print("\nFat Percentage:")
print("Mean:", mean_fat_percentage)
print("Median:", median_fat_percentage)
print("Standard Deviation:", std_dev_fat_percentage)

# Drawing boxplots
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['age'])
plt.title('Boxplot of Age')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['fat_percentage'])
plt.title('Boxplot of Fat Percentage')

plt.tight_layout()
plt.show()

# Drawing scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='age', y='fat_percentage', data=df)
plt.title('Scatter Plot of Age vs Fat Percentage')
plt.xlabel('Age')
plt.ylabel('Fat Percentage')
plt.show()

# Drawing Q-Q plot
plt.figure(figsize=(8, 6))
stats.probplot(df['fat_percentage'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Fat Percentage')
plt.xlabel('Theoretical quantiles')
plt.ylabel('Ordered Values')
plt.show()
