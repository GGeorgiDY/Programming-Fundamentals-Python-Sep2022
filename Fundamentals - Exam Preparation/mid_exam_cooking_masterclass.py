import math
budget = float(input())
students = int(input())
price_for_package_of_flour = float(input())
price_for_single_egg = float(input())
price_for_single_apron = float(input())

total_price_flour = 0
total_price_egg = 0
total_price_apron = 0
flour_package_counter = 0

for student in range(1, students + 1):
    flour_package_counter += 1
    if flour_package_counter % 5 != 0:
        total_price_flour += price_for_package_of_flour
    total_price_egg += price_for_single_egg * 10

total_price_apron = price_for_single_apron * math.ceil(students * 1.2)

total_price = total_price_egg + total_price_flour + total_price_apron
difference = abs(budget - total_price)
if total_price > budget:
    print(f"{difference:.2f}$ more needed.")
else:
    print(f"Items purchased for {total_price:.2f}$.")

