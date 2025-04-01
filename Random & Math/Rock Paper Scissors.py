import random
options = ["Rock", "Paper", "Scissors"]
user_input = input("Enter a move: Rock, Paper, or Scissors: ")
computer_choice = random.choice(options)

print("You chose: ", user_input)
print("The computer chose: ", computer_choice)

if user_input == computer_choice:
    print("It's a tie!")
elif user_input == "Rock" and computer_choice == "Scissors":
    print("Rock smashes scissors, you win!")
elif user_input == "Paper" and computer_choice == "Rock":
    print("Paper covers rock, you win!")
elif user_input == "Scissors" and computer_choice == "Paper":
    print("Scissors cuts paper, you win!")
else:
    print("You lose! Try again next time.")