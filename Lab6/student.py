class Student:
    def __init__(self,name,id,major):
        #attribute of student class
        self.name = name
        self.id = id
        self.major = major
    def student_profile(self):
        print(f'STD Name:{self.name} ID:{self.id} Major:{self.major}')

#create object of student class
if __name__ == "__main__" :
    std1 = Student("Puriwat Lertkrai","001","MIT")
    std1.student_profile()

    std2 = Student("Piyapong Seananut","002","AC")
    std2.student_profile()

    std1.major = "LM"
    std1.student_profile()



