#### Lists Basics ####


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

# For Loops with Lists, Multiple Assignments and Augmented Operators

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
