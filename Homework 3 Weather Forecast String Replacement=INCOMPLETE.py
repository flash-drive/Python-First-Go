# Homework 3 Weather Forecast String Replacement

# Mark Tenorio 5/16/2018

# Write a function that takes in 3 inputs. One input is a list string.
# The second input is a word that will be replaced in the list string.
# The third input is the word that will replace the second input.

# Function to replae the string
def replacement(string,word1,word2):
    index = string.find(word1)
    lengther = index + len(word1)
    output = string[:index] + word2 + string[lengther:]
    return output

# Handle user input
print('Input string')
string = input()
print('input word to be changed in the string')
word1 = input()
print('Input word to replace the word to be replaced')
word2 = input()

# Call function
result = replacement(string,word1,word2)

# Print result
print(result)
    
    
