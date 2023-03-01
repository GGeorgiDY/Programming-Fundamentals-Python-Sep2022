my_dictionary = {}
number_of_heroes = int(input())
for heroes in range(number_of_heroes):
    hero = input().split()
    hero_name = hero[0]
    HP = int(hero[1])
    MP = int(hero[2])
    if HP > 100:
        HP = 100
    if MP > 200:
        HP = 200
    my_dictionary[hero_name] = {"HP" : HP, "MP" : MP}

# print(my_dictionary)# {'Solmyr': {'HP': 85, 'MP': 120}, 'Kyrre': {'HP': 99, 'MP': 50}}

command = input()
while command != 'End':
    cmd_type, hero_name, *data = command.split(" - ")
    if "CastSpell" in cmd_type:
        mp_needed = int(data[0])
        spell_name = data[1]
        if hero_name in my_dictionary:
            if mp_needed <= my_dictionary[hero_name]["MP"]:
                my_dictionary[hero_name]["MP"] -= int(mp_needed)
                print(f"{hero_name} has successfully cast {spell_name} and now has {my_dictionary[hero_name]['MP']} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    if "TakeDamage" in cmd_type:
        damage = int(data[0])
        attacker = data[1]
        if hero_name in my_dictionary:
            my_dictionary[hero_name]["HP"] -= damage
            if my_dictionary[hero_name]["HP"] <= 0:
                print(f"{hero_name} has been killed by {attacker}!")
                del my_dictionary[hero_name]
            else:
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {my_dictionary[hero_name]['HP']} HP left!")

    if "Recharge" in cmd_type:
        amount = int(data[0])
        amount_recovered = 0
        if hero_name in my_dictionary:
            my_dictionary[hero_name]["MP"] += amount
            if my_dictionary[hero_name]["MP"] > 200:
                amount_recovered = amount + (200 - my_dictionary[hero_name]["MP"])
                my_dictionary[hero_name]["MP"] = 200
            else:
                amount_recovered = amount
            print(f"{hero_name} recharged for {amount_recovered} MP!")

    if "Heal" in cmd_type:
        amount = int(data[0])
        amount_recovered = 0
        if hero_name in my_dictionary:
            my_dictionary[hero_name]["HP"] += amount
            if my_dictionary[hero_name]["HP"] > 100:
                amount_recovered = amount + (100 - my_dictionary[hero_name]["HP"])
                my_dictionary[hero_name]["HP"] = 100
                print(f"{hero_name} healed for {amount_recovered} HP!")
            else:
                amount_recovered = amount
                print(f"{hero_name} healed for {amount_recovered} HP!")

    command = input()

for key, item in my_dictionary.items():
    print(f"{key}")
    print(f"    HP: {my_dictionary[key]['HP']}")
    print(f"    MP: {my_dictionary[key]['MP']}")


# 2
# Solmyr 85 120
# Kyrre 99 50
# Heal - Solmyr - 10
# Recharge - Solmyr - 50
# TakeDamage - Kyrre - 66 - Orc
# CastSpell - Kyrre - 15 - ViewEarth
# End

# 4
# Adela 90 150
# SirMullich 70 40
# Ivor 1 111
# Tyris 94 61
# Heal - SirMullich - 50
# Recharge - Adela - 100
# CastSpell - Tyris - 1000 - Fireball
# TakeDamage - Tyris - 99 - Fireball
# TakeDamage - Ivor - 3 - Mosquito
# End
