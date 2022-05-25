def evpoly(poly,x):
    p = 1
    ans = 0
    for i in poly:
        ans += p*i
        p *= x
    return ans

coef=[3,-2,4,0,0,3]
print(evpoly(coef,5))