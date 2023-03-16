class Teacher:
    teacher_name = ""

class Department:
    department_name = ""
    teacher_list = list()

    def add_teacher(self,Teacher):
        self.teacher_list.append(Teacher)
    def display_teacher(self):
        print(f'Teacher in {self.department_name}:')
        for x in self.teacher_list:
            print(x.teacher_name)

# create object
# d1 = Department()
# d1.department_name = "MT"

t1 = Teacher()
t1.teacher_name = "Aj.Sam"
t2 = Teacher()
t2.teacher_name = "Aj.Ton"

# d1.add_teacher(t1)
# d1.display_teacher()
#
# d1.add_teacher(t2)
# d1.display_teacher()

print(t1.teacher_name)

