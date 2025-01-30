num = int(input("Enter a number: "))
digits = 0
i = 1

while num != 0:
    num //= 10
    digits += i 

print("The number of digits in your number is ", digits)