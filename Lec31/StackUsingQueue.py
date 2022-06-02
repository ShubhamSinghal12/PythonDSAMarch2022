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
        self.q.enqueue(ele)
    
    def pop(self):
        nq = DynamicQueue()
        for i in range(self.q.size-1):
            nq.enqueue(self.q.dequeue())
        x = self.q.dequeue()
        self.q = nq
        return x

    def peek(self):
        nq = DynamicQueue()
        for i in range(self.q.size-1):
            nq.enqueue(self.q.dequeue())
        x = self.q.dequeue()
        nq.enqueue(x)
        self.q = nq
        return x

    def ar(self,qu):
        if qu.isEmpty():
            return
        else:
            n = qu.dequeue()
            self.ar(qu)
            # print(n)
            qu.enqueue(n)

    def dispR(self,qu):
        self.ar(qu)
        qu.display()
        self.ar(qu)

    def display(self):
        self.dispR(self.q)


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