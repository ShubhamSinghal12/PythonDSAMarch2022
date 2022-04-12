ll = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

n = len(ll[0])
m = len(ll)

minr = 0
maxr = m-1
minc = 0
maxc = n-1

te = m*n

e = 0

while e < te :

    i = minc
    while i < maxc+1 and e < te:
        print(ll[minr][i],end=" ")
        e += 1
        i += 1
    
    minr += 1

    for i in range(minr,maxr+1):
        print(ll[i][maxc],end = " ")
        e += 1
    
    maxc -= 1

    for i in range(maxc,minc-1,-1):
        print(ll[maxr][i],end = " ")
        e += 1
    
    maxr -= 1

    for i in range(maxr,minr-1,-1):
        print(ll[i][minc],end=" ")
        e += 1
    
    minc += 1
    # print(e)

print()
