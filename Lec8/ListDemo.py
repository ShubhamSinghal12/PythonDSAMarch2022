# a = [10,20,30,40,50,60]
# print(a,type(a))

# print(len(a))

# # i = 0
# # while i < len(a):
# #     print(a[i],end= " ")
# #     i += 1

# # print()

# # for i in range(0,len(a),2):
# #     print(a[i])

# a.append(100)
# print(a)

# b = a.pop(2)
# print(a,b)

# b = a.pop(4)
# print(a,b)

# a.insert(100,1000)
# print(a)
# # b = a.pop(100)


# a = [10,20,30]
# b = [10,20,40]

# a[0] = 1000

# print(b)

# b = a

# print(b)



# arr = input().split()
# a = []
# for i in arr:
#     a.append(int(i))

# print(arr)
# print(a)

# arr = []
# n = int(input())
# for i in range(n):
#     # x = int(input())
#     arr.append(i)

# print(arr)

# n = int(input())
# arr = [int(input()) for i in range(n)]


arr = [int(i) for i in input().split()]


def search(arr,ele):
    
    for i in range(len(arr)):
        if arr[i] == ele:
            return i
    
    return -1

if search(arr,20) == -1:
    print("Element is not there")
else:
    print("Element is there")


