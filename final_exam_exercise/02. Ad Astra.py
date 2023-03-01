# import math
# import re
#
# total_calories = 0
# calories_per_day = 2000
# my_dict = {}
# # pattern = r"(^#|\|)([A-Z][a-z]+)(\1)((\d{2})/(\d{2})/(\d{2}))(\1)(\d+)\b"
# # pattern = r"(#|\|)(([A-Z][a-z]+\s?)*)(\1)(\d{2}/\d{2}/\d{2})(\1)(\d+)"
# pattern = r"([#|\|])(?P<item>[A-Za-z ]+)\1(?P<date>[\d]{2}\/[\d]{2}\/[\d]{2})\1(?P<cal>[\d]+)\1"
# data = input()
# result = re.findall(pattern, data)
# for i in result:
#     item_name = i[1]
#     expiration_date = str(i[4])
#     calories = int(i[6])
#     if calories > 10000:
#         continue
#     total_calories += calories
#     my_dict[item_name] = {1: expiration_date, 2: calories}
#
# days = math.floor(total_calories / calories_per_day)
# print(f"You have food to last you for: {days} days!")
# for k, v in my_dict.items():
#     print(f"Item: {k}, Best before: {v[1]}, Nutrition: {v[2]}")

# горния код е грешен.... 33/100

#Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|

import re

text = input()
pattern = re.compile(r"([#|\|])(?P<item>[A-Za-z ]+)\1(?P<date>[\d]{2}\/[\d]{2}\/[\d]{2})\1(?P<cal>[\d]+)\1")
result = re.finditer(pattern, text)

cal = 0
food_per_day = 2000
products = list()
for item in result:
    cal += int(item['cal'])
    products.append(f"Item: {item['item']}, Best before: {item['date']}, Nutrition: {item['cal']}")
days = cal // food_per_day
print(f"You have food to last you for: {days} days!")

for prints in products:
    print(prints)