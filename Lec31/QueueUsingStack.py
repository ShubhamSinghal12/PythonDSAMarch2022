from DynamicStack import DynamicStack

class QueueUsingStack:

    def __init__(self,n=10):
        self.st = DynamicStack(n)
    
    def isEmpty(self):
        return self.st.isEmpty()
    
    def isFull(self):
        return self.st.isFull()
    
    def Qsize(self):
        return self.st.size()
    
    def enqueue(self,ele):
        self.st.push(ele)
    
    def dequeue(self):
        nst = DynamicStack()
        for i in range(self.st.size()):
            nst.push(self.st.pop())
        x = nst.pop()
        for i in range(nst.size()):
            self.st.push(nst.pop())
        
        return x
    
    def peek(self):
        nst = DynamicStack()
        for i in range(self.st.size()):
            nst.push(self.st.pop())
        x = nst.peek()
        for i in range(nst):
            self.st.push(nst.pop())
        
        return x
    
    def dispRR(self,st):
        if st.size() == 0:
            return 
        else:
            n = st.pop()
            self.dispRR(st)
            print(n,end=" ")
            st.push(n)
    
    def display(self):
        self.dispRR(self.st)
        print()

qu = QueueUsingStack()
for i in range(1,11):
    qu.enqueue(i)
    qu.display()

qu.display()
print(qu.dequeue())
print(qu.dequeue())
qu.enqueue(10)
qu.enqueue(20)
qu.display()