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
    


st = DynamicStack()
for i in range(1,10):
    st.push(i)

st.display()
print()
ar(st)
print()
st.display()