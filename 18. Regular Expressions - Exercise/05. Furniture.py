import re

patern = r">>([A-Za-z]+)<<(\d+\.?\d*)\!(\d+)" #? означава че може и да го има, може и да го няма
total_cost = 0
lst = []
while True:
    command = input()
    if command == "Purchase":
        break
#     result = re.findall(patern, command)
#     for i in result:
#         lst.append(i[0])
#         total_cost += float(i[1])*int(i[2])
# print("Bought furniture:")
# for i in lst:
#     print(f"{i}")
# print(f"Total money spend: {total_cost:.2f}")
# и горният код работи

    result = re.search(patern, command)
    if result:
        #хубаво е винаги да проверяваш дали има нач, защото при крив ход това не работи
        # furniture = match.group(1)
        # price = match.group(2)
        # quantity = match.group(3)
        furniture, price, quantity = result.groups()
        lst.append(furniture)
        total_cost += float(price)*int(quantity)
print("Bought furniture:")
#print('\n'.join())
for i in lst:
    print(f"{i}")
print(f"Total money spend: {total_cost:.2f}")


# >>Sofa<<312.23!3
# >>TV<<300!5
# >Invalid<<!5
# Purchase
