class MyHeap:
    def __init__(self):
        self.heap = []
    
    def size(self):
        return len(self.heap)
    
    def isEmpty(self):
        return not self.heap
    
    def add(self,ele):
        self.heap.append(ele)
        self.__upheapify(len(self.heap)-1)
    
    def __upheapify(self,ci):
        if ci == 0:
            return
        pi = (ci-1)//2
        if self.heap[pi] < self.heap[ci]:
            t = self.heap[pi]
            self.heap[pi] = self.heap[ci]
            self.heap[ci] = t

            self.__upheapify(pi)
    
    def display(self):
        print(self.heap)
    
    def getMax(self):
        return self.heap[0]
    
    def __downheapify(self,pi):
        c1 = 2*pi+1
        c2 = 2*pi+2

        maxI = pi
        if c1 < len(self.heap) and self.heap[maxI] < self.heap[c1]:
            maxI = c1

        if c2 < len(self.heap) and self.heap[maxI] < self.heap[c2]:
            maxI = c2
        
        if pi != maxI:
            t = self.heap[pi]
            self.heap[pi] = self.heap[maxI]
            self.heap[maxI] = t

            self.__downheapify(maxI)


    def remove(self):
        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]
        t = self.heap.pop()
        self.__downheapify(0)
        return t


hp = MyHeap()
hp.add(10)
hp.add(20)
hp.add(30)
hp.add(40)
hp.add(50)
hp.add(60)
hp.add(70)

hp.display()

print(hp.getMax())
print(hp.remove())

hp.display()
    


