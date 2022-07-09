class MyHashMap:

    th = 2

    class Node:
        def __init__(self,key = 0, value = 0, next = None):
            self.key = key
            self.value = value
            self.next = next
    
    def __init__(self,bsize = 4) -> None:
        self.buckets = [None for i in range(bsize)]
        self.size = 0
    
    def hashfn(self,key):
        val = hash(key)
        return val%len(self.buckets)
    
    def put(self,key,value):
        bn = self.hashfn(key)
        temp = self.buckets[bn]
        while temp != None:
            if temp.key == key:
                temp.value = value
                return
            temp = temp.next

        n = self.Node(key,value,self.buckets[bn])
        self.buckets[bn] = n
        self.size += 1

        lf = self.size//len(self.buckets)
        if lf >= MyHashMap.th:
            self.rehash()

    def rehash(self):
        nb = [None for i in range(2*len(self.buckets))]
        ob = self.buckets

        self.buckets = nb
        self.size = 0
        for head in ob:
            while head != None:
                self.put(head.key,head.value)
                head = head.next
    
    def get(self,key):
        bn = self.hashfn(key)
        temp = self.buckets[bn]
        while temp != None:
            if temp.key == key:
                return temp.value
            temp = temp.next
        
        return None
    
    def contains(self,key):
        bn = self.hashfn(key)
        temp = self.buckets[bn]
        while temp != None:
            if temp.key == key:
                return True
            temp = temp.next
        
        return False
    
    def remove(self,key):
        bn = self.hashfn(key)
        temp = self.buckets[bn]
        prev = None
        while temp != None:
            if temp.key == key:
                break
            else:
                prev = temp
                temp = temp.next
        if temp == None:
            return None
        
        if prev == None:
            self.buckets[bn] = self.buckets[bn].next
        else:
            prev.next = temp.next
        
        return temp.value
    
    def __str__(self):
        st = "[ "
        for head in self.buckets:
            while head != None:
                st += str(head.key) +" : " +str(head.value)+" , "
                head = head.next
        st += " ]"
        return st

dt = MyHashMap()
dt.put("Ram",10)
dt.put("Vishal",100)
dt.put("Shyam",20)
dt.put("Sohail",40)

print(dt)
# print(dt.get("Vishal"))
dt.put("Ram",2000)
dt.remove("Ram")
print(dt)

        

