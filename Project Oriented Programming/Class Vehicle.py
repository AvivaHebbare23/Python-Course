#creating a class
class Vehicle:

    #create init method
    def __init__(self, maxSpeed, mileage):

        #bind the arguments
                self.maxSpeed = maxSpeed
                self.mileage = mileage

#create object
modelX = Vehicle(240, 18)

#access variables in init method
print("Model's max speed is: ", modelX.maxSpeed)
print("Model's mileage: ", modelX.mileage)