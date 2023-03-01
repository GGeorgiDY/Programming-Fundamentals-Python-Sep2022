number_of_cars = int(input())

my_dictionary = {}
for i in range(number_of_cars):
    cars_themselves = input()
    cars_themselves = cars_themselves.split("|")
    car = cars_themselves[0]
    mileage = int(cars_themselves[1])
    fuel = int(cars_themselves[2])
    my_dictionary[car] = {'mileage': mileage, 'fuel': fuel}
# print(my_dictionary)
# {'Audi A6': {'mileage': 38000, 'fuel': 62}, 'Mercedes CLS': {'mileage': 11000, 'fuel': 35}, 'Volkswagen Passat CC': {'mileage': 45678, 'fuel': 5}}

while True:
    command = input()
    if command == "Stop":
        break

    command = command.split(" : ")
    action = command[0]

# за подадената кола, шофирай подадените км, като увеличиш километража и намалиш резервоара с подадените литри
# трябва да внимаваш дали има достатъчно гориво
# колата мине ли 100 000км трябва да я изтриеш
    if action == "Drive":
        vechicle = command[1]
        new_distance = int(command[2])
        new_fuel = int(command[3])
        if my_dictionary[vechicle]['fuel'] > new_fuel:
            my_dictionary[vechicle]['fuel'] -= new_fuel
            my_dictionary[vechicle]['mileage'] += new_distance
            print(f"{vechicle} driven for {new_distance} kilometers. {new_fuel} liters of fuel consumed.")
            if my_dictionary[vechicle]['mileage'] >= 100000:
                print(f"Time to sell the {vechicle}!")
                del my_dictionary[vechicle]
        else:
            print("Not enough fuel to make that ride")

# зареди колата с подадените литри бензин. Не може да има повече от 75 литра
    if action == "Refuel":
        vechicle = command[1]
        new_fuel = int(command[2])
        if my_dictionary[vechicle]['fuel'] + new_fuel > 75:
            new_fuel = 75 - my_dictionary[vechicle]['fuel']
            my_dictionary[vechicle]['fuel'] = 75
        else:
            my_dictionary[vechicle]['fuel'] += new_fuel
        print(f"{vechicle} refueled with {new_fuel} liters")

# намали километража на колата (не може да пада под 10 000).
    if action == "Revert":
        vechicle = command[1]
        new_mileage = int(command[2])
        mileage = my_dictionary[vechicle]['mileage']
        if mileage - new_mileage >= 10000:
            mileage = mileage - new_mileage
            my_dictionary[vechicle]['mileage'] = mileage
            print(f"{vechicle} mileage decreased by {new_mileage} kilometers")
        elif mileage - mileage >= 0:
            mileage = 10000
            my_dictionary[vechicle]['mileage'] = mileage

for key, value in my_dictionary.items():
    print(f"{key} -> Mileage: {my_dictionary[key]['mileage']} kms, Fuel in the tank: {my_dictionary[key]['fuel']} lt.")


# 3
# Audi A6|38000|62
# Mercedes CLS|11000|35
# Volkswagen Passat CC|45678|5
# Drive : Audi A6 : 543 : 47
# Drive : Mercedes CLS : 94 : 11
# Drive : Volkswagen Passat CC : 69 : 8
# Refuel : Audi A6 : 50
# Revert : Mercedes CLS : 500
# Revert : Audi A6 : 30000
# Stop
