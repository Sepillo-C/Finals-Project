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