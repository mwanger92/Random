from random import randint

board = []
board_size = 10
air_car_size = 5
air_car=[]

for x in range(board_size):
    board.append(["O"] * board_size)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def place_a_c(board):
    row=random_row(board) 
    col=random_col(board)
    for i in range(0, air_car_size):
        direction = randint(0,3)
        print "b4 if %d" % i
        if i < 1:
            print row,col
            air_car.append((row, col))
        elif i < 2:
            print i, direction
            if direction%2==0:
                print direction
                row=row
                allcol = col
                print "in nested if"
                while col == allcol:
                    col=randint(col-1, col+1)
                    print col 
                    board[row][col]=="X"
                    return col
            if direction%2==1:
                print direction
                col=col
                allrow = row
                print "in nested if"
                while row == allrow:
                    row=randint(row-1, row+1)
                    print row 
                    board[row][col]=="X"
                    return row


ship_row=1
ship_col=place_a_c(board)
#ship_row = random_row(board)
#ship_col = random_col(board)
#print ship_row
#print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(0,4):
    guess_row = int(raw_input("Guess Row:"))
    if guess_row == -1:
        guess_col = -1
        print ship_row, ship_col
    guess_col = int(raw_input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > board_size-1) or (guess_col < 0 or guess_col > board_size-1):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
    print turn + 1
    print_board(board)
    if turn == 3:
        print "Game Over"    
