n = 6

nst = 1
nsp = 2*n-3

row = 1
val = 1
while row <= n:

    cst = 1
    cval = val
    while cst <= nst:
        print(cval,end="\t")
        cst+=1
        cval += 1
    
    csp = 1
    while csp <= nsp:
        print(" ",end="\t")
        csp+=1
    
    cst = 1
    if row==n:
        cst = 2
        cval -= 1
    
    cval -= 1
    while cst <= nst:
        print(cval,end="\t")
        cst+=1
        cval -= 1

    nst += 1
    nsp -= 2
    row += 1
    print()