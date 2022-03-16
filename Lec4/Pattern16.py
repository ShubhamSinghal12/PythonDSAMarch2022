n = 5

row = 1
nst = n
nsp = n-1

while row <= 2*n-1:

    csp = 1
    while csp <= nsp:
        print(" ",end=" ")
        csp += 1

    cst = 1
    while cst <= nst:
        print("*",end=" ")
        cst += 1
    
    print()
    if row < n:
        nst -= 1
        nsp -= 1
    else:
        nst += 1
        nsp += 1
    
    row += 1
    # print()
