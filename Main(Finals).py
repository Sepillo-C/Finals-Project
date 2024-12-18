import os

from Functions import CodeChallenges
from Functions import Activities

def execute_and_clear(func):

    func()
    os.system('cls')

name = str(input("What is your name? "))

while True:
    os.system('cls')
    print("\t========= Menu =========")
    print("\t1 - Code Challenges \n\t2 - Activities \n\t3 - Close Program")
    print("\t========= Menu =========")
    choose = input(f"Which 'Code Challenge' would you like to run, {name.title()}? ")

    if choose == "1":
        while True:
            os.system('cls')
            print("\n\t========= Print Statements =========")
            print("\t1 - Diamond \n\t2 - Diamond with Name")
            print("\n\t========= 'For' Loops =========")
            print("\t3 - Sum of 10 \n\t4 - Inverted Triangle \n\t5 - Diamond Even \n\t6 - Diamond Odd \n\t7 - Arrow \n\t8 - Number Diamond")
            print("\n\t========= 'While' Loops =========")
            print("\t9 - Sum until Zero \n\t10 - Triangles")
            print("\n\t========= Basic Programs =========")
            print("\t11 - Biodata \n\t12 - Calculator \n\t13 - Temperature \n\t14 - Grade \n\t15 - Grocery \n\t16 - Bank")
            print("\t17 - Return to Main Menu")
            
            ask = input("\nHello! What 'Code Challenge' program would you like to run? ")
            
            if ask == "1":
                execute_and_clear(CodeChallenges.Diamond)
            elif ask == "2":
                execute_and_clear(CodeChallenges.Diamond_name)
            elif ask == "3":
                execute_and_clear(CodeChallenges.SumOfTen)
            elif ask == "4":
                execute_and_clear(CodeChallenges.InvertedTriangel)
            elif ask == "5":
                execute_and_clear(CodeChallenges.DiamondEven)
            elif ask == "6":
                execute_and_clear(CodeChallenges.DiamondOdd)
            elif ask == "7":
                execute_and_clear(CodeChallenges.LoopArrow)
            elif ask == "8":
                execute_and_clear(CodeChallenges.DiamondNum)
            elif ask == "9":
                execute_and_clear(CodeChallenges.sumuntilzero)
            elif ask == "10":
                execute_and_clear(CodeChallenges.triangles)
            elif ask == "11":
                execute_and_clear(CodeChallenges.biodata)
            elif ask == "12":
                execute_and_clear(CodeChallenges.calculator)
            elif ask == "13":
                execute_and_clear(CodeChallenges.temperature)
            elif ask == "14":
                execute_and_clear(CodeChallenges.grade)
            elif ask == "15":
                execute_and_clear(CodeChallenges.grocery)
            elif ask == "16":
                execute_and_clear(CodeChallenges.bank)
            elif ask == "17":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please select a valid activity.")

    elif choose == "2":
        while True:
            os.system('cls')
            print("\t========= Activities =========")
            for i in range(1, 20):
                print(f"\t{i} - Activity({i})")
            print("\t20 - Exit to Main Menu")

            ask = input(f"\nWhich 'Activity' would you like to run, {name.title()}? ")

            if ask == "1":
                execute_and_clear(Activities.Activity1)
            elif ask == "2":
                execute_and_clear(Activities.Activity2)
            elif ask == "3":
                execute_and_clear(Activities.Activity3)
            elif ask == "4":
                execute_and_clear(Activities.Activity4)
            elif ask == "5":
                execute_and_clear(Activities.Activity5)
            elif ask == "6":
                execute_and_clear(Activities.Activity6)
            elif ask == "7":
                execute_and_clear(Activities.Activity7)
            elif ask == "8":
                execute_and_clear(Activities.Activity8)
            elif ask == "9":
                execute_and_clear(Activities.Activity9)
            elif ask == "10":
                execute_and_clear(Activities.Activity10)
            elif ask == "11":
                execute_and_clear(Activities.Activity11)
            elif ask == "12":
                execute_and_clear(Activities.Activity12)
            elif ask == "13":
                execute_and_clear(Activities.Activity13)
            elif ask == "14":
                execute_and_clear(Activities.Activity14)
            elif ask == "15":
                execute_and_clear(Activities.Activity15)
            elif ask == "16":
                execute_and_clear(Activities.Activity16)
            elif ask == "17":
                execute_and_clear(Activities.Activity17)
            elif ask == "18":
                execute_and_clear(Activities.Activity18)
            elif ask == "19":
                execute_and_clear(Activities.Activity19)
            elif ask == "20":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please select a valid activity.")

    elif choose == "3":
        print("Closing Program")
        break
    else:
        print("Invalid Answer. Please choose between 1, 2, or 3.")
        input("Press Enter to try again...")