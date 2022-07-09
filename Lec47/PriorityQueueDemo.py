from queue import PriorityQueue


pq = PriorityQueue()
pq.put((-1,10))
pq.put((-2,20))
pq.put((-3,30))
# pq.put(40)
# pq.put(50)
# pq.put(60)
# pq.put(70)

# print(pq)
while not pq.empty():
    i = pq.get()
    print(i)