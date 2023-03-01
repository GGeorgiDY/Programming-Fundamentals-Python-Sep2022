key = int(input())
number_of_lines = int(input())
lst = []

for i in range(number_of_lines):
    letter = input()
    number_in_letter = ord(letter)
    number_in_letter += key
    letter = chr(number_in_letter)
    lst.append(letter)

lst = "".join(lst)
print(lst)