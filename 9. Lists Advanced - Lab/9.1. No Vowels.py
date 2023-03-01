# def removing_all_vowels(simple_string):
#     lst = []
#     for i in simple_string:
#         if i not in "aeiouAEIOU":
#             lst.append(i)
#     lst = "".join(lst)
#     return lst
#
#
# some_string = input()
# print(removing_all_vowels(some_string))

##################
# def removing_all_vowels(simple_string):
#     return "".join([char for char in simple_string if char not in "aeiouAEIOU"])
#
#
# some_string = input()
# print(removing_all_vowels(some_string))
#################

text = input()
vowels = ["a", "o", "u", "e", "i"]
result = [char for char in text if char.lower() not in vowels]
print("".join(result))
