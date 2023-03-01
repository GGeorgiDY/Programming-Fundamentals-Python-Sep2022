my_dict = {}
while True:
    command = input()
    if command == "stop":
        break

    resource = command
    quantity = int(input())
    if resource not in my_dict:
        my_dict[resource] = quantity
    else:
        my_dict[resource] += quantity

for key, value in my_dict.items():
    print(f"{key} -> {value}")

# gold
# 155
# silver
# 10
# copper
# utils
# gold
# 15
# stop

