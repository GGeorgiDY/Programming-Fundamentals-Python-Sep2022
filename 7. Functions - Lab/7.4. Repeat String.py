# def repeat_string(current_string, num):
#     return current_string * num
#
# my_string = input()
# number = int(input())
# print(repeat_string(my_string, number))


my_string = input()
number = int(input())
result = lambda my_string, num: my_string * number
print(result(my_string, number))