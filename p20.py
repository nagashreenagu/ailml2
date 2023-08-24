import numpy as np
import pandas as pd

#reading data from an existing file
data=pd.read_csv("D:/Dataset/mpg.csv")
print(data)

#statistical deatails of data set
stats = data.describe()
print(stats)

#get all car with 8 cyclinders
df=data[data['cylinders']==8]['name']
print(df)

print(data['year'].value_counts())

