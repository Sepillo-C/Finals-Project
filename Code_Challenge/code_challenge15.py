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
