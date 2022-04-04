a = [5,1,3,4,2]


def insert(a):
    l = len(a)-1
    t = a[l]
    flag = True
    for i in range(len(a)-2,-1,-1):
        if a[i] > t:
            a[i+1] = a[i]
        else:
            flag = False
            a[i+1] = t
            break
    
    if flag:
        a[0] = t

def insert2(a,l):
    t = a[l]
    for i in range(l-1,-1,-1):
        if a[i] > t:
            a[i+1] = a[i]
        else:
            a[i+1] = t
            break
    else:
        a[0] = t

def insertionSort(a):
    for i in range(1,len(a)):
        insert2(a,i)

insertionSort(a)
print(a)        
