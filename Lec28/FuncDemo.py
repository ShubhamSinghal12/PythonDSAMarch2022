def fn(a,b,*kargs):
    print(kargs,type(kargs))


fn(1,2,3,4,5,6)


a,b,*c = 1,2,3,4,5,6,7,8,9
print(c)