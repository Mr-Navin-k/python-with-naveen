# Arithamatic operator
# + - * / // % **

# n1 = ['10']
# n2 = ['20'] 
# print(n1+n2)
# print(dir(n1))
# print(n1.__add__(n2))

# l = [1,2,3]
# l1 = {3,4}
# print(l*2)

n1 = 10
n2 = 3
print(n1**n2)

# campairtion operators
# == != > < >= <=
n1 = 10
n2 = 11
print(n1>n2)  # False
print(n1<n2)  # True
print(n1>=n2)  # False
print(n1<=n2)  # True
print(n1==n2) #False
print(n1!=n2)  # True

# logical operators
# and or not

# identity operators
# is is not

# what is different between is and ==
# is checks the identity of the object, while == checks the value of the object
s1 = "naveen"
s2 = "naveen"
print(s1==s2)
print(s1 is s2)  # True, because both refer to the same object in memory

# membership operators
# in not in
l = [1,2,3,4,5]
print(1 in l)  # True
print(6 in l)  # False

r = "naveen"
print('n' in r)  # True
print('x' in r)  # False
print('n' not in r)  # False
print('x' not in r)  # True

# Assignment operators
# = += -+ /= //= 
num =10
num+=5
print(num)

num = 10
num %= 2
print(num)
numbers = [1,6,3,7]
sum = 0
for n in numbers:
    sum = sum+n
    print(sum)

# Reverse the string method - 1
name = 'java by kiran'
rev = ''
# print(name[::-1])
for char in name:
    rev = char+rev
print(rev)

# Reverse the string method - 2
institute = 'java by kiran'
words = institute.split()
l = []
for word in words:
    # print(word)
    rev = ''
    for char in word:
        # print(char)
        rev = char+rev
    print(rev)
    l.append(rev)
    print(l)

