class Person:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def display_info(self):
        print(f'ID: {self.id} Name: {self.name} Age: {self.age}')

class Student(Person):
    def __init__(self,id,name,age,sid,major,gpa):
        super().__init__(id,name,age)
        self.sid = sid
        self.major = major
        self.gpa = gpa
    def display_info(self):
        super().display_info()
        print(f'SID: {self.sid} Major: {self.major} GPA: {self.gpa}')

#create object
p1 = Person("P001","Sam",37)
s1 = Student("P002","Panupong",24,"STD001","MIT",3.00)

for x in [p1,s1]:
    x.display_info()
