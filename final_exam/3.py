my_dictionary = {}

while True:
    command = input()
    if command == 'Log out':
        break

    command = command.split(": ")
    action = command[0]

    if action == 'New follower':
        new_follower = command[1]
        if new_follower not in my_dictionary:
            my_dictionary[new_follower] = {"likes": 0, "comments": 0}

    if action == 'Like':
        name = command[1]
        likes = int(command[2])
        if name not in my_dictionary:
            my_dictionary[name] = {'likes': likes, 'comments': 0}
        else:
            my_dictionary[name]['likes'] += likes

    if action == 'Comment':
        username = command[1]
        if username not in my_dictionary:
            my_dictionary[username] = {'likes': 0, 'comments': 1}
        else:
            my_dictionary[username]['comments'] += 1

    if action == 'Blocked':
        username = command[1]
        if username not in my_dictionary:
            print(f"{username} doesn't exist.")
        else:
            del my_dictionary[username]

# print(my_dictionary)

for key, value in my_dictionary.items():
    my_dictionary[key]['likes'] = my_dictionary[key]['likes'] + my_dictionary[key]['comments']


print(f"{len(my_dictionary)} followers")
for key, value in my_dictionary.items():
    print(f"{key}: {value['likes']}")
