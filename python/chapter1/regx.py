import re

file = open("google.txt")
for i in file:
    patternmatch = re.findall(r"^\w+",i)
    if patternmatch:
        print(patternmatch)
