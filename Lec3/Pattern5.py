n = 5

nsp = 0
nst = n
row = 1

while row <= n:

    csp = 1
    while csp <= nsp:
        print(" ",end = " ")
        csp += 1
    
    cst = 1
    while cst <= nst:
        print("*",end = " ")
        cst += 1
    
    print()
    row += 1
    nsp += 1
    nst -= 1