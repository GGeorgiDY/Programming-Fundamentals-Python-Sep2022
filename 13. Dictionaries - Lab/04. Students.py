students_dict = {}
command = input()
while ":" in command:
    info = command.split(":")
    name, id, course = info[0], info[1], info[2]
    if course not in students_dict:
        students_dict[course] = {} #тук можеш да го направиш и с [] ако имаш дублажи на имената
    students_dict[course][id] = name
    command = input()

course = ' '.join(command.split("_")) #правим programming_basics да стане programming basics
#course = course.replace("_", " ") и така става горния ред
for key, value in students_dict.items():
    if key == course:
        for id, name in value.items():
            print(f"{name} - {id}")