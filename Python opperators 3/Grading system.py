markOne = int(input("Enter mark One"))
markTwo = int(input("Enter mark Two"))
markThree = int(input("Enter mark Three"))
markFour = int(input("Enter mark Four"))
markFive = int(input("Enter markk Five"))

total = markOne + markTwo + markThree + markFour + markFive 
average = total/500

if average>= 91 and average <=100:
    print("Your grade is A1")
elif average >= 81 and average < 91:
    print("Your grade is A2")
elif average >= 71 and average <81:
    print("Your grade is B1")
elif average >= 61 and average <71:
    print("Your grade is B2")
elif average >= 51 and average <61:
    print("Your grade is C1")
elif average >= 41 and average <51:
    print("Your grade is C2")
elif average >= 31 and average <41:
    print("Your grade is D1")
elif average >= 21 and average <23:
    print("Your grade is E1")
elif average >=0 and average <21:
    print("Your grade is E2")
else:
    print("Invalid Input")