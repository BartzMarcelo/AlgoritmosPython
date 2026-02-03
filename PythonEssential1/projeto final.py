from random import randrange

def display_board(board):
    # Desenha o tabuleiro conforme o layout solicitado
    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # Pede o movimento do usuário e valida a entrada
    while True:
        try:
            move = int(input("Digite seu movimento (1-9): "))
            if move < 1 or move > 9:
                print("Número inválido! Escolha entre 1 e 9.")
                continue
            
            # Converte o número 1-9 para índices [linha][coluna]
            row = (move - 1) // 3
            col = (move - 1) % 3
            
            if board[row][col] in ['X', 'O']:
                print("Este campo já está ocupado!")
                continue
                
            board[row][col] = 'O'
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def make_list_of_free_fields(board):
    # Retorna uma lista de tuplas com (linha, coluna) dos campos vazios
    free = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free.append((r, c))
    return free

def victory_for(board, sign):
    # Verifica linhas, colunas e diagonais
    # Linhas e Colunas
    for i in range(3):
        if all([board[i][j] == sign for j in range(3)]) or \
           all([board[j][i] == sign for j in range(3)]):
            return True
    # Diagonais
    if board[0][0] == board[1][1] == board[2][2] == sign or \
       board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def draw_move(board):
    # Movimento aleatório do computador
    free = make_list_of_free_fields(board)
    if free:
        idx = randrange(len(free))
        row, col = free[idx]
        board[row][col] = 'X'

# --- Início do Jogo ---

# Inicializa o quadro com números de 1 a 9
board = [[str(3 * r + c + 1) for c in range(3)] for r in range(3)]

# O computador sempre começa no meio (quadrado 5, que é board[1][1])
board[1][1] = 'X'

while True:
    display_board(board)
    
    # Vez do usuário
    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("Você ganhou!")
        break
    
    if not make_list_of_free_fields(board):
        display_board(board)
        print("Empate!")
        break

    # Vez do computador
    draw_move(board)
    if victory_for(board, 'X'):
        display_board(board)
        print("O computador ganhou!")
        break