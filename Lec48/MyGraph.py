from collections import deque


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
    
    def hasPathBFS(self,u,v):
        qt = deque()
        visited = set()

        qt.append(u)
        while len(qt) != 0:
            x = qt.popleft()
            if x in visited:
                continue

            visited.add(x)
            
            if x == v:
                return True
            
            for nbrs in self.map[x]:
                if nbrs not in visited:
                    qt.append(nbrs)
        
        return False
    
    def BFST(self):
        qt = deque()
        visited = set()

        for u in self.map:
            if u in visited:
                continue

            qt.append(u)
            while len(qt) != 0:
                x = qt.popleft()
                if x in visited:
                    continue

                visited.add(x)
                print(x,end=" ")
                
                
                for nbrs in self.map[x]:
                    if nbrs not in visited:
                        qt.append(nbrs)
            print()
    
    def noOfConnectedComponents(self):
        qt = deque()
        visited = set()
        cnt = 0

        for u in self.map:
            if u in visited:
                continue

            cnt += 1
            qt.append(u)
            while len(qt) != 0:
                x = qt.popleft()
                if x in visited:
                    continue

                visited.add(x)
                
                
                for nbrs in self.map[x]:
                    if nbrs not in visited:
                        qt.append(nbrs)
        
        return cnt
    
    def isConnected(self):
        return self.noOfConnectedComponents() == 1
    
    def isCycle(self):
        qt = deque()
        visited = set()

        for u in self.map:
            if u in visited:
                continue

            qt.append(u)
            while len(qt) != 0:
                x = qt.popleft()
                if x in visited:
                    return True

                visited.add(x)
                # print(x,end=" ")
                
                
                for nbrs in self.map[x]:
                    if nbrs not in visited:
                        qt.append(nbrs)
            # print()
        return False
    
    def isTree(self):
        return self.isConnected() and not self.isCycle()
    

    def allConnectedComponents(self):
        qt = deque()
        visited = set()
        ans = []

        for u in self.map:
            if u in visited:
                continue

            l = []
            qt.append(u)
            while len(qt) != 0:
                x = qt.popleft()
                if x in visited:
                    continue

                visited.add(x)
                # print(x,end=" ")
                l.append(x)
                
                
                for nbrs in self.map[x]:
                    if nbrs not in visited:
                        qt.append(nbrs)
            ans.append(l)
        return ans
    
    def DFST(self):
        qt = []
        visited = set()

        for u in self.map:
            if u in visited:
                continue

            qt.append(u)
            while len(qt) != 0:
                x = qt.pop()
                if x in visited:
                    continue

                visited.add(x)
                print(x,end=" ")
                
                
                for nbrs in self.map[x]:
                    if nbrs not in visited:
                        qt.append(nbrs)
            print()
    
    class DisjointSets:

        class Node:
            def __init__(self,val):
                self.data = val
                self.parent = self
                self.rank = 0
        
        def __init__(self):
            pass

        def createSet(self,vtx):
            pass
        
        def union(self,u,v):
            pass
        
        def find(self,u):
            pass



gp = Graph(7)
gp.addEdge(1,2,10)
gp.addEdge(1,3,60)
gp.addEdge(2,4,20)
gp.addEdge(3,4,30)
# gp.addEdge(3,5,80)
gp.addEdge(5,6,90)
gp.addEdge(6,7,5)
gp.addEdge(5,7,14)

gp.DFST()
# print(gp.noOfConnectedComponents())
# print(gp.allConnectedComponents())
# print(gp.isTree())

# gp.BFST()
# print(gp.hasPathBFS(1,7))
# gp.printAllPath(1,7)
# gp.display()
# print(gp.containsEdge(1,7))
# print(gp.noOfEdges())

# gp.removeEdge(2,4)
# gp.removeVertex(4)
# print()
# gp.display()



