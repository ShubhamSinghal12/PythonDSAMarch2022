def lcs(s,t,i,j):
    if i == len(s) or j == len(t):
        return 0
    else:
        if s[i] == t[j]:
            return 1 + lcs(s,t,i+1,j+1)
        else:
            return max(lcs(s,t,i+1,j),lcs(s,t,i,j+1))

def lcsBU(s,t):
    dp = [[0 for j in range(len(t)+1)]for i in range(len(s)+1)]

    for i in range(len(s)-1,-1,-1):
        for j in range(len(t)-1,-1,-1):
            if s[i] == t[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j+1])
    
    return dp[0][0]


s = "abcde"
t = "dace"
print(lcsBU(s,t))