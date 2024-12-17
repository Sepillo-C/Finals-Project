import os

from Functions import CodeChallenges


def cleaning():
    asking = input("Would you like to clear the terminal? (yes/no): ")
    if asking.lower() == "yes":
        os.system('cls')


while True:
    print("Code Challenges - 1\nActivities - 2\nClose Program - 3")
    choose = input("Which program would you like to use? ")
    if choose == "1":
        while True:
            print("\n===== Print Statements =====")
            print("Diamond - 1\nDiamond with Name - 2")
            print("\n===== 'For' Loops =====")
            print("Sum of 10 - 3 \nInverted Triangle - 4 \nDiamond Even - 5\nDiamond Odd - 6\nArrow - 7\nNumber Diamond - 8")
            print("\n===== 'While' Loops =====")
            print("Sum until Zero - 9\nTriangles - 10")
            print("\n===== Basic Programs =====")
            print("Biodata - 11\nCalculator - 12\nTemperature - 13\nGrade - 14\nGrocery - 15\nBank - 16")
            ask = input("\nHello! What program would you like to run? ")
            if ask == "1":
                CodeChallenges.diamond()
                cleaning()
            elif ask == "2":
                CodeChallenges.diamond_name()
                cleaning()
            elif ask == "3":
                CodeChallenges.SumOfTen()
                cleaning()
            elif ask == "4":
                CodeChallenges.InvertedTriangel()
                cleaning()
            elif ask == "5":
                CodeChallenges.DiamondEven()
                cleaning()
            elif ask == "6":
                CodeChallenges.DiamondOdd()
                cleaning()
            elif ask == "7":
                CodeChallenges.LoopArrow()
                cleaning()
            elif ask == "8":
                CodeChallenges.DiamondNum()
                cleaning()
            elif ask == "9":
                CodeChallenges.sumuntilzero()
                cleaning()
            elif ask == "10":
                CodeChallenges.triangles()
                cleaning()
            elif ask == "11":
                CodeChallenges.biodata()
                cleaning()
            elif ask == "12":
                CodeChallenges.calculator()
                cleaning()
            elif ask == "13":
                CodeChallenges.temperature()
                cleaning()
            elif ask == "14":
                CodeChallenges.grade()
                cleaning()
            elif ask == "15":
                CodeChallenges.grocery()
                cleaning()
            elif ask == "16":
                CodeChallenges.bank()
                cleaning()
            else:
                print("Invalid Answer")
                break
    elif choose == "3":
        print("Closing Program")
        break
    else:
        print("Invalid Answer. Please choose between 1 or 2")
        continue
