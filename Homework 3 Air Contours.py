# Homework 3 Air Contours

# Mark Tenorio 5/14/2018

# Write a function that takes in two vectors of numbers
# If the two vectors have different increasing/decreasing patterns,
# return true. If they both have the same increasing/decreasing patterns,
# return false.

import numpy as np # Enables the use of diff and array
import ast # Converts user input (string) into list

# Function to compare two vectors
def contours(vector1,vector2):
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    differenVec1 = np.diff(vector1)
    differenVec2 = np.diff(vector2)
    signs = np.sign(differenVec1) == np.sign(differenVec2)
    result = all(signs)
    result = not result
    return result

# Handle user input
print('Enter two vectors of integers of the same size starting with the first vector:')
vector1 = input()
print('Enter the second vector that is the same size as the first inputted vector:')
vector2 = input()

# Convert the two vectors into list using the module ast
vector1 = ast.literal_eval(vector1)
vector2 = ast.literal_eval(vector2)

# Call function
result = contours(vector1,vector2)

# Print output
print(result)

    
