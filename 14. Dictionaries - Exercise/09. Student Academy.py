my_dictionary = {}
the_next_pair_of_rows = int(input())
for pair in range(the_next_pair_of_rows):
    student_name = input()
    student_grade = float(input())
    if student_name not in my_dictionary:
        my_dictionary[student_name] = []
        my_dictionary[student_name].append(student_grade)
    else:
        my_dictionary[student_name].append(student_grade)

for i in my_dictionary:
    average_score = sum(my_dictionary[i]) / len(my_dictionary[i])
    if average_score >= 4.50:
        print(f"{i} -> {average_score:.2f}")

# 5
# Amanda
# 3.5
# Amanda
# 4
# Rob
# 5.5
# Christian
# 5
# Robert
# 6


