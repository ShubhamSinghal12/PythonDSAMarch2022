def ds(s,t,i,j):
    if j == len(t):
        return 1
    if i == len(s):
        return 0
    else:
        inc = 0
        if s[i] == t[j]:
            inc = ds(s,t,i+1,j+1)

        exc = ds(s,t,i+1,j)

        return inc + exc

def dsBu(s,t):
    dp = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    for i in range(len(s)+1):
        dp[i][len(t)] = 1
    
    for i in range(len(s)-1,-1,-1):
        for j in range(len(t)):
            inc = 0
            if s[i] == t[j]:
                inc = dp[i+1][j+1]

            exc = dp[i+1][j]

            dp[i][j] = inc+exc

    return dp[0][0]




s = "rrabbbit"
t = "rabbit"
print(dsBu(s,t))