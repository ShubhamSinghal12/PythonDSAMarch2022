n = 5

nst = 1
nsp = 2*n-1
row = 1
val = n

while row <= 2*n+1:
    cst = 1
    cval = val
    while cst <= nst:
        print(cval,end=" ")
        cst += 1
        cval -= 1
    
    csp = 1
    while csp <= nsp:
        print(" ",end=" ")
        csp += 1
    
    cst = 1
    cval += 1
    if row == n+1:
        cst = 2
        cval += 1

    while cst <= nst:
        print(cval,end=" ")
        cst += 1
        cval += 1
    
    if row <= n:
        nst += 1
        nsp -= 2
    else:
        nst -= 1
        nsp += 2
    
    row += 1
    print()