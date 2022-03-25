var = 10

def fn():
    print(var)

fn()

if False:
    fn(10)

def fn():
    # global var
    var = 100
    print(var)

fn()
print(var)

a = 10
b = str(a)
print(b)
print("123"+"3")
