name = "naveen"
print(name)
# import demo1
# print(demo1.age, demo1.city)

# from module import name
from demo1 import city
print(city)

from sys import getsizeof
s = ['vijay','sujay','ajay']
x = ('vijay','sujay','ajay')
print('list size :',getsizeof(s))
print("tuple lize is :",getsizeof(x))

# immutable tuples
# t2 = (11,22,33)
# t1 = (11,22,33)
# print(id(t1),id(t2))

# mutable lists
t2 = [11,22,33]
t1 = [11,22,33]
print(id(t1),id(t2))