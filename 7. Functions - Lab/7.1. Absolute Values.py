# number = input().split(" ")
# lst = []
#
# for i in number:
#     lst.append(abs(float(i)))
# print(lst)

numbers = list(map(float, input().split(" ")))
result = [abs(num) for num in numbers]
print(result)