def compareTo(a,b):
    s1 = int(str(a)+str(b))
    s2 = int(str(b)+str(a))
    
    return s1-s2



def bubbleSort(a):

    for j in range(len(a)):
        swap = 0
        for i in range(len(a)-1-j):
            if compareTo(a[i],a[i+1]) < 0:
                t = a[i]
                a[i] = a[i+1]
                a[i+1] = t

                swap += 1
        # print(a)
        if swap == 0:
            break

a = [548,546,54,60]
bubbleSort(a)
print(a)