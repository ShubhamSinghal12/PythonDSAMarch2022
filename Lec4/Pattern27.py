n = 5

nsp = n-1
nst = 1
row = 1
val = 1
# cval = val
while row <= n:

    # val = 1

    csp = 1
    while csp <= nsp:
        print(" ",end = " ")
        csp += 1
    
    cst = 1

    cval = val
    
    while cst <= nst:
        print(cval,end = " ")
        
        if cst <= nst//2:
            cval += 1
        else:
            cval -= 1
        cst += 1
    
    print()
    val += 1
    row += 1
    nsp -= 1
    nst += 2