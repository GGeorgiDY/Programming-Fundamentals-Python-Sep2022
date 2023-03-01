first_string, second_string = input().split(" ")
total_sum = 0
if len(first_string) > len(second_string):
    for i in range(len(second_string)):
        total_sum += int(ord(first_string[i])) * int(ord(second_string[i]))
    for i in range(len(second_string), len(first_string)):
        total_sum += int(ord(first_string[i]))

if len(first_string) < len(second_string):
    for i in range(len(first_string)):
        total_sum += int(ord(second_string[i])) * int(ord(first_string[i]))
    for i in range(len(first_string), len(second_string)):
        total_sum += int(ord(second_string[i]))

if len(first_string) == len(second_string):
    for i in range(len(first_string)):
        total_sum += int(ord(first_string[i])) * int(ord(second_string[i]))

print(total_sum)

# George Peter        52114
# 123 522             7647
# a aaaa              9700