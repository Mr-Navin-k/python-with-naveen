'''
def:- String is a sequence of characters are used to store text data.
# Methos of strings

lower() converts all alphabets into lowercase
upper() converts all alphabets into uppercase
capitalize() capitalize the first Character of the string
title() Converts the first character of each word to uppercase
isalpha()  it checks all the elements are alphabetical or not
isnumeric()  it checks all the elements are numeric or not
isalnum()  it checks both alphabets and  numeric
isspace()  it checks if there is only space in string
split()   list method is used to break a string into a list of substrings

# Methos of strings - 2

islower() checks if all characters in the string are lowercase & returns in boolean condition
isupper() Checks if all characters in the string are uppercase & returns in boolean condition
istitle() Checks if the string is in title case (first character of each word is uppercase) & returns in boolean condition
index()  Returns the index of the first occurrence of a substring in the string
count()  Counts the occurrences of a substring in the string
startswith()  Checks if the string starts with a specified prefix
endswith()  Checks if the string ends with a specified suffix
center()   Centers the string within a specified width, padding with a specified character
strip()  Removes leading and trailing whitespace characters
lstrip()  Removes leading whitespace characters
rstrip()  Removes trailing whitespace characters
replace() replace the old value to new value

list[]   List is a data type which 'enclose data with in square brackets' seprated by commas.

list[]   List is a data type which 'enclose data with in square brackets' seprated by commas.
list is hetrogeneous data type we can store different data types in list
list is mutable we can change the value of a list
List CRUD Operations

append()  Adds an element to the end of the list
insert()  Inserts an element at a specified position in the list
remove()  Removes the first occurrence of a specified element from the list
pop()  Removes and returns the element at a specified position in the list
clear()  Removes all elements from the list

max()   Returns the maximum value in the list
min()   Returns the minimum value in the list

-------------------------------------Set-------------------------------------------

# Set is comma seprated values with in {}
# it is unorderd, mutable, hetrogenous collection of immutable elemnts where duplicates are NOT allowed.

add()   Adds the specified element to the set
discard()  Removes the specified element from the set if it exists
remove()  Removes the specified element from the set
intersection()  Returns a new set with elements common to the set and all others
intersection_update()  Updates the set with elements common to the set and all others
difference()  Returns a new set with elements in the set that are not in the others
symmetric_difference()  Returns a new set with elements in either the set or the others but not both
union()  Returns a new set with elements from both sets
update()  Updates the set with elements from both sets

--------------------------------------Tuples-------------------------------------------
# tuples
# def of tuples :- it is a ordered, immutable, hertogenious collection of elements

--------------------------------------Dict---------------------------------------------
how to add element into dictionary
var_name[]='value'

access from dictionary
var_name[]

acces with method
# get()
# clear()
'''
import tkinter as tk
from tkinter import messagebox, simpledialog

student = []

def add_item():
    item = simpledialog.askstring("Add Item", "Enter value to add:")
    if item:
        student.append(item)
        update_listbox()
        print(student)

def remove_item():
    item = simpledialog.askstring("Remove Item", "Enter value to remove:")
    if item in student:
        student.remove(item)
        update_listbox()
        print(student)
    else:
        messagebox.showinfo("Info", f"{item} not found in list.")

def update_item():
    old = simpledialog.askstring("Update Item", "Enter value to update:")
    if old in student:
        new = simpledialog.askstring("Update Item", "Enter new value:")
        idx = student.index(old)
        student[idx] = new
        update_listbox()
        print(student)
    else:
        messagebox.showinfo("Info", f"{old} not found in list.")

def read_items():
    messagebox.showinfo("Student List", f"Current List:\n{student}")

def update_listbox():
    listbox.delete(0, tk.END)
    for item in student:
        listbox.insert(tk.END, item)

win = tk.Tk()
win.title("List CRUD Operations")

listbox = tk.Listbox(win, width=40)
listbox.pack(pady=10)

btn_add = tk.Button(win, text="Add", command=add_item)
btn_add.pack(side=tk.LEFT, padx=5, pady=5)

btn_remove = tk.Button(win, text="Remove", command=remove_item)
btn_remove.pack(side=tk.LEFT, padx=5, pady=5)

btn_update = tk.Button(win, text="Update", command=update_item)
btn_update.pack(side=tk.LEFT, padx=5, pady=5)

btn_read = tk.Button(win, text="Show List", command=read_items)
btn_read.pack(side=tk.LEFT, padx=5, pady=5)
def clear_list():
    if student:
        student.clear()
        update_listbox()
        print("List cleared:", student)
    else:
        messagebox.showinfo("Info", "List is already empty.")

# ...existing code...

btn_clear = tk.Button(win, text="Clear List", command=clear_list)
btn_clear.pack(side=tk.LEFT, padx=5, pady=5)

# ...existing code...
win.mainloop()