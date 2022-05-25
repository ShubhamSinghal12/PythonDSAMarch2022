class MyQueue:

    def __init__(self,n=10):
        self.l = [0 for i in range(n)]
        self.front = 0
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == len(self.l)
    
    def Qsize(self):
        return self.size
    
    def enqueue(self,ele):
        if self.isFull():
            raise Exception("Queue OverFlow!!")
        
        self.l[(self.front+self.size)%len(self.l)] = ele
        self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue UnderFlow!!")
        
        t = self.l[self.front]
        self.front = (self.front+1)%(len(self.l))
        self.size -= 1
        return t
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue UnderFlow!!")
        
        t = self.l[self.front]
        return t
    
    def display(self):
        for i  in range(self.front,self.front+self.size):
            print(self.l[i%(len(self.l))],end = " ")
        print()

qu = MyQueue()
for i in range(1,11):
    qu.enqueue(i)
    qu.display()

qu.display()
print(qu.dequeue())
print(qu.dequeue())
qu.enqueue(10)
qu.enqueue(20)
qu.display()
