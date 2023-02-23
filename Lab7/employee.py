class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.__salary = salary # private member

    def employee_info(self):
        print(f'Name: {self.name} position: {self.position} salary:{self.__salary}')

    # getter and setter method
    def get_salary(self):
        return self.__salary
    def set_salary(self,new_salary):
        self.__salary = new_salary


if __name__ == "__main__":
    # create object
    emp1 = Employee("SAM","Teacher",20000)
    emp1.employee_info()

    # change position
    emp1.position = "Project Manager"
    emp1.employee_info()
    # change salary
    emp1.__salary = 30000
    emp1.employee_info()
    # using name_mangling
    emp1._Employee__salary = 30000   #_classname__attribute
    emp1.employee_info()
    # using getter and setter method
    print(emp1.get_salary())
    emp1.set_salary(40000)
    print(emp1.get_salary())
    emp1.employee_info()