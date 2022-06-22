# 10 true 20 true 40 false false true 50 false false true 30 fasle true 60 false false


from collections import deque


class BinaryTree:

    class Node:
        def __init__(self,data = 0,left = None,right = None):
            self.data = data
            self.left = left
            self.right = right

        def __repr__(self) -> str:
            return str(self.data)
        
        def __str__(self) -> str:
            return str(self.data)
    
    def __init__(self) -> None:
        self.root = None
    
    def createTree2(self):
        n1 = self.Node(10)
        n2 = self.Node(20)
        n3 = self.Node(30)
        n4 = self.Node(40)
        n5 = self.Node(50)
        n6 = self.Node(60)
        n7 = self.Node(70)
        n8 = self.Node(80)
        n9 = self.Node(90)

        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n3.right = n6
        n5.left = n7
        n6.left = n8
        n3.left = n9

        self.root = n1


    def createTree(self):
        self.root = self.__CT(None,True)

    def __CT(self,parent : "Node",ilr):
        if parent == None:
            print("Enter data for root")
        elif ilr:
            print("Enter data for left child of Node "+str(parent.data))
        else:
            print("Enter data for right child of Node "+str(parent.data))
        
        n = int(input())
        nn = self.Node(n)

        print("Is there a left Child of Node "+str(n))
        f = input()
        if f.lower() == 'true':
            nn.left = self.__CT(nn,True)
        
        print("Is there a right Child of Node "+str(n))
        f = input()
        if f.lower() == 'true':
            nn.right = self.__CT(nn,False)
        
        return nn
    
    def display(self):
        self.__disp(self.root)
    
    def __disp(self,cur : "Node"):
        if cur == None:
            return
        else:
            s = ""
            if cur.left != None:
                s += str(cur.left.data)
            
            s += " --> " + str(cur.data) + " <-- "

            if cur.right != None:
                s += str(cur.right.data)
            
            print(s)

            self.__disp(cur.left)
            self.__disp(cur.right)
    
    def size(self):
        return self.__size(self.root)

    def __size(self,cur : "Node"):
        if cur == None:
            return 0
        else:

            lc = self.__size(cur.left)
            rc = self.__size(cur.right)

            return lc+rc+1
    
    def maximum(self):
        return self.__max(self.root)

    def __max(self,cur : "Node"):
        if cur == None:
            return -10**9
        else:
            
            lmax = self.__max(cur.left)
            rmax = self.__max(cur.right)

            return max(lmax,rmax,cur.data)
    
    def search(self,ele):
        return self.__search(self.root,ele)

    def __search(self,cur,ele):
        if cur == None:
            return False
        else:
            return cur.data == ele or self.__search(cur.left,ele) or self.__search(cur.right,ele) 
    
    def ht(self):
        return self.__ht(self.root)-1
    
    def __ht(self,cur):
        if cur == None:
            return 0
        else:
            lht = self.__ht(cur.left)
            rht = self.__ht(cur.right)

            return max(lht,rht)+1
    

    def preorder(self):
        self.__preOrder(self.root)
        print()

    def __preOrder(self,cur):
        if cur == None:
            return
        else:
            print(cur.data,end= " ")
            self.__preOrder(cur.left)
            self.__preOrder(cur.right)
    
    def inorder(self):
        self.__inOrder(self.root)
        print()

    def __inOrder(self,cur):
        if cur == None:
            return
        else:
            self.__inOrder(cur.left)
            print(cur.data,end= " ")
            self.__inOrder(cur.right)
    
    def postorder(self):
        self.__postOrder(self.root)
        print()

    def __postOrder(self,cur):
        if cur == None:
            return
        else:
            self.__postOrder(cur.left)
            self.__postOrder(cur.right)
            print(cur.data,end= " ")
    
    def printAtLevel(self,lvl):
        self.__pal(self.root,lvl)
        print()

    def __pal(self,cur,lvl):
        if cur == None:
            return
        elif lvl == 0:
            print(cur.data,end= " ")
            return
        else:
            self.__pal(cur.left,lvl-1)
            self.__pal(cur.right,lvl-1)
    
    def BFS(self):
        qt = deque()
        qt.append(self.root)

        while len(qt) != 0:
            x = qt.popleft()
            print(x.data,end = " ")
            if x.left != None:
                qt.append(x.left)
            if x.right != None:
                qt.append(x.right)
        
        print()
    
    def levelbylevel(self):
        qt = deque()
        qt.append(self.root)
        qt.append(None)

        while len(qt) != 1:
            x = qt.popleft()
            if x == None:
                print()
                qt.append(None)
            else:
                print(x.data,end = " ")
                if x.left != None:
                    qt.append(x.left)
                if x.right != None:
                    qt.append(x.right)
        
        print()
    
    def levelbylevel2(self):
        qt = deque()
        qt.append(self.root)

        tmp = deque()

        while len(qt) != 0:
            x = qt.popleft()
            print(x.data,end = " ")
            if x.left != None:
                tmp.append(x.left)
            if x.right != None:
                tmp.append(x.right)
            
            if len(qt) == 0:
                print()
                qt = tmp
                tmp = deque()
    
    def zigzag(self):
        qt = deque()
        qt.append(self.root)
        lvl = 0
        tmp = deque()

        while len(qt) != 0:
            # if len(tmp) == 0:
            #     if lvl%2==0:
            #         for i in qt:
            #             print(i.data,end = " ")
            #     else:
            #         pass
            #         # qt.reverse()
            #         # qt.reverse()

            x = qt.popleft()
            print(x.data,end = " ")

            if lvl%2 == 0:
                if x.left != None:
                    tmp.appendleft(x.left)
                if x.right != None:
                    tmp.appendleft(x.right)
            else:
                if x.right != None:
                    tmp.appendleft(x.right)
                if x.left != None:
                    tmp.appendleft(x.left)
            
            if len(qt) == 0:
                print()
                qt = tmp
                tmp = deque()
                lvl += 1
        
        # print()

    def isBal(self):
        return self.__isBal(self.root)
    
    def __isBal(self,cur):
        if cur == None:
            return True
        else:
            lh = self.__ht(cur.left)
            rh = self.__ht(cur.right)

            f = abs(lh-rh) <= 1
            lisb = self.__isBal(cur.left)
            risb = self.__isBal(cur.right)

            return f and lisb and risb
    
    def isBal2(self):
        return self.__isBal2(self.root)[0]
    
    def __isBal2(self,cur):
        if cur == None:
            return True,-1
        else:

            lisb,lh = self.__isBal2(cur.left)
            risb,rh = self.__isBal2(cur.right)

            f = abs(lh-rh) <= 1

            return f and lisb and risb, max(lh,rh)+1



# f = input()
# print(f.lower())
mt = BinaryTree()
mt.createTree2()
# mt.display()
# print(mt.size())
# print(mt.maximum())
# print(mt.search(300))
# print(mt.ht())
# mt.postorder()
# mt.printAtLevel(3)
# mt.zigzag()
# qt = deque()
# qt.append(mt.Node(10))
# qt.append(mt.Node(20))
# print(qt)
print(mt.isBal2())


