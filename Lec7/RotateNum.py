import math
n = 123456


def nod(x):
    return int(math.log10(x))+1

def rotate(n,k):
    nd = nod(n)
    i = 1
    k = k%nd
    # if k < 0:
    #     k += nd
    # while i <= k:
    #     r = n%10
    #     q = n//10

    #     n = r*(10**(nd-1))+q

    #     i += 1

    r = n%(10**k)
    q = n//(10**k)
    n = r*(10**(nd-k))+q

    print(n)


rotate(n,100)
