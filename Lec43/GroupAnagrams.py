# Sort a String

# s = "safdghm"
# t = "".join(sorted(s))
# print(t)


def groupAna(strs):
    ans = []
    d = {}
    for i in strs:
        st = "".join(sorted(i))
        if st in d:
            d[st].append(i)
        else:
            d[st] = [i]
    
    for k in d:
        ans.append(d[k])
    
    return ans

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAna(strs))
