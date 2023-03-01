import re
from audioop import reverse

number_of_inputs = int(input())

counter = 0
lst = []
my_dictionary = {}
for i in range(number_of_inputs):
    command = input()
    for ch in command:
        if ch == "s" or ch == "S" or ch == "t" or ch == "T" or ch == "a" or ch == "A" or ch == "r" or ch == "R":
            counter += 1
    for ch in command:
        ch = int(ord(ch)) - counter
        new_ch = chr(ch)
        lst.append(new_ch)
    word = ''.join(lst)
    lst.clear()
    counter = 0
    pattern = re.compile(r"[\@\-\!\:\>]+(?P<planet>[A-Za-z]+)([?[0-9\@\-\!\:\>]*)[\@\-\!\:\>]+(?P<population>\d+)([?[0-9\@\-\!\:\>]*)[\@\-\!\:\>]+(?P<attack_type>A|D)[\@\-\!\:\>]+([?[0-9\@\-\!\:\>]*)[\@\-\!\:\>]+(?P<soldier_count>\d+)")
    result = re.finditer(pattern, word)
    for i in result:
        if i['attack_type'] not in my_dictionary:
            my_dictionary[i['attack_type']] = []
            my_dictionary[i['attack_type']].append(i['planet'])
        else:
            my_dictionary[i['attack_type']].append(i['planet'])

# print(my_dictionary)
# {'A': ['Alderaa'], 'D': ['Cantonica']}
# my_dictionary = dict(sorted(my_dictionary.items(), key=lambda x: x[-1], reverse=True))

counter = 0
for k,v in my_dictionary.items():
    if k == 'A':
        print(f"Attacked planets: {len(my_dictionary[k])}")
        if len(my_dictionary[k]) > 0:
            for i in sorted(v):
                print(f"-> {i}")

    elif k == 'D':
        if "A" not in my_dictionary.keys():
            if counter == 0:
                print(f"Attacked planets: 0")
                counter += 1
        print(f"Destroyed planets: {len(my_dictionary[k])}")
        if len(my_dictionary[k]) > 0:
            for i in sorted(v):
                print(f"-> {i}")