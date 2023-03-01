import re

given_key = ''.join(input().split())
len_of_given_key = len(given_key) - 1
final_list = []

while True:
    command = input()
    if command == 'find':
        break

    counter = 0
    for ch in command:
        ch = ord(ch)
        ch -= int(given_key[counter])
        ch = chr(ch)
        final_list.append(ch)
        counter += 1
        if len_of_given_key < counter:
            counter = 0
    hidden_message = ''.join(final_list)
    final_list = []
    pattern_type = re.compile(r'((&)(?P<type>[A-Za-z0-9]+)(&))')
    pattern_coordinates = re.compile(r'((<)(?P<coordinates>[A-Za-z0-9]+)(>))')
    result_type = re.finditer(pattern_type, hidden_message)
    result_coordinates = re.finditer(pattern_coordinates, hidden_message)
    type = [x['type'] for x in result_type]
    coordinates = [x['coordinates'] for x in result_coordinates]
    print(f"Found {''.join(type)} at {''.join(coordinates)}")

# 1 2 1 3
# ikegfp'jpne)bv=41P83X@
# ujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA
# find

