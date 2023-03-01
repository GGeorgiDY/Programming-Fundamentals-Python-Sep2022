budget = float(input())
price_one_kg_flour = float(input())
price_one_pack_of_eggs = 0.75 * price_one_kg_flour
price_one_kg_of_milk = 1.25 * price_one_kg_flour
price_of_milk_for_bread = price_one_kg_of_milk / 4

total_price_per_bread = price_one_kg_flour + price_one_pack_of_eggs + price_of_milk_for_bread
bread_counter = 0
colored_eggs_counter = 0


while budget > total_price_per_bread:
    budget -= total_price_per_bread
    bread_counter += 1
    colored_eggs_counter += 3
    if bread_counter % 3 == 0:
        colored_eggs_counter -= bread_counter - 2
        if colored_eggs_counter < 0:
            colored_eggs_counter = 0

print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")
