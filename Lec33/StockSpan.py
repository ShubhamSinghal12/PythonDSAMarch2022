l=[100,80,60,70,60,75,85,110]

def stockSpan(l):
    ans = []
    st = []
    for i in range(len(l)):
        while len(st) != 0 and l[i] > l[st[-1]]:
            st.pop()
        
        if len(st) == 0:
            ans.append(i+1)
        else:
            ans.append(i-st[-1])
        
        st.append(i)
    
    print(ans)

stockSpan(l)


