list1 = [10, 11, 12, 13, 14, 15]
list2 = [11, 24, 23, 31, 46, 79]

even = [x for x in list1 if x%2==0]
print("Here's a list of even numbers from List 1: ", even)

odd = [x for x in list2 if x%2==1]
print("Here's a list of odd numbers from List 2: ", odd)

print("\nCombining the two lists...")
combination = list(map(lambda x, y: x + y, list1, list2))
print("Here is the combined list: ", combination)

combEven = [x for x in combination if x%2==0]
print("Here's a list of even numbers from the combined lists: ", combEven)

