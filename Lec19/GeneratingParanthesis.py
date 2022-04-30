def gp(op,cl,ans):
    if op < 0 or cl < op:
        return
    elif op == 0 and cl == 0:
        print(ans)
    else:
        gp(op,cl-1,ans+")")
        gp(op-1,cl,ans+"(")
        # gp(op,cl-1,ans+")")

n = 3
gp(n,n,"")