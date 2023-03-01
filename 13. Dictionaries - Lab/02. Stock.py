# това са ни input данните
#cheese 10 bread 5 ham 10 chocolate 3
#jam cheese ham tomatoes
data = input().split()
searched_products = input().split()

product_dict = {}
for i in range(0, len(data), 2):
    product = data[i]
    value = data[i + 1]
    product_dict[product] = int(value)

for i in searched_products:
    if i in product_dict.keys():
        print(f"We have {product_dict[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")