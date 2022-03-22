from sys import getsizeof
from webbrowser import get

a = 2**100
print(type(a))
print(getsizeof(a))

b = "a"
print(type(b))

c = 10.234
print(type(c))

d = True
print(type(d))
print(getsizeof(d))

e = 10+5j
print(type(e))

f = None
print(type(f))


a = 30
print(id(a))
a = 30000

print(id(a))