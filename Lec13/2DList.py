# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# l3 = [9,10,11,12]

# ll = [l1,l2,l3]

# for i in ll:
#     for j in i:
#         print(j,end=" ")
#     print()

ll = []
m = 3
n = 4

# for i in range(m):
#     ll.append([])
#     for j in range(n):
#         ll[i].append(int(input()))

# for i in range(m):
#     ll.append([])
#     for j in input().split():
#         ll[i].append(int(j))

# ll = [[int(i) for i in input().split()] for j in range(m)]

# ll = [[int(input()) for j in range(n)] for i in range(m)]

ll = [[0 for j in range(n)] for i in range(m)]


# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# l3 = [9,10,11,12]

# ll = [l1,l1,l1]

# ll[0][0] = 10


# ll=[[0]*n]*m
# print(ll)
# ll[1][0] = 100


for i in range(len(ll)):
    for j in range(len(ll[i])):
        print(ll[i][j],end=" ")
    print()



