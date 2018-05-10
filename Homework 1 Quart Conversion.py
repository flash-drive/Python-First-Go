# Python Homework 1
# Mark Tenorio 05/10/2018

# Write a program that has one input-the amount of liquid in quarts, and
# outputs three different conversions- the amount of liquid in gallons,
# pints, and cups.

# Function to handle the conversions
def convert(quarts):
    gallon =  float(quarts) / 4
    pints = 2 * float(quarts)
    cups = 2 * pints
    return gallon, pints, cups

# Handle's user input
print('Input an integer or a float')
print('This will be evaluated as quarts which will be converted to gallons, pints, and cups')
quarts = input()

# Call fucntion and hold output as list
[gallon,pints,cups] = convert(quarts)

# Print output
print('For every ' +str(quarts)+ ' quarts, you have '+str(gallon)+' gallons.')
print('For every ' +str(quarts)+ ' quarts, you have '+str(pints)+' pints.')
print('For every ' +str(quarts)+ ' quarts, you have '+str(cups)+' cups.')
