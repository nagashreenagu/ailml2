#lambda
a= lambda x :x+5
print("sum is :",a(3))
l = lambda a,b :a+b
print("the sum of 2 numbers is :",l(9,8))
c = lambda y,z : y if (y>z)else z
print("greatest number is :",c(10,72))
a= lambda y :y**2
print("the square is :",a(8))

#map
lst = [1,2,3,4,5,6,7,8]
l1 = list(map(lambda x :x+5,lst))
print(l1)

#filter
lst = [1,2,3,4,5,6,7,8]
l2 = list(filter(lambda x :x%2,lst))
l3=list(filter(lambda x:x%2==0,lst))
print("filter of odd numbers:",l2)
print("filter of even numbers :",l3)
#reduce
from functools import reduce
lst = [1,2,3,4,5,6,7,8]
l3 = (reduce(lambda a,b :a+b,lst))
print("the single element is :",l3)





