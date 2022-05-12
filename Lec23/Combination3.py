def combinationSum(n,k_i,k,summ,ans,big_ans,lp):
    if k_i == k and summ==n:
        big_ans.append(list(ans))
    elif summ>n or k_i > k:
        return
    else:
        for x in range(lp,10):
            ans.append(x)
            # summ +=x
            combinationSum(n,k_i+1,k,summ + x,ans,big_ans,x+1)
            ans.pop()
            # summ-=x

n = 10
k = 3
big_ans = []
combinationSum(n,0,k,0,[],big_ans,1)
print(big_ans)