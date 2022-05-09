n = 4
k = 2
ques = n
# ques = [int(x) for x in range(1,n+1)]
# print(ques)
lans = []
def comb(ques,lu,ans,k):
    # print(type(ans))
    if len(ans) == k:
        lans.append(ans.copy())
        return
    else:
        for i in range(lu,ques+1):
            ans.append(i)
            comb(ques,i+1,ans,k)
            ans.pop()
            
comb(ques,1,[],k)
print(lans)
