

def ccp(coins,amount,ans):
    if amount == 0:
        print(ans)
    elif amount < 0 :
        return
    else:
        for i in coins:
            # amount -= i
            ccp(coins,amount-i,ans+str(i)+" ")
            # amount += i

coins = [5,1,3,2]

# ccp(coins,5,"")


def ccc(coins,amount,ans,lp):
    if amount == 0:
        print(ans)
    elif amount < 0 :
        return
    else:
        for i in range(lp,len(coins)):
            
            ccc(coins,amount-coins[i],ans+str(coins[i])+" ",i)

# ccc(coins,5,"",0)



def ccr(coins,amount,ans,i):
    if amount == 0:
        print(ans)
    elif amount < 0 or i >= len(coins):
        return
    else:
        ccr(coins,amount-coins[i],ans+str(coins[i])+" ",i)

        ccr(coins,amount,ans,i+1)

ccr(coins,5,"",0)