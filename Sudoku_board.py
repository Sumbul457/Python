def print_board(board):
    for i in range(9):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - ")
        for j in range(9):
            if j%3==0 and j!=0:
               print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def is_valid(board,col,row,num):
    for i in range(9):
        if board[row][i] == num:
            return False
        
    for j in range(9):
        if board[j][col] == num:
            return False
        
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
        return True
    
def solved_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1,10):
                    if is_valid (board, col, row, num):
                        board[row][col] = num
                        if solved_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

sudoku_board = []
print("Enter 18 values for sudoku board:")
for i in range(9):  # Loop for 3 rows
    row = []
    for j in range(9):  # Loop for 3 columns
        value = int(input(f"Enter value for location ({i},{j}): "))
        row.append(value)
    sudoku_board.append(row)

print("\nOriginal Sudokue board:")
for row in sudoku_board:
    print(row)

print("\nOriginal Sudoku_board")
print_board(sudoku_board)

if solved_sudoku(sudoku_board):
    print("\nSolved Sudoku board\n")
    print_board(sudoku_board)
else:
    print("Solution not possible\n")


# sudoku_board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]