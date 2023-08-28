import pandas as pd
data=pd.read_csv("D:/Dataset/mpg.csv")
print(data)
stats=data.describe()
print(stats)

