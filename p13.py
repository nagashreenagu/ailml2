import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-07/Desktop/dataset2/titanic.csv")
print(data)
print(pd.DataFrame(data))
c = data.dropna()
print(c.sum())
print(c["Fare"].sum())
print(c.value_counts())
print(c['Survived'].value_counts())
print(c.agg(['sum','max','min']))

