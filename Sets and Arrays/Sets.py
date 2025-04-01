my_set = {1, 2, 3}
print(my_set)

my_set = {1.0, "Hello", (1, 2, 3, 4, 5)}
print(my_set)

my_set = {1, 2, 3, 3, 4, 4, 5}
print(my_set)

my_set = set([1, 2, 3, 2, 1])
print(my_set, "\n")

num_set = set([0, 1, 2, 3, 4, 5])
print("Original set: ")
print(num_set)
num_set.pop()
print("After removing an element from the original set:")
print(num_set)