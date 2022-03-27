n = 32145

ans = 0
place = 1

while n!=0 :
    rem = n%10
    ans += place*(10**(rem-1))

    n = n//10
    place += 1

print(ans)