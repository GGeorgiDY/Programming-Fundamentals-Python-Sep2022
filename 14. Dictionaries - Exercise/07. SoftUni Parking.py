number_of_commands = int(input())
my_dicionary = {}
for i in range(number_of_commands):
    command = input()
    if "unregister" not in command:
        command = command.split(" ")
        name = command[1]
        if name not in my_dicionary:
            license_plate_number = command[2]
            my_dicionary[name] = license_plate_number
            print(f"{name} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    else:
        command = command.split(" ")
        username = command[1]
        if username not in my_dicionary:
            print(f"ERROR: user {username} not found")
        else:
            my_dicionary.pop(username)
            print(f"{username} unregistered successfully")

for key, value in my_dicionary.items():
    print(f"{key} => {value}")

# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy
