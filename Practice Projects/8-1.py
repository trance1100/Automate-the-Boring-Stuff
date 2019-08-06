#! /usr/share/python
# madLibs - Given a text file the user will provide a Adjective, noun, adverb or verb and replace it for the user input.

import re   

regexExp = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
madlibs = open('text.txt')
content = madlibs.read()

mo = regexExp.findall(content)
print(mo)
mo = list(dict.fromkeys(mo))

for words in mo:
    word = input("Enter an " + words + ": ")
    content = re.sub(re.escape(words), word, content)

print(content)