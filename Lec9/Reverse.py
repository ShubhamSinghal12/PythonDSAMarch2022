
def reverse(arr,si,ei):

    while si < ei:
        t = arr[si]
        arr[si] = arr[ei]
        arr[ei] = t

        si += 1
        ei -= 1

# arr = [int(i) for i in input().split()]
arr = [5,3,4,1,2]

reverse(arr,1,4)
print(arr)

print(arr[6])