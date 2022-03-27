import math

def nod(x):
    return int(math.log10(x))+1

def isArmstrong(x):
    d = nod(x)
    t = x
    ans = 0
    while x!=0:
        r = x%10
        ans += r**d

        x = x//10
    
    if ans == t:
        return True
    else:
        return False


def printAllArmstrong(n):
    i = 1
    while i <= n:
        if isArmstrong(i):
            print(i)
        i += 1


printAllArmstrong(1000)
