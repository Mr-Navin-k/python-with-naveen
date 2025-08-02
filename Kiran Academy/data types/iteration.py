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

# sum of all numbers
numbers = [1,2,3,4,5]
sum = 0
for num in numbers:
    sum = sum+num
print(sum)

# WAP to calculate of all numbers
numbers = [1,2,3,4,5]
multiply = 1
for num in numbers:
    multiply = num*multiply
print(multiply)

# 
books = {'python':300,'java':500,'data science':400,'ML':700}
t = 0
for total in books.values():
    t=total+t
    print(total)
print(t)

rajesh_result = {'teat1':80,'test2':70,'test3':69,'test4':90}
obt = 0
for marks in rajesh_result.values():
    obt = obt+marks
    total = len(rajesh_result)*100
    per = obt/total*100
print(per,'%')

data = {'ishwar':{'test1':60,'test2':70,'test3':80},'Navneet':{'test1':70,'test2':75,'test3':85},'Yash':{'test1':66,'test2':78,'test3':90}}
result={}
for name,test_marks in data.items():
    print(name,test_marks)
    obt = 0
    for marks in test_marks.values():
        obt = obt+marks
        total = len(test_marks)*100
        per = obt/total*100
        result[name]=per
print(result)

number = [1,2,3,4,5,6]
sum = 0
for num in number:
    sum = sum+num
print(sum)

number = [1,2,3,4,5,6]
m = 1
for mul in number:
    m=m*mul
print(m)

books = {'python':300,'java':500,'data science':400,'ML':700}
sum=0
for book in books.values():
    dis = book*10/100
    sum = sum+book-dis
print(sum)







