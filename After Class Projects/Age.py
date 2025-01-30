try:
    age = int(input("Enter an age: "))
    print("Your age is: ", age)
    if age % 2 == 0:
        print("Your age", age, " ,is an even number.")
    else:
        print("Your age,", age, " ,is an odd number.")

except:
    print("Invalid input.")
