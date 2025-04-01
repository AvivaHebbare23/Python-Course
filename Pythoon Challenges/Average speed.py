cyclist1 = 10
cyclist2 = 20
cyclist3 = 30

average_speed = cyclist1 + cyclist2 + cyclist3 / 3
print("The average speed is", average_speed)

if average_speed >= cyclist1:
    print("The average speed is greater than the first cyclist")
elif average_speed >= cyclist2:
    print("The average speed is greater than the second cyclist")
elif average_speed >= cyclist3:
    print("The average speed is greater than the third cyclist")
else:
    print("Invalid")