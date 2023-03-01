devisor = int(input())
boundary = int(input())

while boundary % devisor != 0:
    boundary -= 1
print(boundary)