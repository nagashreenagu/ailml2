import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('C:/Users/SPTINT-07/Downloads/tips (2).csv')
print(data)
plt.scatter(data['sex'],data['tip'])

plt.xlabel('day')
plt.ylabel('tips')
plt.show()

