import re

pattern = r"\d+"
data = input()
while True:
    if data:
        match = re.findall(pattern, data)
        if match: #проверяваме дали има числа в импута
            print(' '.join(match), end=" ")
        data = input()
    else:
        break

# The300
# What is that?
# I think it's the 3rd movie
# Let's watch it at 22:45