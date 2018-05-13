#### Lists Basics ####
# Mark Tenorio


#### Indexing ####
# spam = ['cat','bat','rat','elephant']
# spam[0] = 'cat'

# spam = [['cat','bat'],[10,20,30]]
# spam[0]
# >> ['cat','bat']
# spam[1][2]
# >> [30]

# spam = [10,20,30]
# spam[1] = 'Hello'
# >> [10,'Hello',30]

# spam = ['cat','bat','rat','elephant']
# spam[-1]
# >>'elephant'
# spam[-2]
# >>'rat'

#### Slicing ####

# spam = ['cat','bat','rat','elephant']
# spam[:2]
# >>['cat','bat']
# [:2] goes up to but not including the 2

# spam = ['cat','bat','rat','elephant']
# spam[1:]
# >>['bat','rat','elephant']

#### Deleting from a list ####

# spam = ['cat','rat','bat]
# del spam[2]
# >>['cat','rat']

### List and "Scalers" ###

# [1,2,3,] + [1,2,3,4]
# >>[1,2,3,1,2,3,4]

# [1,2,3] * 3
# >>[1,2,3,1,2,3,1,2,3,]

### Converting to List ###

# list('Hello')
# >>['H','e','l','l'l,'o']

### Determining if a value exists within a list ###

# 'howdy' in ['hello','hi','howdy','heyes']
#>> True

# 'howdy' not in ['hello','hi','howdy','heyes']
#>> False

# name = 'Zophie'
# 'Zo' in name
# >>True
# 'xxxx' in name
# >>False

# name = 'Zohpie'
# for letter in name:
# print(letter)
# >>Z;o;p;h;i;e

#### For Loops with Lists, Multiple Assignments and Augmented Operators ####

#### For Loops #####

# for i in range(4)
#   print(i)

# range(4)
# >>[0,1,2,3]

# for i in [0,1,2,3]:
#   print(i)

# list(range(0, 100, 2))
# Start from 0 all the way to 100 in
# increments of 2. [0,2,4,6,..100]

# supplies = ['pens','staplers','flame-throwers','binders']
# for i in range(len(supplies)):
#   print('Index '+str(i)+' in supplies is: '+supplies[i])
# Index 0 in supplies is: pens

##### Multiple Assignments #####

# cat = ['fat','orange','loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

# size,color,disposition = cat

# size, color, disposition= 'skinny','black',quiet'

#### Swappping variables ####

# a = 'AAA'
# b = 'BBB'
# a, b = b, a
# You cannot do a,b= 200 Length needs to match

#### Augmented Assignment Operators ####

# spam = 42
# spam = spam + 1

# spam += 1
# this adds 1 to spam. Can also do for multiplication, division, mod, subtraction

#### List Methods ####

# Works like a function but attached to a list.
# Each data type has their own set of methods.
# Each method can only be used within their respective data types     

# spam = ['hello','hi','howdy','heyas']
# spam.index('hello')
# >>0
# index('hello') will not work. Need to "attach it."
# If the value is not within the index, it will return an exception.

# spam = ['hello','hi','howdy','howdy']
# spam.index('howdy')
# >> 2 # will only return the first index it appears in.

### Appending and Inserting Values in a List ###

# spam = ['cat','dog','bat']
# spam.append('moose')
# >> ['cat','dog','bat','moose']

# spam = ['cat','dog','bat']
# spam.insert(1,'chicken')
# >> ['cat','chickn','dog','bat']
# Everything gets bumped up one.

### Removing from a list ###

# spam = ['cat','dog','bat','moose']
# spam.remove('dog')
# >>['cat','bat','moose']
# This is differentf from the "del" operation because you
# do not need to know the index.

# spam = ['cat','bat','rat','hat','cat']
# spam.remove('cat')
# >>['bat','rat','hat','cat']
# Will only remove the first instance of cat.

#### Sorting ####

# spam = [2,5,3.14,1,-7]
# spam.sort()
# >>[-7,1,2,3.4,5]
# Works also for strings
# Use spam.sort(reverse=True) to reverse sort
# CANNOT sort a list with different data-types

# spam = ['a','z','A','Z']
# spam.sort(key=str.lower)
# >>['A,'Z','a','z']
# Sorting strings does NOT sort by alphabetical order
# Instead it sorts by ASCII values, so uppercase will go first
# spam.sort(key=str.lower)
# >>['A','a','Z','z']
# Will sort in "true" alphabetical order
