
def ed(s,t,i,j):
    if i == len(s):
        return len(t)-j
    if j == len(t):
        return len(s)-i
    else:
        if s[i] == t[j]:
            return ed(s,t,i+1,j+1)
        else:
            insert = ed(s,t,i,j+1)
            delete = ed(s,t,i+1,j)
            replace = ed(s,t,i+1,j+1)

            return min(insert,delete,replace)+1

def edBU(s,t):
    dp = [[0 for j in range(len(t)+1)]for i in range(len(s)+1)]

    for j in range(len(t)):
        dp[len(s)][j] = len(t)-j
    
    for i in range(len(s)):
        dp[i][len(t)] = len(s)-i
    
    for i in range(len(s)-1,-1,-1):
        for j in range(len(t)-1,-1,-1):
            if s[i] == t[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                insert = dp[i][j+1]
                delete = dp[i+1][j]
                replace = dp[i+1][j+1]

                dp[i][j] = min(insert,delete,replace)+1
    return dp[0][0]


print(edBU("horse","ros"))