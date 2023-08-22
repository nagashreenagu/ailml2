import pandas as pd
import numpy as np
dict = {'first score':[10,19,np.nan, 30],
        'second score':[np.nan,40,56,91],
        'third score':[51,15,np.nan,51]}
data = pd.DataFrame(dict)
print(data)
print(data.isnull())
print(data.notnull())
print(data.fillna(0))
print(data.fillna(method='pad'))
print(data.fillna(method='bfill'))
print(data.replace(to_replace=np.nan,value=-99))
print(data.dropna())
print(data.dropna(how="all"))

