# tuples 
# def of tuples :- it is a ordered, immutable, hertogenious collection of elements where dublicates are allowed.,
# are immutable sequences in Python, meaning they cannot be changed after creation.

# t = (11, 22, 33, 44, 55, 66, 77, 88, 99)
# print(type(t))  # <class 'tuple'>

# x=(11,22,33,44)
# print(x.count(11))  # Counts the occurrences of 22 in the tuple
# print(x.index(22))  # Returns the index of the first occurrence of 33 in the tuple
  
# x=(11,22,33,44)
# print(x[-2])
# print(x[0:2:1])  # Slicing the tuple to get elements from index 1 to 2



# #start index
# x=(11,22,33,44,55,66)
# print(x[0:5:2])  # Slicing the tuple to get elements from index 2 to the end


# x=(11,22,33,44,55,66)
# print(x[-2:-5:-1]) # Slicing the tuple to get elements from index -2 to -5 with a step of -1


# # end index
# x=(11,22,33,44,55,66)
# print(x[2:-1:1])  # Slicing the tuple to get elements from index 2

# x=(11,22,33,44,55,66)
# print(x[2::1])# Slicing the tuple to get elements from index 2 to the end


# x=[11,22,33,44,55,66]
# print(x[-3::-1])  # Slicing the list to get elements from index -3 to the end

# #step value
# x=(11,22,33,44,55,66)
# print(x[1:-2:])  # Slicing the tuple to get elements from index 0 to 5 with a step of 2


t=(11,22,33,44,(10,20,30,40,50,60),55,66,77,88,)
print(t[:3:])  # Slicing the tuple to get elements from index 0 to 2

print(t[6::])#(66, 77, 88)


print(t[3::-1])

print(t[:-3:-1])  # Slicing the tuple to get elements from index -3 to the end with a step of -1


print(t[4][::-1])# (60,50, 40, 30, 20, 10)


print(t[4][2:5:1])  # Slicing the tuple to get elements from index 2 to 4 with a step of 1

t = 11,22,33,44,55,66
print(type(t))  # <class 'tuple'>, tuples can be created without parentheses

num = ('naaveen')
print(type(num))  # <class 'str'>, single value in parentheses is treated as a string
students = ["naveen","ishwar","pratham"]

