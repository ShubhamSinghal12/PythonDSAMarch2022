def lis(nums,i):
    # if i >= len(nums):
    #     print("1")
    #     return 0
    # else:
        m = 0
        for j in range(i+1,len(nums)):
            if nums[j] > nums[i]:
                m = max(m,lis(nums,j))
        
        return m+1

def lisTD(nums,i,ans):
    if ans[i] != -1:
        return ans[i]
    else:
        m = 0
        for j in range(i+1,len(nums)):
            if nums[j] > nums[i]:
                m = max(m,lisTD(nums,j,ans))
        
        ans[i] = m+1
        return ans[i]

def lisBU(nums):
    ans = [ 0 for i in range(len(nums))]

    for i in range(len(nums)-1,-1,-1):
        m = 0
        for j in range(i+1,len(nums)):
            if nums[j] > nums[i]:
                m = max(m,ans[j])
        
        ans[i] = m+1
    
    return max(ans)
    




nums = [10,9,2,5,3,7,101,18]
# m = 0
# ans = [-1 for i in range(len(nums))]
# for i in range(len(nums)):
#     m = max(m,lisTD(nums,i,ans))

# print(m)
print(lisBU(nums))