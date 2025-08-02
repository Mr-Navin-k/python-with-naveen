fees_structure = {
    'python':40000,
    'data science':60000,
    'java':30000,
    'aws':20000,
    'angular':10000,
    'frontend':30000
}
student_data = {101:{
    'name':'vaibhav',
    'email':'vaibhav@gmail.com',
    'course':'python',
    'coursefee':40000,
    'payedfees':20000,
    'remainingfees':20000
}}
print("Welcome The Kiran Academy".center(110,"-"))
while True:
    print('''
1. Add Student
2. Record
3. Update data
4. Delete
5. Filter
6. Search
7. logout''')
    ch = int(input("Enter Your Choice: "))
    if ch==1:
        reg=101+len(student_data)
        name=input("Enter name: ")
        email=input("Enter email: ")
        while not email.endswith("@gmail.com"):
            email=input("Invalid email Please enter valid email: ")
        course=input("Enter course: ")
        while course not in fees_structure:
            course=input("Please enter valid course: ")
        payedfees = int(input("Enter Fees: "))
        # dis = int(input("Enter Your Dis %: "))
        coursefee = fees_structure[course]
        remainingfees = coursefee-payedfees
        student_data[reg] = {'name':name,'email':email,'course':course,'coursefee':coursefee,'payedfees':payedfees,'remainingfees':remainingfees}
        print(' \nData Successfully Added...!')
    elif ch==2:
        print('-'*138)
        print("|{:^10}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format('Rg.No','Name','Email','Course','Course Fees','Payed Fees','Remaining Fees'))
        if student_data:
            print('-'*138)
            for reg in student_data:
                print("|{:^10}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(reg,student_data[reg]['name'],student_data[reg]['email'],student_data[reg]['course'],student_data[reg]['coursefee'],student_data[reg]['payedfees'],student_data[reg]['remainingfees']))
                print('-'*138)
        else:
            print('\n-----------------------------------------------------------------> Invalid Data <---------------------------------------------------------')
    elif ch==3:
        reg = int(input("\nEnter Reg. No: "))
        print('''\nWhat You Want to Update
1. Name
2. Email''')
        ud = int(input("Enter Your Choice: "))
        if ud==1:
            uname=input('Enter Name: ')
            student_data[reg]['name']=uname
            print('\nUpdated Sucessfully...')
        elif ud==2:
            uemail = input('Enter Email: ')
            student_data[reg]['email']=uemail
            print('\nUpdated Sucessfully...')
        else:
            print("\ninvalid input")
    elif ch==4:
        reg = int(input("\nEnter Reg. No: "))
        student_data.pop(reg)
        print('\nDeleted Sucessfully...')
    elif ch==5:
        print('''\n1. course''')
        ch = int(input("Enter Your Choice: "))
        if ch==1:
            c = input("Enter Course: ")
            print('-'*138)
        print("|{:^10}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format('Rg.No','Name','Email','Course','Course Fees','Payed Fees','Remaining Fees'))
        if student_data:
            print('-'*138)
            for reg in student_data:
                if student_data[reg]['course']==c:
                    print("|{:^10}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(reg,student_data[reg]['name'],student_data[reg]['email'],student_data[reg]['course'],student_data[reg]['coursefee'],student_data[reg]['payedfees'],student_data[reg]['remainingfees']))
                    print('-'*138)
        else:
            print('\n-----------------------------------------------------------------> Invalid Data <---------------------------------------------------------')
    elif ch==6:
        print('Search')
        n = str(input("Enter Name :"))
        while reg in student_data:
            if n in student_data[reg]['name']==n:
                print('-'*138)
                print("|{:^10}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format('Rg.No','Name','Email','Course','Course Fees','Payed Fees','Remaining Fees'))
                print('-'*138)
                print("|{:^10}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(reg,student_data[reg]['name'],student_data[reg]['email'],student_data[reg]['course'],student_data[reg]['coursefee'],student_data[reg]['payedfees'],student_data[reg]['remainingfees']))
                print('-'*138)
            # else:
            #     print("Data is not exist...!")
    elif ch==7:
        print("Program Logout...!")    
        break
    else:
        print("\ninvalid input...!")
        print('ReEnter Your Choice')