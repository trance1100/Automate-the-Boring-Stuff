import re

word = re.compile(r'''
    [\d{3}]+(,)+''', re.VERBOSE)

test1 = '123,123,123'
test2 ='12,12,12'

obj1 = word.search(test1)
obj2 = word.search(test2)

print(obj1.group(0))
print(obj2.group(0))