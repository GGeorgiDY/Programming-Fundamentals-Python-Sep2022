# def is_number_perfect(number):
#     number_is_perfect = False
#     sum_of_divisors = 0
#     for i in range(1, number + 1):
#         if number % i == 0:
#             sum_of_divisors += i
#         if sum_of_divisors == number:
#             number_is_perfect = True
#     return number_is_perfect
#
#
# given_number = int(input())
# result = is_number_perfect(given_number)
# if result:
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")

def is_number_perfect(number):
    sum_of_divisors = 0
    for i in range(1, number + 1):
        if number % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == number:
        return "We have a perfect number!"
    return "It's not so perfect."


given_number = int(input())
print(is_number_perfect(given_number))