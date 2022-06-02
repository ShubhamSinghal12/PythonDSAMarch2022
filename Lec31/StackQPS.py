from DynamicStack import DynamicStack

def dispR(st):
    st2 = DynamicStack()
    for i in range(st.size()):
        st2.push(st.pop())
    st2.display()

    for i in range(st2.size()):
        st.push(st2.pop())


def dispRR(st):
    if st.size() == 0:
        return 
    else:
        n = st.pop()
        dispRR(st)
        print(n,end=" ")
        st.push(n)

def ar(st):
    st2 = DynamicStack()
    st3 = DynamicStack()

    for i in range(st.size()):
        st2.push(st.pop())

    for i in range(st2.size()):
        st3.push(st2.pop())

    for i in range(st3.size()):
        st.push(st3.pop())

def ar2(st):
    st2 = DynamicStack()
    for i in range(st.size()):
        st2.push(st.pop())
    
    arhelp(st,st2)

def arhelp(st,st2):
    if st2.size() == 0:
        return
    else:
        n = st2.pop()
        arhelp(st,st2)
        st.push(n)

def pushFirst(st,ele):
    if st.size() == 0:
        st.push(ele)
    else:
        n = st.pop()
        pushFirst(st,ele)
        st.push(n)

def ar3(st):
    if st.size() == 0:
        return
    else:
        n = st.pop()
        ar3(st)
        pushFirst(st,n)

st = DynamicStack()
for i in range(1,10):
    st.push(i)

st.display()
print()
ar3(st)
print()
st.display()