valuesList = []
value = input("Enter a list of numbers between 2 and 12 separated by spaces: ").split()

for num in value:
    num = int(num)
    if 2 <= num <= 12:
         valuesList.append(num)

squaredList = []
oddNumber = []
evenNumber = []

for num in valuesList:
     squared = num ** 2 
     squaredList.append(squared)
    
if squared % 2 == 0:
    evenNumber.append(squared)
else:
    oddNumber.append(squared)

print("The squared numbers are: ", squaredList)

if oddNumber and evenNumber:
    print("The odd squared numbers are: ", oddNumber)
    print("The even squared numbers are: ", evenNumber)
elif not oddNumber:
    print("There are no odd squared numbers.")
    print("The even squared numbers are: ", evenNumber)
elif not evenNumber:
    print("The odd squared numbers are: ", oddNumber)
    print("There are no even squared numbers found.")
