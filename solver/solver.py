def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return board
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid_move(board, num, (row, col)):
            board[row][col] = num
            
            if solve_sudoku(board):
                return board
            
            board[row][col] = 0
    
    return None

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid_move(board, num, position):
    row, col = position
    
    if num in board[row]:
        return False
    
    if num in [board[i][col] for i in range(9)]:
        return False
    
    square_row = row // 3 * 3
    square_col = col // 3 * 3
    for i in range(square_row, square_row + 3):
        for j in range(square_col, square_col + 3):
            if board[i][j] == num:
                return False
    
    return True
