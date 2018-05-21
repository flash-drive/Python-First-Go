#### Creating Dictionaries ####

#### Creating a dictionary ####
# myCat = {'size':'fat','color':'gray','disposition':'loud'}

#my cat has ' +myCat['color'] +' fur'.

#####

# Dictionaries are un-ordered

# eggs = {'name':'Zophie','species':'cat','age':8}
# ham = {'species': 'cat','name':'Zophie','age':8}
# eggs = ham
# >True

# 'name in eggs'
# >True

#### Dictionaries are mutable ####

#### Dictionary methods ####

# list(eggs.keys())
# >['name','species','age']

# list(eggs.values())
# >['Zophie','cat',8]

# list(eggs.items())
# [('name','Zophie'),('species','cat'),('age',8)]

# Keep in mind that these return in list value

# eggs.keyes()
# >dict_keys(['name','species','age'])

#### For Loops and Keys ####

# for k in eggs.keys()
#   print(k)

# >name
# >species
# >age

# Can have multiple items in for loops
# for k, v in eggs.items():
#   print(k,v)

# name Zophie
# species cat
# age 8

# if only one variable, it would be in tuple form:
# ('name','Zophie')
# ('species','cat')
# ('age',8)
# Tuples are bascially lists but are immutable and are in parenthesis instead of brackets

# 'cat' in eggs.values(
# True

#### Dictionary conditionals and errors
# if i in eggs.items()
#   print(i)

# >('name','Zophie)
# >('species','cat')
# >('age',8)

# eggs['color']
# >error; does not exist

# Can have two arguments in one expression:
# eggs = {'name':'Zophie','species':'cat','age':8)
# eggs.get('age',0)
# 8
# Here, if there is a key called age, return the value of it, otherwise, return 0

#### Set default if it does not already exists ####

# eggs = {'name':'Zophie','species':'cat','age':8)
# eggs.setdefault('color','orange')

# eggs = {'name':'Zophie','color':'black','species':'cat','age':8)
# Will not do anything if 'color' key already exists
