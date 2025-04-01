import array as arr

array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("The original array: "+str(array_num))

print("The number of occurences of the number 3 is: " +str(array_num.count(3)))

array_num.reverse()
print("Reversing the order: ")
print(str(array_num))