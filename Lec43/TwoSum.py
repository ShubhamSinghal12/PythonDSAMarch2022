def twoSum(l:list,target):
    d = {}
    ans = []

    for i in range(len(l)):
        if target-l[i] in d:
            ans.append((d[target-l[i]],i))
            print(target-l[i],l[i])
        else:
            d[l[i]] = i
    
    return ans


l = [3,4,2,1,5,6,7,8,10,9]
print(twoSum(l,10))
