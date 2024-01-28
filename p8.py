class property:
    type=""
    price=""

    def rent(self):
        t=""
        print("\nGreat, We have lots of properties on rent...")
        t=int(input("\nPlease select type of property:\n1.Flat\n2.Bunglow\n"))
        match t:
            case 1:
                print("\nGreat, We have lots of flats available on rent...")
                f=int(input("\nPlease select flat type:\n0: 1HK\n1: 1BHK\n2: 2BHK\n3: 3BHK\n"))
                match f:
                    case 0:
                        self.type="1 HK"
                    case 1:
                        self.type="1 BHK"
                    case 2:
                        self.type="2 BHK"
                    case 3:
                        self.type="3 BHK"
                print("Nice! You want " + self.type + " flat on rent. We will call you soon. Thank you...")
            case 2:
                print("\nGreat, We have lots of Bunglow available on rent...")
                f=int(input("\nPlease select Bunglow type:\n1: 1BHK\n2: 2BHK\n3: 3BHK\n"))
                match f:
                    case 1:
                        self.type="1 BHK"
                    case 2:
                        self.type="2 BHK"
                    case 3:
                        self.type="3 BHK"
                print("Nice! You want " + self.type + "Bunglow on rent. We will call you soon. Thank you...")

    def buy(self, t, p):
        self.type=t
        self.price=p

    def show(self):
        print("Property Details: \n Type: "+ self.type + "\n Price: " + str(self.price))

p1=property()
option=0
print("\nHello, Welcome to Property Company...")
while(1):
    option=int(input("Please select what type of property you are looking:\n1.Rent\n2.Buy\n3.Others\n "))
    if option == 1:
        p1.rent()
        break
    elif option==2:
        p1.buy()
        break
    elif option==3:
        print("\nWe will contact you soon...")
        break
    else:
        print("\nInvalid Choice\nPlease try again...")
    break