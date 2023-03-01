def replace_all_occurrences(first_string, second_string):
    for i in first_string:
        i = ''.join(i)
        len_of_i = len(i)
        while i in second_string:
            second_string = second_string.replace(i, "*" * len_of_i)
    return second_string


first_string = input().split(", ")
long_text = input()
print(replace_all_occurrences(first_string, long_text))