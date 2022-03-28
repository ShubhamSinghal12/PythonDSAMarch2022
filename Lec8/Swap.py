
def swap1(x,y):
    t = x
    x = y
    y = t 

def swap2(arr):
    t = arr[0]
    arr[0] = arr[1]
    arr[1] = t 

def swap3(arr,brr):
    t = arr[0]
    arr[0] = brr[0]
    brr[0] = t 

a = [1,2,3,4]
b = [6,7,4,2]

print(a[0],b[0])

swap3(a,b)

print(a[0],b[0])

print(-100%6)