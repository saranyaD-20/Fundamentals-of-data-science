import pandas as pd
data = {
    'DISEASE_NAME': ['Hypertension', 'Asthma', 'Depression', 'Arthritis', 'Migraine'],
    'DIAGNOSED_PATIENTS': [250, 180, 160, 140, 80]
}

df = pd.DataFrame(data)

df_sorted = df.sort_values(by='DIAGNOSED_PATIENTS', ascending=False)

most_common_issue = df_sorted.iloc[0]['DISEASE_NAME']
frequency = df_sorted.iloc[0]['DIAGNOSED_PATIENTS']

print("Most Common Health Issue:")
print("Health Issue:", most_common_issue)
print("Number of Diagnosed Patients:", frequency)

print("\nFrequency Distribution of Health Issues:")
print(df_sorted)
