prelim = eval(input("Enter your grade in Prelim: "))
midterm = eval(input("Enter your grade in Midterm: "))
semifinals = eval(input("Enter your grade in Semi Finals: "))
finals = eval(input("Enter your grade in Finals: "))
quiz = eval(input("Enter your grade in Quiz: "))
project = eval(input("Enter your grade in Project: "))

pregrade = prelim * 0.15
midgrade = midterm * 0.15
semigrade = semifinals * 0.15
finalsgrade = finals * 0.15
quizgrade = quiz * 0.25
projectgrade = prelim * 0.15

fgrade = pregrade + midgrade + semigrade + finalsgrade + quizgrade + projectgrade

if fgrade >= 75 and fgrade <= 100:
    print(f"You passed! Your grade is {fgrade}")
elif fgrade <= 74 and fgrade >= 60:
    print(f"You failed! Your grade is {fgrade}")
elif fgrade < 60 or fgrade > 100:
    print(f"Invalid Grade!")