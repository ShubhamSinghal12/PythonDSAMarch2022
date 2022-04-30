def mp(cr,cc,m,n,ans):
    if cr == m and cc == n:
        print(ans)
    elif cr > m or cc > n:
        return
    else:
        # if cc < n:
            mp(cr,cc+1,m,n,ans+"H")
        # if cr < m:
            mp(cr+1,cc,m,n,ans+"V")
            mp(cr+1,cc+1,m,n,ans+"D")

m,n = 3,3

mp(1,1,m,n,"")