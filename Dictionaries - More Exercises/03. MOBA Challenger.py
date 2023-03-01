def main(players_total_skill_dictionary, my_dictionary, command):
    if "->" in command:
        command = command.split(" -> ")
        player = command[0]
        position = command[1]
        skill = int(command[2])
        if player not in my_dictionary:
            my_dictionary[player] = {}
            my_dictionary[player][position] = skill
        else:
            if position not in my_dictionary[player]:
                my_dictionary[player][position] = skill
            else:
                if my_dictionary[player][position] < skill:
                    my_dictionary[player][position] = skill

    if " vs " in command:
        command = command.split(" vs ")
        player1 = command[0]
        player2 = command[1]
        if player1 and player2 in my_dictionary:
            for match in my_dictionary[player1].keys():
                if match in my_dictionary[player2]:
                    skill = my_dictionary[player1][match]
                    if skill > my_dictionary[player2][match]:
                        del my_dictionary[player2]
                        break
            if player2 in my_dictionary:
                for match in my_dictionary[player2].keys():
                    if match in my_dictionary[player1]:
                        skill = my_dictionary[player2][match]
                        if skill > my_dictionary[player1][match]:
                            del my_dictionary[player1]
                            break


def total_skills(players_total_skill_dictionary, my_dictionary):
    counter = 0
    lst = []
    for player, position in my_dictionary.items():
        for i in my_dictionary[player].values():
            counter += i
        if player not in players_total_skill_dictionary:
            players_total_skill_dictionary[player] = counter
        else:
            players_total_skill_dictionary[player] += counter
        counter = 0


players_total_skill_dictionary = {}
my_dictionary = {}

while True:
    command = input()
    if command == 'Season end':
        break

    main(players_total_skill_dictionary, my_dictionary, command)
# print(my_dictionary)
# {'Peter': {'Adc': 400}, 'Frank': {'Mid': 200, 'Support': 250, 'Tank': 250}}

total_skills(players_total_skill_dictionary, my_dictionary)
# print(players_total_skill_dictionary)
# {'Peter': 400, 'Frank': 700}

for username, points in sorted(players_total_skill_dictionary.items(), key=lambda x: (-x[1], x[0])):
    print(f"{username}: {points} skill")
    for key, value in sorted(my_dictionary[username].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {key} <::> {value}")




# Peter -> Adc -> 400
# Bush -> Tank -> 150
# Frank -> Mid -> 200
# Frank -> Support -> 250
# Frank -> Tank -> 250
# Peter vs Frank
# Frank vs Bush
# Frank vs Hide
# Season end

