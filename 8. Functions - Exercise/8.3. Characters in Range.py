def my_function(character1, character2):
    value_of_character1 = ord(character1)
    value_of_character2 = ord(character2)
    lst = []
    for i in range(value_of_character1 + 1, value_of_character2):
        new_sign = chr(i)
        lst.append(new_sign)
    return lst


first_sign = input()
second_sign = input()
result = my_function(first_sign,second_sign)
print(' '.join(result)) # това (join) ми преобразува лист-а в някаква поредица
# print(*result) това е другият начин за разпакетиране на лист