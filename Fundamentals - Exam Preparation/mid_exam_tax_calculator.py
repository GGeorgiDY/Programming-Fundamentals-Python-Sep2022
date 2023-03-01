import math
vechicles = input().split(">>")
total_of_total_tax = 0
for car in vechicles:
    total_tax = 0
    my_car = car.split(" ")
    car_type = my_car[0]
    years_the_tax_should_be_paid = int(my_car[1])
    kilometres_traveled = int(my_car[2])
    if car_type == "family" or car_type == "heavyDuty" or car_type == "sports":
        if car_type == "family":
            index = math.floor(kilometres_traveled / 3000)
            total_tax = index * 12 + (50 - years_the_tax_should_be_paid * 5)
            total_of_total_tax += total_tax
            print(f"A {car_type} car will pay {total_tax:.2f} euros in taxes.")
        if car_type == "heavyDuty":
            index = math.floor(kilometres_traveled / 9000)
            total_tax = index * 14 + (80 - years_the_tax_should_be_paid * 8)
            total_of_total_tax += total_tax
            print(f"A {car_type} car will pay {total_tax:.2f} euros in taxes.")
        if car_type == "sports":
            index = math.floor(kilometres_traveled / 2000)
            total_tax = index * 18 + (100 - years_the_tax_should_be_paid * 9)
            total_of_total_tax += total_tax
            print(f"A {car_type} car will pay {total_tax:.2f} euros in taxes.")
    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total_of_total_tax:.2f} euros in taxes.")
