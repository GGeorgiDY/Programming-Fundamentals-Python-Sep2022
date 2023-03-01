new_student = input()
my_list = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]

while new_student != "Welcome!":
    if new_student == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(new_student) < 5:
        print(f"{new_student} goes to {my_list[0]}.")
    if len(new_student) == 5:
        print(f"{new_student} goes to {my_list[1]}.")
    if len(new_student) == 6:
        print(f"{new_student} goes to {my_list[2]}.")
    if len(new_student) > 6:
        print(f"{new_student} goes to {my_list[3]}.")
    new_student = input()

if new_student != "Voldemort":
    print("Welcome to Hogwarts.")
