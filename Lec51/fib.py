def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n-1)+fib(n-2)

def fibTD(n,ans):
    if n == 1 or n == 0:
        return n
    elif ans[n] != 0:
        return ans[n]  #Reterive
    else:
        t = fibTD(n-1,ans)+fibTD(n-2,ans)
        ans[n] = t  #Store
        return t

def fibBU(n):
    ans = [0 for i in range(n+1)]
    ans[1] = 1
    for i in range(2,n+1):
        ans[i] = ans[i-1]+ans[i-2]

    return ans[n]

def fibBUSE(n):
    a = 0
    b = 1
    c = n
    for i in range(2,n+1):
        c = a+b

        a = b
        b = c

    return c

n = 5000
# ans = [0 for i in range(n+1)]
# print(fibTD(n,ans))
print(fibBUSE(n))