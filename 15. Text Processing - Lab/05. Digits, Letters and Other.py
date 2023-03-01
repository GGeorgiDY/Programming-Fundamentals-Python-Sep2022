# data = input()
# digits = ""
# letters = ""
# others = ""
# for i in data:
#     if i.isdigit():
#         digits += i
#     elif i.isalpha():
#         letters = ""
#         letters += i
#     else:
#         others += i
#
# print(digits)
# print(letters)
# print(others)

def get_digits(data):
    return "".join(str(i) for i in data if i.isdigit())


def get_lettes(data):
    return "".join(str(i) for i in data if i.isalpha())


def get_other_signs(data):
    return "".join(str(i) for i in data if not i.isalpha() and not i.isdigit())


data = input()
print(get_digits(data))
print(get_lettes(data))
print(get_other_signs(data))
