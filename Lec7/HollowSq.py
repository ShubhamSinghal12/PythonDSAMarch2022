n = 7
row = 1
nst = n
nsp = n-1
while row <= n:
    csp = 1
    while csp <= nsp:
        print(" ",end=" ")
        csp += 1

    cst = 1
    while cst <= nst:
        if row == 1 or row == n or cst == 1 or cst == nst or cst == row or cst+row == n+1:
            print("*",end = " ")
        else:
            print(" ",end=" ")
        cst += 1
    
    print()
    row += 1
    nsp -= 1

