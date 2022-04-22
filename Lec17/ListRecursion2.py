

def FO_1(l : list , i, ele):
    if i == len(l):
        return -1
    else:
        if l[i] == ele:
            return i
        else:
            return FO_1(l,i+1,ele)


def FO_2(l,n,ele):
    if n == -1:
        return -1
    else:
        ans = FO_2(l,n-1,ele)
        if ans != -1:
            return ans
        elif l[n] == ele:
            return n
        else:
            return -1


def LO(l,n,ele):
    if n == -1:
        return n
    else:
        if l[n] == ele:
            return n
        else:
            return LO(l,n-1,ele)


def allO(l,i,ele):
    if i == len(l):
        return []
    else:
        ans = allO(l,i+1,ele)
        if l[i] == ele:
            ans.insert(0,i)
        
        return ans


def allO1(l,i,ele,ans):
    if i == len(l):
        return 
    else:
        # ans = allO(l,i+1,ele)
        if l[i] == ele:
            ans.append(i)
        
        allO1(l,i+1,ele,ans)
        # return ans

def allO2(l,i,ele,count):
    if i == len(l):
        return [0]*count
    else:
        if l[i] == ele:
            count += 1
        
        ans = allO2(l,i+1,ele,count)

        if l[i] == ele:
            ans[count-1] = i
        
        return ans


def reverseR(l,si,ei):
    if si >= ei:
        return
    else:
        reverseR(l,si+1,ei-1)
        l[si],l[ei] = l[ei],l[si]
        
def BS(l,si,ei,ele):
    if si > ei:
        return -1
    else:
        mid = (si+ei)//2
        if l[mid] == ele:
            return mid
        elif l[mid] > ele:
            return BS(l,si,mid-1,ele)
        else:
            return BS(l,mid+1,ei,ele)



l = [5,2,3,1,2,6,7,2,4,2]
ans = []
ans = allO2(l,0,2,0)
print(ans)

reverseR(l,0,len(l)-1)
print(l)

l = [1,2,3,4,5,6,7,8,9]
print(BS(l,0,len(l)-1,3))

