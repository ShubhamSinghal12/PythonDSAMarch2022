class A:
    def __init__(self):
        print("Entering A")
        print("Exiting A")
    
    def hello(self):
        print("A says Hello")

class B(A):
    def __init__(self):
        print("Entering B")
        super().__init__()
        print("Exiting B")
    
    def hello(self):
        print("B says Hello")

class C(B):
    def __init__(self):
        print("Entering C")
        super().__init__()
        print("Exiting C")
    
    def hello(self):
        print("C says Hello")



def poly(ob):
    ob.hello()

# c = C()
# c.hello()
# print(help(c))
a = A()
b= B()
c = C()

poly(a)
poly(b)
poly(c)
