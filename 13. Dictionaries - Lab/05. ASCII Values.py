# a, b, c, a

data = input().split(', ')
# lst = []
#
# for i in data:
#     my_letter = i
#     letters_number = ord(i)
#     lst.append(letters_number)
#     my_dict = dict(zip(data, lst))

my_dict = {key:ord(key) for key in data}
print(my_dict)
