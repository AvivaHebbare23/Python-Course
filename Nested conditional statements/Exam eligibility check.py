medical_excuse = input("Did you have a medical related excuse? Y or N ")

attendance = int(input("Input your attendance"))

if medical_excuse == 'Y':
    print("You are excused")
else:
    if attendance >= 75:
        print("You are excused")
    else:
        print("You are not allowed")