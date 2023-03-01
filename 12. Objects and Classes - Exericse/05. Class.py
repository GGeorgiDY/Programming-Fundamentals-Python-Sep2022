class Class:

    def __init__(self, class_name):
        self.class_name = class_name
        students_count = 22
        self.students_count = students_count
        students = []
        grades = []
        self.students = students
        self.grades = grades

    def add_student(self, name: str, grade: float):
        if self.students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        sum_of_all_grades = 0
        for x in self.grades:
            sum_of_all_grades += x
        my_average_grade = sum_of_all_grades / len(self.grades)
        return my_average_grade

    def __repr__(self):
        return f"The students in {self.class_name}: {', '.join(self.students)}. Average grade: {self.get_average_grade():.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)