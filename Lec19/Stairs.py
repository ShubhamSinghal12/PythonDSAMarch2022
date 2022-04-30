
def stairs(i,n,stairL,ans):
    if i == n:
        print(ans)
        return 1
    elif i > n:
        return 0
    else:
        c = 0
        for j in range(len(stairL)):
            c += stairs(i+stairL[j] , n , stairL ,ans+str(stairL[j]))
        return c

def stairs1(i,n,stairL,ans,lp):
    if i == n:
        print(ans)
        return 1
    elif i > n:
        return 0
    else:
        c = 0
        for j in range(lp,len(stairL)):
            c += stairs1(i+stairL[j] , n , stairL ,ans+str(stairL[j]),j)
        return c


print(stairs1(0,5,[1,2,3],"",0))
