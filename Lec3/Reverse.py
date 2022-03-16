#Reverse and Count digits

num = int(input())
digit = 3
count = 0
# ans = 0
while num > 0:
    rem = num%10
    if rem == digit:
        count += 1
    # ans = ans*10+rem
    num = num//10

# print(ans)
print(count)