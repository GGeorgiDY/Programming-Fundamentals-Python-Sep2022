def users_total_points(users_total_points_dictionary, username, points):
    if username not in users_total_points_dictionary:
        users_total_points_dictionary[username] = int(points)
    else:
        users_total_points_dictionary[username] += int(points)


def main(contests_dictionary, users_total_points_dictionary, command):
    username, contest, points = command.split(' -> ')
    if contest not in contests_dictionary:
        contests_dictionary[contest] = {}
        contests_dictionary[contest][username] = int(points)
        users_total_points(users_total_points_dictionary, username, points)
    else:
        if username not in contests_dictionary[contest]:
            contests_dictionary[contest][username] = int(points)
            users_total_points(users_total_points_dictionary, username, points)
        else:
            if contests_dictionary[contest][username] < int(points):
                diff = int(points) - contests_dictionary[contest][username]
                contests_dictionary[contest][username] += diff
                users_total_points(users_total_points_dictionary, username, diff)


def result(contests_dictionary, users_total_points_dictionary):
    for contest in contests_dictionary:
        print(f"{contest}: {len(contests_dictionary[contest])} participants")
        counter = 1
        for username, points in sorted(contests_dictionary[contest].items(), key=lambda x: (-x[1], x[0])):
            print(f"{counter}. {username} <::> {contests_dictionary[contest][username]}")
            counter += 1
    print("Individual standings:")
    counter = 1
    for username, points in sorted(users_total_points_dictionary.items(), key=lambda x: (-x[1], x[0])):
        print(f"{counter}. {username} -> {users_total_points_dictionary[username]}")
        counter += 1


contests_dictionary = {}
users_total_points_dictionary = {}

while True:
    command = input()
    if command == 'no more time':
        break

    main(contests_dictionary, users_total_points_dictionary, command)

# print(contests_dictionary)
# {'OOP': {'Peter': 350, 'George': 300, 'Prakash': 300}, 'Advanced': {'Simo': 600, 'Prakash': 250}, 'JSCore': {'Ani': 400}}
# print(users_total_points_dictionary)
# {'Peter': 350, 'George': 300, 'Simo': 600, 'Prakash': 550, 'Ani': 400}

result(contests_dictionary, users_total_points_dictionary)

# Peter -> OOP -> 350
# George -> OOP -> 250
# Simo -> Advanced -> 600
# George -> OOP -> 300
# Prakash -> OOP -> 300
# Prakash -> Advanced -> 250
# Ani -> JSCore -> 400
# no more time
