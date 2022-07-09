l = [2,12,9,16,10,5,3,20,21,11,1,8,6,7]

s = set(l)
print(s)
mct = 0
for i in s:
    if i-1 not in s:
        print(i,end=" ")
        c = i+1
        while c in s:
            print(c,end=" ")
            c += 1
        ct = c-i
        if ct > mct:
            mct = ct
        print()

print("Max:",mct)