ll = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


for i in range(len(ll)+len(ll[0])-1):

    if i < len(ll):
        row = len(ll)-i-1
        col = 0
    else:
        row = 0
        col = i-len(ll)+1
    
    l = []

    while row < len(ll) and col < len(ll[0]):
        l.append(ll[row][col])
        row += 1
        col += 1
    
    if i%2 == 0:
        print(l)
    else:
        l.reverse()
        print(l)
    # print()
print()
