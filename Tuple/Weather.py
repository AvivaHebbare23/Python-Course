weather = (1, 0, 0, 0, 1, 1, 0)
rainy = 0
sunny = 0

for i in range(0, 7):
    if(weather[i] == 0):
        rainy += 1
    else:
        sunny += 1

if(sunny > rainy):
    print("The weather will by sunny.")
else:
    print("The weather will be rainy.")
