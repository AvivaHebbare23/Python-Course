class Employee:

    def __init__(self):
        print('Employee Created.')

    #calling destructor
    def __del__(self):
        print("Destructor called.")

def CreateObj():
    print("Creating object...")
    obj = Employee()
    print("Function End.")
    return obj

print("Calling CreateObj() function.")
obj = CreateObj()
print("Program End.")