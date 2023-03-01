number_of_characters = int(input())

total_sum = 0

for i in range(1, number_of_characters + 1):
    new_character = input()
    total_sum += ord(new_character)


print(f"The sum equals: {total_sum}")