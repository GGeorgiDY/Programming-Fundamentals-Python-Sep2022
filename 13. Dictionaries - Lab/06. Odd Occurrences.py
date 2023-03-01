#Java C# PHP PHP JAVA C java ни е инпута
# трябва да ни върне тези думи, които ги има нечетен брой пъти в списъка

# from collections import defaultdict
#
# words = input().split(" ")
# counter_of_words = defaultdict(int)
#
# for i in words:
#     counter_of_words[i.lower()] += 1
#
# print(' '. join(i for i, count in counter_of_words.items() if count % 2 != 0))

words = input(). split(" ")
dict = {}

for i in words:
    word_lower = i.lower()
    if word_lower not in dict:
        dict[word_lower] = 0
    dict[word_lower] += 1

print(dict)

for k, v in dict.items():
    if v % 2 != 0:
        print(k, end=" ")





