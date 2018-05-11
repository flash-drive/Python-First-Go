# Homework 2 Fall time
# Mark Tenorio 5/10/2018

# Write a program that determines the time it takes for an object
# to hit the ground at a given height

# Recall the kinematics equation:
# distance = velocity(initial) * t + (1/2)*acceleration*time^2
# Assume that velocity(initial) is zero m/s.
# Assume that acceleration is a constant 9.8 m/s.

# Function to find time it takes for an object to reach the ground
def time(height):
    time = ((float(height) * 2) / 9.8) ** (1/2)
    time = round(time,2)
    return time

# Handle user input
print('Input a height in meters')
height = input()

# Call function
time = time(height)

# Print output
print('It takes '+(str(time))+' seconds to reach the ground from '+str(height)+' meters.')
