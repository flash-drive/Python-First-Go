# Homework 2 Clockhands

# Mark Tenorio 5/10/2018

# Write a program that determines where the current position
# of the clock hands are given an input of minutes

import math

def clockhands(hour,minute,change):
    totalMin = float(hour) * 60 + float(minute)
    totalMin = totalMin + float(change)

    hourUpdate = (totalMin/60) % 12
    hourUpdate = int(math.floor(hourUpdate))
    
    minuteUpdate = int(totalMin % 60)

    return hourUpdate,minuteUpdate

print('Input given hour:')
hour = input()
print('Input given minute:')
minute = input()
print('Input change in minutes:')
change = input()

[hourUpdate,minuteUpdate] = clockhands(hour,minute,change)

print('The updated time is '+str(hourUpdate)+':' +str(minuteUpdate)+'.')
