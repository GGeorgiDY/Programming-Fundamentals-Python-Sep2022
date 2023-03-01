# инпута ни е:
# bread 10 butter 4 sugar 9 jam 12

data = input().split(" ")

# може да се реши с for loop:
# products_dict = {}
# for i in range(0, len(data), 2):
#     products_dict[data[i]] = int(data[i + 1])

# може да се реши и с dict comprehension
#products_dict = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}

products_dict = {}
for i in range(0, len(data), 2):
    key = data[i]
    value = data[i + 1]
    products_dict[key] = int(value)

print(products_dict)