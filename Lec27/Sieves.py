def sieve(n):
    l = [False]*(n+1)
    sn = int(n**(0.5))
    for i in range(2,sn+1):
        if l[i] == False:
            multi = i
            while i*multi <= n:
                l[multi*i] = True
                multi += 1
    
    for i in range(2,n+1):
        if not l[i]:
            print(i)

sieve(100)

# n = 10**9
# l = [False for i in range(n)]
# print(len(l))