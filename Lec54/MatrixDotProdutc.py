def mdp(nums1,nums2,i,j):
    if i == len(nums1) or j == len(nums2):
        return -10**7
    else:
        inc = nums1[i]*nums2[j] + max(mdp(nums1,nums2,i+1,j+1),0)
        f = mdp(nums1,nums2,i+1,j)
        s = mdp(nums1,nums2,i,j+1)

        return max(inc,f,s)

def mdpBU(nums1,nums2):
    dp = [[0 for i in range(len(nums1)+1)] for j in range(len(nums2)+1)]

    for i in range(len(nums1)+1):
        dp[len(nums2)][i] = -10**7
    for i in range(len(nums2)+1):
        dp[i][len(nums1)] = -10**7

    for i in range(len(nums2)-1,-1,-1):
        for j in range(len(nums1)-1,-1,-1):
            inc = nums1[j]*nums2[i] + max(0,dp[i+1][j+1])
            f = dp[i+1][j]
            s = dp[i][j+1]

            dp[i][j]= max(inc,f,s)

    return dp[0][0]

nums1 = [-2]
nums2 = [3]
print(mdp(nums1,nums2,0,0))
