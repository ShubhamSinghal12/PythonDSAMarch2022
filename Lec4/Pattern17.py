n = 9

nst = n//2
nsp = 1

row = 1
while row <= n:

    cst1 = 1
    while cst1 <= nst:
        print("*",end=" ")
        cst1 += 1

    csp = 1
    while csp <= nsp:
        print(" ",end=" ")
        csp += 1

    cst2 = 1
    while cst2 <= nst:
        print("*",end=" ")
        cst2 += 1
    
    if row < (n+1)/2:
        nst -= 1
        nsp += 2
    else:
        nst += 1
        nsp -= 2
    
    row += 1
    print()