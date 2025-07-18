# List is a data type which enclose data with in square brackets seprated by commas.
# List is a mutaiable we can change the value of an list
numbers = [1, 2, 3, 4, 5]
print(type(numbers))  # <class 'list'>
numbers.append(6)
print(numbers)

ind = [1,2.2,True,1+7j,'Str']
print(ind[1])

inumbers = [11,22,33,44,55]
print(numbers[1])  #22
print(numbers[-1]) #55

print("end.............")

# List indexing and slicing
students = ['sanket','ajay',['abhijeet','shivam',[1,2,3,4,5],'vijay','samarth','vaibhav'],'akash']
print(students[1])
print(students[2][1])
print(students[2][3])
print(students[2][4])
print(students[2][2][2])
print(students[2][0][-4])
print(students[2][2][-1])

numbers = [11,22,33,44,55,66]
print(numbers[-2:1:-1])
print(numbers)

num2 = [10,20,30,40,[11,22,33,44,55,[1,2,3,4,5],66,77,88],50,60,70,80]

# print(num2[-2:-5:-1])
# print(num2[4][5][-3:0:-1])
print(num2[4][5][4])  #5
print(num2[1:4:1])  #[20,30,40]
print(num2[-2:-5:-1])  #[70,60,50]
print(num2[4][0:3:1])  #[11,22,33]
print(num2[-5][-1:-6:-2])  #[88,66,55]
print(num2[4][5][-3:-6:-1]) #[3,2,1]

# Example of list indexing
roll = [111,222,333,444,555,[11,22,33,44,[1,2,3,4,[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],5,6,7,8,9],55,66,77,88,99],666,777,888,999]
print(roll[5][4][4][3:-2:1])
print(roll[5][4][4][5:9:1])

name = "i'm a python developer from abc college solapur"
print(name.startswith("s"))
print(name.endswith("r"))
print(name.center(100,'-'))

# append() 
marks = [11,22,33,44,55,66,77,88,99]
marks.append(100)  # Append 100 to the end of the list
print(len(marks))
marks.insert(0,10)  # Insert 10 at the beginning of the list
print(marks,len(marks))

# insert()
s = ['kunal','raj','pavan']
s.insert(0,'naveen')  # Insert 'naveen' at the beginning of the list
print(s)  # ['naveen', 'kunal', 'raj', 'pavan']

n = [10,20,30,50,[11,22,33,55,66,77],60,80]
n.append(90)
n.insert(3,40)
n.insert(4,88)
print(n)

# Example of insert() & append()
students2 = ['pranali','tejal','samruddhi',['pranjal','ajay',['ajinkya','nikhil'],'vaibhav','abhijeet'],'mayuri','aarati']
students2.append('akash')  #['pranali', 'tejal', 'samruddhi', ['pranjal', 'ajay', ['ajinkya', 'nikhil'], 'vaibhav', 'abhijeet'], 'mayuri', 'aarati', 'akash']
students2.insert(2,'samarth')  #['pranali', 'tejal', 'samarth', 'samruddhi', ['pranjal', 'ajay', ['ajinkya', 'nikhil'], 'vaibhav', 'abhijeet'], 'mayuri', 'aarati', 'akash']
students2[4].append('vijay')  #['pranali', 'tejal', 'samarth', 'samruddhi', ['pranjal', 'ajay', ['ajinkya', 'nikhil'], 'vaibhav', 'abhijeet', 'vijay'], 'mayuri', 'aarati', 'akash']
students2[4].insert(2,'atul')  #['pranali', 'tejal', 'samarth', 'samruddhi', ['pranjal', 'ajay', 'atul', ['ajinkya', 'nikhil'], 'vaibhav', 'abhijeet', 'vijay'], 'mayuri', 'aarati', 'akash']
students2[4][3].append('nitin')  #['pranali', 'tejal', 'samarth', 'samruddhi', ['pranjal', 'ajay', 'atul', ['ajinkya', 'nikhil', 'nitin'], 'vaibhav', 'abhijeet', 'vijay'], 'mayuri', 'aarati', 'akash']
students2[4][3].insert(0,'pavan')  #['pranali', 'tejal', 'samarth', 'samruddhi', ['pranjal', 'ajay', 'atul', ['pavan', 'ajinkya', 'nikhil', 'nitin'], 'vaibhav', 'abhijeet', 'vijay'], 'mayuri', 'aarati', 'akash']
print(students2)

