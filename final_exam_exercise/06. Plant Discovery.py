first_line = int(input())

my_dictionary = {}
while True:
    command = input()
    if "<->" not in command:
        break

    command = command.split("<->")
    plant_name = command[0]
    rarity = int(command[1])
    my_dictionary[plant_name] = {"rarity": rarity, "rating": []}
# създадох този речник, който ще пълня със следващите операции по-долу
# {'Arnoldii': {'rarity': 4, 'rating': []}, 'Woodii': {'rarity': 7, 'rating': []}, 'Welwitschia': {'rarity': 2, 'rating': []}}

while True:
    if command == "Exhibition":
        break

    command = command.split(": ")
    action = command[0]
    other_info = command[1]

    # добавям всеки новоподаден рейтинг за всяко растение в неговия си лист
    if action == "Rate":
        other_info = other_info.split(" - ")
        plant_name = other_info[0]
        plant_rating = int(other_info[1])
        if plant_name in my_dictionary:
            my_dictionary[plant_name]['rating'].append(plant_rating)
        else:
            print('error')

    # ъпдейтвам rarity-то на дадено растение с новоподаденото rarity от инпут-а
    if action == "Update":
        other_info = other_info.split(" - ")
        plant_name = other_info[0]
        new_rarity = int(other_info[1])
        if plant_name in my_dictionary:
            my_dictionary[plant_name]['rarity'] = new_rarity
        else:
            print('error')

    # изтривам рейтинга за даденото растение от инпута -> правя лист-а празен
    if action == "Reset":
        plant_name = command[1]
        if plant_name in my_dictionary:
            my_dictionary[plant_name]['rating'] = []
        else:
            print('error')
    command = input()

print(f'Plants for the exhibition:')

for key in my_dictionary.keys():
    average_rating = 0
    if my_dictionary[key]['rating']:
        average_rating = sum(my_dictionary[key]['rating']) / len(my_dictionary[key]['rating'])
    print(f"- {key}; Rarity: {my_dictionary[key]['rarity']}; Rating: {average_rating:.2f}")


# 3
# Arnoldii<->4
# Woodii<->7
# Welwitschia<->2
# Rate: Woodii - 10
# Rate: Welwitschia - 7
# Rate: Arnoldii - 3
# Rate: Woodii - 5
# Update: Woodii - 5
# Reset: Arnoldii
# Exhibition
