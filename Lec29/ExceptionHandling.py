# def divide(a,b):
#     try:
#         if b == 0:
#             print("b = 0")
#             raise Exception(" Zero Division !!!")
#             print("b = 0")
#         else:
#             return a/b
#         # print("ABC")
#     except Exception as e:
#         print("Error !!!")
#         print(e)
#         return 0
#     finally:
#         print("Finally Block")
    
#     print("Hello ABC")


# print(divide(10,0))

# try:
#     print("Hi")
#     print(divide(10,0))
#     print("Bye")
# except:
#     print("Error!!!")
# finally:
#     print("Bye for Last")

# try:
#     print("Hi")
#     a = 10
#     print(a)
#     b = 20
#     print(b)
#     print("Bye")
# except NameError:
#     print("Name Error")
# except ZeroDivisionError:
#     print("Divided by 0")
# else:
#     print("Else Block")

# finally:
#     print("Finally Block")




def A():
    print("A Hi")
    try:
        B()
    except:
        print("Handeled in A")
    print("A Bye")

def B():
    print("B Hi")
    # try:
    #     C()
    # except:
    #     print("Handeled")
    C()

    print("B Bye")

def C():
    raise Exception("Error in c!!")
    

A()
print("Treminate Program")