# dictionary it is a comma seprated. key and value pair{}
# key => unique value & mutable
s1 = dict()
print(type(s1),s1)  # <class 'dict'> {}

# Example of dictionary
ishwar = {'name':'Ishwar','age':22,'city':'pune','mob':1234567890}
print(type(ishwar),ishwar)

# emp details
emp = {"name":"Naveen","salary":450000,"employee_id":12345,"type":"Full time"}
print(type(emp), emp)

# value => duplicates and both => mutable and immutable
details = {'name':'Naveen','roll':60,'per':60,'courses':['python','java','AWS'],'marks':{'python':50,"java":60,'AWS':70}}
print(type(details))
print(details)

# Example of dictionary -1
cube = {1:1,2:8,3:27,4:64,5:125,6:216,7:343,8:512,9:729,10:1000}
cubes = {1:1**3,2:2**3,3:3**3,4:4**3,5:5**3}
print(cube)
print(cubes)

# Example of dictionary -2
captial = {"maharashtra":"mumabi","karnataka":"bangalore","taminadu":"chennai","andrapradesh":"hyderabad","goa":"panaji"}
print(captial)

india = {'maharashtra':{'mumbai':['andheri','dadar','kandivali'],'pune':['kothrud','pimpri chinchwad','swargate'],'solapur':['barshi','pandharpur','mangalvedha']},'karnataka':{'bangalore':['koramangala','indiranagar','jayanagar']}}
print(india)

# Example of dictionary -3
batch1272 = {1:{'name':"naveen",'age':21,'courses':['python','java','aws']},2:{'name':'ishwar','age':22,'courses':['html','css','javascript']}}
print(batch1272)

# abc = {'operation':{1001:{'emp_id':101,'emp_name':'adarsh','emp_age':22}},1002:{'emp_id':102,'emp_name':'naveen','emp_age':23},'faculty':{1001:{}},'jbk_emp':{{}}}

# jbk = {'python':{'batch1263':{{'name':'naveen','roll':101,},{'name':'ishwar','roll':102}},'batch1272':{{'name':'pradnya','roll':201},{'name':'pallavi','roll':202}},'batch1276':{'name':'pratham',}},'java':{'batch1263':[],'batch1272':[],'batch1276':[]}}

details = {'name':'yogesh','age':23}
# add
details['city'] = 'pune'
details['percentage'] = 89
print(details)
# access
print(details['name'])
print(details['age'])
# access with method
print(details.get('city','print if it is present in dict'))

jbk_faculty = {101:{'name':'vaibhav','age':27},102:{'name':'sagar','age':35}}
print(jbk_faculty[101])
print(jbk_faculty[102]['age'])
print(jbk_faculty[101]['name'])
jbk_faculty[101]['salary']=45000
print(jbk_faculty)

# square={1:1, 2:4, 3:9}
# square[4]=16
# square[5]=25
# print(square)

one_plus={'ce1':{'ram':['4gb','8gb','12gb'],'color':['black','white'],'camara':'48mp','os':'android'},'ce2':{'ram':['4gb','8gb','12gb'],'color':['red','white'],'camara':'64mp','os':'android'}}
one_plus['ce1']['battery'] = '6000mAH'
print(one_plus['ce1']['camara'])
print(one_plus.get('ce1'))
print(one_plus['ce2']['ram'][2])
# add multiple values to existing key
one_plus['ce2']['security'] = ['fingerprint','face lock','password']
one_plus['ce1']['security'] = ['fingerprint','face lock','password']
print(one_plus)


# update
details = {'name':'kunal','age':26,'salary':30000}
details['department'] = "HR"
details['salary'] = 900000
print(details)

# delete
details.pop('age')  # removes the key 'age' and its value

one_plus={'ce1':{'ram':['4gb','8gb','12gb'],'color':['black','white'],'camara':'48mp','os':'android'},'ce2':{'ram':['4gb','8gb','12gb'],'color':['red','white'],'camara':'64mp','os':'android'}}
one_plus['ce1']['camara'] = "108mp"
one_plus['ce1']['os'] = 'linux'
one_plus['ce2']['ram'][2] = '14gb'
one_plus.pop('ce2')
one_plus['ce1'].pop('camara')   #delete camara
one_plus['ce1']['ram'].pop(0)   #delete 
print(one_plus)
print('----------------------------------------------------------------')

# Delete by using del keyword
one_plus={'ce1':{'ram':['4gb','8gb','12gb'],'color':['black','white'],'camara':'48mp','os':'android'},'ce2':{'ram':['4gb','8gb','12gb'],'color':['red','white'],'camara':'64mp','os':'android'}}
del one_plus['ce2']
del one_plus['ce1']['camara']
print(one_plus)

# methods

# clear()
details = {'name':'kunal','age':26,'salary':30000}
details.clear()
print(details)  # {}


# copy()
details = {'name':'kunal','age':26,'salary':30000}
print(details.copy())  #{'name':'kunal','age':26,'salary':30000}

# keys()
details = {'name':'kunal','age':26,'salary':30000}
print(details.keys())  #dict_keys(['name', 'age', 'salary'])

# values()
details = {'name':'kunal','age':26,'salary':30000}
print(details.values())  #dict_values(['kunal', 26, 30000])

# items()
details = {'name':'kunal','age':26,'salary':30000}
print(details.items())  #dict_items([('name', 'kunal'), ('age', 26), ('salary', 30000)])

# pop()
details = {'name':'kunal','age':26,'salary':30000,'dipartment':'HR'}
print(details.popitem())  # removes the last inserted key-value pair
print(details)

# update()
details = {'name':'kunal','age':26,'salary':30000}
details.update(city='pune')
print(details)

# update() entire dictionary
details = {'name':'kunal','age':26,'salary':30000}
d1 = {'roll':101,'percentage':90}
details.update(d1)
print(details)  # {'name': 'kunal', 'age': 26, 'salary': 30000, 'roll': 101, 'percentage': 90}

# values() can be updated using update method
details = {'name':'kunal','age':26,'salary':30000}
details.values()  # dict_values(['kunal', 26, 30000])

# setdefault()
# details = {'name':'kunal','age':26,'salary':30000}
# fromkeys , setdefault