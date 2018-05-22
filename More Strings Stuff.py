#### More String Stuff ####

#### Functions ####

# .isupper()
# .islower()
# these return boolean

# 'Hello'.upper()
# 'HELLO'

# 'Hello'.upper().isupper()
# >True

# .isalpha() # all alphabets
# .isalnum() # all numbers
# .isdecimal # all numbers
# .isspace() # empty space
# .istitle() # all words start with uppercase

# .startswith(input) # Does it start with input
# .endswith(input) # Does it end with input

# ','.join(['cats','rats','bats'])
# >'cats,rats,'bats'
# ''.join(['cats',rats',bats'])
# >'catsratsbats'

# 'My name is Simon'.split()
# >['My,'name','is','simon'].split()
# 'My name is Simon'.split('m)
# >will split until it reaches 'm' (won't include 'm')

# 'Hello'.rjust(10)
# >'     Hello' #makes it length ten on the right side
# 'Hello'.ljust(10)
# >'Hello      ' #makes it length ten on the left side
# 'Hello.center(10,'=')
# '====Hello====='

# .strip() # removes white space
#  .lstrip() # removes white space from left side
# .rstrip() # removes white space from right side.
# .strip(input) #will remove input from the string

# .replace(input,input1) # replace input with input1
