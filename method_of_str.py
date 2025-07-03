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

# islower()
name = "naveen"
print(name.islower())  #True

# isupper()
print(name.isupper())  #True

# istitle()
print(name.istitle())  #False

institute = "Java By Kiran, karve nagar"
print(institute.index("K"))  # 4
print(institute.index("By"))  # 5
print(institute.index("a",3))  #3
print(institute.index("a",5))  #11

# count()
institute = "Java By Kiran, karve nagar"
print(institute.count('a'))
print(institute.count('n'))
print(institute.count('a',-11))
print(institute.count('a',0,4))

#startswith()
institute = "Java By Kiran, karve nagar"
print(institute.startswith('J'))  #True
print(institute.startswith('N'))  #False
print(institute.startswith('K',8)) #True

#endswith()
print(institute.endswith('u'))
print(institute.endswith('r'))
print(institute.endswith('a',0,4))

#center()
ins = "Navin"
print(ins.center(70,'-'))   #--------------------------------Navin---------------------------------

# strip()
name = "rowdy"
print(name.Lstrip(''))
print(name.strip())
print(name.rstrip(''))
print(name.rstrip(''))





