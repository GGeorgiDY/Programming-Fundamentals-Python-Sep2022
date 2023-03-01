# def only_even_numbers(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
#
# input_lst = input().split(" ")
# result = filter(only_even_numbers, input_lst)
# final_result = list(result)
# print(final_result)


def even(num):
    result = list(filter(lambda a: a % 2 == 0, num))
    return result


numbers = list(map(int, input().split(" ")))
print(even(numbers))