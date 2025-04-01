my_dict = {'Hello' : 1, 'how' : 4, 'are' : 4, 'you' : 3, 'today' : 4}

repeating = 4
total = 0

for key in my_dict:
    if my_dict[key] == repeating:
        total = total + 1

print("The repeating number repeats", total, "times.")