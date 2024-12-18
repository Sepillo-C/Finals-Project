def Diamond():
    print ("\t\t\t\t\t\t\t\t\t\t\t\t   * \n\t\t\t\t\t\t\t\t\t\t\t\t  *** \n\t\t\t\t\t\t\t\t\t\t\t\t ***** \n\t\t\t\t\t\t\t\t\t\t\t\t******* \n\t\t\t\t\t\t\t\t\t\t\t\t ***** \n\t\t\t\t\t\t\t\t\t\t\t\t  *** \n\t\t\t\t\t\t\t\t\t\t\t\t   *")

def Diamond_name():
    name = input ("What is your name? ---> ")
    print ("\t\t\t\t\t\t\t\t\t\t\t\t    * \n\t\t\t\t\t\t\t\t\t\t\t\t   *** \n\t\t\t\t\t\t\t\t\t\t\t\t  ***** \n\t\t\t\t\t\t\t\t\t\t\t\t ******* \n\t\t\t\t\t\t\t\t\t\t\t\t*Hi," + name + "* \n\t\t\t\t\t\t\t\t\t\t\t\t ******* \n\t\t\t\t\t\t\t\t\t\t\t\t  ***** \n\t\t\t\t\t\t\t\t\t\t\t\t   *** \n\t\t\t\t\t\t\t\t\t\t\t\t    *")

def biodata():
    Name = input("What is your Name? ")
    Gender = input("What is your Gender? ")
    Age = int(input("How old are you? "))
    City_Address = input("What is your City Address? ")
    Contact_Number = int(input("What is your Contact Number? "))
    Email_Address = input("What is your E-mail Address? ")
    DOB = input("When is your Birthday? (MM/DD/YYYY) ")
    POB = input("Place of Birth? ")
    Civil_Status = input("Are you Single, Married, Divorced? ")
    Citizenship = input("What is your Citizenship? ")
    Height = float(input("What is your Height? "))
    Weight = float(input("What is your Weight? "))
    Employed = input("Are you currently employed? (yes/no) ")

    Elementary = input("What is the name of your Elementary school? ")
    EYG = int(input("What year did you graduate Elementary? "))
    Highschool = input("What is the name of your Highschool? ")
    HYG = int(input("What year did you graduate Highschool? "))
    College = input("What is the name of your College? ")
    CYG = int(input("What year did you graduate College? "))
    Degree_Received = input("What degree did you receive in College? ")
    Special_Skills = input("Do you have any special skills? ")

    print("Personal Data:\n\tName: " + Name +
        "\n\tGender: " + Gender +
        "\n\tAge: " + str(Age) +
        "\n\tCity Address: " + City_Address +
        "\n\tContact No: " + str(Contact_Number) +
        "\n\tEmail Address: " + Email_Address +
        "\n\tDate of Birth: " + DOB +
        "\n\tPlace of Birth: " + POB +
        "\n\tCivil Status: " + Civil_Status +
        "\n\tCitizenship: " + Citizenship +
        "\n\tHeight: " + str(Height) +
        "\n\tWeight: " + str(Weight) +
        "\n\tCurrently Employed: " + str(Employed) +
        "\n\nEducational Background:\n\tElementary: " + Elementary +
        "\n\tYear of Graduate (Elementary): " + str(EYG) +
        "\n\tHighschool: " + Highschool +
        "\n\tYear of Graduate (Highschool): " + str(HYG) +
        "\n\tCollege: " + College +
        "\n\tYear of Graduate (College): " + str(CYG) +
        "\n\tDegree Received: " + Degree_Received +
        "\n\tSpecial Skills: " + Special_Skills)

def calculator():
    a = eval(input("Enter a number: "))
    b = eval(input("Enter another number: "))

    c = a + b
    d = a - b
    e = a * b
    f = a / b
    g = a % b
    h = a ** b
    i = a // b

    print("The sum of " + str(a) + " and " + str(b) + " is " + str(c))
    print("The difference of " + str(a) + " and " + str(b) + " is " + str(d))
    print("The product of " + str(a) + " and " + str(b) + " is " + str(e))
    print("The quotient of " + str(a) + " divided by " + str(b) + " is " + str(f))
    print("The remainder of " + str(a) + " divided by " + str(b) + " is " + str(g))
    print("The result of " + str(a) + " raised to the power of " + str(b) + " is " + str(h))
    print("The floor division of " + str(a) + " divided by " + str(b) + " is " + str(i))

