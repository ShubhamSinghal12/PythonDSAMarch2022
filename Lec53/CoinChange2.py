def ccr(coins,amount,i):
    if amount == 0:
        return 1
    elif i >= len(coins):
        return 0
    else:

        inc = 0
        if amount >= coins[i]:
            inc = ccr(coins,amount-coins[i],i)

        exc = ccr(coins,amount,i+1)

        return inc + exc


def ccrTD(coins,amount,i,dp):
    if amount == 0:
        return 1
    elif i >= len(coins):
        return 0
    elif dp[i][amount] != -1:
        return dp[i][amount]
    else:
        inc = 0
        if amount >= coins[i]:
            inc = ccrTD(coins,amount-coins[i],i,dp)

        exc = ccrTD(coins,amount,i+1,dp)

        dp[i][amount]  = inc + exc
        return dp[i][amount]

def ccrBU(coins,amount):
    dp = [[0 for j in range(amount+1)] for i in range(len(coins)+1)]
    for i in range(len(coins)+1):
        dp[i][0] = 1
    
    for i in range(len(coins)-1,-1,-1):
        for j in range(1,amount+1):
            inc = 0
            if j >= coins[i]:
                inc = dp[i][j-coins[i]]
            exc = dp[i+1][j]
            dp[i][j]  = inc + exc
    
    return dp[0][amount]

def ccrBUSE(coins,amount):
    dp = [0 for j in range(amount+1)]
    dp[0] = 1
    
    for i in range(len(coins)-1,-1,-1):
        for j in range(coins[i],amount+1):
            inc = dp[j-coins[i]]
            exc = dp[j]
            dp[j]  = inc + exc
    
    return dp[amount]

amount = 5
coins = [1,2,5]
# dp = [[-1 for j in range(amount+1)] for i in range(len(coins))]
# print(ccrTD(coins,amount,0,dp))
print(ccrBUSE(coins,amount))