my_dictionary = {}
number_of_inputs = int(input())
for _ in range(number_of_inputs):
    command = input()
    dragon_type, name, damage, health, armor = command.split(' ')
    if damage == "null":
        damage = int(45)
    if health == "null":
        health = int(250)
    if armor == "null":
        armor = int(10)
    if dragon_type not in my_dictionary:
        my_dictionary[dragon_type] = {}
        my_dictionary[dragon_type][name] = [damage, health, armor]
    else:
        if name not in my_dictionary[dragon_type]:
            my_dictionary[dragon_type][name] = [damage, health, armor]
        else:
            my_dictionary[dragon_type][name] = [damage, health, armor]

# print(my_dictionary)
# {'Red': {'Bazgargal': [100, 2500, 25], 'Obsidion': [220, 2200, 35]}, 'Black': {'Dargonax': [200, 3500, 18]}, 'Blue': {'Kerizsa': [60, 2100, 20], 'Algordox': [65, 1800, 50]}}

# калкулиране на средния размер на атака, здраве и защита на всеки вид дракон
for type, value in my_dictionary.items():
    damage = 0
    health = 0
    armor = 0
    for data in value.values():
        damage += int(data[0])
        health += int(data[1])
        armor += int(data[2])
    average_damage = damage / len(value)
    average_health = health / len(value)
    average_armor = armor / len(value)
    print(f"{type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    # сортиране на драконите по азбучен ред
    # принтиране на драконите и техните стойности
    for key, values in sorted(value.items(), key=lambda x: x[0]):
        print(f"-{key} -> damage: {values[0]}, health: {values[1]}, armor: {values[2]}")

# 5
# Red Bazgargal 100 2500 25
# Black Dargonax 200 3500 18
# Red Obsidion 220 2200 35
# Blue Kerizsa 60 2100 20
# Blue Algordox 65 1800 50
