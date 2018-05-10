#Import necessary files that are not already built in
import random
import sys

#Grab initial inputs
print('Welcome to the random number game!')
print('What is your name?')
nameInput = input() 
print('Well, ' +nameInput+ ', please guess a number from 1-20.')
numberInput = input()

#Create the random number
secretNumber = random.randint(1,20)

#create parameters for "hot"
secretNumberHOT1 = secretNumber + 1
secretNumberHOT2 = secretNumber - 1

#Counter to keep track of how many guessses it took
counter = 1;

print('You have 6 guesses')

#For loop that goes through possible outcomes of user input
for i in range(1,6):

    if int(numberInput) == secretNumberHOT1:
        print('You are HOT! Try again!!!')
        numberInput = input()
    elif int(numberInput) == secretNumberHOT2:
        print('You are HOT! Try again!!!')
        numberInput = input()    
    elif int(numberInput) < secretNumber:
        print('Too low!')
        counter = counter + 1
        print('Try again.')
        numberInput = input()
    elif int(numberInput) > secretNumber:
        print('Too high!')
        counter = counter + 1
        print('Try again.')
        numberInput = input()
    else:
        counter = counter + 1
        print('Great job! ' +nameInput+ ' ,you guessed the secret number :)')
        print('The secret number was ' +str(secretNumber)+ '. It took you '+str(counter)+' times to guess right.')
        sys.exit()

#Print statement in the event user did not guess that right number
#in the amounted of guesses given.
print('You did not guess the magic number :( it was ' +str(secretNumber)+'.')
        
