import re

word = re.compile(r'''(
    ['Alice'|'Bob'|'Carol']
    # [eats|pets|throws]\s
    # [apple|cats|baseballs]
    # /.$
    )''', re.IGNORECASE|re.VERBOSE)

test1 = 'Alice eats apples.'
test2 = 'Carol throws baseballs.'

obj1 = word.findall(test1)
obj2 = word.findall(test2)

print(obj1)
print(obj2)
