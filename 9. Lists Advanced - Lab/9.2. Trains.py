# def train(number_of_wagons):
#     lst = []
#     for i in range(number_of_wagons):
#         lst.append(0)
#         lst = list(map(int, lst))
#     command = input()
#     while command != "End":
#         new_list = []
#         new_list = command.split()
#         if new_list[0] == "add":
#             del new_list[0]
#             new_list = list(map(int, new_list))
#             lst[-1] += new_list[0]
#         if new_list[0] == "insert":
#             del new_list[0]
#             for x in new_list[0]
#             new_list = list(map(int, new_list))
#
#         command = input()
#     return lst
#
#
# wagons = int(input())
# print(train(wagons))
# горния код е грешен :D
#####################################

number = int(input())
wagons = [0] * number
command = input()

while command != "End":

    split_command = command.split(' ')
    current_command = split_command[0]

    if current_command == "add":
        people_to_add = int(split_command[1])
        wagons[-1] += people_to_add

    elif current_command == "insert":
        index = int(split_command[1])
        people_to_add = int(split_command[2])
        wagons[index] += people_to_add

    elif current_command == "leave":
        index = int(split_command[1])
        people_to_add = int(split_command[2])
        wagons[index] -= people_to_add

    command = input()

print(wagons)
