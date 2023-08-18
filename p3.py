import numpy as np
a=np.array([[1,3,5],[7,2,1]])
b=np.array([[6,3,2],[8,5,2]])
print("sum of array is:",a.sum())
print("min of array is:",a.min())
print("max of array is:",a.max())
print("add of array is:",a+b)
print("sub of array is:",a-b)
print("mul of array is:",a*b)
print("the average of array:",b.mean())
print("the min of array:",a.min(axis=1))
print("the max of array:",a.max(axis=1))
print("the cumulative sum of array:",a.cumsum())

