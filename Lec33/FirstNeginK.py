from collections import deque

l = [2,-1,-7,8,-15,30,24,6]
k = 4

def firstNegK(l,k):
    qu = deque()
    for i in range(k):
        if l[i] < 0:
            qu.append(i)
    if len(qu) == 0:
        print(0)
    else:
        print(l[qu[0]])
    
    for i in range(k,len(l)):
        if len(qu)!=0 and qu[0] == i-k:
            qu.popleft()
        if l[i] < 0:
            qu.append(i)
        if len(qu) == 0:
            print(0)
        else:
            print(l[qu[0]])
        
        
firstNegK(l,k)