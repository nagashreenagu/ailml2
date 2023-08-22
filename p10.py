import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-07/Desktop/dataset2/titanic.csv",index_col='Name')
print(data.shape)
print(data.info)
print(data.loc[data['Age']>50])
print(data.iloc[4:9,11:15])

