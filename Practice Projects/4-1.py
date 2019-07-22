spam = ['apple', 'bananas', 'tofu', 'cats']
string = ""
for item in spam[:-1]:
    string += item + ", "
string += "and " + spam[-1]
print(string)

    