try:
    num1, num2 = eval(input("Enter two numbers that are separated by a comma: "))
    result = num1 / num2
    print("The result is: ", result)

except ZeroDivisionError:
    print("You cannot divide by 0. There is an error.")

except SyntaxError:
    print("The dividing comma is missing. Please enter numbers separated by a comma.")

except:
    print("Wrong Input.")

else:
    print("No exceptions.")

finally:
    print("This statement will execute no matter what.")
