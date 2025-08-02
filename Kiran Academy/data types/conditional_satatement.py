
# if condition 
# if => execuye a block of code if the condition is true if condition is false no code will be executed
# num = int(input("Enter Number :"))
'''
# if num>0:
#     print("Number is positive")
# print("End of codeing.....")

# WAP to check number is > 10
n = int(input("Enter Number :"))
if n>10:
    print("number is greater then 10")

# WAP to check number is * 5
n = int(input("Enter Number :"))
if n%5==0:
    print("number is divisible by 5")

# WAP to check number is divisible by 3 & 4
a = int(input("Enter Number :"))
if a%4==0 and a%3==0:
    print("number is divisible by")
'''
# 
# numbers = [1,-2,3,4,-5,6,-7,8,9,10]
# for n in numbers:
#     if n>0:
#         print(n)

# WAp to iterate number which is divisible by 5
# numbers = [3,5,6,10,15,17,80,25,28,50]
# for num in numbers:
#     if num%5==0:
#         print(num)

# # wap to iterate only odd numbers
# numbers = [3,5,6,10,15,17,80,25,28,50]
# for num in numbers:
#     if num%2!=0:
#         print(num)
# WAP to check if starting letter starts with k
# student = ['kunal','pavan','vijay','akash','arun','kiran','kirti']
# for s in student:
#     if s[0]=='k':
#         print(s)

# student = ['kunal','ajay','pavan','vijay','akash','arun','kiran','sujay','kirti']
# for s in student:
#     if s.endswith('jay'):
#         print(s)

# student = ['kunal','ajay','pavan','vijay','akash','arun','kiran','sujay','kirti']
# for s in student:
#     if s[-3:]=='jay':
#         print(s)

# wap to prt lis of passed students
stud = {'kunal':89,'pavan':32,'karan':21,'vijay':80,'akash':75}
l = []
for n,m in stud.items():
    if m>=40:
        l.append(n)
print(l)  #['kunal', 'vijay', 'akash']

# wap to prt dict of passed students

#
emp = {'kunal':89000,'pavan':32000,'karan':21000,'vijay':80000,'akash':75000}
for name,salary in emp.items():
    if salary<50000:
        inc = salary*20/100
        emp[name]=salary+inc
print(emp)

# if else condition 
# num = int(input("Enter Number :"))
# if num>0:
#     print("Number is positive")
# else:
#     print("Number is negative")

# WAP to check number is greater then 10
# n = int(input("Enter number :"))
# if n>10:
#     print("num is greater then 10")
# else:
#     print("num is not greater then 10")

# WAP to check number is divisible by 12 or not
# n = int(input("Enter number :"))
# if n%12==0:
#     print("number is divisible by 12")
# else:
#     print("number is not divisible by 12")

# WAP to check number is even or odd
# even_or_odd = int(input("Enter number :"))
# if even_or_odd%2==0:
#     print("even...")
# else:
#     print("odd...")

# WAP to print list of positive number and print list of negtive number
# numbers = [-1,2,-3,4,5,-6,7,8,-9,10]
# positive = []
# negative = []
# for n in numbers:
#     if n>0:
#         positive.append(n)
#     else:
#         negative.append(n)
# print(f"positive number {positive}")
# print(f"negative number {negative}")

# WAP to print set of square of even numbers and list of cube of odd numbers
# numbers2 = [1,2,3,4,5,6,7,8,9,10]
# even_square = set()
# odd_cube = list()
# for n2 in numbers2:
#     if n2%2==0:
#         odd_cube.append(n2**3)
#         print(n2)
#     else:
#         even_square.add(n2**2)
#         print(n2)
# print(f"Even Numbers {even_square}")
# print(f"Odd Numbers {odd_cube}")

# WAP to print list of name of passed student and list of name of failed student
# student = {'samarth':90,'abhijeet':70,'akash':21,'snehal':91,'sanket':32,'ajinkya':33}
# passed = []
# failed = []
# for name,marks in student.items():
#     if marks>40:
#         passed.append(name)
#     else:
#         failed.append(name)
# print(f"passed students : {passed}")
# print(f"failed students : {failed}")


# emp = {'samarth':90000,'abhijeet':70000,'akash':21000,'snehal':91000,'sanket':32000,'ajinkya':33000}
# for name,salary in emp.items():
#     if salary<50000:
#         inc = salary*20/100
#         emp[name]=inc+salary
#     else:
#         inc = salary*10/100
#         emp[name]=inc+salary
# print(emp)

# hacker rank

# dmart_mrp = {'sakhar':42,'shengdana':120,'shabudana':80,'mungdal':80,'turdal':140,'kaju':1000,'badam':500}
# sel_price = {}
# for items,mrp in dmart_mrp.items():
#     # print(items,mrp)
#     if mrp>100:
#        dic = mrp*15/100
#        sel_price[items] = mrp-dic
#     else:
#         dic = mrp*10/100
#         sel_price[items] = mrp-dic
# print(dmart_mrp)
# print(sel_price)

# range --> 
for i in range(1,10,2):
    print(i)

# if elif else statement
# WAP to check if number is negative, positive or zero
# num = int(input("Enter Number :"))
# if num>0:
#     print('positive number')
# elif num<0:
#     print("negative number")
# else:
#     print('Zero number')

# marks = int(input("enter marks :"))
# if marks>90:
#     print("A+")
# elif marks>80:
#     print("A")
# elif marks>70:
#     print("B+")
# elif marks>60:
#     print("B")
# else:
#     print("C")

# n1 = int(input("Number 1 :"))
# op = input("Enter Operator :")
# n2 = int(input("Number 2 :"))
# if op=="+":
#     p = n1+n2
#     print(p)
# elif op=="-":
#     s = n1-n2
#     print(s)
# elif op=="*":
#     m = n1*n2
#     print(m)
# elif op=="/":
#     d = n1/n2
#     (d)
# else:
#     print("enter valid operator")

emp = {"Abhijeet":60000,"Rushikesh":30000,"Sonal":70000,"Pranjali":90000,"Yash":40000,"Uttam":80000,"Nirav":20000,"Akash":100000}
for name,salary in emp.items():
    print(name,salary)
    if salary<=35000:
        new = salary*20/100
        emp[name]=new+salary
    elif salary<=50000:
        new = salary*15/100
        emp[name]=new+salary
    elif salary<=85000:
        new = salary*10/100
        emp[name]=new+salary
    else:
        new = salary*5/100
        emp[name]=new+salary
print(emp)