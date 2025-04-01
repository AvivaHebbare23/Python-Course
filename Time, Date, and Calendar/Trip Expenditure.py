def hotelCosts(nights):
    return 140 * nights

def planeTicket(city):
    if "Charlotte" == city:
        return 180
    elif "Tampa" == city:
        return 220
    elif "New York" == city:
        return 450
    elif "Los Angeles" == city:
        return 400
    else:
        return 0
    
def rentalCar(days):
    if days >= 7:
        return 60 * days
    elif days <= 7:
        return 45 * days
    else:
        return 0

def totalCost(city, days, nights):
    return rentalCar(days) + hotelCosts(nights) + planeTicket(city)

hotelStay = int(input("How many nights are you going to stay at the hotel? "))
tripTicket = input("Where are you going? ")
carCost = int(input("How many days are you renting a car? "))

print("Cost of rental car is: ", rentalCar(carCost))
print("Cost of plane ticket is: ", planeTicket(tripTicket))
print("Cost of hotel room is: ", hotelCosts(hotelStay))
print("The total cost of the trip is: ", totalCost(tripTicket, carCost, hotelStay))

