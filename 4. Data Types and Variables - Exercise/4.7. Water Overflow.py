number_of_lines = int(input())
tank_capacity = 255
water_counter = 0
for i in range(number_of_lines):
    litres_of_water = int(input())
    if tank_capacity < litres_of_water:
        print("Insufficient capacity!")
        continue
    tank_capacity -= litres_of_water
    water_counter += litres_of_water
print(water_counter)




