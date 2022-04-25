def stairs(i,n,ans):
    if i == n:
        print(ans)
        return 1
    elif i > n:
        return 0
    else:
        c = 0
        c += stairs(i+1,n,ans+"1")
        c += stairs(i+2,n,ans+"2")
        return c

def stairs1(i,n,ans):
    if i == n:
        print(ans)
        return 1
    elif i > n:
        return 0
    else:
        c = 0
        if not ans.endswith("2"):
            c += stairs1(i+1,n,ans+"1")
        c += stairs1(i+2,n,ans+"2")
        return c

print(stairs1(0,5,""))