# Homework 3 Sweater Weather
# Mark Tenorio 5/13/2018

# Write a program that takes in a list
# comprised of two vectors. Combine these two vectors where
# you alternate between the two indexes.

# Import module to convert string list to list
import ast

# Function to combined two vectors in alternating sequence
def alternate(vectors):
    vector1 = list(vectors[0])
    vector2 = list(vectors[1])
    combined = vector1 + vector2
    combined[::2] = vector1
    combined[1::2] = vector2
    return combined

# Handle user input
print('Input two strings in vector form')
print('They should be of the following form:')
print('[string 1, string 2]')
vectors = input()

# Convert the string list to list using module
vectors = ast.literal_eval(vectors)

# Call function
combined = alternate(vectors)

# Print output
print(''.join(combined))
