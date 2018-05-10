# Python Homework 1 Pizza to Person Ratio
# Mark Tenorio 05/10/218

# Write a program that determines the amount of pizza slices that each
# person receives given a pizza.

# Function to find pizza slices to people ratio

import math

def pizzaShare(people,pizza):
    slices = int(pizza) * 8
    portions = slices / int(people)
    remainder = slices % int(people)
    return portions, remainder

# Handle user input
print('Please input the number of people attending the party')
people = input()
print('Please input the number of pizzas ordered. Each pizza will be divided into 8 slices')
pizza = input()

# Call function
[portions,remainder] = pizzaShare(people,pizza)

portions = math.trunc(portions)

# Print output
print('You ordered '+str(pizza)+' pizzas which can be divided into ' +str(portions)+' amongst '+str(people)+' people with a remainder of '+str(remainder)+' slice.')
