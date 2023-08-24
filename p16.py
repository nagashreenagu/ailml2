import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('C:/Users/SPTINT-07/Downloads/tips (2).csv')
print(data)
print(data['day'].value_counts())
plt.bar(data['day'],data['tip'])
plt.xlabel('day')
plt.ylabel('tips')
plt.show()

