class Student:
    name=""
    roll_no=""
    marks=""

    def input_data(self):
        self.name=input("Enter Students Name: ")
        self.roll_no=int(input("Enter students Roll No: "))
        self.marks=int(input("enter Students Marks: "))

    def show(self):
        print("Students Details are:\nName: "+self.name + "\nRoll No: "+ str(self.roll_no) + "\nMarks: "+ str(self.marks))
    
s1=Student()
s1.input_data()
s1.show()