class Parrot:
    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blue = Parrot("Blue", 10)
woo = Parrot("Woo", 15)

print("Blue is a {}".format(blue.species))
print("Woo is a {}".format(woo.species))

print("{} is {} years old".format(blue.name, blue.age))
print("{} is {} years old".format(woo.name, woo.age))