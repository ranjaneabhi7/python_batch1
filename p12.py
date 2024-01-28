class classA:
    def method1(self):
        print("Class A method")

class classB(classA):
    def method1(self):
        print("Class B method")

a1=classA()
a1.method1()

b1=classB()
b1.method1()