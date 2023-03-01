number_of_inputs = int(input())
lst = []
filtered_lst = []

for i in range(number_of_inputs):
    new_input = int(input())
    lst.append(new_input)
command = input()
if command == "even":
    for y in lst:
        if y % 2 == 0:
            filtered_lst.append(y)
elif command == "odd":
    for y in lst:
        if y % 2 != 0:
            filtered_lst.append(y)
elif command == "negative":
    for y in lst:
        if y < 0:
            filtered_lst.append(y)
elif command == "positive":
    for y in lst:
        if y >= 0:
            filtered_lst.append(y)

print(filtered_lst)


