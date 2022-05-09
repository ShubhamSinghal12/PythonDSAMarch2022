
coins = [1,2,3,5]

def ccc(coins,amount,ans,bigAns,lp):
    if amount == 0:
        bigAns.append(list(ans))
        print(ans)
    elif amount < 0 :
        return
    else:
        for i in range(lp,len(coins)):
            ans.append(coins[i])
            ccc(coins,amount-coins[i],ans,bigAns,i)
            ans.pop()

def ccr(coins,amount,ans,bigAns,i):
    if amount == 0:
        bigAns.append(list(ans))
        print(ans)
    elif amount < 0 or i >= len(coins):
        return
    else:
        ans.append(coins[i])
        ccr(coins,amount-coins[i],ans,bigAns,i)
        ans.pop()

        ccr(coins,amount,ans,bigAns,i+1)
        # ans.pop()

bigAns = []
ccr(coins,5,[],bigAns,0)
print(bigAns)
