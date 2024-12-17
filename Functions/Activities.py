def BasicFunction():
    a = 5 + 5
    b = 2 - 1

    print(f"5 + 5 is {a} \n 2 - 1 is {b}")

def SimpleInputs():
    name = input("What is your name? ")
    age = input("How old are you? ")
    city = input("Where do you live? ")

    print("\nHello,", name, "!")
    print("You are", age, "years old and live in", city + ".")  

def Addition():
    number1 = eval(input("Enter a number: "))
    number2 = eval(input("Enter a number: "))
    print(f"The sum of {number1} + {number2} is {number1 + number2}")

def AssingOpp():
    a = 1
    print(a)

    a += 2
    print(a)

    a -=1
    print(a)

def AssingVar():
    x = 5
    print(f"{x}")

    x = x + 10
    print(f"{x}")

    x += 15
    print(f"{x}")

def Diamond():
    diamond = 0
    miner = input("What is your name: ")
    isDiamond = input("Is your mineral Diamond: ")

    if isDiamond.lower() == "yes":
        Diamond += 1
        print(f"Hello {miner}, your Diamond is {diamond}")
    else:
        print(f"Hello {miner}, your Diamond is {diamond}")

def Password():
    password = str(input("Enter your password: "))

    if password.lower() == "secret":
        print("Enjoy!")
        print("Access Granted")
    elif password.lower() == "pogiako123":
        print("The confidence")
        print("Access Granted")
    else:
        print("Wrong Password, Access Denied")
        print("Thank your for using the program.")

def Age():   
    age = int(input("Enter your age: "))

    if 1 <= age <= 7:
        print("You are a Toddler")
    elif 8 <= age <= 13:
        print("You are in a PreTeen")
    elif 14 <= age <= 18:
        print("You are a Teenager")
    elif 19 <= age <= 31:
        print("You are in Early Adulthood")
    elif 32 <= age <= 45:
        print("You are in Middle Adulthood")
    elif 46 <= age <= 59:
        print("You are in Post Adulthood")
    elif age >= 60:
        print("You are a Senior Citizen")
    else:
        print("Invalid age")

def StudentLevel():
    name = input("Enter your name: ")
    Student = input("Are you a current student of DLL (yes / no): ")

    if Student.lower() == "yes":
        yearLevel = input("What year are you currently enrolled on? \nF - Freshmen\nS - Sophomore\nJ - Junior\nSN - Senior\n")
        if yearLevel.lower() == "f":
            print(f"Hi {name}, You are a Freshmen in DLL")
        elif yearLevel.lower() == "s":
            print(f"Hi {name}, You are a Sophomore in DLL")
        elif yearLevel.lower() == "j":
            print(f"Hi {name}, You are a Junior in DLL")
        elif yearLevel.lower() == "SN":
            print(f"Hi {name}, You are a Freshmen in DLL")
    else:
        print("Thank your for using the system.")

def CountingFive():
    for x in range(1,6):
        print(x)

def TwoSFourS():
    for x in range(10, 1, -1):
        print(x)

    print()

    for x in range(10, 2, -2):
        print(x)

def Factorial():
    fac = 1
    num = int(input("Enter a number: "))

    for x in range(1, num + 1):
        fac *= x

    print(f"The factorial of {num} is {fac}")

def AsterisksAndNumbers():
    for x in range(0, 7):
        print(x, end=" ")   
        for y in range(0, 7):
            print("*", end=" ")
    print() 

def Triangle():
    for x in range(0,11):
        print("", x, end = "")
        for y in range(0, x):
            print("*", end = "")
        print("\n")    

def ReverseTri():
    lines = 5 
    inv = 0
    for x in range(lines, 0, -1):
        print(" " * inv, end="")
        print("* " * x)
        inv += 2

def MultiTable():
    ask = int(input("Enter mumber of columns: "))
    for lines in range(1, ask + 1):
        print(f" {lines}", end="")
        for product in range(2, ask + 1):
            print(f"\t{product * lines}",end="")
        print()

def Triangle():
    ask = int(input("Enter number of triangles: "))

    for x in range(1, 6):
        for y in range(1, ask + 1):
            print("* " * x, end="  " * (6 - x))
        print()

def SevenNames():
    print(" Enter 7 names, type 'stop' to terminate names")

    for x in range(0,5):
        ask = input(" Enter your name: ")
        if ask.lower()== "stop":
            print(" Program terminated.")
            break
        else:
            print(f" Hello {ask}")

def UnliNames():
    print("Keep asking for name until user types 'stop'. Type 'stop' to terminate the program.")

    while True:
        name = input("Enter name: ")
        if name.lower() == "stop":
            break
        print(name)

#Do Activity 22 Tomorrow


    