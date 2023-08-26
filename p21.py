import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-07/Downloads/athele events.csv")
print(data)

df=pd.DataFrame(data)
plt.hist(data['Age'])
plt.show()

data[data['Sex']=='M'],data['Medal'].value_counts().plot(kind='bar')
plt.title("Medal wone by males")
plt.show()

plt.scatter(data['Height'],data['Weight'])
plt.title("height and weight")
plt.show()

data[data['Year']==2000]['Medal'].value_counts().plot(kind='bar')
plt.title("medals won in the year")
plt.show()

