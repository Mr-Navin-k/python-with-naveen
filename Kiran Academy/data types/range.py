# d = {}
# for i in range(int(input("Enter Number of Students :"))):
#     name = (input("Student Name :"))
#     marks = int(input("Student Marks :"))
#     d[name]=marks
# print(d)

# student = {'hindi':70,'english':90,'maths':80,'science':67,'marathi':39}
# for sub,marks in student.items():
#     obt = 0
#     total = len(student)*100
#     obt = marks+obt
#     print(obt)
    # print(total)

# name = input("enter something :")
# if name:
#     print("ok")
# else:
#     print("not ok")

# i = 0
# while i<5:
#     print("hello world")
#     i+=1
# print("coding")

# WAP a print number from 11 - 20 by using while loop
# i=11
# while i<=20:
#     print(i)
#     i+=1

# WAP to prt square of numbers from 1-10
# square = 1
# while square<=10:
#     print(square**2)
#     square+=1

# WAP to prt 11-20 square numbers
s = 11
d = {}
while s<=20:
    d[s]=s**2
    s+=1
print(d)

# WAP to cal sum of all numbers from 1-10
sum =0
num =1
while num<=10:
    sum+=num
    num+=1
print(sum)

# WAP to cal 11-20 all even numbers
# sum = 0
# e = 11
# while e<=20:
#     if e%2==0:
#         sum = sum+e
#     e+=1
# print(sum)

# WAP to prt outside from list
numbers = [11,22,33,44,55,66]
index = 0
while index<len(numbers):
    print(numbers[index])
    index+=1

# continue skip the current statement
# conditional satatement keywords are pass,continue,break
l = [1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i==7:
        break
    print(i)

