N = 5
n = 0

while n<=N:
    
    ncr = 1
    r = 0
    while r<=n:
        print(ncr,end=" ")
        r += 1
        ncr = int(((n-r+1)/r)*ncr)
    
    n += 1
    print()