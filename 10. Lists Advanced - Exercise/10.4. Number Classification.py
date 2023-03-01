numbers = input().split(", ")

# positive_numbers = ", ".join([x for x in numbers if int(x) >= 0])
# negative_numbers = ", ".join([x for x in numbers if int(x) < 0])
# even_numbers = ", ".join([x for x in numbers if int(x) % 2 == 0])
# odd_numbers = ", ".join([x for x in numbers if int(x) % 2 != 0])
#
# print(f"Positive: {positive_numbers}")
# print(f"Negative: {negative_numbers}")
# print(f"Even: {even_numbers}")
# print(f"Odd: {odd_numbers}")


def positive_numbers(sum_numbers):
    return[x for x in sum_numbers if int(x) > 0]


def negative_numbers(sum_numbers):
    return [x for x in sum_numbers if int(x) < 0]


def odd_numbers(sum_numbers):
    return [x for x in sum_numbers if int(x) % 2 != 0]


def even_numbers(sum_numbers):
    return [x for x in sum_numbers if int(x) % 2 == 0]


print(f"Positive: {', '.join (positive_numbers(numbers))}")
print(f"Positive: {', '.join (negative_numbers(numbers))}")
print(f"Positive: {', '.join (even_numbers(numbers))}")
print(f"Positive: {', '.join (odd_numbers(numbers))}")