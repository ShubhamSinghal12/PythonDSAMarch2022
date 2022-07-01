
d1 = dict({"ram":20,"nitin":20,"india":20})
d2 = dict({2:"abc",5:"xyz",10:"def"})
# print(d1,type(d1))
# print(d2,type(d2))

d1['ram'] = 200
d1[10] = 40
print(d1,d1['ram'])
# print(d1[20])
# d1.pop('ram')
# d1.clear()
print(d1.get('r',10))
# d1['ram'] = 100

# d1.popitem()
# d1.update(d2)

d2 = dict.fromkeys(["ram","India"],[10,20])

# d2["ram"].append(100)

# print(d2)
# print(d1)
# print(d1.items())
# print(d1.keys())
# print(d1.values())

# l = list(d1.keys())
# for k in l:
#     print(k,d1[k])
#     d1.pop(k)

# print(d1)

# for k in d1:
#     print(k,d1[k])

# for k,v in d1.items():
#     # k,v = i
#     print(k,v)


