number_of_electrons = int(input())
lst = []
sum_of_electrons_in_shell = 0
n = 1
while number_of_electrons != sum_of_electrons_in_shell:
    current_electrons_in_shell = 2 * n ** 2
    if sum_of_electrons_in_shell + current_electrons_in_shell > number_of_electrons:
        current_electrons_in_shell = number_of_electrons - sum_of_electrons_in_shell
    sum_of_electrons_in_shell += current_electrons_in_shell
    lst.append(current_electrons_in_shell)
    n += 1
print(lst)
