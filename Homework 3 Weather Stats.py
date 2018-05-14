# Homework 3 Weather Stats
# Mark Tenorio 5/13/2018

# Write a program that takes in a list
# comprised of a vector and a string. Output the maximum and average
# of the vector and output the string.

# Import modules
from statistics import mean
import ast

# Function to output max, average, and string from list
def weatherStats(info):
    numbers = info[0]
    forecast = str(info[1])
    maxNum = max(numbers)
    avgNum = mean(numbers)
    avgNum = round(avgNum)
    return maxNum, avgNum,forecast

# Handle user input
print('Please input the vector and forecast in a list')
print('The format should be [[vector],string]')
info = input()

# Convert string list into actual list
info = ast.literal_eval(info)

# Call function
[maxNum,avgNum,forecast] = weatherStats(info)

# Print output
print("Today's weather was "+forecast.lower()+", with a high temperature of "+str(maxNum)+" degrees and an average temperature of "+str(avgNum)+" degrees.")
