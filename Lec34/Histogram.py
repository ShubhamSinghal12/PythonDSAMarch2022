l = [6,2,5,4,5,1,6]

def maxArea(l):
    st = []
    maxarea = 0
    for i in range(len(l)):
        while len(st) != 0 and l[i] < l[st[-1]]:
            x = st.pop()
            # print(x)
            r = i
            if len(st) == 0:
                left = -1
            else:
                left = st[-1]

            area = (r-left-1)*l[x]
            if area > maxarea:
                maxarea = area
        st.append(i)
    
    while len(st) != 0:
        x = st.pop()
        r = len(l)
        if len(st) == 0:
            left = -1
        else:
            left = st[-1]

        area = (r-left-1)*l[x]
        if area > maxarea:
            maxarea = area
    
    return maxarea

def hist(l):
    if len(l) == 0:
        return 0
    else:
        mini = 0
        for i in range(len(l)):
            if l[mini] > l[i]:
                mini = i
        
        maxl = hist(l[0:mini])
        maxr = hist(l[mini+1:])
        cur = l[mini]*len(l)

        return max(maxl,maxr,cur)



print(hist(l))