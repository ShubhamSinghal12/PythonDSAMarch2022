n = 57

ans = 0
multi = 1
while n != 0:
    rem = n%2
    n = n//2

    ans = ans + rem*(multi)
    multi = multi*10


print(ans)