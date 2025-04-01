playingBoard = {'7': '', '8': '',  '9': '',
         '4': '', '5': '', '6': '',
         '1': '', '2': '', '3': ''}
board_keys = []

for key in playingBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(playingBoard)
        print("It's your turn, " + turn + ". Move to which spaces?")

        move = input()

        if playingBoard[move] == '':
            playingBoard[move] = turn
            count += 1
        else:
            print("That space is already filled. Please choose another.")
            continue 

        if count >= 5:
            if playingBoard['7'] == playingBoard['8'] == playingBoard['9'] != '':
                print(playingBoard)
                print("\nGame Over!\n")
                print(" **** " + turn + " won. **** ")
                break
            elif playingBoard['1'] == playingBoard['2'] == playingBoard['3'] != '':
                print(playingBoard)
                print("\nGame Over!\n")
                print(" **** " + turn + " won. **** ")
                break
            elif playingBoard['4'] == playingBoard['5'] == playingBoard['6'] != '':
                print(playingBoard)
                print("\nGame Over!\n")
                print(" **** " + turn + " won. **** ")
                break
            elif playingBoard['1'] == playingBoard['4'] == playingBoard['7'] != '':
                print(playingBoard)
                print("\nGame Over!\n")
                print(" **** " + turn + " won. **** ")
                break
            elif playingBoard['2'] == playingBoard['5'] == playingBoard['8'] != '':
                print(playingBoard)
                print("\nGame Over!\n")
                print(" **** " + turn + " won. **** ")
                break
            elif playingBoard['3'] == playingBoard['6'] == playingBoard['9'] != '':
                print(playingBoard)
                print("\nGame Over!\n")
                print(" **** " + turn + " won. **** ")
                break
            elif playingBoard['7'] == playingBoard['5'] == playingBoard['3'] != '':
                print(playingBoard)
                print("\nGame Over!\n")
                print(" **** " + turn + " won. **** ")
                break
            elif playingBoard['1'] == playingBoard['5'] == playingBoard['9'] != '':
                print(playingBoard)
                print("\nGame Over!\n")
                print(" **** " + turn + " won. **** ")
                break

        if count == 9:
            print("\nGame Over!\n")
            print("It's a Tie!")

        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'

    choice = input("Would you like to play again? Yes or No")
    if choice == "Yes":
            for key in board_keys:
                playingBoard[key] = ""

            game()

if __name__ == "__main__":
    game()