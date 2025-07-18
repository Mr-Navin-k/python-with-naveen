# # upper()  # Converts all characters to uppercase
# institute = "the kiran acamedy"
# print(institute.upper())  
# print(institute)

# # lower()  # Converts all characters to lowercase
# ins = "JAVA BY KIRAN"
# print(ins.lower()) 
# print(ins)

# # title()   # Converts the first character of each word to uppercase
# name = 'java by kiran'
# print(name.title())  
# print(name)

# # capitalize()  # Capitalizes the first character of the string
# institute = "the kiran academy"
# print(institute.capitalize())  
# print(institute)

# # isalpha()   #isalpha() checks if all characters in the string are alphabetic
# name = "Naveen"
# print(name.isalpha())  #True

# name = "Naveen@123"
# print(name.isalpha())  #False

# name = "Naveen Kairamkonda"
# print(name.isalpha())  #False 

# # isnumeric() checks if all characters in the string are numeric
# n1 = "1234567890"
# print(n1.isnumeric())

# # isspace()
# name = "naveen"
# print(name.isspace())  #False

# name = " "
# print(name.isspace())  #True

# isalnum()

# name = "Naveen"
# print(name.isalnum())  #True
# name = "12345"
# print(name.isalnum())   #True
# name = "Naveen@123"
# print(name.isalnum())   #False

# # split()
# name = "The python introduction"
# print(name.split())    #['The', 'python', 'introduction']

# name = "The python introduction"
# print(name.split(sep="o"))   #['The pyth', 'n intr', 'ducti', 'n']

# islower() islower() checks if all characters in the string are lowercase & returns in boolean condition

name = "naveen"
print(name.islower())  #True

# isupper()  isupper() Checks if all characters in the string are uppercase & returns in boolean condition
print(name.isupper())  #True

# istitle() istitle() Checks if the string is in title case (first character of each word is uppercase) & returns in boolean condition
print(name.istitle())  #False

institute = "Java By Kiran, karve nagar"
print(institute.index("K"))  # 4
print(institute.index("By"))  # 5
print(institute.index("a",3))  #3
print(institute.index("a",5))  #11

# index() 
institute = "Java By Kiran, karve nagar"
print(institute.index('By'))  #5

# index() example of list
roll = [111,222,333,444,555,[11,22,33,44,[1,2,3,4,[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],5,6,7,8,9],55,66,77,88,99],666,777,888,999]
print(roll[5][4][4].index(0.4))

# count()  # Counts the occurrences of a substring in the string
# It returns the number of occurrences of the specified substring in the string.
institute = "Java By Kiran, karve nagar"
print(institute.count('a'))
print(institute.count('n'))
print(institute.count('a',-11))
print(institute.count('a',0,4))

#startswith()  # Checks if the string starts with a specified prefix
# It returns True if the string starts with the specified prefix, otherwise False.
institute = "Java By Kiran, karve nagar"
print(institute.startswith('J'))  #True
print(institute.startswith('N'))  #False
print(institute.startswith('K',8)) #True

#endswith()  # Checks if the string ends with a specified suffix
print(institute.endswith('u'))  #False
print(institute.endswith('r'))  #True
print(institute.endswith('a',0,4))  #True

#center()  # Centers the string within a specified width, padding with a specified character
ins = "Navin"
print(ins.center(70,'-'))   #--------------------------------Navin---------------------------------

# strip()  # Removes leading and trailing whitespace characters
# lstrip()  # Removes leading whitespace characters
# rstrip()  # Removes trailing whitespace characters
name = " naveen "
print(name.lstrip(' '))
print(name.strip(' '))
print(name.rstrip('n'))

# string methods is immutable we can't change the ogirinal value
print(name.replace("ee","iq"))

# how to find longest string in a sentences 
x = "Python String Manupulation is fun"
longest = max(x.split(), key=len)
print(longest)



