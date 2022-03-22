a = 0
b = 1

n = 100

i = 1
while i <= n:
    c = a+b

    a = b
    b = c
    i += 1

print(a)