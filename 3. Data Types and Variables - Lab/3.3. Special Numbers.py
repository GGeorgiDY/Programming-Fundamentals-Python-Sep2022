imput_number = int(input())

moi_spisak = [5, 7, 11]

for number in range(1, imput_number + 1):
    check_number = str(number)
    sum_of_digits = 0
    if len(check_number) < 2:
        sum_of_digits = int(check_number)
    else:
        first_number = int(check_number[0])
        second_number = int(check_number[1])
        sum_of_digits = int(first_number)+int(second_number)
    if sum_of_digits in moi_spisak:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")