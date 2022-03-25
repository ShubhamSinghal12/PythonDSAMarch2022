
def sub():
    a = 20
    b = 10
    c = a-b
    # add(a,b)
    print(c)

def add(a,b):
    c = a+b
    sub()
    print(c)
    return c

sub()
c = add(10,20)
print("Second",c)
# add(10,20)
