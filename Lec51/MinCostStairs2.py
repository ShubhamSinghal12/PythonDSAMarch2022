def minC(cost,i):
    if i < 0:
        return 0
    else:
        t = min(minC(cost,i-1),minC(cost,i-2))
        return t + cost[i]

def minCTD(cost,i,ans):
    if i < 0:
        return 0
    elif ans[i] != -1:
        return ans[i]
    else:
        t = min(minCTD(cost,i-1,ans),minCTD(cost,i-2,ans))
        ans[i] =  t + cost[i]
        return ans[i]

def minCBU(cost):
    ans = []
    ans.append(cost[0])
    ans.append(cost[1])
    for i in range(2,len(cost)):
        t = min(ans[i-1],ans[i-2]) + cost[i]
        ans.append(t)
    
    return ans[-1]



cost = [1,100,1,1,1,100,1,1,100,1]
# cost = [10,15,20]

cost.append(0)
ans = [-1 for i in range(len(cost))]

# print(minCTD(cost,len(cost)-1,ans))
print(minCBU(cost))