def optimalGame(nums,si,ei):
    if si > ei:
        return 0
    else:
        f = nums[si]+min(optimalGame(nums,si+2,ei),optimalGame(nums,si+1,ei-1))
        l = nums[ei]+min(optimalGame(nums,si+1,ei-1),optimalGame(nums,si,ei-2))
        return max(f,l)

def optBU(nums):
    dp = [[0 for j in range(len(nums))] for i in range(len(nums))]
    
    for i in range(len(nums)):
        dp[i][i] = nums[i]
    for si in range(len(nums)-1):
        dp[si][si+1] = max(nums[si],nums[si+1])
    
    for si in range(len(nums)-3,-1,-1):
        for ei in range(si+2,len(nums)):
            f = nums[si]+min(dp[si+2][ei],dp[si+1][ei-1])
            l = nums[ei]+min(dp[si+1][ei-1],dp[si][ei-2])
            dp[si][ei] = max(f,l)
    
    return dp[0][len(nums)-1]

nums = [10,100,20]
print(optBU(nums))
