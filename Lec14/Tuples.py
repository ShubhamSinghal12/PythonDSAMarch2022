# l = [1,2,3,4]

# t1 = (1,2,3,4)
# t2 = (5,)

# t3 = t1+t2

# print(t1)
# print(t3)
# print(type(t3))
# print(l[0],t3[1:3])

# l[0] = 100

# lt = list(t3)
# print(lt)

# lt.append(100)

# t3 = tuple(lt)
# print(t3)
# # t[0] = 100



# Unpacking
t = (1,2,3,4,5)
l = [1,2,3,4,5]

a,*b,c = t

print(a,b,c)


t1 = 1,2,3,4
print(t1,type(t1))


a,b = 1,2



def fn():
    a = 30
    b = 10
    return a,b


a,b = fn()
print(t1,type(t1))


t = (l,)

print(t)
l.append(100)
print(t)


