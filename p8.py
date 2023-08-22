import pandas as pd
import numpy as np
data = pd.DataFrame([[1,2,3,4],[5,6,7,8],[11,12,13,10]],columns=["kan","eng","maths","science"])
print(data)
print(data.sum)
print(data["maths"].sum())
print(data.value_counts())
print(data["eng"].value_counts())
print(data.agg(['sum','min','max']))
print(data.describe())

