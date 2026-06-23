def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def check_winner(board):
    lines = list(board)
    lines += [[board[r][c] for r in range(3)] for c in range(3)]
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2-i] for i in range(3)])
    for line in lines:
        if line[0] != ' ' and line[0] == line[1] == line[2]:
            return line[0]
    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, is_max):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif is_full(board):
        return 0
    if is_max:
        best = -float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == ' ':
                    board[r][c] = 'X'
                    best = max(best, minimax(board, False))
                    board[r][c] = ' '
        return best
    else:
        best = float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == ' ':
                    board[r][c] = 'O'
                    best = min(best, minimax(board, True))
                    board[r][c] = ' '
        return best

def best_move(board):
    best_val, move = -float('inf'), None
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = 'X'
                val = minimax(board, False)
                board[r][c] = ' '
                if val > best_val:
                    best_val, move = val, (r, c)
    return move

board = [['X', 'O', 'X'],
         ['O', 'X', ' '],
         [' ', ' ', 'O']]

print_board(board)
print("Best move for X:", best_move(board))