my_dict = {}
while True:
    command = input()
    if command == "End":
        break
    command = command.split(" -> ")
    company = command[0]
    information = command[1]
    if company not in my_dict:
        my_dict[company] = []
        my_dict[company].append(information) #така може да апендваме в речника
    else:
        if information not in my_dict[company]: # така проверяваме дали value-то вече го има, и ако да не го добавя
            my_dict[company].append(information)

for i in my_dict:
    print(i)
    for y in my_dict[i]: #обхождаме всяко value в key-a
        print(f"-- {y}")

# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End
