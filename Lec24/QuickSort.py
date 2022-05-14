import random


def partition(arr,si,ei):
    pivot = arr[ei]
    j = si
    for i in range(si,ei):
        if arr[i] < pivot:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
            j += 1

    arr[j],arr[ei] = arr[ei],arr[j]
    return j

def randpartition(arr,si,ei):
    a = random.randint(si,ei)
    arr[a],arr[ei] = arr[ei],arr[a]

    pivot = arr[ei]
    j = si
    for i in range(si,ei):
        if arr[i] < pivot:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
            j += 1

    arr[j],arr[ei] = arr[ei],arr[j]
    return j


def quickSort(arr,si,ei):
    if si >= ei:
        return 
    else:
        j = randpartition(arr,si,ei)
        quickSort(arr,si,j-1)
        quickSort(arr,j+1,ei)


arr = [3,7,2,4,6,1,8,5]
# partition(arr,0,len(arr)-1)
quickSort(arr,0,len(arr)-1)
print(arr)

