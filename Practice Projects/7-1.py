# Project: Write a regular expression to make sure the password string it is passed is strong.
# Regex must matc
#   - Eight Characters long
#   - Contain both uppercase and lowercase characters
#   - Has atleast one digit.


import re

passwordRegex = re.compile(r'''
    [A-Za-z0-9]{8,}     # Just a simple class made to match anything that has both capitalized and lowercase letters.
    ''', re.VERBOSE)    # Checks to see if its atleast eight characters long. Also that it contains numbers

test1 = "Larry1011x"    # Patterns used to test my regex expression
test2 = "idk123"

obj1 = passwordRegex.search(test1)  # Testing the regex expression
obj2 = passwordRegex.search(test2)

try:                                # Prints if it finds a match. If it didn't it'll print out "No match found"
   print(obj1.group())     
except AttributeError:
    print("Couldn't find a match")
    
try:
   print(obj2.group())     
except AttributeError:
    print("Couldn't find a match")


