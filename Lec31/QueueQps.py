from DynamicQueue import DynamicQueue


def ar(qu):
    if qu.isEmpty():
        return
    else:
        n = qu.dequeue()
        ar(qu)
        # print(n)
        qu.enqueue(n)

def dispR(qu):
    ar(qu)
    qu.display()
    ar(qu)






st = DynamicQueue()
for i in range(1,10):
    st.enqueue(i)

st.display()
print()
dispR(st)
print()
st.display()
