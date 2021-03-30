def display(board):
    print(board[0])
    print(board[1])
    print(board[2])

def escolha():

    x = 'not digit'
    y = 'not digit'

    while x.isdigit() == False or y.isdigit() == False:

        x = input('Digite a linha da sua marca:\n')
        y = input('Digite a coluna da sua marca:\n')

    while int(x) < 1 or int(x) > 3 or int(y) < 1 or int(y) > 3:

        x = input('Selecione uma linha válida\n')
        y = input('Selecione uma coluna válida\n')

        if x.isdigit() == True and y.isdigit() == True:
            if int(x) < 1 or int(x) > 3 or int(y) < 1 or int(y) > 3:
                continue
        else: 
            while x.isdigit() == False or y.isdigit() == False:
                x = input('Digite a linha da sua marca:\n')
                y = input('Digite a coluna da sua marca:\n')


    return int(x) - 1, int(y) - 1



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

#Início da lógica
#OBS: Esse código apresenta erros quando input não for inteiro ou estiver fora do range

board = [' ',' ',' '], [' ',' ',' '], [' ',' ',' ']

display(board)

contador = 1
while contador < 10:

    movimento(contador)
    contador += 1

    if board[0][0] + board [0][1] + board [0][2] == 'XXX' or board[1][0] + board [1][1] + board [1][2] == 'XXX' or board[2][0] + board [2][1] + board [2][2] == 'XXX' or board[0][0] + board [1][0] + board [2][0] == 'XXX' or board[0][1] + board [1][1] + board [2][1] == 'XXX' or board[0][2] + board [1][2] + board [2][2] == 'XXX' or board[0][0] + board [1][1] + board [2][2] == 'XXX' or board[0][2] + board [1][1] + board [2][0] == 'XXX':
        print('X venceu')
        break
    elif board[0][0] + board [0][1] + board [0][2] == 'OOO' or board[1][0] + board [1][1] + board [1][2] == 'OOO' or board[2][0] + board [2][1] + board [2][2] == 'OOO' or board[0][0] + board [1][0] + board [2][0] == 'OOO' or board[0][1] + board [1][1] + board [2][1] == 'OOO' or board[0][2] + board [1][2] + board [2][2] == 'OOO' or board[0][0] + board [1][1] + board [2][2] == 'OOO' or board[0][2] + board [1][1] + board [2][0] == 'OOO': 
        print('O venceu')
        break



    #int(x) in [1,2,3] == False or int(y) in [1,2,3] == False: // isso era a condição do segundo while