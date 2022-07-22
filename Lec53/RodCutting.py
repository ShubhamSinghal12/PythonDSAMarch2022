length = [1,2,3,4,5,6,7,8]
price = [1,5,8,9,10,17,17,20]


def rodcut(length,price,n):
    if n == 0:
        return 0
    else:
        m = 0
        for i in range(len(length)):
            if length[i] <= n:
                m = max(m,price[i]+rodcut(length,price,n-length[i]))
        return m

def rodBU(length,price,n):
    ans = [0 for i in range(n+1)]
    for j in range(1,len(ans)):
        m = 0
        for i in range(len(length)):
            if length[i] <= j:
                m = max(m,price[i]+ans[j-length[i]])
        ans[j] = m
    
    return ans[n]
        


# print(rodcut(length,price,9))
print(rodBU(length,price,9))