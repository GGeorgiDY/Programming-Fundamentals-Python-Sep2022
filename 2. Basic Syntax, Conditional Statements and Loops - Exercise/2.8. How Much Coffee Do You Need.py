event = input()
needed_coffee = 0

while event != "END":
    if event.lower() == "coding"\
        or event.lower() == "cat"\
        or event.lower() == "dog"\
        or event.lower() == "movie":
        if event.islower():
            needed_coffee += 1
        else:
            needed_coffee += 2
    event = input()

if needed_coffee > 5:
    print("You need extra sleep")
else:
    print(needed_coffee)




