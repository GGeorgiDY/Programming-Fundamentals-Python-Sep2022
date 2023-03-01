number = int(input())
prime = True
for i in range(2, number):
    for y in range(2, number):
        if i * y == number:
            prime = False
            print("False")
            break
        if not prime:
            break
    if not prime:
        break

if prime:
    print("True")


