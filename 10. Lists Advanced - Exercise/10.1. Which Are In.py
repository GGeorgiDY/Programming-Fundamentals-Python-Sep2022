first_sequence = input().split(", ")
second_sequence = input().split(", ")
# substrings = []
#
# for first_word in first_sequence:
#     for second_word in second_sequence:
#         if first_word in second_word and first_word not in substrings:
#             substrings.append(first_word)
#             break

substrings = [first for first in first_sequence if any(first in second for second in second_sequence)]
# in any -> итератор, който проверява дали е True или False. Т.е. проверява дали поне едно е вярно

print(substrings)
