def dec(fnc):
    def newF():
        print("In Deco")
        fnc()
        print("Out Deco")
    
    return newF


@dec
def hello():
    print("Hello")


hello()