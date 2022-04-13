ll = [[1,5,10,11],[3,7,12,13],[5,8,15,17],[10,12,18,20]]

def search(ll,ele):
    row = 0
    col = len(ll[0])-1

    while row < len(ll) and col >= 0:
        # print(row,col)
        if ll[row][col] == ele:
            return True
        elif ll[row][col] > ele:
            col -= 1
        else:
            row += 1
    
    return False

print(search(ll,9))
