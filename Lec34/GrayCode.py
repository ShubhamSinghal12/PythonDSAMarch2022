n = 3

def grayCode(n):
    if n == 1:
        return ["0","1"]
    else:
        rr = grayCode(n-1)
        ans = []
        for i in rr:
            ans.append("0"+i)
        
        for i in range(len(rr)-1,-1,-1):
            ans.append("1"+rr[i])
        
        return ans

print(grayCode(3))
