import numpy as np
#creating array from list with type float
a = np.array([[1,2,4],[5,8,7]],dtype = 'float')
print("array created using assed list:\n",a)
#creating array from tuple
b = np.array((1,3,2))
print("\n array created using passed tule:\n",b)
#creaing a 3*4 array with all zeros
c = np.zeros((3,4))
print("\n an array initialized with all zeros:\n",c)
#create a constant value array of complex type
d=np.full((3,3,),6,dtype='complex')
print("\n an array initailzed with all 6s","array type is complex:\n",d)
#creating an array with random values
e=np.random.random((2,2))
print("\n a random array:\n",e)
g=np.linspace(0,5,10)
print("sequiential array with 10 values :",g)
h=a.reshape(2,3)
print("reshape of an array:",h)


