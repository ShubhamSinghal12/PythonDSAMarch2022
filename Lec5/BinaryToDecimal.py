n = 111001

ans = 0
multi = 1
while n != 0:
    rem = n%10
    n = n//10

    ans = ans + rem*(multi)
    multi = multi*2


print(ans)