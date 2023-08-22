from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

# Check validation


def isValid(row, col, val, board):
    for i in range(9):
        if board[row][i] == val and val != 0 and i != col:
            return False
        if board[i][col] == val and val != 0 and i != row:
            return False
        nrow = (row//3)*3+(i // 3)
        ncol = (col//3)*3+(i % 3)
        if board[nrow][ncol] == val and val != 0 and row != nrow and col != ncol:
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


# Index page
def index(request):
    r, c = 9, 9
    board = [[0 for i in range(c)] for j in range(r)]

    sudoku = board
    visual = "none"

    if request.method == "POST":
        for i in "123456789":
            for j in "123456789":
                nm = "num" + i + j
                temp = int(request.POST.get(nm, '0'))
                row = int(i) - 1
                col = int(j) - 1
                sudoku[row][col] = temp
        flag = True
        for i in range(9):
            for j in range(9):
                if not isValid(i, j, sudoku[i][j], sudoku):
                    flag = False
                    break

        if flag:
            if solveSudoku(sudoku):
                board = sudoku
                visual = "block"
                messages.error(request, "Hurrah !!, solution found. ", extra_tags="alert alert-success alert-dismissible fade show")
            else:
                messages.error(request, "No solution found. Please check your input.", extra_tags="alert alert-danger alert-dismissible fade show")
                return redirect('index')  # Redirect back to the form
        else:
            messages.error(request, "Invalid input. Please make sure the Sudoku rules are followed.", extra_tags="alert alert-warning alert-dismissible fade show")
            return redirect('index')  # Redirect back to the form

    return render(request, 'index.html', {'board': board, 'visual': visual})

# def index(request):
#     r, c = 9, 9
#     board = [[0 for i in range(c)] for j in range(r)]

#     sudoku = board

#     visual = "none"

#     if request.method == "POST":
#         for i in "123456789":
#             for j in "123456789":
#                 nm = "num"+i+j
#                 temp = int(request.POST.get(nm, '0'))
#                 row = int(i)-1
#                 col = int(j)-1
#                 sudoku[row][col] = temp
#         flag = True
#         for i in range(9):
#             for j in range(9):
#                 if not isValid(i, j, sudoku[i][j], sudoku):
#                     flag = False
#                     break

#         if flag:
#             if solveSudoku(sudoku):
#                 board = sudoku
#                 visual = "block"

#     return render(request, 'index.html', {'board': sudoku, 'visual': visual})
