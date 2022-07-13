class Graph:

    def __init__(self,nv = 0):
        self.map = {}
        for i in range(1,nv+1):
            self.map[i] = {}
    
    def addEdge(self,u,v,val=0):
        self.map[u][v] = val
        self.map[v][u] = val
    
    def containsEdge(self,u,v):
        return v in self.map[u]
    
    def noOfEdges(self):
        cnt = 0
        for u in self.map:
            cnt += len(self.map[u])

        return cnt//2
    
    def removeEdge(self,u,v):
        if self.containsEdge(u,v):
            self.map[u].pop(v)
            self.map[v].pop(u)

    def display(self):
        for u in self.map:
            print(u,":",self.map[u])
    
    def addVertex(self,u):
        self.map[u] = {}
    
    def containsVertex(self,u):
        return u in self.map
    
    def noOfVertex(self):
        return len(self.map)
    
    def removeVertex(self,u):
        if u in self.map:
            for v in self.map[u]:
                self.map[v].pop(u)

            self.map.pop(u)
    
    def hasPath(self,u,v):
        return self._hp(u,v,set())

    def _hp(self,u,v,visited:"set"):
        if u == v:
            return True
        else:
            visited.add(u)
            for nbrs in self.map[u]:
                if nbrs not in visited:
                    if self._hp(nbrs,v,visited):
                        return True
            
            return False
    
    def printAllPath(self,u,v):
        self._pall(u,v,set(),"")

    def _pall(self,u,v,visited:"set",ans):
        if u == v:
            print(ans+" - "+str(u))
        else:
            visited.add(u)
            for nbrs in self.map[u]:
                if nbrs not in visited:
                    self._pall(nbrs,v,visited,ans +" - "+str(u))
            visited.remove(u)


gp = Graph(7)
gp.addEdge(1,2,10)
gp.addEdge(1,3,60)
gp.addEdge(2,4,20)
gp.addEdge(3,4,30)
gp.addEdge(3,5,80)
gp.addEdge(5,6,90)
gp.addEdge(6,7,5)
gp.addEdge(5,7,14)

# print(gp.hasPath(1,7))
gp.printAllPath(1,7)
# gp.display()
# print(gp.containsEdge(1,7))
# print(gp.noOfEdges())

# gp.removeEdge(2,4)
# gp.removeVertex(4)
# print()
# gp.display()



