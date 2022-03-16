n=7
nsp=n//2
nst=1
row=1
while row<=n:
    csp=1
    while csp<=nsp:
        print(' ',end=' ')
        csp+=1
    cst=1
    while cst<=nst:
        print('*',end=' ')
        cst+=1
    if row<(n+1)/2:
        nst+=2
        nsp-=1
    else:
        nst-=2
        nsp+=1
    row+=1
    print()