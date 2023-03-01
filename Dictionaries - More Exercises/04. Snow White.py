my_dictionary = {}
lst = []
while True:
    command = input()
    if command == 'Once upon a time':
        break

    command = command.split(' <:> ')
    dwarf_name = command[0]
    dwarf_hat_color = command[1]
    dwarf_physics = int(command[2])
    if dwarf_hat_color not in my_dictionary:
        my_dictionary[dwarf_hat_color] = {dwarf_name: dwarf_physics}
    elif dwarf_name in my_dictionary[dwarf_hat_color]:
        if dwarf_physics > my_dictionary[dwarf_hat_color][dwarf_name]:
            my_dictionary[dwarf_hat_color][dwarf_name] = dwarf_physics
    elif dwarf_hat_color in my_dictionary:
        my_dictionary[dwarf_hat_color][dwarf_name] = dwarf_physics

# print(my_dictionary)
# {'Red': {'Grumpy': 10000}, 'Blue': {'Grumpy': 10000, 'Happy': 10000}}

for hat_color in my_dictionary.keys():# Red Blue
    for name, physics in my_dictionary[hat_color].items():
        lst.append({"hat_len": len(my_dictionary[hat_color]), "name": name, "physics": physics, "hat": hat_color})
# print(lst)
# [{'hat_len': 1, 'name': 'Grumpy', 'physics': 10000, 'hat': 'Red'}, {'hat_len': 2, 'name': 'Grumpy', 'physics': 10000, 'hat': 'Blue'}, {'hat_len': 2, 'name': 'Happy', 'physics': 10000, 'hat': 'Blue'}]

for i in sorted(lst, key=lambda x: (-x["physics"], -x["hat_len"])):
    # print(i)
    # {'hat_len': 2, 'name': 'Grumpy', 'physics': 10000, 'hat': 'Blue'}
    # {'hat_len': 2, 'name': 'Happy', 'physics': 10000, 'hat': 'Blue'}
    # {'hat_len': 1, 'name': 'Grumpy', 'physics': 10000, 'hat': 'Red'}
    print(f"({i['hat']}) {i['name']} <-> {i['physics']}")
    # (Blue) Grumpy <-> 10000
    # (Blue) Happy <-> 10000
    # (Red) Grumpy <-> 10000


# Grumpy <:> Red <:> 5000
# Grumpy <:> Blue <:> 10000
# Grumpy <:> Red <:> 10000
# Happy <:> Blue <:> 10000
# Once upon a time

