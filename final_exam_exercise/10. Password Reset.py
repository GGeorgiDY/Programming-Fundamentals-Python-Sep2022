some_string = input()
lst = []

command = input()
while command != "Done":

    cmd_type, *data = command.split()

    if cmd_type == "TakeOdd":
        for pos, ele in enumerate(some_string):
            if pos % 2 != 0:
                lst.append(ele)
        some_string = "".join(lst)
        print(some_string)

    elif cmd_type == "Cut":
        index = int(data[0])
        lenght = int(data[1])
        second_index = index + lenght
        if second_index <= len(some_string):
            some_string = some_string[:index] + some_string[second_index:]
            print(some_string)

    elif cmd_type == "Substitute":
        substring = data[0]
        substitute = data[1]
        if substring in some_string:
            some_string = some_string.replace(substring, substitute)
            print(some_string)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {some_string}")

# Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr
# TakeOdd
# Cut 15 3
# Substitute :: -
# Substitute | ^
# Done

# up8rgoyg3r1atmlmpiunagt!-irs7!1fgulnnnqy
# TakeOdd
# Cut 18 2
# Substitute ! ***
# Substitute ? .!.
# Done