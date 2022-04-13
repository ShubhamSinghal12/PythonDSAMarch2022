l1=[1,1,2,3,3,3,4,5,6]
l2=[1,2,3,3,3,3,6,8,10]
l3=[]

si = 0
ei = 0

while si < len(l1) and ei < len(l2):
    if l1[si] == l2[ei] :
        l3.append(l1[si])
        ei += 1
        si += 1
    elif l1[si] > l2[ei]:
        ei += 1
    else:
        si += 1

print(l3)