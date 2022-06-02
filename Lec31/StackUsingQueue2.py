from DynamicQueue import DynamicQueue

class StackUsingQueue:

    def __init__(self,n = 10):
        self.q = DynamicQueue(n)
    
    def isEmpty(self):
        return self.q.isEmpty()

    def isFull(self):
        return self.q.isFull()
    
    def size(self):
        return self.q.Qsize()
    
    def push(self,ele):
        nq = DynamicQueue()
        for i in range(self.q.Qsize()):
            nq.enqueue(self.q.dequeue())
        
        self.q.enqueue(ele)
        for i in range(nq.Qsize()):
            self.q.enqueue(nq.dequeue())
    
    def pop(self):
        return self.q.dequeue()

    def peek(self):
        return self.q.peek()


    def display(self):
        self.q.display()


st = StackUsingQueue(5)

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