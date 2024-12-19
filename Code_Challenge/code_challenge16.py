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