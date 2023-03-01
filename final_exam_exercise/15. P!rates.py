my_dictionary = {}

command = input()
while command != "Sail":

    command = command.split("||")
    town = command[0]
    population = int(command[1])
    gold = int(command[2])
    if town in my_dictionary:
        new_population = population + my_dictionary[town]['population']
        new_gold = gold + my_dictionary[town]['gold']
        my_dictionary[town] = {'population': new_population, 'gold': new_gold}
    else:
        my_dictionary[town] = {"population": population, "gold": gold}
    command = input()

# {'Tortuga': {'population': 345000, 'gold': 1250}, 'Santo Domingo': {'population': 240000, 'gold': 630}, 'Havana': {'population': 410000, 'gold': 1100}}


command = input()
while command != "End":

    command = command.split("=>")
    action = command[0]

# на подадения град трябва да му намяля златото и хората, а ако някое от тях падне до 0 или по-малко
# трябва да го изтрия от списъка
    if action == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        if town in my_dictionary:
            my_dictionary[town]['population'] -= people
            my_dictionary[town]['gold'] -= gold
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            if my_dictionary[town]['population'] <= 0 or my_dictionary[town]['gold'] <= 0:
                print(f"{town} has been wiped off the map!")
                del my_dictionary[town]

# увеличаваме златото и хората в даден град, в случай че подадените стойности са положителни
    if action == "Prosper":
        town = command[1]
        gold = int(command[2])
        if town in my_dictionary:
            if gold < 0:
                print("Gold added cannot be a negative number!")
            else:
                my_dictionary[town]['gold'] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {my_dictionary[town]['gold']} gold.")

    command = input()

if len(my_dictionary) < 1:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(my_dictionary)} wealthy settlements to go to:")
    for key, value in my_dictionary.items():
        print(
            f"{key} -> Population: {my_dictionary[key]['population']} citizens, Gold: {my_dictionary[key]['gold']} kg")

# Tortuga||345000||1250
# Santo Domingo||240000||630
# Havana||410000||1100
# Sail
# Plunder=>Tortuga=>75000=>380
# Prosper=>Santo Domingo=>180
# End
