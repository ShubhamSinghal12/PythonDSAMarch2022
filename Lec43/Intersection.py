def intersect(l1,l2):
    l3 = []
    d = {}
    for i in l1:
        d[i] = d.get(i,0)+1
    
    for i in l2:
        if d.get(i,0) > 0:
            l3.append(i)
            d[i] = d[i]-1

    return l3


l1 = [1,1,1,1,2,2,3,4,4,4,5,6,6,7,7,7,8,8,8]
l2 = [1,1,2,2,3,3,3,4,4,4,4,4,5,5,5,5,6,6,7,8,8,9,9,9,10]

print(intersect(l1,l2))