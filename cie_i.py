# -*- coding: utf-8 -*-
"""CIE I.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zC1mumBtduuHwW66U9mWNlVxc5TMqCV2
"""

import pandas as pd
import numpy as np

series_A=pd.Series([1,2,3,4,5])
series_B=pd.Series([2,4,6,8,10])
cmn=series_A[series_A.isin(series_B)]
df=np.abs(cmn)
print(df.values)

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('mtcars.csv')

plt.figure(figsize=(8,6))
plt.hist(df['mpg'],bins=10,edgecolor='k')
plt.title("Histogram of MPG")
plt.xlabel("MPG")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('mtcars.csv')
plt.scatter(df['mpg'],df['wt'],color='blue')
plt.title('Scatter Plot')
plt.xlabel('mpg')
plt.ylabel('wt')
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

pd.read_csv('mtcars.csv')
transmission_counts = df['am'].value_counts()
transmission_counts.plot(kind='bar')
plt.title('Frequency Distribution of Transmission Type')
plt.xlabel('Transmission Type')
plt.ylabel('Frequency')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('mtcars.csv')
plt.boxplot(df['mpg'])
plt.title("Boxplot")
plt.xlabel('MPG')
plt.grid(True)
plt.show()

print("hello world This is second commit")