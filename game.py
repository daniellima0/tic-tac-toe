def display(board):
    print(board[0])
    print(board[1])
    print(board[2])

def escolha():

    x = int(input('Digite a linha da sua marca:\n'))
    y = int(input('Digite a coluna da sua marca:\n'))

    while  x < 1 or x > 3 or y < 1 or y > 3:

        x = int(input('Selecione uma linha válida\n'))
        y = int(input('Selecione uma coluna válida\n'))
    
    return x - 1, y - 1



def movimento(contador):

    x,y = escolha()
    
    
    if contador%2 != 0 and board[x][y] == ' ':
        board[x][y] = 'O'
    elif contador%2 == 0 and board[x][y] == ' ':
        board[x][y] = 'X'
    else:
        while  board[x][y] != ' ':

            x = int(input('Selecione uma linha válida\n')) - 1
            y = int(input('Selecione uma coluna válida\n')) - 1
            
        if contador%2 != 0:
            board[x][y] = 'O'
        elif contador%2 == 0:
            board[x][y] = 'X'

    display(board)

###

if board[1][1] + board [1][2] + board [1][3] == 'XXX' or board[2][1] + board [2][2] + board [2][3] == 'XXX' or board[3][1] + board [3][2] + board [3][3] == 'XXX' or board[1][1] + board [2][1] + board [3][1] == 'XXX' or board[1][2] + board [2][2] + board [3][2] == 'XXX' or board[1][3] + board [2][3] + board [3][3] == 'XXX' or board[1][1] + board [2][2] + board [3][3] == 'XXX' or board[1][3] + board [2][2] + board [3][1] == 'XXX':
    


###

#Início da lógica
#OBS: Esse código apresenta erros quando input não for inteiro ou estiver fora do range

board = [' ',' ',' '], [' ',' ',' '], [' ',' ',' ']

display(board)

contador = 1
while contador < 10:

    movimento(contador)
    contador += 1