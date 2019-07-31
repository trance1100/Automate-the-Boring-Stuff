# Objective: Create a clone of strip() using the sub function from the regex module.
# If no arguments are given, simply delete spaces from the beginning and end of the string.
# If argument is provided delete those characters from the string.

import re

def fakestrip(text, argument=None):
    if argument == None:
        subsText = re.compile(r'^\s+\s')
        print(subsText.sub('', text))
    else:
        subsText = re.compile(r'[re.escape(argument)]')
        print(subsText.sub('', text))

text = "     delete all whitespaces     "
text2 = "Im happy"

fakestrip(text)
fakestrip(text2, "happy")