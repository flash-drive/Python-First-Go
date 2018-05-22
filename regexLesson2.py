import re

message = '45-55-11'

phoneNumRegex = re.compile(r'(\d\d)-\d\d-\d\d|/d/d/d') #create regex object #use pipe symbol as an "or." Basically a catch all.
mo = phoneNumRegex.search(message) #create match object #use .findall to find all the phone number patterns
print(mo.group()) #group gets matched string
