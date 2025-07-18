# Set is comma seprated values with in {}
# it is unorderd, mutable, hetrogenous collection of immutable elemnts where duplicates are NOT allowed.
num = {11,22,33}
print(type(num))  # <class 'set'>
print(num)  # {11, 22, 33}

s={11,10.89,True,(1,2,3),"jay"}
print(s)  # {True, 10.89, 11, (1, 2, 3), 'jay'}
print(type(s))  # <class 'set'>

# add elements to set
s = {11, 22, 33}
s.add(44)  # Adds the specified element to the set
s.add(55)  # Adds another element to the set
print(s)

# remove elements from set
s1={11,22,33,44,55}
s1.remove(22)  # Removes the specified element from the set
print(s1)  # {33, 11, 44, 55}
print(s1,'\n',s1.pop())  # Removes and returns an arbitrary element from the set

# discard elements from set
s2={11,22,33,44,55}
s2.discard(222)  # Removes the specified element from the set if it exists
print(s2)

# intersection()  # Returns a new set with elements common to the set and all others
s1 = {11,22,33,44,55}
s2 = {33,44,55,66,77}
print(s1.intersection(s2))

s1 = {11,22,33,44,55}
s2 = {33,44,55,66,77}
l1 = {33,44,99,88}
t1 = {33,44,78,90}
print(s1.intersection(s2,l1,t1)) #{{33, 44} <-- common value} # Returns a new set with elements common to the set and all others

# defference()  # Returns a new set with elements in the set that are not in the others
s1 = {11,22,33,44,55}
s2 = {33,44,55,66,77}
print(s1.difference(s2))  # {11, 22}
print(s2.difference(s1))  # {66, 77}

# intersection_update()
s1.intersection_update(s2)  # Updates the set with elements common to the set and all others
print(s1)  # {33, 44, 55}

# symmetric_difference()
s1 = {11,22,33,44,55}
s2 = {33,44,55,66,77}
print(s1.symmetric_difference(s2)) # Returns a new set with elements in either the set or the others but not both
print(s1,s2)

batch1272 = {'jay','ajay','pavan','vijay','ramesh'}
batch1276 = {'kunal','umesh','arun','pavan','ajay','abhijeet'}
s = batch1272.union(batch1276)  # Returns a new set with elements from both sets
print(s)

p = batch1272.update(batch1276)  # Updates the set with elements from both sets
print(p)

s1 = {11,22,33,44,55,66}
s2 = {11,22,33}
print(s1.issuperset(s2))
print(s1.issubset(s2))  # Checks if the set is a subset of another set
print(s2.issuperset(s1))
print(s2.issubset(s1))

