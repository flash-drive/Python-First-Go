# Homework 4 Fruit Decryption Using Regex

# Mark Tenorio 5/24/2018

# Write a function that will take an encrypted message and decipher it by following rules.
# 1. Remove any numbers, punctuation characters, and spaces.
# 2. Move all uppercase letters to the beginning of the vector, followed by all lowercase
# letters (while preserving the order of both).
# 3. Make any remaining characters lowercase.
# 4. Remove any character that comes immediately AFTER one of the character in the word
# "fruit" (​'f'​, ​'r'​, ​'u'​, ​'i'​, and ​'t'​). If the last letter is one of these characters, you can
# ignore it.

# Input:​ 'in3Mt%.pef90wrYFI:1cZ)u AVn#iOR21 Adt0s'
# > 'inMtpefwrYFIcZuAVniORAdts' (removes non alphabet characters)
# > 'MYFIZAVORAintpefwrcunidts' (reorders values based on capitalization)
# > 'myf​iz​avor​a​i​n​t​p​ef​w​r​c​u​n​i​d​t​s​' (lowercase all values)
# Output: 'myfavoritefruit

# Import modules
import re

# Function to decrypt
def deCoder(string):
    upperOnly = re.compile(r'[A-Z]')
    upperOnly = upperOnly.findall(string)
    lowerOnly = re.compile(r'[a-z]')
    lowerOnly = lowerOnly.findall(string)
    output = upperOnly+lowerOnly
    output = ''.join(output)
    output = output.lower()
    output = list(output)
    indices = [index for index, value in enumerate(output) if value == 'f']
    indices = list(map(lambda x: x + 1, indices))
    somelist = [i for j, i in enumerate(output) if j not in indices]
    indices = [index for index, value in enumerate(somelist) if value == 'r']
    indices = list(map(lambda x: x + 1, indices))
    somelist = [i for j, i in enumerate(somelist) if j not in indices]
    indices = [index for index, value in enumerate(somelist) if value == 'u']
    indices = list(map(lambda x: x + 1, indices))
    somelist = [i for j, i in enumerate(somelist) if j not in indices]
    indices = [index for index, value in enumerate(somelist) if value == 'i']
    indices = list(map(lambda x: x + 1, indices))
    somelist = [i for j, i in enumerate(somelist) if j not in indices]
    indices = [index for index, value in enumerate(somelist) if value == 't']
    indices = list(map(lambda x: x + 1, indices))
    somelist = [i for j, i in enumerate(somelist) if j not in indices]
    somelist = ''.join(somelist)
    
    return somelist

# Handle user input
print('Input a string to decrypt')
string = input()

# Call function
decrypted = deCoder(string)

# Print output
print(decrypted)
