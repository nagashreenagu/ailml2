import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-07/Desktop/dataset2/titanic.csv")
print(data)
print(data.info)
print(data.shape)
print(data.isnull().sum())
print(len(data))
print(data['Survived'].value_counts().plot(kind = 'bar'))
print(data[data['Sex']=='female']['Survived'].value_counts().plot(kind = 'bar'))
print(data[data['Pclass']==1]['Survived'].value_counts().plot(kind = 'bar'))
plt.hist(data['Age'])
plt.pie(data["Pclass"])

