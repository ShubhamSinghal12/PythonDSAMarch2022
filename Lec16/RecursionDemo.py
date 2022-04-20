

def sum(n):

    if n == 1:
        return n

    s = sum(n-1)

    return s+n

def PD(n):
    if n == 1:
        print(n)
    else:
        print(n)
        PD(n-1)



def PI(n):
    if n == 1:
        print(n)
    else:
        PI(n-1)
        print(n)


def PDI(n):
    if n == 0:
        # print(n)
        return
    else:
        print(n)
        PDI(n-1)
        print(n)

def PI2(i,n):
    if i == n:
        print(i)
    else:
        print(i)
        PI2(i+1,n)

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

def factTail(n,ans):
    if n == 0:
        return ans
    else:
        return factTail(n-1,ans*n)

def pow(a,b):
    if b==0:
        return 1
    else:
        return a*pow(a,b-1)

def powTail(a,b,ans=1):
    if b == 0:
        return ans
    else:
        return powTail(a,b-1,ans*a)

print(powTail(2,10)) 


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

def fibTail(n,a,b):
    if n == 0: 
        return a
    else:
        return fibTail(n-1,b,a+b)



print(fibTail(5,0,1))

# print(factTail(10,1))
# PI2(1,10)
# print(sum(5))