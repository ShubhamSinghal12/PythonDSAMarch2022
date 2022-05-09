def qp(board,qpsf,tq,ans):
    if qpsf == tq:
        print(ans)
    else:
        for i in range(len(board)):
            if board[i] == False:
                board[i] = True
                qp(board,qpsf+1,tq, ans+"q"+str(qpsf)+"b"+str(i)+" ")
                board[i] = False #BackTracking


board = [False for i in range(4)]
# qp(board,0,2,"")


def qc(board,qpsf,tq,ans,lastP):
    if qpsf == tq:
        print(ans)
    else:
        for i in range(lastP+1,len(board)):
            if board[i] == False:
                board[i] = True
                qc(board,qpsf+1,tq, ans+"q"+str(qpsf)+"b"+str(i)+" ",i)
                board[i] = False #BackTracking


def qc2(board,qpsf,tq,ans,lastP):
    if qpsf == tq:
        print(ans)
    else:
        for i in range(lastP+1,board):
            qc2(board,qpsf+1,tq, ans+"q"+str(qpsf)+"b"+str(i)+" ",i)

# qc2(4,0,2,"",-1)

def qcbr(board,i,qpsf,tq,ans):
    if qpsf == tq:
        print(ans)
    elif i >= len(board):
        return
    else:
        board[i] = True
        qcbr(board,i+1,qpsf+1,tq,ans+"qb"+str(i)+" ")
        board[i] = False

        qcbr(board,i+1,qpsf,tq,ans)

qcbr(board,0,0,2,"")
