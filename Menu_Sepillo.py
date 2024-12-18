import os
from Functions import CodeChallenges
from Functions import Activities

def clearhistory():     
    ask = str(input("\nCleaning your history..."))




while True:
    print("\t========= Username =========")
    name = str(input("What is your name? "))
    while True:
        os.system('cls')
        print("\t========= Menu =========")
        print("\t1 - Code Challenges \n\t2 - Activities \n\t3 - Close The Menu")
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
                print("\n\t=======================")
                print("\t17 - Return to Main Menu")
                
                ask = input("\nHello! What 'Code Challenge' program would you like to run? ")
                
                if ask == "1":
                    CodeChallenges.Diamond()
                    clearhistory()
                elif ask == "2":
                    CodeChallenges.Diamond_name()
                    clearhistory()
                elif ask == "3":
                    CodeChallenges.SumOfTen()
                    clearhistory()
                elif ask == "4":
                    CodeChallenges.InvertedTriangel()
                    clearhistory()
                elif ask == "5":
                    CodeChallenges.DiamondEven()
                    clearhistory()
                elif ask == "6":
                    CodeChallenges.DiamondOdd()
                    clearhistory()
                elif ask == "7":
                    CodeChallenges.LoopArrow()
                    clearhistory()
                elif ask == "8":
                    CodeChallenges.DiamondNum()
                    clearhistory()
                elif ask == "9":
                    CodeChallenges.sumuntilzero()
                    clearhistory()
                elif ask == "10":
                    CodeChallenges.triangles()
                    clearhistory()
                elif ask == "11":
                    CodeChallenges.biodata()
                    clearhistory()
                elif ask == "12":
                    CodeChallenges.calculator()
                    clearhistory()
                elif ask == "13":
                    CodeChallenges.temperature()
                    clearhistory()
                elif ask == "14":
                    CodeChallenges.grade()
                    clearhistory()
                elif ask == "15":
                    CodeChallenges.grocery()
                    clearhistory()
                elif ask == "16":
                    CodeChallenges.bank()
                    clearhistory()
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
                    print("\n\t========= Basic Programs =========")
                print("\t20 - Exit to Main Menu")

                ask = input(f"\nWhich 'Activity' would you like to run, {name.title()}? ")

                if ask == "1":
                    Activities.Activity1()
                    clearhistory()
                elif ask == "2":
                    Activities.Activity2()
                    clearhistory()
                elif ask == "3":
                    Activities.Activity3()
                    clearhistory()
                elif ask == "4":
                    Activities.Activity4()
                    clearhistory()
                elif ask == "5":
                    Activities.Activity5()
                    clearhistory()
                elif ask == "6":
                    Activities.Activity6()
                    clearhistory()
                elif ask == "7":
                    Activities.Activity7()
                    clearhistory()
                elif ask == "8":
                    Activities.Activity8()
                    clearhistory()
                elif ask == "9":
                    Activities.Activity9()
                    clearhistory()
                elif ask == "10":
                    Activities.Activity10()
                    clearhistory()
                elif ask == "11":
                    Activities.Activity11()
                    clearhistory()
                elif ask == "12":
                    Activities.Activity12()
                    clearhistory()
                elif ask == "13":
                    Activities.Activity13()
                    clearhistory()
                elif ask == "14":
                    Activities.Activity14()
                    clearhistory()
                elif ask == "15":
                    Activities.Activity15()
                    clearhistory()
                elif ask == "16":
                    Activities.Activity16()
                    clearhistory()
                elif ask == "17":
                    Activities.Activity17()
                    clearhistory()
                elif ask == "18":
                    Activities.Activity18()
                    clearhistory()
                elif ask == "19":
                    Activities.Activity19()
                    clearhistory()
                elif ask == "20":
                    print("Returning to Main Menu...")
                    break
                else:
                    print("Invalid choice. Please select a valid activity.")

        elif choose == "3":
            os.system('cls')
            print("Closing Menu...")
            break
        else:
            print("Invalid Answer. Please choose between 1, 2, or 3.")
            input("Press Enter to try again...")