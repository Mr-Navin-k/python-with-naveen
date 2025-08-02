books = {
    'B101': {'title': 'Python Basics', 'author': 'John Doe', 'category': 'Programming', 'quantity': 5}
}
members = {
    'M101': {'name': 'Alice', 'email': 'alice@example.com', 'mobile': '9876543210'}
}
print("Library Management System".center(130,'-'))
admin_credential = {'admin':'admin123','navin':'navin@123'}
username = input("Username: ")
password = input("Password: ")
if username in admin_credential and admin_credential.get(username)==password:
    print('Login Sucessfully'.center(130,'-'))
    while True:
        print('\n1. Book Management\n2. Member Management\n3. Issue and Return System\n5. Logout System')
        ch = int(input("Enter your choice: "))
        if ch==1:
            print('Book Management'.center(130,'-'))
            print('1. Add Book\n2. View All Books\n3. Update Book Info\n4. Delete Book\n5. Search Book')
            ch = int(input("Enter your choice: "))
            if ch==1:
                book_id = f'B{101+len(books)}'
                title = input('title: ')
                author = input('author: ')
                category = input('category: ')
                quantity = input('quantity: ')
                while not quantity.isdigit():
                    quantity = input('please enter valid quantity: ')
                books[book_id]={'title': title, 'author': author, 'category': category, 'quantity': quantity}
                print('Data added sucessfully'.center(130,'-'))
                # print(books)
            elif ch==2:
                if books:
                    print('-'*131)
                    # table head 
                    print("|{:^25}|{:^25}|{:^25}|{:^25}|{:^25}|".format('Book_id','Title','Author','Category','Quantity'))
                    for book_id in books:
                        print('-'*131)
                        print("|{:^25}|{:^25}|{:^25}|{:^25}|{:^25}|".format(book_id,books[book_id]['title'],books[book_id]['author'],books[book_id]['category'],books[book_id]['quantity']))
                    print('-'*131)
                else:
                    print('-'*131)
                    print("|{:^25}|{:^25}|{:^25}|{:^25}|{:^25}|".format('Book_id','Title','Author','Category','Quantity'))
                    print('-'*131)
                    print('--------------------------------------------------------> Invalid Data <-----------------------------------------------------------')
            elif ch==3:
                book_id = input("\nenter book id: ")
                if book_id in books:
                    print('\n1. title\n2. author\n3. quantity')
                    ch = int(input("Enter your choice: "))
                    if ch ==1:
                        new_title = str(input('title: '))
                        books[book_id]['title']=new_title
                        print('Data Sucessfully Updated'.center(130,'-'))
                    elif ch==2:
                        new_author = str(input('author: '))
                        books[book_id]['author']=new_author
                        print('Data Sucessfully Updated'.center(130,'-'))
                    elif ch==3:
                        new_quantity = str(input('quantity: '))
                        books[book_id]['quantity']=new_quantity
                        print('Data Sucessfully Updated'.center(130,'-'))
                    else:
                        print("Invalid Input".center(130,'-'))
            elif ch==4:
                book_id = input("enter book id: ")
                books.pop(book_id)
                print('Book has deleted'.center(130,'-'))
            elif ch==5:
                # search
                search_book_id = input("enter book id: ")
                if search_book_id in books:
                    print('-'*131)
                    # table head 
                    print("|{:^25}|{:^25}|{:^25}|{:^25}|{:^25}|".format('Book_id','Title','Author','Category','Quantity'))
                    for book_id_book in books:
                        print('-'*131)
                        print("|{:^25}|{:^25}|{:^25}|{:^25}|{:^25}|".format(book_id_book,books[book_id_book]['title'],books[book_id_book]['author'],books[book_id_book]['category'],books[book_id_book]['quantity']))
                    print('-'*131)
                else:
                    print('-'*131)
                    print("|{:^25}|{:^25}|{:^25}|{:^25}|{:^25}|".format('Book_id','Title','Author','Category','Quantity'))
                    print('-'*131)
                    print('--------------------------------------------------------> Invalid Data <-----------------------------------------------------------')
            else:
                print("Invalid Input".center(130,'-'))
        elif ch==2:
            # members = {'M101': {'name': 'Alice', 'email': 'alice@example.com', 'mobile': '9876543210'}}
            print('Member Management'.center(130,'-'))
            print('1. Register Member\n2. View All Members\n3. Update Member Info\n4. Delete Member')
            ch = int(input("Enter your choice: "))
            if ch==1:
                member_id = f'M{101+len(members)}'
                # print(member_id)
                # add member
                name = input('Name: ')
                while not name.isalpha():
                    name = input('Please Enter Valid Name: ')
                email = input('Email: ')
                while not email.endswith('@gmail.com'):
                    email = input('Please Enter Valid Email: ')
                mobile = input('Mobile: ')
                while not mobile.isdigit and len(mobile)==10:
                    mobile = input('Please Enter Valid Mobile: ')
                members[member_id]={'name': name, 'email': email, 'mobile': mobile}
                print(members)
            elif ch==2:
                print('-'*100)
                print("|{:^20}|{:^25}|{:^30}|{:^20}|".format('Member Id','Name','Email','Mobile'))
                for member_id in members:
                    print('-'*100)
                    print("|{:^20}|{:^25}|{:^30}|{:^20}|".format(member_id,members[member_id]['name'],members[member_id]['email'],members[member_id]['mobile']))
                print('-'*100)
            elif ch==3:
                # Update Member Info
                print('1. Name\n2. Contact')
                ch = int(input("Enter your choice: "))
                if ch==1:
                    member_id = input('enter member id: ')
                    name = input('Enter Name: ')
                    members[member_id]=name
                elif ch==2:
                    contact = int(input('Enter Contact: '))
                    members[member_id]=contact
                else:
                    print('invalid')
            elif ch==4:
                member_id = input('enter member id: ')
                members.pop(member_id)
                print("Member has deleted".center(130,'-'))
            else:
                print('invalid')
        elif ch==3:
            print("data Temporary is invalid")
            pass
        elif ch==4:
            print("Logout Successful".center(130,'-'))
            break
        else:
            print('invalid')
else:
    print("Invalid username or password".center(130,'-'))