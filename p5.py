def addition(no1, no2):
    sum=no1+no2
    print("Addition= " + str(sum))

def substraction(no1,no2):
    sub=no1-no2
    print("Subtraction = "+ str(sub))

def multiplication(no1, no2):
    mult = no1*no2
    print("Multiplacation = "+ str(mult))

def division(no1,no2):
    div = no1/no2
    print("Division = "+ str(div))

no1=int(input("Enter 1st no = "))
no2=int(input("Enter 2nd no = "))

while(1):
    operation=int(input("Please select your choice:\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Break\n"))
    if operation==1:
        addition(no1,no2)
    elif operation==2:
        substraction(no1,no2)
    elif operation==3:
        multiplication(no1,no2)
    elif operation==4:
        division(no1,no2)
    elif operation==5:
        print("Thank you...")
        break
    else:
        print("\nInvalid Choice")
    