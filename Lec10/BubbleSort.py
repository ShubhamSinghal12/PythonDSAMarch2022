a = [5,1,3,4,2]

def bubbleSort(a):

    for j in range(len(a)):
        swap = 0
        for i in range(len(a)-1-j):
            if a[i] > a[i+1]:
                t = a[i]
                a[i] = a[i+1]
                a[i+1] = t

                swap += 1
        print(a)
        if swap == 0:
            break

bubbleSort(a)
print(bool(0))

