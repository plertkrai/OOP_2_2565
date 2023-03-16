class Teacher:
    def __init__(self,name,department):
        self.name = name
        self.department = department

    def introduce(self):
        print(f'My name is {self.name}, I am a teacher at {self.department}')
