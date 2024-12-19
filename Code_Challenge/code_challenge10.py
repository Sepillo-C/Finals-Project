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