import re

message = '13-45-33-19-29-8'

phoneNumRegex = re.compile(r'\d\d|\d-\d\d|\d-\d\d|\d-\d\d|\d-\d\d|\d-\d\d|\d') #create regex object #use pipe symbol as an "or." Basically a catch all.
mo = phoneNumRegex.findall(message) #create match object #use .findall to find all the phone number patterns
c = mo.group() #group gets matched string
new = c.replace('-',',')
print(type(new))
listed = list(map(int,new.split(',')))
print(listed)
print(type(listed))
