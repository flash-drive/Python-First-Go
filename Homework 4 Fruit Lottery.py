# Homework Fruit Loterry

# Mark Tenorio 05/22/2018 

# Write a function that takes in 3 inputs; your lottery ticket, the
# winning lottery ticket, and the initial investment required to open up a fruit store.
# Rules for determining winnings from lottery ticket numbers:
# 1. Compare the first five integers in both numbers. For every integer in your lottery ticket
# number that matches ​any​ of the first five integers in the winning lottery ticket number,
# add $100,000 to your total prize.
# 2. If the last number matches, then double the prize amount determined by the first 5
# numbers.
# 3. Compare your earnings to the required initial investment, and output a true if your
# earnings are greater than or equal to the investment, and a false otherwise

# import modules needed to convert to array
# and to use regular expressions
import numpy as np
import re

# Function to make list from string
def makeList(ticket):
    #compileStep1 = re.compile(r'\d\d|\d-\d\d|\d-\d\d|\d-\d\d|\d-\d\d|\d-\d\d|\d')
    #mo1 = compileStep1.findall(ticket)
    #mo1Step = mo1.group()
    #mo1Step = mo1Step.replace('-',',')
    #listed = list(map(int,mo1Step.split(',')))

    listed = re.findall(re.compile(r'\d+'), ticket)
    listed = list(map(int, listed))
    
    return listed

# Function to calculate total winnings and see if you have enough for a fruit stand.
def winningsCalc(yourTicket,winTicket,cost):
    totalMatch = [sum(yourTicket[0]==winTicket[:5]), sum(yourTicket[1]==winTicket[:5]),sum(yourTicket[2]==winTicket[:5]),sum(yourTicket[3]==winTicket[:5]),sum(yourTicket[4]==winTicket[:5])]
    totalMatch = sum(totalMatch)
    totalWinnings = totalMatch * 100000
    bigNum = sum([yourTicket[5]==winTicket[5]])*totalWinnings
    bigMoneyPlayer = bigNum + totalWinnings
    logic = bigMoneyPlayer >=cost
    return logic
    
        
    
# Handle user input
print('Input your lottery ticket in the form ##-##-##-##-##-##')
yourTicket = input()
print('Input winning loterry ticket in the form ##-##-##-##-##')
winTicket = input()
print('Input money needed to open up fruit store')
cost = input()
cost = int(cost)

# Make user input a list and then an array
yourTicket = makeList(yourTicket)
yourTicket = np.array(yourTicket)
winTicket = makeList(winTicket)
winTicket = np.array(winTicket)

# Call function
logical = winningsCalc(yourTicket,winTicket,cost)

# Print output
print(logical)
