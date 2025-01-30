dec = int(input("Enter a decimal number: "))
binary = ""

while dec > 0:
    remainder = dec % 2
    binary = str(remainder) + binary 
    dec //= 2 

print("The binary version of this decimal is: ", binary)
