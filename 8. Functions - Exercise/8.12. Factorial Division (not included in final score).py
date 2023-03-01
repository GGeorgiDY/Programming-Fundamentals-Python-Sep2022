def factorial(number1, number2):
    first_number_factorial = 1
    second_number_factorial = 1
    for i in range(1, number1 + 1):
        first_number_factorial = first_number_factorial * i
    for y in range(1, number2 + 1):
        second_number_factorial = second_number_factorial * y
    result = first_number_factorial / second_number_factorial
    return f"{result:.2f}"


first_number = int(input())
second_number = int(input())
print(factorial(first_number, second_number))