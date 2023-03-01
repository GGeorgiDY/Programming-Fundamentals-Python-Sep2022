number_of_lines = int(input())
opening_brackets = 0
closing_brackets = 0

for i in range(number_of_lines):
    new_line = input()
    if new_line == "(":
        opening_brackets += 1
    elif new_line == ")":
        closing_brackets += 1

if opening_brackets == closing_brackets:
    print("BALANCED")
else:
    print("UNBALANCED")

