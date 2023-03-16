class Student:
    def __init__(self, name, department,major):
        self.name = name
        self.department = department
        self.major = major

    def introduce(self):
        print(f'My name is {self.name}, '
              f'I am a student at {self.department} '
              f'and studying in {self.major} major.')
