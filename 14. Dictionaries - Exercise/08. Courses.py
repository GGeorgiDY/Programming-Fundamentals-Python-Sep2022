my_dictionary = {}
while True:
    command = input()
    if command == 'end':
        break

    command = command.split(" : ")
    course = command[0]
    name = command[1]

    if course not in my_dictionary:
        my_dictionary[course] = []
        my_dictionary[course].append(name)
    else:
        my_dictionary[course].append(name)

for i in my_dictionary:
    print(f"{i}: {len(my_dictionary[i])}")
    for y in my_dictionary[i]:
        print(f" -- {y}")

# Algorithms : Jay Moore
# Programming Basics : Martin Taylor
# Python Fundamentals : John Anderson
# Python Fundamentals : Andrew Robinson
# Algorithms : Bob Jackson
# Python Fundamentals : Clark Lewis
# end
