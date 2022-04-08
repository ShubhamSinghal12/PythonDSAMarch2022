arr = [1,2,3,4]

def APES1(arr):

    ans = []

    for i in range(len(arr)):
        multi = 1
        for j in range(len(arr)):
            if i != j:
                multi *= arr[j]
        ans.append(multi)

    print(ans)

def APES2(arr):

    lp = [0 for i in range(len(arr))]
    p = 1
    for i in range(len(arr)):
        lp[i] = p
        p *= arr[i]
    
    rp = [0 for i in range(len(arr))]
    p = 1
    for i in range(len(arr)-1,-1,-1):
        rp[i] = p
        p *= arr[i]

    ans = []
    for i in range(len(arr)):
        ans.append(lp[i]*rp[i])
    
    print(ans)
    return ans

def APES3(arr):

    lp = [0 for i in range(len(arr))]
    p = 1
    for i in range(len(arr)):
        lp[i] = p
        p *= arr[i]
    
    p = 1
    for i in range(len(arr)-1,-1,-1):
        lp[i] *= p
        p *= arr[i]

    print(lp)
    return lp

APES3(arr)