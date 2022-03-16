# n=7
# nsp=n//2
# nst=1
# row=1
# while row<=n:
#     csp=1
#     while csp<=nsp:
#         print(' ',end=' ')
#         csp+=1
#     cst=1
#     while cst<=nst:
#         if cst == 1 or cst == nst:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#         cst+=1
#     if row<(n+1)/2:
#         nst+=2
#         nsp-=1
#     else:
#         nst-=2
#         nsp+=1
#     row+=1
#     print()



n = 7

nsp1 = n//2
nsp2 = -1


row = 1

while row <= n:

    csp1 = 1
    while csp1 <= nsp1:
        print(" ",end= " ")
        csp1 += 1
    
    print("*",end =" ")

    csp2 = 1
    while csp2 <= nsp2:
        print(" ",end= " ")
        csp2 += 1
    
    if row != 1 and row != n:
        print("*",end = " ")

    if row < (n+1)/2:
        nsp1 -= 1
        nsp2 += 2
    else:
        nsp1 += 1
        nsp2 -= 2
    
    row += 1
    print()

