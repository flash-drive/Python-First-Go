# Homework 2 Distance Between Two Points

# Mark Tenorio 5/10/2018

# Write a program that finds the distance between two points
# on the cartesian plane

# Function to find distance between two points
def distance(x1,y1,x2,y2):
    distance = ((((float(x2)-float(x1)) ** 2) + ((float(y2)-float(y1)) ** 2)) ** (1/2))
    distance = round(distance,2)
    return distance

# Grab user's inputs
print('Please input the two cartesian points to find the distance in the form [x1,y1] and [x2,y2]')
print('Input a value for x1:')
x1 = input()
print('Input a value for y1:')
y1 = input()
print('Input a value for x2:')
x2= input()
print('Input a value for y2:')
y2=input()

# Call function
distance = distance(x1,y1,x2,y2)

# Print output
print('The distance between ['+str(x1)+','+str(y1)+'] and ['+str(x2)+','+str(y2)+'] is '+str(distance)+'.')
