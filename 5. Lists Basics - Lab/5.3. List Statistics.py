number = int(input())
positive_list = []
negative_list = []
count_positive = 0
sum_negative = 0

for i in range(number):
    new_input = int(input())
    if new_input >= 0:
        positive_list.append(new_input)
        count_positive += 1
    else:
        negative_list.append(new_input)
        sum_negative += new_input

print(positive_list)
print(negative_list)
print(f"Count of positives: {count_positive}")
print(f"Sum of negatives: {sum_negative}")
