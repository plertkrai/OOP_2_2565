class Teacher:
    teacher_name = ""
    advisee_student = list()

    def set_advisee(self,lst_student):
        self.advisee_student = lst_student
    def display_advisee(self):
        print(f'Teacher name: {self.teacher_name}')
        print("Advisee list: ")
        for x in self.advisee_student:
            print(x.student_name)

class Student:
    student_name = ""
    advisor = list()
    def set_advisor(self,lst_advisor):
        self.advisor = lst_advisor
    def display_advisor(self):
        print(f'Student name: {self.student_name}')
        print("Advisor list: ")
        for x in self.advisor:
            print(x.teacher_name)

# object Teacher
t1 = Teacher()
t1.teacher_name = "Puriwat Lertkrai"
t2 = Teacher()
t2.teacher_name = "Piyapong Seananut"
t3 = Teacher()
t3.teacher_name = "Pornprasert Thimsawat"
# object Student
s1 = Student()
s1.student_name = "Panupong"
s2 = Student()
s2.student_name = "Panuwat"

t1.set_advisee([s1,s2])
t1.display_advisee()

s1.set_advisor([t1,t2])
s1.display_advisor()
