# age = 21
# city = "Bangalore"
# wp to sum numbers 5 to 0
# name='raj'
# name[::-1]
# print(name[::-1])

#wap to print a list of numbers of square 
# numbers={1,2,3,4,5}
# dic={}
# for num in numbers:
#     dic[num]=numbers
# print(dic)

#wap to convert string into integer
# x='1,2,3,4,5' 
# sum=int(x)
# print(sum)
# print(type(sum))
# print(num)

# # WAP to print reverse string and remove whitespace from string
# str = ' GFE DCB A'
# s=str.replace(" ","")
# p=str[::-1]
# print(s,p)



# WAP to print the percentge of all subjects
# subjects = {'english':68,'marathi':59,'science':89,'maths':90}
# obt = 0
# for marks in subjects.values():
#     obt = obt+marks
#     total = len(subjects)*100
#     per = obt/total*100
# print(f"Total percentage is :{per}%")
# print(obt)

# a = True+False+False
# print(a)
# student = {102:{'name':'vaibhav','marks':75,'age':21}}
# stud = {101:{'name':'Navin','age':23,'city':'solapur'}}
# for a in range(int(input("Enter Number of students :"))):
#     if a<=5:
#         key = input('enter key :')
#         name = input('enter name :')
#         age = input('enter age :')
#         city = input('enter city :')
#         stud[key] = {'name':name,'age':age,'city':city}
# print(stud)

# Library mangement System #
books = {'B101': {'title': 'Python Basics', 'author': 'John Doe', 'category': 'Programming', 'quantity': 5}}

# Member Example:
members = {'M101': {'name': 'Vaibhav patil', 'email': 'Vaibhav@example.com', 'mobile': '9876543210'}}
admin_information={
    'admin': 'admin@123',
    'vaibhav':'vaibhav123'
}
username=input("username")
password=input("password")
if username in admin_information and admin_information.get(username)==password:
    print(f'1.Book Mangement\n2.Member Management')
    ch=int(input(" select your option: "))
    if ch==1:
        print('1.Add Book\n2.Display Book\n3.Delete Book\n4.Filter\n5.Search Book\n')
        ch=input("Enter your choice: ")
        if ch==1:
            book_id=f'B{101+len(books)}'
            title=input("title")
            author=input("author")
            category=input("category")
            quantity=input("quantity")
            books[book_id]={'title':title,'author':author,'category':category,'quntity':quantity}
            print(books)    
        elif ch==2:
            pass
        elif ch==3:
            pass
        elif ch==4:
            pass
        elif ch==5:
            pass
        else:
            print("Enter Data Is Not Available: ")
    elif ch==2:
        print("data Temporary is invalid")
    else:
        print('invaild Input:  ' )