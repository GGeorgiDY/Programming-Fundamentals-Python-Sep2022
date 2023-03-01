first_index_name = 0
second_index_name = 0
first_index_age = 0
second_index_age = 0

number_of_integers = int(input())
for i in range(number_of_integers):
    command = input()
    counter = 1
    for ch in command:
        if ch == "@":
            first_index_name = counter
        if ch == "|":
            second_index_name = counter
        if ch == "#":
            first_index_age = counter
        if ch == "*":
            second_index_age = counter
        counter += 1
    name = command[first_index_name:second_index_name -1]
    age = command[first_index_age:second_index_age -1]
    print(f"{name} is {age} years old.")