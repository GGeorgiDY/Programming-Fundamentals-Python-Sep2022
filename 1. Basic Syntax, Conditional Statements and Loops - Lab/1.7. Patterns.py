number = int(input())
promenliva = 0
for i in range(1, number +1):
    promenliva = i * "*"
    print(promenliva)
for y in range(number -1, 0, -1):
    promenliva = y * "*"
    print(promenliva)