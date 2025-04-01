num = int(input("Enter a number: "))
t = num
numLen = 0

while t > 0:
    numLen = numLen + 1
    t = int(t/10)

if numLen >= 4:
    numLen = int(numLen/2)
    check = 0
    while num > 0:
        rem = num % 10
        if check == numLen:
            midOne = rem
        elif check == (numLen -1):
            midTwo = rem
        num = int(num/10)
        check = check + 1
    product = midOne * midTwo 

print("\nThe product of the mid digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ", product)