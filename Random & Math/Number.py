import random
playing = True
number = str(random.randint(10, 20))

print("A number between 10 and 20 will be generated. You have to guess the number one digit at a time.")

while playing:
    guess = input("Enter a guess: \n")
    if number == guess:
        print("Correct!")
        print("The number is: ", number)
        break

    else:
        print("Your guess is incorrect. Try again.")