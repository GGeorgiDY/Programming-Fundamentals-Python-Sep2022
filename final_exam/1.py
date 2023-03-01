some_string = input()

while True:
    command = input()
    if command == "Finish":
        break

    command = command.split(" ")
    action = command[0]

    if action == "Replace":
        string_to_be_replaced = command[1]
        new_string = command[2]
        some_string = some_string.replace(string_to_be_replaced, new_string)
        print(some_string)

    if action == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= end_index < len(some_string):
            some_string = some_string[:start_index] + some_string[end_index + 1:]
            print(some_string)
        else:
            print("Invalid indices!")

    if action == "Make":
        up_or_lower = command[1]
        if up_or_lower == "Upper":
            some_string = some_string.upper()
            print(some_string)
        else:
            some_string = some_string.lower()
            print(some_string)

    if action == "Check":
        checked_message = command[1]
        if checked_message in some_string:
            print(f"Message contains {checked_message}")
        else:
            print(f"Message doesn't contain {checked_message}")

    if action == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 < start_index <= end_index < len(some_string):
            new_string = some_string[start_index:end_index + 1]
            result = 0
            for ch in new_string:
                result += ord(ch)
            print(result)
        else:
            print("Invalid indices!")