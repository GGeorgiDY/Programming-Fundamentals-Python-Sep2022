def total_price(product, quantity, cash):
    if product == "coffee":
        cash = 1.50
    elif product == "coke":
        cash = 1.40
    elif product == "water":
        cash= 1.00
    elif product == "snacks":
        cash = 2.00
    result = cash * quantity
    return(f"{result:.2f}")

product = input()
quantity = int(input())
cash = 0
print(total_price(product, quantity, cash))
