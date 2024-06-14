import pandas as pd
import matplotlib.pyplot as plt
data = {
    'SmokingStatus': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
    'LungCancer': [True, False, True, False, True, True, True, False]
}
pd.set_option('future.no_silent_downcasting', True)
df = pd.DataFrame(data)
smoking_map = {'Yes': 1, 'No': 0}
df['SmokingStatus_Num'] = df['SmokingStatus'].replace(smoking_map)
correlation = df['SmokingStatus_Num'].corr(df['LungCancer'])
print("Correlation coefficient:", correlation)
plt.figure(figsize=(8, 6))
plt.scatter(df['SmokingStatus_Num'], df['LungCancer'], c='blue', alpha=0.7)
plt.xlabel('Smoking Status (0=No, 1=Yes)')
plt.ylabel('Lung Cancer (True/False)')
plt.title('Smoking Status vs. Lung Cancer Incidence')
plt.grid(True)
plt.show()
