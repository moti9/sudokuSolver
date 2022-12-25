from django.shortcuts import render

# Create your views here.

# Check validation


def isValid(row, col, val, board):
    for i in range(9):
        if board[row][i] == val:
            return False
        if board[i][col] == val:
            return False
        nrow = (row//3)*3
        ncol = (col//3)*3
        if board[nrow + (i // 3)][ncol + (i % 3)] == val:
            return False

    return True

# Solve sudoku


def solveSudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for val in range(1, 10):
                    if isValid(i, j, val, board):
                        board[i][j] = val
                        if solveSudoku(board):
                            return True
                        else:
                            board[i][j] = 0
                else:
                    return False
    return True

# Index page


def index(request):
    r, c = 9, 9
    board = [[0 for i in range(c)] for j in range(r)]

    sudoku = board

    visual = "none"

    if request.method == "POST":
        for i in "123456789":
            for j in "123456789":
                nm = "num"+i+j
                temp = int(request.POST.get(nm, '0'))
                row = int(i)-1
                col = int(j)-1
                sudoku[row][col] = temp

        if solveSudoku(sudoku):
            board = sudoku
            visual="block"

    return render(request, 'index.html', {'board': sudoku, 'visual': visual})