name_list = []
number_list = []
while True:
    command = input().split("-")
    if len(command) < 2:
        break
    name = command[0]
    number = command[1]
    name_list.append(name)
    number_list.append(number)

my_dict = dict(zip(name_list, number_list))
command = ' '.join(command)

for i in range(int(command)):
    searched_name = input()
    if searched_name not in my_dict.keys():
        print(f"Contact {searched_name} does not exist.")
    else:
        print(f"{searched_name} -> {my_dict[searched_name]}")

# Adam-+359888001122
# Ralf-666
# George-5559393
# Silvester-02/987665544
# 4
# Silvester
# silvester
# Rolf
# Ralf

