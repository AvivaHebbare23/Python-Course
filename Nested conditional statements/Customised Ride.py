print("Select your ride: ")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("What type of bike?")
    print("1. Scooty")
    print("2. Scooter")

    choice2 = int(input("Enter your choice: "))
    if choice2 == 1:
        print("You have chosen Scooty")
    elif choice2 == 2:
        print("You have chosen Scooter")
    else:
        print("Invalid choice")
else:
    if choice == 2:
        print("What type of car?")
        print("1. Sedan")
        print("2. XUV")

        choice3 = int(input("Enter your choice: "))
        if choice3 == 1:
            print("You have chosen Sedan")
        elif choice3 == 2:
            print("You have chosen XUV")
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")
