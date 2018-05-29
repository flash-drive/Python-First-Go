 # Data Structures and Algorithms 2

#### Memory ####

# Also called RAM
# Two ways to store data; memory(RAM) and storage)
# Storage is permanent while memory is not. If you turn off laptop,
# stuff in storage is still there while in memory it will not be there.

# An example is where when you're working on a document and the computer crashes
# and you lose your progress because you did not hit the save button. That save button
# saves your progress to the storage part of the computer

# So why can't we just store everything on storage?
# Reading in and storing data into storage is slow
# Memory is like a temporary desk. Quicker to write data to and from memory.
# This is why too many applications running on memory can slow the computer

### So how does this relate to programming? ###

# int a = 1 # This integer 1 is stored in memory
# This integer 1 is expressed as 32 one's and zeros; e.g., 000...1
# 2 would be represented as 000010...
# Each of these zeros or ones are called a bit. 32 bits for ints
# a bit is either 1 or 0

# Memory = long tape of bytes. See illustration below
#  _ _ _ _ _ _ _ _ _ 
# |_|_|_|_|_|_|_|_|_|
# byte = a small unit of data= 8 bits. E.g., 10110101
# Each box is comprised of a byte. Thus, each box has a bunch of bits

# Your computer will need to find any particular byte very easily.
# The computer does this by assigning an address to each byte.
# Address is represented by a single integer. Increases consecuteively

# Question: How many bytes do you need to store each integer?
# You need 4 bytes to store 1 integer

# Going back to our original question on why we could not add two more
# integers to the array, the array needs consecutive bytes.
# There may be another integer or character after the original array.
# You will need to create an entirely new array. Copy the original array
# to the new array DYNAMICALLY.
