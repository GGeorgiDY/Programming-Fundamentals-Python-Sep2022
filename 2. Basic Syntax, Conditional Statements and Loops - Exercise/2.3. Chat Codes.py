number_of_messages = int(input())

for i in range(1, number_of_messages + 1):
    new_number = int(input())
    if new_number == 88:
        print("Hello")
    elif new_number == 86:
        print("How are you?")
    elif new_number != 88 and new_number != 86 and new_number <88:
        print("GREAT!")
    else:
        print("Bye.")