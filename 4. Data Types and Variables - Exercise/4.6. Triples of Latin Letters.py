number = int(input())

for i in range(0, number):
    for y in range(0, number):
        for u in range(0, number):
            print(f"{chr(97 + i)}{chr(97 + y)}{chr(97 + u)}")