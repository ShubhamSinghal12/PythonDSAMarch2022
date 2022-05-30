class X:
    def __init__(self):
        print("Entering X")
        super().__init__()
        print("Exiting X")

class A(X):
    def __init__(self,x):
        print("Entering A")
        super().__init__(10,20)
        print("Exiting A")
    
    def hello(self):
        print("A says Hello")

class B(X):
    def __init__(self,x,y):
        print("Entering B")
        super().__init__()
        print("Exiting B")
    
    def hello(self):
        print("B says Hello")

class C(A,B):
    def __init__(self):
        print("Entering C")
        super().__init__(10)
        # A.__init__(self)
        # B.__init__(self)
        # A.__init__(self)
        # super().__init__()
        # super(A,self).__init__()
        print("Exiting C")
    
    # def hello(self):
    #     print("C says Hello")


c = C()
c.hello()
# print(help(c))
