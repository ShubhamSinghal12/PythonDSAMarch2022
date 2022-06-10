l = [[0,1,1,0],[0,0,1,0],[0,0,0,0],[1,0,1,0]]


def celeb(l):
    st = []
    for i in range(len(l)):
        st.append(i)
    
    while len(st) > 1:
        a = st.pop()
        b = st.pop()
        if l[a][b] == 1:
            st.append(b)
        else:
            st.append(a)
    
    c = st.pop()
    flag = True
    for i in range(len(l)):
        if i != c:
            if l[c][i] != 0 or l[i][c] != 1:
                flag = False
                break
    print(c)
    if flag:
        print("Celeb: ",c)
    else:
        print("No Celeb")


celeb(l)