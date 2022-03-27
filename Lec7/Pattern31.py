n = 6

val = n
row = 1
nst = n
while row <= n:
    cst = 1
    cval = val
    while cst <= nst:
        if cst+row == n+1:
            print("*",end = " ")
        else:
            print(cval,end= " ")

        cst += 1
        cval -= 1

    print()
    row+=1
    