st = "cbaeibce"

def isVowel(s):
    s = s.lower()
    st = "aeiou"
    return s in st

def pgst(st):
    count = 0
    m = 0
    for i in st:
        if isVowel(i):
            count += 1
            m = max(count,m)
        else:
            count = 0
    
    print(m)

pgst(st)


