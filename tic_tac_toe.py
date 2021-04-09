# Defining functions

# Function to display the board

def display(board):
    print(board[0])
    print(board[1])
    print(board[2])

# Function to validate if a moviment is valid

def choice():

    x = 'not digit'
    y = 'not digit'

    while x.isdigit() == False or y.isdigit() == False:

        x = input('Insert row:\n')
        y = input('Insert column:\n')

    while int(x) < 1 or int(x) > 3 or int(y) < 1 or int(y) > 3:

        x = input('Insert a valid row\n')
        y = input('Insert a valid column\n')

        if x.isdigit() == True and y.isdigit() == True:
            if int(x) < 1 or int(x) > 3 or int(y) < 1 or int(y) > 3:
                continue
        else: 
            while x.isdigit() == False or y.isdigit() == False:
                x = input('Insert a row:\n')
                y = input('Insert a column:\n')


    return int(x) - 1, int(y) - 1

# Function to insert X and O's

def moviment(counter):

    x,y = choice()
    
    if counter%2 != 0 and board[x][y] == ' ':
        board[x][y] = 'O'
    elif counter%2 == 0 and board[x][y] == ' ':
        board[x][y] = 'X'
    else:
        while  board[x][y] != ' ':

            x = int(input('Insert a valid row\n')) - 1
            y = int(input('Insert a valid column\n')) - 1
            
        if counter%2 != 0:
            board[x][y] = 'O'
        elif counter%2 == 0:
            board[x][y] = 'X'

    display(board)

# Start of the game logic

board = [' ',' ',' '], [' ',' ',' '], [' ',' ',' ']

display(board)

counter = 1

while counter < 10:

    moviment(counter)
    counter += 1

    if board[0][0] + board [0][1] + board [0][2] == 'XXX' or board[1][0] + board [1][1] + board [1][2] == 'XXX' or board[2][0] + board [2][1] + board [2][2] == 'XXX' or board[0][0] + board [1][0] + board [2][0] == 'XXX' or board[0][1] + board [1][1] + board [2][1] == 'XXX' or board[0][2] + board [1][2] + board [2][2] == 'XXX' or board[0][0] + board [1][1] + board [2][2] == 'XXX' or board[0][2] + board [1][1] + board [2][0] == 'XXX':
        print('X won')
        break
    elif board[0][0] + board [0][1] + board [0][2] == 'OOO' or board[1][0] + board [1][1] + board [1][2] == 'OOO' or board[2][0] + board [2][1] + board [2][2] == 'OOO' or board[0][0] + board [1][0] + board [2][0] == 'OOO' or board[0][1] + board [1][1] + board [2][1] == 'OOO' or board[0][2] + board [1][2] + board [2][2] == 'OOO' or board[0][0] + board [1][1] + board [2][2] == 'OOO' or board[0][2] + board [1][1] + board [2][0] == 'OOO': 
        print('O won')
        break

# Finish