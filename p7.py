class vehicle:
    color="White"
    price=600000

    def show(self):
        print("Vehicle Details are:\nColor: "+ self.color+"\nPrice: "+str(self.price))

class bike:
    color="black"
    price=80000
def show(self):
        print("Bike Details are:\nColor: "+ self.color+"\nPrice: "+str(self.price))

v1=vehicle()
b1=bike()

v1.show()