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