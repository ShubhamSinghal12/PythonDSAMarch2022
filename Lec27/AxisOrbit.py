def countPSS(st):
    count = 0
    #ODD
    for i in range(len(st)):
        li = i
        ri = i
        while li >= 0 and ri < len(st):
            if st[li] == st[ri]:
                count+=1
                print(st[li:ri+1])
                li -= 1
                ri += 1
            else:
                break
    #EVEN
    for i in range(len(st)-1):
        li = i
        ri = i+1
        while li >= 0 and ri < len(st):
            if st[li] == st[ri]:
                count+=1
                print(st[li:ri+1])
                li -= 1
                ri += 1
            else:
                break
    return count 

    
print(countPSS("abba"))