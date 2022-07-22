def hr(nums,i):
    if i >= len(nums):
        return 0
    else:
        t = max(nums[i]+hr(nums,i+2),hr(nums,i+1))
        return t

def hrBU(nums):
    ans = [0 for i in range(len(nums)+2)]

    for i in range(len(nums)-1,-1,-1):
        ans[i] = max(nums[i]+ans[i+2],ans[i+1])
    
    return ans[0]

nums = [2,7,9,3,1]
print(hrBU(nums))