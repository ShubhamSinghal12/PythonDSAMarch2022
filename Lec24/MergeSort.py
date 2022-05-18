def merge(arr,brr):
    r = []
    i = 0
    j = 0
    while i < len(arr) and j < len(brr):
        if arr[i] <= brr[j]:
            r.append(arr[i])
            i += 1
        else:
            r.append(brr[j])
            j += 1

    # while i < len(arr):
    #     r.append(arr[i])
    #     i += 1
    
    # while j < len(brr):
    #     r.append(brr[j])
    #     j += 1
    
    # if i < len(arr):
    r += arr[i:]

    # if j < len(brr):
    r += brr[j:]

    return r


def mergeSort(arr,si,ei):
    if si == ei:
        return [arr[si]]
    else:
        mid = (si+ei)//2
        left = mergeSort(arr,si,mid)
        right = mergeSort(arr,mid+1,ei)

        return merge(left,right)

arr = [3,2,6,7,1,8,5,4,10,3,7]
print(mergeSort(arr,0,len(arr)-1))

