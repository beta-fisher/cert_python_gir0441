'''
Autor: Angel Armando Ramirez Vazquez
Fecha: 6 sep 2022
'''
def DisplayBoard(board):
   # La función acepta un parámetro el cual contiene el estado actual del tablero
   # y lo muestra en la consola.
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ",  end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")


def  EnterMove(board):
    global change_number
    ok = False 
    while not ok:
        move = input("Enter your move: ") 
        ok = len(move) == 1 and move >= '1' and move <= '9' 
        if not ok:
            print("Bad move - repeat your input!") 
            continue
        change_number = int(move)
        move = int(move) - 1       
        row = move // 3        
        col = move % 3              
        sign = board[row][col]    
        ok = sign not in ['O','X'] 
        if not ok:               
            print("Field already occupied - repeat your input!")
            continue
    board[row][col] = 'O'  


def MakeListOfFreeFields(board, board_move):
   # La función examina el tablero y construye una lista de todos los cuadros vacíos.
   # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.

    free = []  
    for row in range(3): 
        for col in range(3): 
            if board[row][col] in ['X']: 
                sign = "X"
                change_numberX = row*3+col+1
                change_board(board_move, change_numberX ,sign)
    for row in range(3): 
        for col in range(3): 
            if board[row][col] not in ['O','X']: 
                free.append((row,col)) 
    return free


def VictoryFor(board, sign):   
    
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    
    if sign == "X": 
        who = 'me' 
    elif sign == "O": 
        who = 'you' 
    else:
        who = None 
    cross1 = cross2 = True  
    for rc in range(3):
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign: 
            return who
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign: 
            return who
        if board[rc][rc] != sign: 
            cross1 = False
        if board[2 - rc][rc] != sign: 
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def think_next_position(board_move):
    for i ,element in enumerate(board_move):
        if element.count("X")==2 and element.count("O")==0:
            for number in element:
                if isinstance(number ,int):
                    return number
    for i ,element in enumerate(board_move):
        if element.count("O")==2:
            for number in element:
                if isinstance(number ,int):
                    return number
    for i ,element in enumerate(board_move):
        if element.count("X")==1 and element.count("O")==0:
            for number in element:
                if isinstance(number ,int):
                    return number
    for i ,element in enumerate(board_move):
        if element.count("X")==0 and element.count("O")==0:
            for number in element:
                if isinstance(number ,int):
                    return number
        else:
            continue     
    return None
   
        
def Draw_Move(board , board_move):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    number = 0            
    free = MakeListOfFreeFields(board, board_move) 
    cnt = len(free)
    if cnt > 0: 
        if cnt > 1:
            number = think_next_position(board_move)
            if number != None:
                number -=1        
                row = number // 3             
                col = number % 3              
        else:
            cnt -=1
            row, col = free[0]
        board[row][col] = 'X'
    return cnt
        
    
def change_board(board_move,new_number,sign):
    for element in board_move:
        for i ,pic in enumerate(element):
            if pic == new_number:
                element[i]= sign
    return board_move
    

board = [[3*j+i+1 for i in range(3)] for j in range(3)] 
board_move =  [[1,5,9],[3,5,7],[1,2,3],[1,4,7],[2,5,8],[3,6,9],[4,5,6],[7,8,9]]

board[1][1] = 'X'
free = MakeListOfFreeFields(board,board_move)
print(free)     
human_turn = True 
cnt = 1
    
while len(free):
    DisplayBoard(board)
    if human_turn:
        sign = "O"
        EnterMove(board)
        change_board(board_move ,change_number , sign)
        victory = VictoryFor(board,'O')
    else:
        cnt = Draw_Move(board , board_move )
        victory = VictoryFor(board,'X')
    if victory != None:
        DisplayBoard(board)
        print(f"{victory} Has Gaando!")
        break
    if victory == None and cnt == 0:
        DisplayBoard(board)
        exit()
    human_turn = not human_turn
    free = MakeListOfFreeFields(board,board_move)    