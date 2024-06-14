import pandas as pd
import numpy as np
property_data=pd.DataFrame({'property_ID':[1,2,3,4,5],
                'location':['A','B','C','D','B'],
                'no of bedrooms':[1,2,3,4,5],
                'area in square':[2000, 2500, 3000, 1800, 3500],
                'listing price':[200,390,300,400,890]})

avg=property_data.groupby('location')['listing price'].mean()
avg.columns=['location','average lisitng price']
print(avg)
no_of_bedrooms=(property_data['no of bedrooms']>4).sum()
print("/n number of bedrooms with more than four bedrooms:",no_of_bedrooms)
larger=property_data.loc[property_data['area in square'].idxmax()]
print(larger)
n
