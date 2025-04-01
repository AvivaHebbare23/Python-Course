def shutdown():
    if command == "Shutdown" or command == "1.":
        choice = input("Are you sure? ")
        if choice == "Yes":
            print("Shutting down...")
        else:
            print("Sorry.")
    elif command == "Nothing" or command == "2.":
        print("See you next time!")
    else:
        print("See you next time!")

print("What would you like to do?")
print("1. Shutdown")
print("2. Nothing")

command = input("Please select an option: ")

shutdown()