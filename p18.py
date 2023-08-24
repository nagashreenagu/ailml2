import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('C:/Users/SPTINT-07/Downloads/tips (2).csv')
print(data)
plt.hist(data['total_bill'])
plt.show()

