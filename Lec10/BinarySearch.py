a = [1,2,3,3,3,5,5,5,7]

def binarySearch(a,ele):
    si = 0
    ei = len(a)-1

    while si <= ei:
        mid = (si+ei)//2

        if a[mid] == ele:
            return mid
        elif a[mid] > ele:
            ei = mid-1
        else:
            si = mid+1
    
    return -1

def lowerBound(a,ele):
    si = 0
    ei = len(a)-1
    ans = -1
    while si <= ei:
        mid = (si+ei)//2

        if a[mid] == ele:
            ans = mid
            ei = mid-1
        elif a[mid] > ele:
            ei = mid-1
        else:
            si = mid+1
    
    return ans

def upperBound(a,ele):
    si = 0
    ei = len(a)-1
    ans = -1
    while si <= ei:
        mid = (si+ei)//2

        if a[mid] == ele:
            ans = mid
            si = mid+1
        elif a[mid] > ele:
            ei = mid-1
        else:
            si = mid+1
    
    return ans
print(upperBound(a,5))
