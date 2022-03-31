arr = [5,3,1,4,2]

for i in range(len(arr)-1):
    min_i = i
    for j in range(i+1,len(arr)):
        if arr[min_i] > arr[j]:
            min_i = j
    
    t = arr[i]
    arr[i] = arr[min_i]
    arr[min_i] = t

print(arr)