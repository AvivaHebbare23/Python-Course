import random

print("Your password will be randomly generated and contain a mix of Uppercase letters, Lowercase letters, and Numbers.\n ")

letters = "abcdefghijklmnopqrstuvwxyz"
password = ""

randomLowercase = []
randomUppercase = []
randomNumbers = []

while len(password) < 10:
    passLowercase = random.choice(letters).lower()
    passUppercase = random.choice(letters).upper()
    passNumbers = str(random.randint(1, 50))

    randomLowercase.append(passLowercase)
    randomUppercase.append(passUppercase)
    randomNumbers.append(passNumbers)

    password += passLowercase + passUppercase + passNumbers

print("\nRandomised Lowercase letters are: ", randomLowercase)
print("Randomised Uppercase letters are: ", randomUppercase)
print("Randomised Numbers are: ", randomNumbers)

print("\nAll combined, your final password is: ", password)