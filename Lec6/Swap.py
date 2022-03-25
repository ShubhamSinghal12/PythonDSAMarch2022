
a = 10
b = 20

def swap(a,b):
    t = a 
    a = b
    b = t
    return a,b


print(a,b)

a,b = swap(a,b)

print(a,b)