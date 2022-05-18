def pow(a,b):
    if b == 0:
        return 1
    else:
        x = pow(a,b//2)
        if b%2 == 0:
            return x*x
        else:
            return x*x*a


print(pow(2,10))

