# Create an empty list and add 'apple', 'banana', and 'cherry' to it.
fruits = []
print(len(fruits))
fruits.extend(['apple','banana','cherry'])
print(fruits)  # ['apple', 'banana', 'cherry']
print(len(fruits))

# Given the list [10, 20, 30, 40, 50], add 60 to it and remove 30.
l = [10,20,30,40,50]
l.append(60)
l.remove(30)
print(l)

# Make a copy of the list [1, 2, 3, 4, 5] and reverse it.
l1 = [1,2,3,4,5]
l4 = l1.copy()
l4.reverse()
print("original list =",l1)
print("copy of list =",l4)

# Add 400 to the end and 50 to the beginning of the list [100, 200, 300].
l2 = [100,200,300]
l2.insert(0,50)
l2.append(400)
print(l2)

# Find the index of 40 in the list [10, 20, 30, 40, 50] and replace it with 45.
l3 = [10,20,30,40,50]
print(l3.index(40))  # Returns the index of the first occurrence of 40
l3[3]=45
print(l3)

# Sort the list [9, 2, 8, 4, 1] in ascending order and then in descending order.
s = [9,2,8,4,1]
s.sort()
print("original list :",s)
print("acending order :",s)
s.sort(reverse=True)  # Sorts the list in descending order
print("descending order :",s)

# Count how many times 5 appears in the list [1, 5, 3, 5, 7, 5].
c = [1,5,3,5,7,5]
print("count of 5 in list :",c.count(5),"Times")  # Counts the occurrences of 5 in the list

# Merge two lists: [1, 2, 3] and [4, 5, 6].
m1 = [1,2,3]
m2 = [4,5,6]
m1.extend(m2)
print(m1)

# Clear all elements from the list [10, 20, 30].
cl = [10,20,30]
cl.clear()
print("cleared list :",cl)

# Convert the list ['a', 'b', 'c'] into a string separated by - (e.g., 'a-b-c').
co = ['a','b','c']
print('-'.join(co))

# Extend the list [1, 2, 3] with another list [4, 5, 6].
m1 = [1,2,3]
m2 = [4,5,6]
m1.append(m2)
print(m1)

# Remove the last element from the list [100, 200, 300, 400] and store it in a variable.
r = [100,200,300,400]
print(r)
a = r.pop(-1)
print(a)

# Insert 25 at the second position in the list [10, 20, 30, 40].
i = [10, 20, 30, 40]
i.insert(1,25)
print(i)  # [10, 25, 20, 30, 40]

# Find the index of 'banana' in the list ['apple', 'banana', 'cherry'].
print(fruits.index('banana')) # Returns the index of 'banana' in the list

# Copy the list [5, 10, 15] into a new variable and modify the new list without changing the original.
c = [5, 10, 15]
cp = c.copy()
print(c)
cp.append(20)
print(cp)

# Multiply the list [1, 2, 3] by 3 and store the result.
m = [1,2,3]
result = m[0]*3,m[1]*3,m[2]*3
print(result)

# Check how many times 'apple' appears in the list ['apple', 'orange', 'apple', 'grape'].
c = ['apple', 'orange', 'apple', 'grape']
check = c.count('apple')
print(check)

# Find the maximum and minimum values in the list [7, 2, 9, 1, 5].
f = [7,2,9,1,5]
print(max(f))
print(min(f))

# Convert a string "hello" into a list of characters.
con = 'hello'
c = list(con)
print(c)

mobiles = {'samsung':{'GalaxyA21s':{'ram':{'4gb':'64gb','6gb':'128gb','8gb':'256gb'},'price':[15600,17899,19990],'color':['red','cyan','black']},
                      'GalaxyA22s':{'ram':{'6gb':'128gb','12gb':'256gb'},'price':[21000,22890],'color':['green','blue','red']},
                      'GalaxyA30':{'ram':{''}}},
                      
                      'oppo':{},'vivo':{},'apple':{}}


