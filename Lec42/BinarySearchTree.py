class BST:

    class Node:
        def __init__(self,data = 0,left = None,right = None):
            self.data = data
            self.left = left
            self.right = right
    
    def __init__(self):
        self.root = None
    
    def createTree(self,l):
        self.root = self.__ct(l,0,len(l)-1)

    def __ct(self,l,si,ei):
        if si > ei:
            return None
        else:
            mid = (si+ei)//2
            r = self.Node(l[mid])
            r.left = self.__ct(l,si,mid-1)
            r.right = self.__ct(l,mid+1,ei)

            return r

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

    def search(self,ele):
        return self.__search(self.root,ele)
    
    def __search(self,cur,ele):
        if cur == None:
            return False
        else:
            if cur.data == ele:
                return True
            elif cur.data > ele:
                return self.__search(cur.left,ele)
            else:
                return self.__search(cur.right,ele)
    def min(self):
        return self.__min(self.root)
    
    def __min(self,cur):
        if cur.left == None:
            return cur.data
        else:
            return self.__min(cur.left)
    
    def add1(self,ele):
        if self.root == None:
            self.root = self.Node(ele)
        else:
            self.__add1(self.root,ele)
    
    def __add1(self,cur:"Node",ele):
        if cur.data > ele:
            if cur.left == None:
                cur.left = self.Node(ele)
            else:
                self.__add1(cur.left,ele)
        else:
            if cur.right == None:
                cur.right = self.Node(ele)
            else:
                self.__add1(cur.right,ele)
    
    def __add2(self,cur:"Node",ele):
        if cur == None:
            return self.Node(ele)
        else:
            if cur.data > ele:
                cur.left = self.__add2(cur.left,ele)
            else:
                cur.right = self.__add2(cur.right,ele)
            
            return cur
    
    def add2(self,ele):
        self.root == self.__add2(self.root,ele)
    
    def remove(self,ele):
        self.root = self.__rm(self.root,ele)
    
    def __rm(self,cur:"Node",ele):
        if cur == None:
            return None
        elif cur.data > ele:
            cur.left = self.__rm(cur.left,ele)
        elif cur.data < ele:
            cur.right = self.__rm(cur.right,ele)
        else:
            if cur.left == None and cur.right == None:
                return None
            elif cur.right == None:
                return cur.left
            elif cur.left == None:
                return cur.right
            else:
                val = self.__min(cur.right)
                cur.data = val
                cur.right = self.__rm(cur.right,val)
        
        return cur

    def decorder(self):
        self.__decOrder(self.root)
        print()

    def __decOrder(self,cur):
        if cur == None:
            return
        else:
            self.__decOrder(cur.right)
            print(cur.data,end= " ")
            self.__decOrder(cur.left)
    
    def rws(self):
        self.__rws(self.root,0)
    
    def __rws(self,cur,sum):
        if cur == None:
            return sum
        else:
            s = self.__rws(cur.right,sum)
            t = cur.data
            cur.data = s
            s = self.__rws(cur.left,s+t)

            return s
    
    def pir(self,l,r):
        self.__pir(self.root,l,r)
        print()

    def __pir(self,cur,l,r):
        if cur == None:
            return
        else:
            if cur.data < l:
                self.__pir(cur.right,l,r)
            elif cur.data >= l and cur.data <= r:
                self.__pir(cur.left,l,r)
                print(cur.data,end=" ")
                self.__pir(cur.right,l,r)
            else:
                self.__pir(cur.left,l,r)
    
    def isBST(self):
        return self.__isBST(self.root,-10**8,10**8)
    
    def __isBST(self,cur,l,r):
        if cur == None:
            return True
        else:
            if l <= cur.data <= r:
                return self.__isBST(cur.left,l,cur.data) and self.__isBST(cur.right,cur.data,r)
            else:
                return False
    
    def isBST2(self):
        return self.__isBST2(self.root)[0]
    # 0 --> isBSt , 1 --> min, 2 --> max 
    def __isBST2(self,cur):
        if cur == None:
            return (True,10**8,-10**8)
        else:
            l = self.__isBST2(cur.left)
            r = self.__isBST2(cur.right)

            cibst = cur.data >= l[2] and cur.data <= r[1]

            return (l[0] and cibst and r[0], min(l[1],r[1],cur.data), max(l[2],r[2],cur.data))




bst = BST()
l = [10,20,30,40,50,60,70,80]
bst.createTree(l)
# bst.add2(25)
# bst.remove(40)
# bst.decorder()
# bst.display()
# print(bst.search(800))
# print(bst.min())
# bst.rws()
# bst.display()
# bst.pir(20,60)
print(bst.isBST2())
