# for loop -->  
# def of loop --> 

numbers = [11,22,33,44]
for num in numbers:
    print(num)
print("end of loop")

name = "Naveen"
for char in name:
    print(char)
print("end of loop..........................")

# numbers = (11,22,33,44)
# for num in numbers:
#     print(num)
# print("end of loop")

# name = 'vaibhav'
# for num in name:
#     print(num)
# print("end of loop")

# we can't add itarable object on int,float,complex

# details = {'name':'harish','age':25,'per':89,'course':"python"}
# for key in details:
#     print(details[key])

# print values 
details = {'name':'harish','age':25,'per':89,'course':"python"}
for k in details.values():
    print(k)

# print keys
details = {'name':'harish','age':25,'per':89,'course':"python"}
for k in details.keys():
    print(k)
# 
details = {'name':'harish','age':25,'per':89,'course':"python"}
for i,j in details.items():
    print(i,":",j)

# WAP to print square of all numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print(i*i)

# WAP to print list of cube of all numbers
numbers = [1,2,3,4,5]
cube = []
for i in numbers:
    c = i**3
    cube.append(c)
print(cube)

# print a set of square of all numbers
numbers = [1,2,3,4,5]
s = set()
for i in numbers:
    e = i**2
    s.add(e)
print(s)    

students = {'kunal','rahul','vijay','ajay'}
l = []
for i in students:
    l.append(i.upper())
print(l)

# create a dict of square of numbers
numbers = [1,2,3,4,5]
square = {}
for i in numbers:
    d = i**2
    square[i] = d
print(square)


# emp = {'kunal':50000,'ajay':40000,'vijay':30000,'umesh':60000}
# for name,price in emp.items():
#     increment = price*10/100
#     emp[name]=price+increment
# print(emp)


emp = {'kunal':50000,'ajay':40000,'vijay':30000,'umesh':60000}
for name,price in emp.items():
    increment = price*10/100
    emp[name]=price+increment
print(emp)

oppo = {"A14":20000,"A15":25000,'A20':30000,'A25':50000} #-20%
for model,price in oppo.items():
    off = price*20/100
    oppo[model] = price-off
print(oppo)


number = [11,22,33,44,55,66,77,88,99]
square = []
for sq in number:
    s = sq**2
    square.append(s)
print(square)

l = [1,2,3,4,5,6,7,8,9,10]
s = set()
for cube in l:
    d = cube**3
    s.add(d)
    print(cube)
print(s)

details = {"s1":{'name':'naveen','id':101,'percentage':78,'course':'python'},"s2":{'name':'pratham','id':102,'percentage':81,'course':'java'}}
for s1 in details['s1'].items():
    print(s1)
for s2 in details['s2'].items():
    print(s2)

company = {"emp1":20000,'emp2':30000,'emp3':40000,"emp4":50000}
for e,s in company.items():
    inc = s*10/100
    company[e]=s+inc
print(company)

cube = [3,4,7,9,11,33,24]
empty =list()
for c in cube:
      v=c**3
      empty.append(v)
print(empty)

company={'emp1':{'sal':20000,'id':[123,234,345,],'name':'navin'},'emp2':{'sal':30000,'id':[124,567,678,789],'name':'ishwar'}}
print(company)
company['emp2']['sal']=50000
print(company)
company['emp1']['id'][1]=321
print(company.update(id=000))
print(company.get('emp1'))












