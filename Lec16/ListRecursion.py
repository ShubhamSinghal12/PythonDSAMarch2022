l = [1,2,30,4,5,6]


def display(l,i):
    if i == len(l):
        return
    else:
        print(l[i])
        display(l,i+1)

def display2(l,i):
    if i == 0:
        print(l[0])
    else:
        display2(l,i-1)
        print(l[i])

def Amax(l,i):
    if i == 0:
        return l[i]
    else:
        return max(l[i],Amax(l,i-1))

def search(l,s,i):
    
    if i==len(l):
        return False
    else:
        if l[i]==s:
            return True
        else:
            return search(l,s,i+1)


print(Amax(l,len(l)-1))

# display2(l,len(l)-1)