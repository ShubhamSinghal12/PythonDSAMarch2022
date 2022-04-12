ll = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# for i in range(len(ll)):
#     if i%2==0:
#         for j in range(len(ll[i])):
#             print(ll[i][j],end = " ")
#     else:
#         for j in ll[i][::-1]:
#             print(j,end = " ")

# print()
# print(ll)

for j in range(len(ll[0])):
    for i in ll:
        print(i[j],end = " ")
    print()



