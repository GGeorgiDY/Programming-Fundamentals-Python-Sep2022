import re

my_dictionary = {}
list_of_participants = input().split(", ")
# print(list_of_participants)
# ['George', 'Peter', 'Bill', 'Tom']
while True:
    command = input()
    if command == "end of race":
        break

    distance = 0

    pattern_name = r"[A-Za-z]"
    pattern_distance = r"\d"

    result_name = re.findall(pattern_name, command)
    name = ''.join(result_name)

    result_distance = re.findall(pattern_distance, command)
    for i in result_distance:
        distance += int(i)

    if name in list_of_participants:
        if name not in my_dictionary:
            my_dictionary[name] = distance
        else:
            my_dictionary[name] += distance

# print(my_dictionary)
# {'George': 55, 'Bill': 11, 'Peter': 25, 'Tom': 19}

sorted_dictionary = dict(sorted(my_dictionary.items(), key=lambda x: (-x[1], -x[1])))
# print(sorted_dictionary)
# {'George': 55, 'Bill': 11, 'Peter': 25, 'Tom': 19}

counter = 1
for k, v in sorted_dictionary.items():
    if counter == 1:
        print(f"1st place: {k}")
    if counter == 2:
        print(f"2nd place: {k}")
    if counter == 3:
        print(f"3rd place: {k}")
    counter += 1

# George, Peter, Bill, Tom
# G4e@55or%6g6!68e!!@
# R1@!3a$y4456@
# B5@i@#123ll
# G@e54o$r6ge#
# 7P%et^#e5346r
# T$o553m&6
# end of race

# result
# 1st place: George
# 2nd place: Peter
# 3rd place: Tom