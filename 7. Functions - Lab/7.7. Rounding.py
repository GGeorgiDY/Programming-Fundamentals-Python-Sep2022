string_of_integers = input().split(" ")
lst = []
asd = 0
for i in string_of_integers:
    asd = round(float(i), 0)
    asd = int(asd)
    lst.append(asd)
print(lst)