# remove()
n = [10,20,30,50,20,[11,22,33,55,66,77],60,80]
n.remove(50)
n.pop(3)
print(n)

# pop()
passed = ['pavan','ajay','kunal']
failed = ['samarth','akash','pranali']
passed.append(failed.pop(1))
print(passed)
print(failed)  # ['samarth', 'pranali']

# clear()  # Removes all elements from the list
marks = [11,22,33,44,55,66,77,88,99]
marks.clear()  # Clear the list
print(marks)  # []

# del()  # Deletes the entire list
marks = [11,22,33,44,55,66,77,88,99]
del marks[-1:-5:-1]
print(marks)

marks = [11,22,33,11,[10,20,30,20,40,50],44,55,66,77]
marks.pop(-2)
marks.pop(3)  #[11, 22, 33, [10, 20, 30, 20, 40, 50], 44, 55, 77]
marks[3].pop(-1)
marks[3].pop(3)
del marks[3][0:-1:1]   #[11, 22, 33, [40], 44, 55, 77]
num = marks.pop(-2)
marks[3].append(num)  #[11, 22, 33, [40, 55], 44, 77]
print(marks)

# tuple()
# set{}
# dictionary{}
# frozenset()
# list[# Creating a tuple

l = [11,22,33,22,44,55]
l.remove(44)
print(l.pop(3))

# sort()  # Sorts the elements of the list in ascending order
l = [2,4,1,6,3]
l.sort()
print(l)  # [1, 2, 3, 4, 6]

# sort(reverse = 'boolean') #it changes the original value of the list
numbers = [11,33,22,55,44,66]
numbers.sort(reverse=True)  # Sorts the list in descending order
print(numbers)  # [66, 55, 44, 33, 22, 11]

# sorted()  # Returns a new sorted list from the elements of any iterable #sorted is function
numbers = [11,33,22,55,44,66]
l = sorted(numbers)
print(l)
print(numbers)

# append() vs extend()
# extend()  # Extends the list by appending elements from another iterable
l1 = [11,22,33]
l2 = [44,55,66]
l1.extend(l2)
print(l1)

# l1 = [11,22,33]
# l2 = [44,55,66]
# l1.append(l2)
# print(l1)

# sort with extend()
# l1 = [11,55,33]
# l2 = [66,22,44]
# l1.extend()
# l.sort()
# print(l)

# copy()  # Creates a shallow copy of the list
# The copy() method returns a shallow copy of the list, meaning it creates a new list
batch1272 = ['naveen','rowdy','ishwar','pratham']
python_students = batch1272.copy()
python_students.append('navneet')
print('copy of batch1272 =',python_students)
print('Original List =',batch1272)  # Original list remains unchanged

# update the list (update the single value)
update = [11,222,333,444,55,66,77,88]
update[0] = 111
print(update)

# update by using slicing method (updates the multiple values)
update[4:8:1] = [555,666,777,888]
print(update)

# unpacking
t=[1,2,3]
a,b,c=t
print(a)
print(b)
print(c)

# packing
x=10
y=20
z=30
t=x,y,z
print(t)
# difference between list and tuple
# tuple requires less memory as compaired to list 
# list requires more memory as compaired to tuple
# tuples executation is fast as compaired to list

name = "Naveen"
l=['ajay']
l.append(name)  # This will raise an error because 'name' is a string, not an iterable of lists
print(l)  # ['ajay', 'N', 'a', 'v', 'e', 'e', 'n']