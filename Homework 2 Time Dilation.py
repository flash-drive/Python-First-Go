# Homework 2 Time Dilation

# Mark Tenorio 5/10/2018

# Write a program that determines the time measured by an observer
# given a time measured by a third party and the velocity of an object.

# Recall that the formula is: T = T(0)/(sqrt(1-(velocity/speed of light^2)) 

# Function that takes in time from a third party and their velocity and
# finds the time relative to the observer
def timeDilation(time,velocity):
    bigT = float(time)/((1-((float(velocity)/299792458)**2))**(1/2))
    bigT = round(bigT,4)
    return bigT

# Handle user's input
print('Input time measured by third party(measured in seconds):')
time = input()
print('Input velocity(measured in meters/second)')
velocity = input()

# Call function
bigT = timeDilation(time,velocity)

# Print output
print('The time dilation is '+str(bigT)+'.')
