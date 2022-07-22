def minC(cost,i):
    if i >= len(cost):
        return 0
    else:
        t = min(minC(cost,i+1),minC(cost,i+2))
        return t + cost[i]

def minCTD(cost,i,ans):
    if i >= len(cost):
        return 0
    elif ans[i] != -1:
        return ans[i]
    else:
        t = min(minCTD(cost,i+1,ans),minCTD(cost,i+2,ans))
        ans[i] =  t + cost[i]
        return ans[i]

def minCBU(cost):
    ans = [0 for i in range(len(cost))]
    ans[-1] = cost[-1]
    ans[-2] = cost[-2]
    for i in range(len(cost)-3,-1,-1):
        t = min(ans[i+1],ans[i+2])
        ans[i] =  t + cost[i]
    
    return min(ans[0],ans[1])
    

cost = [1,100,1,1,1,100,1,1,100,1]

# cost.insert(0,0)
# ans = [-1 for i in range(len(cost))]
# print(min(minCTD(cost,0,ans),minCTD(cost,1,ans)))

print(minCBU(cost))