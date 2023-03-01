number_of_orders = int(input())

current_price = float(0)
total_price = float(0)

for i in range(1, number_of_orders +1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    current_price = price_per_capsule * days * capsules_needed_per_day

    if price_per_capsule < 0.01 or price_per_capsule > 100 or days < 1 or days > 31 or capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue
    else:
        print(f"The price for the coffee is: ${current_price:.2f}")
        total_price += current_price

print(f"Total: ${total_price:.2f}")

