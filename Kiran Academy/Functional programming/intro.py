# # functional programming 
# def mysum():
#     a = int(input("enter number 1: "))
#     b = int(input("enter number 1: "))
#     print(a+b)

# mysum()
# def mysub():
#     a = int(input("enter number 1: "))
#     b = int(input("enter number 1: "))
#     print(a-b)

# mysub()
# def mydiv():
#     a = int(input("enter number 1: "))
#     b = int(input("enter number 1: "))
#     print(a/b)
# mydiv()

# x=10
# y=20
# z=30
# def fun():
#     global x,y,z
#     x=40
#     y=50
#     z=1000
#     print(x,y,z)
# fun()
# print(x,y,z)

# In python , the global keyword is used to declare that a variable inside a function refers to a global variable defined outside the function, rather than creating a new local variable with the same name with in the function's scope.

# def fun():
#     square = int(input("enter num :"))
#     return square**2
# print(fun())

# def fun():
#     x=100
#     y=200
#     print('hello')
#     print('welcome')
#     return x,y
# print(fun())
# WAP TO CALL CUBE OF ANY NUMBER
def cube():
    a = int(input("Enter Cube: "))
    return a**3
# print(cube())

# create a function to check positive or not
# def positive():

# create a funtion to check number is even or not
def eve_not():
    num = int(input("enter number :"))
    if num%2==0:
        return True
    else:
        return False
# print(eve_not())

# def divisible():
#     num = int(input("enter number :"))
#     if num%5==0:
#         return True
#     else:
#         return False
# print(divisible())

# def sum(n1,n2):
#     result = n1+n2
#     return result
# print(sum(10,20))

# create a function square of any number
# def square(s1):
#     return s1**2
# print(square(3)) 

# create a function to check number is odd or not
# def odd(o1):
#     return o1%2==1
# print(odd(3))

def details(name,age,marks):
    data = f'Name:{name}\nAge:{age}\nMarks:{marks}'
    return data
print(details('Navin kairamkonda',23,90))

# create a function to cal sum of all numbers from an itreable
i = [1,2,3,4,5]
def sum_numbers(itrable):
        sum = 0
        for num in itrable:
             sum=sum+num
        return sum
print(sum_numbers(i))

# create a function to reverse a string 
# by using slicing
name='navin'
def reverse(n1):
     r = n1[-1::-1]
     return r
print(reverse(name))

# by using for loop
def reverse_str(word):
    rev = ''
    for char in word:
          rev=char+rev
    return rev
print(reverse_str(name))

# types of arguments
'''
1. POSITIONAL ARGUMENT
2. KEYWORD ARGUMENT
3. DEFAULT ARGUMENT
4. ARBITARY ARGUMENT{
  A.POSITIONAL ARGUMENT (*)
  B.KEYWORD ARGUMENT  {**}
}
'''
# 1. POSITIONAL ARGUMENT
def details(name,city):
    return f'Name: {name}\nCity: {city}'
print(details('navin','solapur'))

# 2. KEYWORD ARGUMENT
def details(name,city):
    return f'Name: {name}\nCity: {city}'
print(details(city='solapur',name='navin'))

# use both positional and keyword
#          positional & keyword
print(details('navin',city='solapur'))

#3. DEFAULT ARGUMENT
def details(name,city,ins='jbk'):
    return f'Name: {name}\nCity: {city}\nInstitute: {ins}'
print(details('navin','solapur'))
print(details('pratham','solapur','TKA'))
print(details('ishwar','solapur','MIT'))

# 4. ARBITARY ARGUMENT :- 
# positional argument
def data(*args):
    print(args)

print(data('navin',23))

# keyword argument
def data2(**args):
     print(args)
print(data('navin',23,89))
rev = ''
for char in name:
     rev = char+rev
print(rev)

# CREATE A FUNCTION TO CHECK NUMBER IS PRIME OR NOT
def prime(num):
    for i in range(2,num):
          if i%num==0:
               return False
    return True
print(prime(5))
          
# CREATE A FUNCTION TO CHECK NUMBER IS PERFECT OR NOT
def isprime(num):
    sum=0
    for i in range(num):
        if num%2==0:
            return True
    return False

def f1():
    print('welcome to f1')
    def f2():
        print('welcome to f2')
    return f2
f2 = f1()
f2()

# calling function
def f1():
    x=10
    def f2():
        y=20
        return y
    return x,f2
x,f2=f1()
y=f2()
print(x,y)

def d1():
    name='vaibhav'
    def d2():
        last_name='patil'
        return last_name
    return name,d2
name,d2=d1()
last_name = d2()
print(name,last_name)

def f1(fname):
    fn=fname.upper()
    def f2(lname):
        ln = lname.upper()
        return f'{fn} {ln}'
    return f2
f2=f1('Navin')
print(f2('kairamkonda'))

# lambda function
# lambda is a ananomouse funtion which is not required any variable or name
print((lambda n1,n2 : n1+n2) (20,67))

print((lambda even : even%2==0) (9)) 

cal = lambda n1,n2 : (n1+n2,n1-n2,n1*n2,n1/n2)
print(cal(9,8))

numbers = [1,2,-3,4,5,-6,-7,8,-9]
def isposititve(num):
    if num>0:
        return True
    else:
        return False
print(set(filter(isposititve,numbers)))

number = [1,3,4,5,6,8,7,9,11,33,44]
def iseven(num):
    if num%2==0:
        return True
    else:
        return False
print(list(filter(iseven,number)))

# numbers = [1,2,-3,4,5,-6,-7,8,-9]
# filter(lambda num : num>0)

numbers = (14,3,4,8,9,12,45,24,36,87,48,60)
def fun(num):
    if num%3==0 and num%4==0:
        return True
    else:
        return False
print(list(filter(fun,numbers)))

result = {'kunal':89,'rajesh':31,'varun':78,'sujay':25,'vijay':35}
print(list(filter(lambda passed : result[passed]>40,result)))

emp = {'kunal':89000,'rajesh':31000,'varun':78000,'sujay':25000,'vijay':36000,'kishor':45000,'rahul':39000}
print(list(filter(lambda name : emp[name]>35000 and emp[name]<50000,emp)))

student = ['kunal','rajesh','varun','sujay','vijay','jay','vaibhav']
print(list(map(lambda name : name.upper(),student)))

numbers = [10,20,30,40,50,60]
print(list(map(lambda half : int(half/2) , numbers)))

numbers = (1,2,3,4,5,6,7,8,9,10)
print(list(map(lambda num : num/2,filter(lambda num : num%2==0 , numbers))))