def temperature():
    f = eval(input("Enter degree in Fahrenheit: "))
    c = ((f - 32) * 5) / 9
    c1 = eval(input("Enter degree in Celsius: "))
    f1 = (c1 * 9/5) + 32

    print(f"{f} degrees Fahrenheit converted to Celsius is {round(c, 2)} degrees.")

    print (f"{c1} degrees in Celsius converted to Farenheit is {round(f1, 2)} degrees.")

def grade():
    prelim = eval(input("Enter your grade in Prelim: "))
    midterm = eval(input("Enter your grade in Midterm: "))
    semifinals = eval(input("Enter your grade in Semi Finals: "))
    finals = eval(input("Enter your grade in Finals: "))
    quiz = eval(input("Enter your grade in Quiz: "))
    project = eval(input("Enter your grade in Project: "))

    pregrade = prelim * 0.15
    midgrade = midterm * 0.15
    semigrade = semifinals * 0.15
    finalsgrade = finals * 0.15
    quizgrade = quiz * 0.25
    projectgrade = prelim * 0.15

    fgrade = pregrade + midgrade + semigrade + finalsgrade + quizgrade + projectgrade

    if fgrade >= 75 and fgrade <= 100:
        print(f"You passed! Your grade is {fgrade}")
    elif fgrade <= 74 and fgrade >= 60:
        print(f"You failed! Your grade is {fgrade}")
    elif fgrade < 60 or fgrade > 100:
        print(f"Invalid Grade!")

def grocery():
    grocery = input("Have you bought any items (yes/no)? ")
    payment = eval(input("How much money do you have: "))

    if grocery.lower() == "yes":
        items = input("What item did you buy? \nTray of Eggs \nSteak \nPork Tenderloin \nEggplant \nThe Item: ")
        tax = 12.3

        if items.lower() == "tray of eggs":
            age = eval(input("How old are you? "))
            eggsprice = 60
            eggstax = eggsprice * .123
            eggstotal = eggsprice + eggstax
            print(f"You have purchased a Tray of Eggs with the price of ${eggsprice}, plus tax of {tax}% (${eggstax:.2f}).")
            
            if age >= 60:
                discount = eggstotal * 0.052
                eggstotal -= discount
                print(f"You're eligible for a senior discount! Your total price is now ${eggstotal:.2f}.")
            else:
                print("You're not eligible for a senior discount.")

            print(f"Total Price: {eggstotal:.2f}")
            print(f"Amount Given: {payment:.2f}")
            print(f"Total Change: {(payment - eggstotal):.2f}")

        elif items.lower() == "steak":
            age = eval(input("How old are you? "))
            steakprice = 120
            steaktax = steakprice * .123
            steaktotal = steakprice + steaktax
            print(f"You have purchased a Steak with the price of ${steakprice}, plus tax of {tax}% (${steaktax:.2f}).")
            
            if age >= 60:
                discount = steaktotal * 0.052
                steaktotal -= discount
                print(f"You're eligible for a senior discount! Your total price is now ${steaktotal:.2f}.")
            else:
                print("You're not eligible for a senior discount.")

            print(f"Total Price: {steaktotal:.2f}")
            print(f"Amount Given: {payment:.2f}")
            print(f"Total Change: {(payment - steaktotal):.2f}")

        elif items.lower() == "pork tenderloin":
            age = eval(input("How old are you? "))
            porkprice = 250
            porktax = porkprice * .123
            porktotal = porkprice + porktax
            print(f"You have purchased a Pork Tenderloin with the price of ${porkprice}, plus tax of {tax}% (${porktax:.2f}).")
            
            if age >= 60:
                discount = porktotal * 0.052
                porktotal -= discount
                print(f"You're eligible for a senior discount! Your total price is now ${porktotal:.2f}.")
            else:
                print("You're not eligible for a senior discount.")

            print(f"Total Price: {porktotal:.2f}")
            print(f"Amount Given: {payment:.2f}")
            print(f"Total Change: {(payment - porktotal):.2f}")

        elif items.lower() == "eggplant":
            age = eval(input("How old are you? "))
            eggplantprice = 40
            eggplanttax = eggplantprice * .123
            eggplanttotal = eggplantprice + eggplanttax
            print(f"You have purchased an Eggplant with the price of ${eggplantprice}, plus tax of {tax}% (${eggplanttax:.2f}).")
            
            if age >= 60:
                discount = eggplanttotal * 0.052
                eggplanttotal -= discount
                print(f"You're eligible for a senior discount! Your total price is now ${eggplanttotal:.2f}.")
            else:
                print("You're not eligible for a senior discount.")

            print(f"Total Price: {eggplanttotal:.2f}")
            print(f"Amount Given: {payment:.2f}")
            print(f"Total Change: {(payment - eggplanttotal):.2f}")

    else:
        print("Goodbye!")

