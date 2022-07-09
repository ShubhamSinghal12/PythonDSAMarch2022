from queue import PriorityQueue


#  (Value , indexNo, ListNo) --> Input in PQ
def merge(l):
    ans = []
    pq = PriorityQueue()
    for i in range(len(l)):
        pq.put((l[i][0],0,i))
    
    while not pq.empty():
        val,ind,ln = pq.get()
        ans.append(val)
        if ind != len(l[ln])-1:
            pq.put((l[ln][ind+1],ind+1,ln))
    
    return ans    

l = [[1,4,5],[1,3,4],[2,6]]
print(merge(l))