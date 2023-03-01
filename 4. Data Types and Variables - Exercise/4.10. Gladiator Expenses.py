loss_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0
number_of_shield_repairs = 0

for i in range(1, loss_fights + 1):
    if i % 2 ==0:
        total_expenses += helmet_price
    if i % 3 ==0:
        total_expenses += sword_price
        if i % 2 == 0:
            total_expenses += shield_price
            number_of_shield_repairs += 1
            if number_of_shield_repairs % 2 ==0:
                total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
