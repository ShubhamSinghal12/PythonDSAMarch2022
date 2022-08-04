a = 40

def countSet(a):
    ct = 0
    while a != 0 and a!=-1:
        if a&1 != 0:
            ct += 1
        a = a >> 1
    print(ct)

def CSBO(a):
    ct = 0
    while a != 0:
        ct += 1
        a = a&(a-1)
    print(ct)

# CSBO(a)
# countSet(a)
first_Set_Bit = a&(~(a-1))
print(first_Set_Bit)