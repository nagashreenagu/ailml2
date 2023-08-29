import pandas as pd
import seaborn as sns
data = pd.read_csv("C:/Users/SPTINT-07/Desktop/dataset/dataset2/titanic.csv")
print(data)
print(data.isna().sum())
print(data.notnull().sum())
sns.heatmap(data.isna())
print(data.shape)
print(data.dropna(inplace=True))
sns.heatmap(data.isna())
print(data.shape)
df = data.drop(['Cabin'],axis=1)
print(df)

