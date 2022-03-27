n = 5

row = 1
nst = 1

a = 0
b = 1

while row <= n:
    cst = 1
    while cst <= nst:
        print(a,end = "\t")
        cst += 1

        c = a+b
        a = b
        b = c
    
    print()
    nst += 1
    row += 1