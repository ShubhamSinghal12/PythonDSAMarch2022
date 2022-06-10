l = [4,5,2,25,11,12]
ans = [-1 for i in range(len(l))]
st = []

for i in range(len(l)):
    while len(st) != 0 and l[i] > l[st[-1]]:
        j = st.pop()
        ans[j] = l[i]
    
    st.append(i)


# for i in st:
#     ans[i] = -1

print(ans)