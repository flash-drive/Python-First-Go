# Python Homework 1 Quart Conversion
# Mark Tenorio 05/10/2018

# Write a program that calculates the number of sides given an interior angle.
# Recall that the formula is theta = (180(n-2))/n

# Function to calculate the number of sides given an interior angle
def sides(angle):
    n = (-360)/(int(angle)-180)
    return n

# Handle user input
print('Please input an interior angle in degrees.')
angle = input()

# Call function
side = sides(angle)

# Print output
print('A polygon with an interior angle of '+str(angle)+' degrees has '+str(side)+' sides.')
