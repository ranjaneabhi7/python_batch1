class classA:
    no1=10
    no2=20
    def arithmetic(self):
        print("Result = "+str(self.no1+self.no2))

class classB(classA):
    def arithmetic(self):
        print("Result = "+str(self.no1-self.no2))

a1=classA()
a1.arithmetic()

b1=classB()
b1.arithmetic()