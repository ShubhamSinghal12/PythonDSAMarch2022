class MyStack:

    def __init__(self,n = 10):
        self.l = [0 for i in range(n)]
        self.top = -1
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def isFull(self):
        if self.top == len(self.l)-1:
            return True
        else:
            return False
    def size(self):
        return self.top+1
    
    def push(self,ele):
        if self.isFull():
            raise Exception("Stack Overflow!!!")

        self.top += 1
        self.l[self.top] = ele
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack UnderFlow!!")
        
        t = self.l[self.top]
        self.top -= 1
        return t 
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack UnderFlow!!")
        
        t = self.l[self.top]
        # self.top -= 1
        return t 
    
    def display(self):
        for i in range(self.top,-1,-1):
            print(self.l[i],end = " ")
        print()


st = MyStack(5)

for i in range(1,6):
    st.push(i)
    st.display()
st.display()
print(st.pop())
print(st.pop())
st.display()
print(st.peek())
st.display()
st.push(10)
st.push(20)
st.display()

