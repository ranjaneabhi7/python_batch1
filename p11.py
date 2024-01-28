class College:
    college_name=""

    def input(self):
        self.college_name=input("Enter College Name: ")

class Department(College):
    dept_name=""
    def input(self):
        super().input()
        self.dept_name=input("Enter Department Name: ")

class Faculty(Department):
    faculty_name=""
    def input(self):
        super().input()
        self.faculty_name=input("Enter Faculty Name: ")

obj=Faculty()
obj.input()