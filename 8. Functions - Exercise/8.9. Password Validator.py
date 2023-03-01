def password_checker(my_password):
    password_is_valid = True
    if len(my_password) < 6 or len(my_password) > 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False

    if not my_password.isalnum(): # преоверява дали са числа или букви
        print("Password must consist only of letters and digits")
        password_is_valid = False

    digit_counter = 0
    for i in my_password:
        if i.isdigit():     #i = 0 or i = 1 or i = 2... i = 9 проверява дали са числа
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False

    return password_is_valid


input_password = input()
result = password_checker(input_password)
if result:
    print("Password is valid")
