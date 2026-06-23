def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve(board, row + 1, n, solutions)

def print_board(board, n):
    for row in board:
        print(' '.join('Q' if c == row else '.' for c in range(n)))
    print()

n = 4
solutions = []
solve([-1] * n, 0, n, solutions)
print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
for sol in solutions:
    print_board(sol, n)
    