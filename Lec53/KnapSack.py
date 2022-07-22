def knap(cost,weight,W,i):
    if i >= len(cost) or W == 0:
        return 0
    else:
        inc = 0
        if W >= weight[i]:
            inc = knap(cost,weight,W-weight[i],i+1) + cost[i]
        exc = knap(cost,weight,W,i+1)

        return max(inc,exc)

def knapTD(cost,weight,W,i,dp):
    if i >= len(cost) or W == 0:
        return 0
    elif dp[i][W] != -1:
        return dp[i][W]
    else:
        inc = 0
        if W >= weight[i]:
            inc = knapTD(cost,weight,W-weight[i],i+1,dp) + cost[i]
        exc = knapTD(cost,weight,W,i+1,dp)

        dp[i][W] = max(inc,exc)
        return dp[i][W]

def knapBU(cost,weight,W):
    dp = [[0 for j in range(W+1)] for i in range(len(weight)+1)]
    for i in range(len(cost)-1,-1,-1):
        for j in range(1,W+1):
            inc = 0
            if j >= weight[i]:
                inc = dp[i+1][j-weight[i]] + cost[i]
            exc = dp[i+1][j]

            dp[i][j] = max(inc,exc)

    return dp[0][W]

cost = [60,100,120]
weight = [10,20,30]
W = 50
dp = [[-1 for j in range(W+1)] for i in range(len(weight))]
print(knapTD(cost,weight,W,0,dp))
print(knapBU(cost,weight,W))