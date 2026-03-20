class student():

    def AddStudent(self,name,age,rollno,gender):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.gender = gender
    def DisplayStudent(self):
        print('Student Name : ',self.name)
        print('Student Age : ',self.age)
        print('Student Roll No : ',self.rollno)
        print('Student Gender : ',self.gender)


s1=student()
name = input('Enter Student Name : ')
age = input('Enter Student Age : ')
rollno = input('Enter Student Roll No : ')
gender = input('Enter Student Gender : ')
s1.AddStudent(name,age,rollno,gender)
s1.DisplayStudent()

