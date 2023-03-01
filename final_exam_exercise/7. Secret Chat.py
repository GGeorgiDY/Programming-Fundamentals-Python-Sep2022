data = input()

while True:
    command = input()
    if command == "Reveal":
        print(f"You have a new text message: {data}")
        break

    command = command.split(":|:")
    action = command[0]

    # добавяме интервал на даден индекс
    if action == "InsertSpace":
        index = int(command[1])
        data = data[:index] + " " + data[index:]
        print(data)

    # ако дадена поредица от букви я има в стринга, трябва да я изтрием и да я сложим в края на стринга - наобратно
    if action == "Reverse":
        substring = command[1]
        if substring in data:
            # reverse_substring = substring[::-1]
            # data = data.replace(substring, reverse_substring)
            data = data.replace(substring, "", 1)
            data = data + substring[::-1]
            print(data)
        else:
            print('error')

    # променяме дадена буква от стринга да е такава каквато ние сме подали от инпута
    if action == "ChangeAll":
        old_string = command[1]
        new_string = command[2]
        data = data.replace(old_string, new_string)
        print(data)


# heVVodar!gniV
# ChangeAll:|:V:|:l
# Reverse:|:!gnil
# InsertSpace:|:5
# Reveal

# Hiware?uiy
# ChangeAll:|:i:|:o
# Reverse:|:?uoy
# Reverse:|:jd
# InsertSpace:|:3
# InsertSpace:|:7
# Reveal