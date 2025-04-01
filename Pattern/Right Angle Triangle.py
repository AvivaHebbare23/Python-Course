print("Half Pyramid Pattern of Stars (*): ")
n = int(input("Enter a number of rows: "))

for i in range(n):
    for j in range(i+n):
        print("*", end ="")
    print()