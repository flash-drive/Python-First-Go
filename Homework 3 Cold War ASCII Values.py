# Homework 3 Cold War

# Mark Tenorio 5/16/2018

# Write a program that takes in 3 inputs. The first input will
# be a string. The second input will represent the "shift" of the even indices.
# The third input will represent the "shift" in the odd indices.

# Import module
import numpy as np #makes array

# Function to shift the string
def shift(string,shift1,shift2):
    value = [ord(c) for c in string] #Convert the string into ASCII value and put in list
    value = np.array(value)
    value[::2] = ord('a') + ((value[::2] - ord('a') + int(shift1))%26)
    value[1::2] = ord('a') +((value[1::2]-ord('a') + int(shift2))%26)
    output = ''.join(map(chr,value))
    return output

#Handle user input
print('Input a string that is to be changed')
string = input()
print('Input shift for even indices')
shift1 = input()
print('Input shift for odd indices')
shift2 = input()

# Call function
result = shift(string,shift1,shift2)

# Print result
print(result)
    
    
    
