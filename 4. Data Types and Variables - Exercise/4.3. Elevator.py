import math
persons = int(input())
capacity = int(input())

# result = 0
# if persons > capacity:
#     for i in range(capacity, persons + 1, capacity):
#         result += 1
# else:
#     result += 1
#
# if persons % capacity != 0 and persons > capacity:
#     result += 1
#
# print(result)

result = math.ceil(persons / capacity)
print(result)