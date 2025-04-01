L = [4, 5, 1, 2, 9, 7, 10, 8]

count = 0

for i in L:
    count += 1

average = count/len(L)

print("The sum is: ", count)
print("The average is:", average)

L.sort()

print("The smallest element is: ", L[0])
print("The largest element is: ", L[-1])