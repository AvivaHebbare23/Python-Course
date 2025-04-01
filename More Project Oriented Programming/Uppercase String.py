class IOString():

    #constructorto set default value
    def __init__(self):
        self.str1 = ""

    #function to get user input
    def getString(self):
        self.str1 = input("Enter a string: ")

    #function to print string in upper case
    def printString(self):
        print("Here's your string: ", self.str1.upper())

#object creation
str1 = IOString()

#call functions
str1.getString()
str1.printString()