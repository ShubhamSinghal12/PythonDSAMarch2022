class Parent:

    x = 10
    def __init__(self,name= " ",age = 0):
        self.name = name
        self.age = age    
    
    def intro(self):
        print("In Parent Class")
        print(self.name+" "+str(self.age))


class Child(Parent):
    # pass
    def __init__(self,name = " ",age = 0):
        # self.name = "M"
        # super().__init__(name,age)
        Parent.__init__(self,name,age)

        # self.rollNo = 100
    def wave(self):
        print(self.name)
    
    def intro(self):
        print("In Child Class")
        print(self.name+" "+str(self.age))


c = Child("Ram",10)
c.intro()
c.wave()
p = Parent("Mohan",25)
p.intro()
# print(help(c))