#! /usr/share/python
# madLibs - Given a text file the user will provide a Adjective, noun, adverb or verb and replace it for the user input.

import re   

regexExp = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
madlibs = open('text.txt')
content = madlibs.read()

mo = regexExp.findall(content)
print(mo)

if 'ADJECTIVE' in mo:
    adjective = input("Enter an adjective:")
    content = re.sub(r'ADJECTIVE', adjective,  content)

if 'NOUN' in mo:
    noun = input("Enter a noun:")
    content = re.sub(r'NOUN', noun,  content)

if 'ADVERB' in mo:
    adverb = input("Enter an adverb")
    content = re.sub(r'ADVERB', adverb,  content)

if 'VERB' in mo:
    verb = input("Enter a verb:")
    content = re.sub(r'VERB', verb,  content)

print(content)