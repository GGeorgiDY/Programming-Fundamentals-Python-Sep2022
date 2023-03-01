import operator

my_dictionary = {}
final_dictionary = {}

while True:
    command = input()
    if command == "end of contests":
        break

    command = command.split(":")
    contest = command[0]
    password_for_contest = command[-1]
    my_dictionary[contest] = {"password_for_contest": password_for_contest}

# {'Part One Interview': {'password_for_contest': 'success'},
# 'JS Fundamentals': {'password_for_contest': 'fundExam'},
# 'C# Fundamentals': {'password_for_contest': 'fundPass'},
# 'Algorithms': {'password_for_contest': 'fun'}}

while True:
    other_commands = input()
    if other_commands == "end of submissions":
        break

    other_commands = other_commands.split("=>")
    contest = other_commands[0]
    password = other_commands[1]
    username = other_commands[2]
    points = int(other_commands[3])

    if contest in my_dictionary:
        if password in my_dictionary[contest]["password_for_contest"]:
            if username not in final_dictionary:
                final_dictionary[username] = {}
                if contest not in final_dictionary[username]:
                    final_dictionary[username][contest] = points
                else:
                    if points > int(final_dictionary[username][contest]):
                        final_dictionary[username][contest] = points
            else:
                if contest not in final_dictionary[username]:
                    final_dictionary[username][contest] = points
                else:
                    if points > int(final_dictionary[username][contest]):
                        final_dictionary[username][contest] = points
        else:
            continue

#     print(final_dictionary)
# print(final_dictionary)

# {'Tanya': {'C# Fundamentals': 350, 'Algorithms': 380, 'Part One Interview': 220, 'JS Fundamentals': 400}, 'Nikola': {'Part One Interview': 120, 'C# Fundamentals': 200}}

# отдлу е кода който показва най-добрия кандидат
best_candidate = " "
current_rank = 0
best_candidate_rank = 0
for key, value in final_dictionary.items():
    # key => Tanya
    # value => {'C# Fundamentals': 350, 'Algorithms': 380, 'Part One Interview': 220, 'JS Fundamentals': 400}
    for i in value:  # 'C# Fundamentals, Algorithms, Part One Interview, JS Fundamentals
        current_rank += final_dictionary[key][i]
        if current_rank > best_candidate_rank:
            best_candidate_rank = current_rank
            best_candidate = key
    current_rank = 0
print(f"Best candidate is {best_candidate} with total {best_candidate_rank} points.")

# сортираме по key-ове
sorted_dictionary = dict(sorted(final_dictionary.items()))
# print(sorted_dictionary)
# {'Nikola': {'Part One Interview': 120, 'C# Fundamentals': 200}, 'Tanya': {'C# Fundamentals': 350, 'Algorithms': 380, 'Part One Interview': 220, 'JS Fundamentals': 400}}

# сортираме по values
for key, value in sorted_dictionary.items():
    value = dict(sorted(value.items(), key=operator.itemgetter(1), reverse=True))
    sorted_dictionary[key] = value
# print(sorted_dictionary)
# {'Nikola': {'C# Fundamentals': 200, 'Part One Interview': 120}, 'Tanya': {'JS Fundamentals': 400, 'Algorithms': 380, 'C# Fundamentals': 350, 'Part One Interview': 220}}


print("Ranking:")
for key, value in sorted_dictionary.items():
    print(key)
    for i in value:
        print(f"#  {i} -> {sorted_dictionary[key][i]}")

# Part One Interview:success
# JS Fundamentals:fundExam
# C# Fundamentals:fundPass
# Algorithms:fun
# end of contests
# C# Fundamentals=>fundPass=>Tanya=>350
# Algorithms=>fun=>Tanya=>380
# Part One Interview=>success=>Nikola=>120
# Java Basics Exam=>wrong_pass=>Teo=>400
# Part One Interview=>success=>Tanya=>220
# OOP Advanced=>password123=>Kay=>231
# C# Fundamentals=>fundPass=>Tanya=>250
# C# Fundamentals=>fundPass=>Nikola=>200
# JS Fundamentals=>fundExam=>Tanya=>400
# end of submissions

# Java Advanced:funpass
# Part Two Interview:success
# Math Concept:asdasd
# Java Web Basics:forrF
# end of contests
# Math Concept=>ispass=>Monika=>290
# Java Advanced=>funpass=>Simona=>400
# Part Two Interview=>success=>Drago=>120
# Java Advanced=>funpass=>Petyr=>90
# Java Web Basics=>forrF=>Simona=>280
# Part Two Interview=>success=>Petyr=>0
# Math Concept=>asdasd=>Drago=>250
# Part Two Interview=>success=>Simona=>200
# end of submissions
