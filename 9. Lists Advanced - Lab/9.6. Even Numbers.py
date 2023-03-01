#да маркираме индексите на всички четни числа
numbers = input().split(", ")
lst = list(map(int, numbers))                 #[3, 2, 1, 5, 8]
#new_list = [x for x in range(len(lst))]       #[0, 1, 2, 3, 4]
new_list = [x for x in range(len(lst)) if lst[x] % 2 == 0]  #[1, 4]
print(new_list)
