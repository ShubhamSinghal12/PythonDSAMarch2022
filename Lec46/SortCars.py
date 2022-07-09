class Car:
    def __init__(self,p,s,c):
        self.price = p
        self.speed = s
        self.color = c
    
    def __str__(self):
        return "Price: "+str(self.price)+" Speed: "+str(self.speed)+" Color: "+self.color
    
    def __repr__(self):
        return "Price: "+str(self.price)+" Speed: "+str(self.speed)+" Color: "+self.color
    
    # def __lt__(self,oth):
    #     return self.price < oth.price

cars = [0 for i in range(5)]
cars[0] = Car(1000,50,"Blue")
cars[1] = Car(10000,80,"Red")
cars[2] = Car(200,70,"Black")
cars[3] = Car(200,50,"White")
cars[4] = Car(1000,80,"Red")

for c in cars:
    print(c)

print("-------------------------")

# cars.sort()
def fn(ob):
    return (ob.price,-ob.speed)

cars = sorted(cars,key=fn)
for c in cars:
    print(c)