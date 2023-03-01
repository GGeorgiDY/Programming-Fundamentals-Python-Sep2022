factor = int(input())
count = int(input())

counter = 0
factor_variable = 0
lst = []

# while counter < count:
#     factor_variable += factor
#     counter += 1
#     lst.append(factor_variable)

for i in range(1, count +1):
    lst.append(i*factor)

print(lst)

