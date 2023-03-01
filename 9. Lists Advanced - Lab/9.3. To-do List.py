# command = input()
# lst = []
# new_list = []
#
# while command != "End":
#     lst.append(command)
#     command = input()
#
# lst.sort()
# for x in lst:
#     asd = x
#     lst = asd.split("-")
#     lst = lst.pop()
#     new_list.append(lst)
#
# print(new_list)


task = []

while True:
    command = input()
    if command == "End":
        break
    split_command = command.split("-")
    priority = int(split_command[0])
    current_task = split_command[1]
    task.append((priority, current_task))

#друг вариант за решението
# sorted_tasks = []
# for task_data in sorted(task):
#     sorted_tasks.append(task_data[1])

#още един вариант е с for цикъл
# sorted_tasks =[]
# for x in sorted(task):
#     sorted_tasks.append(x[1])

sorted_tasks = [x[1] for x in sorted(task)]
print(sorted_tasks)
