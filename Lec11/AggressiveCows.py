n = 5
stalls = [1,2,4,8,9]
c = 3

def isItPossible(stalls,c,min):
    noc = 1
    place = stalls[0]

    for i in range(1,len(stalls)):
        if stalls[i] - place >= min:
            noc += 1
            place = stalls[i]
    
    if noc >= c:
        return True
    else:
        return False

def searchAns(stalls,c):

    for i in range(1,stalls[-1]+1):
        if not isItPossible(stalls,c,i):
            return i-1

def BinarySeacrhAns(stalls,c):
    si = 1
    ei = stalls[-1]
    ans = 0

    while si <= ei:
        mid = (si+ei)//2
        if isItPossible(stalls,c,mid):
            ans = mid
            si = mid+1
        else:
            ei = mid-1 

    return ans

print(BinarySeacrhAns(stalls,c))