def SumOfTen():
    total = 0
    for x in range(10):
        num = eval(input("Enter a number: "))
        total += num 
    print(f"The total of all numbers is {total}")

def InvertedTriangel():
    for x in range(5, 0, -1):
        for y in range(5 - x):
            print(" ", end=" ")
        for z in range(x):
            print("*", end=" ")
        print()
    
def DiamondEven():
    for x in range(1, 5):
        for y in range(4 - x):
            print(" ", end=" ")
        for z in range(2 * x - 2): 
            print("*", end=" ")
        print()

    for x in range(4, 0, -1):
        for y in range(4 - x):
            print(" ", end=" ")
        for z in range(2 * x - 2):
            print("*", end=" ")
        print()

def DiamondOdd():
    for x in range(1, 5):
        for y in range(5 - x):
            print(" ", end=" ")
        for z in range(2 * x - 1): 
            print("*", end=" ")
        print()

    for x in range(5, 0, -1):
        for y in range(5 - x):  
            print(" ", end=" ")
        for z in range(2 * x - 1): 
            print("*", end=" ")
        print()

def LoopArrow():
    for x in range(1, 6):
        for y in range(5 - x):
            print(" ", end=" ")
        for z in range(2 * x):
            print("*", end=" ")
        print() 

    for x in range(6):
        for y in range(4):
            print(" ", end=" ")
        print("* *")

def DiamondNum():
    for x in range(1, 5):
        for y in range(4 - x):
            print(" ", end=" ")
        for z in range(2 * x - 1):
            print(x, end=" ")
        print()


    for x in range(3, 0, -1): 
        for y in range(4 - x):
            print(" ", end=" ")
        for z in range(2 * x - 1):
            print(x, end=" ")
        print()

def sumuntilzero():
    total_sum = 0

    while True:
        num = int(input("Enter a number (0 to stop): "))         
        if num == 0:
            break
        total_sum += num
    print("The sum of all entered numbers is:", total_sum)

def triangles():
    import os

    isTri = True
    numTri = 0

    while isTri == True:
        ask = input("Do you want to create a new triangle (Yes/No)? ")
        if ask.lower() == "yes":
            os.system('cls')
            numTri += 1
            for a in range(1,6):
                for b in range(1, numTri+1):
                    for c in range(1, a+1):
                        print("*", end = " ")
                    for d in range(6, a, -1):
                        print(" ", end = " ")
                    
                print( )
            continue
        elif ask.lower() == "no":
            break
        else:
            os.system('cls')
            print("Invalid answer, please answer yes or no only.")
            continue

def bank():
    while True:
        print("====================")
        print("New account - 1 \nClose Program - 2")
        ask = input("What would you like to do: ")

        if ask == "1":
            total = 0
            account = input("\nPlease enter your name: ")
            while True:
                print("\n====================")
                print(f"Hello {account}, your new total is {total}")
                decision = input(f"\nDeposit Cash - 1 \nWithdraw Cash - 2 \nDenominate - 3 \nLogout - 4 \nHello {account}, what would you like to do: ")
                
                if decision == "1":
                    deposit = float(input("\nHow much would you like to deposit: "))
                    total += deposit
                
                elif decision == "2":
                    withdraw = float(input("\nHow much would you like to withdraw: "))
                    if withdraw > total:
                        print("\nInsufficient balance!")
                    else:
                        total -= withdraw
                
                elif decision == "3":
                    print("\nDenominations:")
                    temp_total = total
                    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
                    for denom in denominations:
                        count = temp_total // denom
                        if count > 0:
                            print(f"{denom}: {count}")
                        temp_total %= denom
                
                elif decision == "4":
                    print(f"\nThank you for using the program, {account}.")
                    break
                
                else:
                    print("\nInvalid option. Please choose between 1, 2, 3, or 4")
        
        elif ask == "2":
            print("\nThank you for using the program.")
            break
        
        else:
            print("\nInvalid option. Please choose between 1 or 2")
            continue