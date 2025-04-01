dict_test = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'coding' : 4}

print("The original dictionary is: " + str(dict_test))

k = 2

res = 0
for key in dict_test:
    if dict_test[key] == k:
        res = res + 1

print("The frequency of 2 is: " + str(res))