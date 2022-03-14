n = int(input("Enter N: "))
max = int(input())
i = 2
while i <= n:
    x = int(input())
    if max < x:
        max = x
    i += 1

print("Max:",max)