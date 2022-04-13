ll = [[1,2,3],[5,6,7],[9,10,11]]


for i in range(len(ll)-1):
    for j in range(i+1,len(ll)):
        t = ll[i][j]
        ll[i][j] = ll[j][i]
        ll[j][i] = t

for i in ll:
    print(i)