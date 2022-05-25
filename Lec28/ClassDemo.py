class Person:

    #Self parameter name can anything
    # def __init__(self):
    #     self.name = ""
    #     self.age = 0

    country = "India" #Class Variables

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    # def __init__(self,p):
    #     self.name = p.name
    #     self.age = p.age 


    def introduceYourself(self):
        print("Hi! My name is "+self.name)

s1 = Person("Rahul",19)
s1.introduceYourself()
s1.__class__.country = "USA"
print(s1.country)
print(s1.name)

print(s1.__class__.country)

s2 = Person("Mohan",25)
# p2 = Person(sh)
print(s2.country)

s2.introduceYourself()

# print(s1.name+" "+s2.name)
# def test(s1,s2):
#     t = s1
#     s1 = s2
#     s2 = t

# def test2(s1,s2):
#     s2 = Person("",10)
#     t = s1.age
#     s1.age = s2.age
#     s2.age = t

#     s1 = Person("",10)
#     t = s1.name
#     s1.name = s2.name
#     s2.name = t

# def test3(s1,age,name,myage,myname):
#     s1.age = 0
#     s1.name = ""
#     age = 0
#     name = ""
#     myage = 0
#     myname = ""


# myage = 100
# myname = "Sh"
# test3(s1,s2.age,s2.name,myage,myname)
# print(s1.name+" "+str(s1.age))
# print(s2.name+" "+str(s2.age))
# print(myname+" "+str(myage))
