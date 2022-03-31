def rotate1_1(arr):
    t = arr[-1]
    i = len(arr)-1
    
    while i >= 1:
        arr[i] = arr[i-1]
        i -= 1

    arr[0] = t
    
def rotate1_2(arr):
    t = arr.pop()
    arr.insert(0,t)

def rotateK_1(arr,k):
    k = k%len(arr)
    for i in range(k):
        rotate1_1(arr)

def rotateK_2(arr,k):
    k = k%len(arr)
    arr = arr[len(arr)-k:]+arr[:len(arr)-k]
    print(arr)

def reverse(arr,si,ei):
    if ei >= len(arr):
        ei = len(arr)-1

    while si < ei:
        t = arr[si]
        arr[si] = arr[ei]
        arr[ei] = t

        si += 1
        ei -= 1

def rotateK_3(arr,k):
    k = k%len(arr)
    reverse(arr,0,len(arr)-1)
    reverse(arr,0,k-1)
    reverse(arr,k,len(arr)-1)


arr = [1,2,3,4,5,6]
rotateK_3(arr,2)
print(arr)

print(max(arr))