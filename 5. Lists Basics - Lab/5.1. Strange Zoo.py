my_list = []
new_list = []
for _ in  range(3):
    data = input()
    my_list.append(data) # с append добавяме неша в списъка


my_list[0], my_list[2] = my_list[2], my_list[0] #слапваме им местата
print(my_list)
