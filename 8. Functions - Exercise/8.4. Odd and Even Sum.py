def sum_of_odd_and_sum_of_even_numbers(single_integer):
    sum_of_odd_numbers = 0
    sum_of_even_numbers = 0
    gosho = 5 #това Gosho си е моя измислица, за да видя дали трябва после на ред 14 да описвам всички променливи във функцията
    for i in single_integer:
        if int(i) % 2 == 0:
            sum_of_even_numbers += int(i)
        else:
            sum_of_odd_numbers += int(i)
    return sum_of_odd_numbers, sum_of_even_numbers, gosho


input_integer_as_string = input()
sum_of_odd_numbers, sum_of_even_numbers, gosho = sum_of_odd_and_sum_of_even_numbers(input_integer_as_string)
print(f"Odd sum = {sum_of_odd_numbers}, Even sum = {sum_of_even_numbers}")