# from MyModule import fn
# from MyModule import a


# # print(type(MyModule))
# # print(dir(MyModule))

# # print(MyModule.fn(10,20))
# # print(MyModule.a)

# print(fn(10,20))
# print(a)

import sys
import os

# sys.path.append("/Users/axyz/Desktop/CBPythonLecture/PythonMarch2022")
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))


from Lec29.MyStack import MyStack

print(MyStack)

