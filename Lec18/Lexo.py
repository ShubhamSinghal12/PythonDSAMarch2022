def lexo(n,ans):
    if ans > n:
        return
    else:
        print(ans)
        if ans != 0:
            lexo(n,ans*10)
        for i in range(1,10):
            lexo(n,ans*10+i)


# for i in range(1,10):
#     lexo(1000,i)

lexo(100,0)

