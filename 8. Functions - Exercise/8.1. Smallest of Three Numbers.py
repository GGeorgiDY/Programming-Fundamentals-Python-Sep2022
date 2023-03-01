# def smallest_numbers(number1, number2, number3):
# 	return min(number1, number2, number3)
#
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
#
# print(smallest_numbers(first_number,second_number,third_number))

def smallest_numbers(numbers):
	return min(numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())

lst = [first_number, second_number, third_number]
min_number = smallest_numbers(lst)

print(min_number)
