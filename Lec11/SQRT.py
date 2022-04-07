n = 1000
# print(n**(0.5))


def sqrt1(n):
    
    for i in range(1,n+1):
        if i*i > n:
            print(i-1)
            return

sqrt1(n)

def sqrt2(n):
    si = 1
    ei = n

    ans = 0

    while si <= ei:
        mid = (si+ei)//2
        if mid*mid > n:
            ei = mid-1
        else:
            ans = mid
            si = mid+1
    return ans

print(sqrt2(n))
