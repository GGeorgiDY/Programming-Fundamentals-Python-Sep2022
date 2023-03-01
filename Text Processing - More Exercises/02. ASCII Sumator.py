first_character = input()
second_character = input()
random_string= input()
sum_of_all_characters = 0

first_character = ord(first_character)
second_character = ord(second_character)
for i in random_string:
    i = ord(i)
    if first_character < i < second_character:
        sum_of_all_characters += i

print(sum_of_all_characters)