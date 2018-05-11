# Homework 1 Volume to Surface Area
# Mark tenorio 5/10/2018

# Write a program where given a volume in cubic centimeters, it will determine
# the surface area in square centimeters.

# Recall that the volume of a sphere is V = 4/3pir^3
# Recall that the area of a sphere is A = 4pir^2

# Import math module to use math.pi
import math

# Function that converts volume in cubic centimeters to surface area in centimeters
def conversion(volume):
    radius = ((float(volume)*3)/(4*math.pi)) ** (1/3)
    area = (4 * math.pi) * (radius **2)
    area = round(area,2)
    return area

# Handle user input
print('Please input volume in cubic centimers to be converted into surface area in square meters:')
volume = input()

# Call function
area = conversion(volume)

# Print output
print('Your input of ' +str(volume)+' in cubic centimeters is ' +str(area)+' in square centimeteres.')
