def sum_numbers(number1, number2):
    return number1 + number2


def subtract(my_sum, number3):
    return my_sum - number3


def add_and_subtract(number1, number2, number3):
    sum_of_first_and_second_number = sum_numbers(number1, number2)
    substraction_of_third_number = subtract(sum_of_first_and_second_number, number3)
    return substraction_of_third_number

first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number,second_number,third_number))


