first_command = input()
while True:
    command = input()
    if command == 'Travel':
        break

    command = command.split(":")
    action = command[0]
    if action == "Add Stop":# на 13 ред в кода добавям нов стринг на определен индекс в стринга ми
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(first_command):
            first_command = first_command[:index] + string + first_command[index:]
        print(first_command)

    elif action == "Remove Stop":# на 20 ред в кода махам всички букви които се намират помежду двата индекса в стринга ми
        first_index = int(command[1])
        second_index = int(command[2])
        if 0 <= first_index < len(first_command) and 0 <= second_index < len(first_command):
            first_command = first_command[0:first_index] + first_command[second_index +1:]
        print(first_command)

    elif action == "Switch":# заменям даден дума с друга в стринга ми
        old_string = command[1]
        new_string = command[2]
        if old_string in first_command:
            first_command = first_command.replace(old_string, new_string)
        print(first_command)

print(f"Ready for world tour! Planned stops: {first_command}")


# Hawai::Cyprys-Greece
# Add Stop:7:Rome
# Remove Stop:11:16
# Switch:Hawai:Bulgaria
# Travel
