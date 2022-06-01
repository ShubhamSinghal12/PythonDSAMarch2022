class Demo:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return str(self.x)+ " "+str(self.y)
    
    def __add__(self,d2):
        return Demo(self.x+d2.x, self.y+d2.y)
    
    


d = Demo(10,20)
d2 = Demo(30,40)
d3 = d+d2
# d3 = d.__add__(d2)
# print(dir(d))
print(d3)