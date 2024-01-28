class Numbers:
    no1=""
    no2=""

    def input_data(self):
        self.no1=int(input("Enter 1st no = "))
        self.no2=int(input("Enter 2nd no = "))

class Arithmetic(Numbers):
    def addition(self):
        print("Addition = "+str(self.no1+self.no2))
    
    def substraction(self):
        print("Substraction = "+str(self.no1-self.no2))
    
    def multiplication(self):
        print("Multiplication = "+str(self.no1*self.no2))
    
    def division(self):
        print("Division = "+str(self.no1/self.no2))
