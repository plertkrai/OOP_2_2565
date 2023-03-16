class University:
    u_name = ""
    department_list = list()

    def get_department(self):
        d1 = Department()
        d1.d_name = "MT"
        d2 = Department()
        d2.d_name = "Sci"

        self.department_list = [d1,d2]
    def display_department(self):
        print(f"Department in {self.u_name}: ")
        for x in self.department_list:
            print(f'{x.d_name}')

class Department:
    d_name = ""


# create object
u = University()
u.u_name = "RUTS"
u.get_department()
u.display_department()





