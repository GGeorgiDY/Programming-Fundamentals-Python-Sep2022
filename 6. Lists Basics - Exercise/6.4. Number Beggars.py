string_of_integers = input().split(", ")
count_of_beggars = int(input())

beggar_counter = 0
lst = []
final_list = []

for i in string_of_integers:
    lst.append(int(i))

while beggar_counter < count_of_beggars:
    sum_of_money = 0
    for i in range(beggar_counter, len(lst), count_of_beggars):
        sum_of_money += lst[i]
    final_list.append(sum_of_money)
    beggar_counter += 1

print(final_list)