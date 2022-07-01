s = 'cdcdfasdfabcdaababa'
d = dict()

for i in s:
    d[i] = d.get(i,0) + 1
    # if i in d:
    #     d[i] = d[i]+1
    # else:
    #     d[i] = 1

srt = sorted(d.keys())

for k in srt:
    print(k,":",d[k])

