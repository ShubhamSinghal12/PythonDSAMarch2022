def VLA(arr,si,ei):
    if si >= ei:
        return 0
    else:
        ts = 0
        for i in range(si,ei+1):
            ts += arr[i]
        
        if ts %2 != 0:
            return 0
        
        s = 0
        for i in range(si,ei+1):
            s += arr[i]
            if s == ts//2:
                return 1 + max(VLA(arr,si,i),VLA(arr,i+1,ei))
        return 0

print(VLA([4,1,0,1,1,0,1],0,6))

# print("+" in "a+b")
print(eval("20*3"))
