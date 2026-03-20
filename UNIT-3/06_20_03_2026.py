class student:
    def __init__(self, name, age, gender, roll):
        self.name = name
        self.age = age
        self.gender = gender
        self.roll = roll
    def DisplayStudentInfo(self):
        print(f'Student Name    : {self.name}')
        print(f'Student Age     : {self.age}')
        print(f'Student Gender  : {self.gender}')
        print(f'Student Roll    : {self.roll}')

class Course(student):
    def __init__(self, name, age, gender, roll, coursename, duration, fee):
        super().__init__(name, age, gender, roll)
        self.coursename = coursename
        self.duration = duration
        self.fee = fee

    def DisplayCourseInfo(self):
        super().DisplayStudentInfo()
        print(f'Course Name     : {self.coursename}')
        print(f'Course Duration : {self.duration} hours')
        print(f'Course Fee      : {self.fee}')


s1 = Course(
    input('Enter Student Name : '),
    int(input('Enter Student Age : ')),
    input('Enter Student Gender : '),
    int(input('Enter Student Roll : ')),
    input('Enter Course Name : '),
    int(input('Enter Course Duration in Hours : ')),
    int(input('Enter Course Fee : '))
)

s1.DisplayCourseInfo()