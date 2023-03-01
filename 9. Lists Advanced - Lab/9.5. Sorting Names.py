#да сортираме по низходящ ред спрямо броя на буквите във всеки елемент от списъка
names = input().split(", ")
result = sorted(names, key=lambda item: (-len(item), item))
print(result)

