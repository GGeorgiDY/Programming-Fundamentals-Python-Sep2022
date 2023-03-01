# това са ни input данните
# bread: 4
# ham: 1
# bread: 1
# cheese: 2
# statistics

products_in_stock = {}

while True:
    command = input()
    if command == "statistics":
        break

    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])

    if product not in products_in_stock:
        products_in_stock[product] = quantity
    else:
        products_in_stock[product] += quantity

print('Products in stock:')
# product_representation = [f"- {i}: {str(products_in_stock[i])}" for i in products_in_stock]
# print('\n'.join(product_representation)
#или
# product_representation = [i for i in products_in_stock]
# for i in product_representation:
#     print(f"{i}: {products_in_stock[i]}")
#или
for product, quantity in products_in_stock.items():
    print(f"{product}: {quantity}")
print(f"Total Products: {len(products_in_stock)}")
print(f"Total Quantity: {sum(products_in_stock.values())}")
