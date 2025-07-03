
# python definaion :- a variable in python is a name that is referance or pointer to an object variable are like container are use to store differnt types of data once a variable is assinged a value you can use in place of value 
name = 'Naveen'
age = 21
print(name)
# id() is used to check id of object
print(id(name))
print(id(age))

# sum of two number
# a = int(input("Enter first num :"))
# b = int(input("Enter second num :"))
# print((a+b))

# input() input is a pre-defined function used to take input from the user
# x = eval(input("Enter Number :"))
# square = x*x
# print("You Enterd",x,"Square is",square)

# WAP Area of Rectangle
# length = eval(input("Enter Length :"))
# width = eval(input("Enter width :"))
# print("Area of rectangle is :",length*width)

''''A data type is used to represend the kind of value a variable holds. it tells python what type of data is bean stored & what operaions can be performe on it'''
# Example of int it is used to rep. int value whole number
num1 = 199
print(type(num1))

# Example of float it is used to rep. float value number wth decimal point

num2 = 189.79
print(type(num2))   #<class 'float'>

num3 = 5+10j
print(type(num3))  #<class 'complex'>
print(num3)

# Example of str is used to represend string or text string is the collection of characters

str1 = "Naveen"
str2 = "199"
print(type(str1))  #<class 'str'>
print(type(str2))  #<class 'str'>


'''Indexing & Slicing'''
# Single character from string
str3 = "Elitebook"
print(str3[0])
print(str3[-2])


# Example of indexing
institute = "the kiran Academy"
print(institute[1])
print(institute[4])
print(institute[-9])

# slicing is a technique it is used to access multiple char.
name = "rajeshkumar"
print(name[0:3])  #raj
print(name[2:-5:1])  #jesh
print(name[-5:-1:1])  #kumar

institute2 = "the kiran academy"
print(institute2[0:3:1])  #the
print(institute2[4:9:1])  #kiran
print(institute2[-9:3:-1])  #narik
print("END OF THE CODE")  
#                                     11 10 9 8 7 6 5 4 3 2 1
#                                       r a m e s h w a r a m
#                                       0 1 2 3 4 5 6 7 8 9 0
name2 = "rameshwaram"
print(name2[0:3:1])   #ram
print(name2[2:6:1])   #mesh
print(name2[4:-1:1])  #shwara
print(name2[-1:-4:-1])  #mar
print(name2[-3:11:1])   #ram
print(name2[2:-12:-1])   #mar
print(name2[-6:-9:-1])

