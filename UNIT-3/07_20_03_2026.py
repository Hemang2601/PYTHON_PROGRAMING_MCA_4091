class Student:
    def student_info(self):
        print("This is Student class")

class Course:
    def course_info(self):
        print("This is Course class")

class Marks:
    def marks_info(self):
        print("This is Marks class")

class Result(Student, Course, Marks):
    def result_info(self):
        print("This is Result class")


r1 = Result()
r1.student_info()
r1.course_info()
r1.marks_info()
r1.result_info()

print("\nMethod Resolution Order (MRO):")
for cls in Result.__mro__:
    print(cls)