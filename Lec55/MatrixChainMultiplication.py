def mcm(matrix,si,ei):
    if si+1 == ei:
        return 0
    else:
        ans = 10**9
        for k in range(si+1,ei):
            l = mcm(matrix,si,k)
            r = mcm(matrix,k,ei)
            sw = matrix[si]*matrix[k]*matrix[ei]

            ans = min(ans,l+r+sw)
        return ans

def mcmBU(matrix):
    dp = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
    for si in range(len(matrix)-3,-1,-1):
        for ei in range(si+2,len(matrix)):
            ans = 10**9
            for k in range(si+1,ei):
                l = dp[si][k]
                r = dp[k][ei]
                sw = matrix[si]*matrix[k]*matrix[ei]

                ans = min(ans,l+r+sw)

            dp[si][ei] = ans
    return dp[0][len(matrix)-1]


mat = [4,2,3,5,1]
# print(mcm(mat,0,len(mat)-1))
print(mcmBU(mat))