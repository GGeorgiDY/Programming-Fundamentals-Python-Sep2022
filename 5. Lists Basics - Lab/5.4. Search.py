number_of_strings = int(input())
special_word = input()
lst = []
second_lst = []

for i in range(number_of_strings):
    new_string = input()
    lst.append(new_string)
    if special_word in new_string:
        second_lst.append(new_string)
print(lst)
print(second_lst)
