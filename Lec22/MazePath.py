def dispMaze(maze):
    for i in maze:
        for j in i:
            if j == 1:
                print(j,end=" ")
            else:
                print("0",end =" ")
        print()

def mazePath(maze,cr,cc,ans):
    if cr == len(maze)-1 and cc == len(maze[0])-1:
        print(ans)
        maze[cr][cc] = 1
        dispMaze(maze)
        maze[cr][cc] = 0

    elif cc < 0 or cc >= len(maze[0]) or cr < 0 or cr >= len(maze) or maze[cr][cc] != 0:
        return
    else:
        maze[cr][cc] = 1

        row = [0,0,-1,1]
        col = [1,-1,0,0]
        st = ["R","L","U","D"]

        for i in range(len(row)):
            mazePath(maze,cr+row[i],cc+col[i],ans+st[i])

        # mazePath(maze,cr,cc+1,ans+"R")
        # mazePath(maze,cr,cc-1,ans+"L")
        # mazePath(maze,cr-1,cc,ans+"U")
        # mazePath(maze,cr+1,cc,ans+"D")

        maze[cr][cc] = 0

m = 3
n = 3
maze = [[0 for j in range(n)] for i in range(m)]
maze[1][1] = 2
maze[0][2] = 2

mazePath(maze,0,0,"")