#### Lists vs Strings #####

# Values in a list can be changed
# Values in a string cannot be changed

# name = 'Zophie the cat'
# name[7]
# >>'t'

# name[7] = ERROR
# If you wanted to change a value in a  string,
# you will need to slice

# name = 'Zophie the cat'
# newName = name[0:7] + 'the' + name[8:12]
# >>'Zophie the 'cat'

#### Difference between mutable and immutable ####

#### References ####

# Notice the difference below:
# spam = 42
# cheese = spam
# spam = 100
# spam
# >> 100
# cheese
# >>42

# spam = [0,1,2,3,4,5]
# cheese = spam
# cheese[1] = 'Hello'
# cheese
# [0,'Hello',2,3,4,5]
# spam
# [0,'Hello',2,3,4,5]
# Python created a reference which is why it "backtracks"
# to all the variables that the list is contained in.
# Applies to ALL mutable variables, not just lists.

# def eggs(cheese):
#   cheese.append('Hello')
# spam = [1,2,3]
# eggs(spam)
# print(spam)

#### Copyng a List ####

# If we wanted to adjust a list without altering the original one,
# we can use:
# import copy
# spam = ['A','B','C','D']
# cheese = copy.deepcopy(spam)
# cheese[1] = 42
# cheese
# >>['A',42,'C','D']
# spam
# ['A','B','C','D']

#### Line Continuation (overflow) ####

# For lists:
# spam = ['apples',
#          'oranges',
#           'cats']

# Other code:
# print('four score and seven \
#    'years ago') #use backslash
