
# student app
from student import Student

if __name__ == "__main__" :

    student_list = []
    x = int(input("Enter your number of student: "))
    for i in range(x):
        print(f'Student {i+1}')
        n = input("Enter student name: ")
        id = input("Enter student id: ")
        m = input("Enter student major: ")

        std = Student(n,id,m)
        student_list.append(std)
        print(f'Student {i + 1} had been saved.')

    print("Display all student info: ")
    for x in student_list:
        x.student_profile()

