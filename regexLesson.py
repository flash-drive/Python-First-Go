import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #create regex object
mo = phoneNumRegex.search(message) #create match object #use .findall to find all the phone number patterns
print(mo.group()) #group gets matched string
