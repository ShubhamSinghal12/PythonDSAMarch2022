
class MyLinkedList:

    class Node:
        def __init__(self,data = 0,next = None):
            self.data = data
            self.next = next
    
    def __init__(self):
        self.head = None
        # self.tail = None
        # self.size = 0
    
    def addFirst(self,ele):
        n = self.Node(ele,self.head)
        self.head = n
        # if self.tail == None:
        #     self.tail = n
    
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data,end = " ")
            temp = temp.next
        print()
    
    def size(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count
    
    def isEmpty(self):
        return self.head == None
    
    def addLast(self,ele):
        
        if self.isEmpty():
            self.addFirst(ele)
            return
         
        # temp = self.head
        # while temp.next != None:
        #     temp = temp.next
        
        temp = self.getNodeAt(self.size()-1)
        temp.next = self.Node(ele)
    
    def addAt(self,idx,ele):
        if idx < 0 or idx >= self.size():
            raise Exception("Index Out of Bound")

        if idx == 0:
            self.addFirst(ele)
            return

        n = self.getNodeAt(idx-1)
        nn = self.Node(ele,n.next)
        n.next = nn

    
    def getFirst(self):
        if self.isEmpty():
            raise Exception("List is Empty")
        else:
            return self.head.data
    def getAt(self,idx):
        if idx < 0 or idx >= self.size():
            raise Exception("Index Out of Bound")
        return self.getNodeAt(idx).data
    
    def getLast(self):
        if self.isEmpty():
            raise Exception("List is Empty")
        else:
            return self.getNodeAt(self.size()-1).data

    def getNodeAt(self,idx):
        temp = self.head
        while idx != 0:
            temp = temp.next
            idx -= 1
        
        return temp
    
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List is Empty")
        else:
            x = self.head.data
            self.head = self.head.next
            return x
    
    def removeLast(self):
        if self.isEmpty():
            raise Exception("List is Empty")
        elif self.size() == 1:
            return self.removeFirst()
        else:
            n = self.getNodeAt(self.size()-2)
            x = n.next.data
            n.next = None
            return x
    
    def removeAt(self,idx):
        if idx < 0 or idx >= self.size():
            raise Exception("Index Out of Bound")
        elif idx == 0:
            return self.removeFirst()
        else:
            n = self.getNodeAt(idx-1)
            x = n.next.data
            n.next = n.next.next
            return x
    
    def reverse(self):
        cur = self.head
        prev = None

        while cur != None:
            ahead = cur.next

            cur.next = prev

            prev = cur
            cur = ahead
        
        self.head = prev
    
    def reverseR(self):
        self.__reverseRR(None,self.head)

    def __reverseRR(self,prev,cur):
        if cur == None:
            self.head = prev
            return
        else:
            self.__reverseRR(cur,cur.next)
            cur.next = prev
    
    def reverseOR(self):
        temp = self.head
        self.__reverseORR(self.head)
        temp.next = None

    def __reverseORR(self,prev):
        if prev.next == None:
            self.head = prev
            return
        else:
            self.__reverseORR(prev.next)
            prev.next.next = prev
    
    def k_reverse(self,k):
        self.head = self.__kReverse(self.head,k)
    
    def __kReverse(self,n,k):
        if n == None:
            return None
        else:
            t = k
            temp = n
            while t > 0 and temp != None:
                temp = temp.next
                t -= 1
            
            prev = self.__kReverse(temp,k)
            cur = n
            while cur != temp:
                ahead = cur.next
                cur.next = prev

                prev = cur
                cur = ahead
            
            return prev
    
    def merge(self,l2 : "MyLinkedList"):
        l3 = MyLinkedList()
        i = self.head
        j = l2.head
        while i != None and j != None:
            if i.data < j.data:
                l3.addLast(i.data)
                i = i.next
            else:
                l3.addLast(j.data)
                j = j.next
        
        while i != None:
            l3.addLast(i.data)
            i = i.next
        
        while j != None:
            l3.addLast(j.data)
            j = j.next
        
        return l3
    
    def midData(self):
        slow = self.head
        fast = self.head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def __midNode(self):
        slow = self.head
        fast = self.head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def mergerSort(self):
        l = self.__mergeSortHelper()
        self.head = l.head

    def __mergeSortHelper(self):
        if self.head.next == None :
            l = MyLinkedList()
            l.head = self.head
            return l
        else:
            mid = self.__midNode()
            l1 = MyLinkedList()
            l2 = MyLinkedList()

            l1.head = self.head
            l2.head = mid.next
            mid.next = None

            l1 = l1.__mergeSortHelper()
            l2 = l2.__mergeSortHelper()

            return l1.merge(l2)
    
    def fold(self):
        mid = self.__midNode()
        l1 = MyLinkedList()
        l2 = MyLinkedList()

        l1.head = self.head
        l2.head = mid.next
        mid.next = None

        l2.reverse()

        h = self.Node(0)
        cur = h
        i = l1.head
        j = l2.head
        while i != None or j != None:
            if i != None:
                cur.next = i
                cur = cur.next
                i = i.next
            if j != None:
                cur.next = j
                cur = cur.next
                j = j.next
        
        self.head = h.next


        


l1 = MyLinkedList()
l2 = MyLinkedList()
for i in range(0,9):
    l1.addLast(i+1)
    # l1.addFirst(2*i+2)
    # ll.display()

l1.display()
# print(l1.midData())
# l1.mergerSort()
l1.fold()
l1.display()
# l2.display()
# l = l1.merge(l2)
# l.display()
# ll.addLast(100)
# ll.addAt(2,500)
# ll.display()
# print(ll.size())
# print(ll.getLast())
# print(ll.removeAt(ll.size()-1))
# ll.k_reverse(4)
# ll.display()
# print(None.next)

    

    

