contests_dictionary = {}
submissions_dictionary = {}
while True:
    contests = input()
    if contests == 'end of contests':
        break
    contests = contests.split(":")
    contest = contests[0]
    password_for_contest = contests[1]
    if contest not in contests_dictionary.keys():
        contests_dictionary[contest] = password_for_contest
    contests_dictionary[contest] = password_for_contest

while True:
    submissions = input()
    if submissions == 'end of submissions':
        break

    submissions = submissions.split("=>")
    contest = submissions[0]
    password = submissions[1]
    username = submissions[2]
    points = int(submissions[3])
    if contest in contests_dictionary.keys():
        if password in contests_dictionary[contest]:
            if contest not in submissions_dictionary:
                submissions_dictionary[contest] = {}
            if username not in submissions_dictionary[contest]:
                submissions_dictionary[contest][username] = points
            else:
                if submissions_dictionary[contest][username] < points:
                    submissions_dictionary[contest][username] = points

print(submissions_dictionary)


