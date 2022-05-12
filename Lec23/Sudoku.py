grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

# for i in grid:
#     print(i)

def isItPossible(board,row,col,val):

    for i in range(len(board[0])):
        if board[row][i] == val:
            return False
    
    for i in range(len(board)):
        if board[i][col] == val:
            return False
    
    sr = row - row%3
    sc = col - col%3

    for i in range(3):
        for j in range(3):
            if board[sr+i][sc+j] == val:
                return False
    
    return True

def sudoku(board,row,col):
    if row == len(board):
        for i in board:
            print(i)
        return True
    elif col >= len(board[0]):
        sudoku(board,row+1,0)
    else:
        if board[row][col] != 0:
            sudoku(board,row,col+1)
        else:
            for i in range(1,10):
                if isItPossible(board,row,col,i):
                    board[row][col] = i
                    s = sudoku(board,row,col+1)
                    board[row][col] = 0
                    if s:
                        return 
                

print(sudoku(grid,0,0))