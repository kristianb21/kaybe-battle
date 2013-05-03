import random

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print("----------------------")
print_board(board)

def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row) #answer for debugging
print(ship_col) #answer for debugging


turn = 0
for turn in range(4):
    guess_row = input("Guess Row:")
    guess_col = input("Guess Col:")
    guess_row = int(guess_row)
    guess_col = int(guess_col)
    
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        print("Game Over")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
            if turn == 3:
                print("Game Over")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
            if turn == 3:
                print("Game Over")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print("Game Over")
    print_board(board)
    print("You have " + str(3 - turn) + " lives!")  
    turn +=1
    
    
    
    
    
