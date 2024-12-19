f = eval(input("Enter degree in Fahrenheit: "))
c = ((f - 32) * 5) / 9
c1 = eval(input("Enter degree in Celsius: "))
f1 = (c1 * 9/5) + 32

print(f"{f} degrees Fahrenheit converted to Celsius is {round(c, 2)} degrees.")

print (f"{c1} degrees in Celsius converted to Farenheit is {round(f1, 2)} degrees.")
