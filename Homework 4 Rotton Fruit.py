# Homework Rotton Fruit

# Mark Tenorio 5/17/2018

# Write a program that takes in a vector of days
# If the vector includes days that are less than 2 and greater than 7 (noninclusive)
# the fruit is rotton. Sum the number of ripe fruits.

# Import modules
import ast
import numpy as np

# Function to compare vector to number 2 and 7
def ripeness(vector):
    vectors = np.array(vector)
    young = vectors < 2
    young = sum(young)
    old = vectors > 7
    old = sum(old)
    total = young + old
    perfect = len(vectors) - total
    return perfect

# Handle user input
print('Input a vector of days to see if fruit is ripe or old')
vector = input()

# Use module to convert string list to list
vector = ast.literal_eval(vector)

# Call function
result = ripeness(vector)

# Print result
print('Number or ripe fruit is '+str(result)+'.')

    
