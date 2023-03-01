# 3
# cute
# adorable
# cute
# charming
# smart
# clever

# the_count_of_the_words = int(input())
# dict = {}
#
# for i in range(the_count_of_the_words):
#     word = input()
#     synonym = input()
#     if word in dict:
#         dict[word].append(synonym)
#     else:
#         dict[word] = [synonym]
#
# # print(dict)
# data = [f"{word} - {', '.join(synonym)}" for word, synonym in dict.items()]
# # print(data)
# print('\n'.join(data))

from collections import defaultdict

synonyms = defaultdict(list)
number = int(input())

for _ in range(number):
    word, synonym = input(), input()
    synonyms[word].append(synonym)

data = [f"{word} - {', '.join(synonym)}" for word, synonym in synonyms.items()]
print('\n'.join(data))