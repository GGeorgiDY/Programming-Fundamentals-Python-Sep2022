budget = int(input())
total_expenses = 0

command = input()
while command != "End":
    total_expenses += int(command)
    if budget - total_expenses < 0:
        print("You went in overdraft!")
        break
    command = input()

if budget - total_expenses >= 0:
    print("You bought everything needed.")
