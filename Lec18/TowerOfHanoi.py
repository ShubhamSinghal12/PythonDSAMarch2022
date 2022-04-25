def toh(n,source,dest,frm):
    if n == 0:
        return
    else:
        toh(n-1,source,frm,dest)
        print("Move "+str(n)+" from "+source +" to "+ dest)
        toh(n-1,frm,dest,source)

toh(3,"A","C","B")

