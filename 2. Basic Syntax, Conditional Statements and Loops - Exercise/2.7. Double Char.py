new_string = input()

while new_string != "End":
    if new_string == "SoftUni":
        new_string = input()
        continue
    else:
        for i in new_string:
            print(i * 2, end="")
        print()
        new_string = input()

