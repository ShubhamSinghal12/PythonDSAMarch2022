n = 5

nsp = n-1
nst = 1
row = 1
val = 1

while row <= n:

    csp = 1
    while csp <= nsp:
        print(" ",end = "\t")
        csp += 1
    
    cst = 1
    while cst <= nst:
        print(val,end = "\t")
        val += 1
        cst += 1
    
    print()
    # val += 1
    row += 1
    nsp -= 1
    nst += 2