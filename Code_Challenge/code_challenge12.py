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