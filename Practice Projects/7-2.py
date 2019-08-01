# Objective: Create a clone of strip() using the sub function from the regex module.
# If no arguments are given, simply delete spaces from the beginning and end of the string.
# If argument is provided delete those characters from the string.

import re

def fakestrip(text, argument=None):
    if argument == None:                    # If no arguments are provided
        subsText = re.compile(r'^\s+\s')    # We create a regex expression
        print(subsText.sub('', text))       # strip it of spaces
    else:
        subsText = re.compile(argument)   # else. make a regex expression
        print("removing: " + argument)
        print(subsText.sub('', text))                       # replaces those characters passed to it in the argument with 
            
text = "     delete all whitespaces     "
text2 = "Im happy"

fakestrip(text)
fakestrip(text2, "happy")