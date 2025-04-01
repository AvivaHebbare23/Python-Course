#create a tuple with different data types
tuplex = ("Tuple", False, 3.2, 1)
print(tuplex)

#create a tuple
tuplex = (4, 5, 6, 1, 2, 3)
print(tuplex)

#you cannot add new elements to tuples.
#you can merge tuples with the + opperator to create a new tuple.
tuplex = tuplex + (9, )
print(tuplex)

#count the number of occurences of 50 in the tuple
tuple1 = (50, 30, 20, 50, 10)
print(tuple1.count(50))

#create a tuple
tuplex = (2, 3, 4, 5, 6, 1, 2, )
#use tuple[start:stop] 
_slice = tuplex[3:5]
print(_slice)

#if the slice isnt defined, it is taken from the start of the tuple
_slice = tuplex[:6]
print(_slice)