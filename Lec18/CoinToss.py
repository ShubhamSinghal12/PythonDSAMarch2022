def ct(n,ans):
    if n == 0:
        print(ans)
        return 1
    else:
        c = 0
        c += ct(n-1,ans+"H")
        c += ct(n-1,ans+"T")
        return c

def ctc(n,ans,l):
    if n == 0:
        print(ans)
        return 1
    elif ans.endswith("HH"):
        return 0
    else:
        c = 0
        if l != 'H':
            c += ctc(n-1,ans+"H","H")
        c += ctc(n-1,ans+"T","T")
        return c


def ctc2(n,ans):
    if ans.endswith("HH"):
        return 0
    elif n == 0:
        print(ans)
        return 1
    else:
        c = 0
        c += ctc2(n-1,ans+"H")
        c += ctc2(n-1,ans+"T")
        return c

def ctc3(n,ans):
    if n == 0:
        print(ans)
        return 1
    else:
        c = 0
        if not ans.endswith("H"):
            c += ctc3(n-1,ans+"H")
        c += ctc3(n-1,ans+"T")
        return c

print(ctc3(4,""))

