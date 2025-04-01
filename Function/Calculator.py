def add(P,Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q 
def divide(P, Q):
    return P / Q 

print("Please select an option:")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")

choice = input("Please enter a choice: ")

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

if choice == "A":
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == "B":
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice == "C":
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == "D":
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("Invalid input.")