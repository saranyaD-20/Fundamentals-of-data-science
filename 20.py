import matplotlib.pyplot as plt
import pandas as pd
dates=pd.date_range(start='2003-09-30',end='2003-10-04')
sales=[1000,2333,4434,500,9000]
sales_df=pd.DataFrame({'date':dates,'sales':sales})
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.bar(sales_df['date'],sales_df['sales'])
plt.xlabel("date")
plt.ylabel("sales")
plt.xticks(rotation=45)

plt.title("bar plot")
plt.subplot(1,2,2)
plt.plot(sales_df['date'],sales_df['sales'])
plt.xlabel("date")
plt.ylabel("sales")
plt.xticks(rotation=45)
plt.title("line plot")
plt.tight_layout()
plt.show()
