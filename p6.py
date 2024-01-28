class student:
    marks=88
    name="Abhijeet"
    trade="IT"

    def show(self):
        print("Students\nName: "+self.name+"\nTrade: "+ self.trade+"\nMarks: "+str(self.marks))
    
    def update(self, m, n, t):
        self.marks=m
        self.trade="Info Tech"
        self.name="Abhijit"

class employee:
    name="Deepak"
    trade="ETC"
    marks=80
    def show(self):
        print("Employee\nName: "+self.name+"Trade: "+ self.trade+"Marks: "+self.marks)

s1=student()
e1=employee()

s1.show()
s1.update(70, "Abhijit", "Info Tech")
