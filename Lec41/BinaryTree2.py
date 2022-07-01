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
        n8.left = n9

        self.root = n1
    
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
    
    def linearize(self):
        self.__linear(self.root)

    def __linear(self,cur):
        if cur == None:
            return
        else:
            self.__linear(cur.left)
            self.__linear(cur.right)

            # l = self.__getleftmost(cur)
            l =cur
            while l.left != None:
                l = l.left
            l.left = cur.right
            cur.right = None

    
    def __getleftmost(self,cur):
        if cur.left == None:
            return cur
        else:
            return self.__getleftmost(cur.left)
    
    def createTreeUsingPreandIn(self,pre,ino):
        self.root = self.__ct(pre,ino,0,len(pre)-1,0,len(ino)-1)

    def __ct(self,pre,ino,plo,phi,inlo,inhi):
        if inlo > inhi:
            return None
        else:
            r = self.Node(pre[plo])
            i = inlo
            while i <= inhi:
                if ino[i] == pre[plo]:
                    break
                else:
                    i += 1
            
            r.left = self.__ct(pre,ino,plo+1,plo+i-inlo,inlo,i-1)
            r.right = self.__ct(pre,ino,plo+i-inlo+1,phi,i+1,inhi)

            return r
    
    def __ht(self,cur):
        if cur == None:
            return -1
        else:
            lht = self.__ht(cur.left)
            rht = self.__ht(cur.right)

            return max(lht,rht)+1

    def diameter(self):
        return self.__dia2(self.root)[0]

    def __dia(self,cur):
        if cur == None:
            return 0
        else:
            ld = self.__dia(cur.left)
            rd = self.__dia(cur.right)
            cd = self.__ht(cur.left) + self.__ht(cur.right) + 2

            return max(ld,rd,cd)
    
    def __dia2(self,cur):
        if cur == None:
            return 0 , -1
        else:
            ld,lh = self.__dia2(cur.left)
            rd,rh = self.__dia2(cur.right)
            cd = lh + rh + 2

            return max(ld,rd,cd),max(lh,rh) + 1
    
    def leftview(self):
        qt = deque()
        qt.append(self.root)

        tmp = deque()
        print(self.root,end=" ")
        while len(qt) != 0:
            x = qt.popleft()
            # print(x.data,end = " ")
            if x.left != None:
                tmp.append(x.left)
            if x.right != None:
                tmp.append(x.right)
            
            if len(qt) == 0:
                if len(tmp) != 0:
                    print(tmp[0],end=" ")
                # print()
                qt = tmp
                tmp = deque()
        print()

    def rightview(self):
        qt = deque()
        qt.append(self.root)

        tmp = deque()
        print(self.root,end=" ")
        while len(qt) != 0:
            x = qt.popleft()
            # print(x.data,end = " ")
            if x.left != None:
                tmp.append(x.left)
            if x.right != None:
                tmp.append(x.right)
            
            if len(qt) == 0:
                if len(tmp) != 0:
                    print(tmp[-1],end=" ")
                # print()
                qt = tmp
                tmp = deque()
        print()
    
    def lv(self):
        self.__lv(self.root,0,0)
        print()

    def __lv(self,cur,lvl,mlvl):
        if cur == None:
            return mlvl
        else:
            if lvl >= mlvl:
                print(cur.data,end= " ")
                mlvl += 1
            m = self.__lv(cur.left,lvl+1,mlvl)
            m = self.__lv(cur.right,lvl+1,m)
            
            return m
    
    def mirrorBinaryTree(self,rt):
        if rt==None:
            return
        else:
            self.mirrorBinaryTree(rt.left)
            self.mirrorBinaryTree(rt.right)
            rt.left,rt.right = rt.right,rt.left
    
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


mt = BinaryTree()
pre = [10,20,40,50,70,30,60,80]
ino = [40,20,70,50,10,30,80,60]
# mt.createTreeUsingPreandIn(pre,ino)
mt.createTree2()
# mt.linearize()
# mt.display()
# print(mt.diameter())
# mt.rightview()
# mt.lv()
# mt.display()
# mt.mirrorBinaryTree(mt.root)
# print("---------------------------------------")
# mt.display()
print(mt.isBST2())
