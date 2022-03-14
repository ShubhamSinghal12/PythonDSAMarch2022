num = int(input())

ans = 0
while num > 0:
    rem = num%10
    ans = ans*10+rem
    num = num//10

print(ans)