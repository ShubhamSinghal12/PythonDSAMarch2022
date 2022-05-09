def qp2d(board,ans,tq,qpsf):
    if tq == qpsf:
        print(ans)
        return 1
    else:
        sum = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if not board[i][j]:
                    board[i][j] = True
                    sum += qp2d(board,ans+"q{}b{}{} ".format(qpsf,i,j),tq,qpsf+1)
                    board[i][j] = False
        return sum

def qc2d(board,ans,tq,qpsf,row,col):
    if tq == qpsf:
        print(ans)
        return 1
    else:
        sum = 0
        for i in range(row,len(board)):
            if i == row:
                c = col
            else:
                c = 0
            for j in range(c,len(board[i])):
                if not board[i][j]:
                    board[i][j] = True
                    sum += qc2d(board,ans+"qb{}{} ".format(i,j),tq,qpsf+1,i,j)
                    board[i][j] = False
        return sum


def qc2dBoard(board,ans,tq,qpsf,i,j):
    if tq == qpsf:
        print(ans)
        return 1
    if i >= len(board):
        return 0
    if j >= len(board[0]):
        return qc2dBoard(board,ans,tq,qpsf,i+1,0)
    else:
        sum = 0
        
        board[i][j] = True
        sum += qc2dBoard(board,ans+"qb{}{} ".format(i,j),tq,qpsf+1,i,j+1)
        board[i][j] = False

        sum += qc2dBoard(board,ans,tq,qpsf,i,j+1)

        return sum


def isItPossible(board,row,col):

    #col
    i = row
    while i >= 0:
        if board[i][col]:
            return False
        i -= 1
    
    #row
    j = col
    while j >= 0:
        if board[row][j]:
            return False
        j -= 1
    
    #upper Left Diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    #Upper Right Diagonal

    i = row
    j = col
    while i >= 0 and j < len(board[0]):
        if board[i][j]:
            return False
        i -= 1
        j += 1
    
    return True


def qc2dKill(board,ans,tq,qpsf,row,col):
    if tq == qpsf:
        print(ans)
        return 1
    else:
        sum = 0
        for i in range(row,len(board)):
            if i == row:
                c = col
            else:
                c = 0
            for j in range(c,len(board[i])):
                if not board[i][j] and isItPossible(board,i,j):
                    board[i][j] = True
                    sum += qc2dKill(board,ans+"qb{}{} ".format(i,j),tq,qpsf+1,i,j)
                    board[i][j] = False
        return sum

def qc2dBoardKill(board,ans,tq,qpsf,i,j):
    if tq == qpsf:
        print(ans)
        return 1
    if i >= len(board):
        return 0
    if j >= len(board[0]):
        return qc2dBoardKill(board,ans,tq,qpsf,i+1,0)
    else:
        sum = 0
        
        if isItPossible(board,i,j):
            board[i][j] = True
            sum += qc2dBoardKill(board,ans+"qb{}{} ".format(i,j),tq,qpsf+1,i,j+1)
            board[i][j] = False

        sum += qc2dBoardKill(board,ans,tq,qpsf,i,j+1)

        return sum

def nqueens(board,ans,tq,qpsf):
    if tq == qpsf:
        print(ans)
        return 1
    else:
        sum = 0
        for j in range(len(board[0])):
            if not board[qpsf][j] and isItPossible(board,qpsf,j):
                board[qpsf][j] = True
                sum += nqueens(board,ans+"qb{}{} ".format(qpsf,j),tq,qpsf+1)
                board[qpsf][j] = False
        return sum

m = 5
n = 5
board = [[False for j in range(n)] for i in range(m)]

s = nqueens(board,"",5,0,)
print(s)