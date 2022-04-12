def firstBadVersion(n: int) -> int:
    si = 1
    ei = n

    ans = 0

    while si <= ei:
        mid = (si+ei)//2
        if isBadVersion(mid):
            ans = mid
            ei = mid-1
        else:
            si = mid+1
    
    return ans