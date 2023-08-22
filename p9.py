import pandas as pd
import numpy as np
data = pd.DataFrame({"days":[1,2,3,4,5,6,7,8,9,10],"steps":[4335,9552,7332,4504,5335,7552,8332,6504,8965,7689]})
data['steps'] =data['steps']+1000
print(data)
hs = data[data['steps']>7000]['days']
print("days:",list(hs))
